#!/usr/bin/python3
'''
Base: mdtex2html version 1.3.1 by Dirk Winkel

https://pypi.org/project/mdtex2html/    
'''

from latex2mathml.converter import convert as tex2mathml
from markdown import markdown as md2html
from markdown import Markdown
import re, random, string

from logger import debug_logger, info_logger

incomplete = '<font style="color:orange;" class="tooltip">&#9888;<span class="tooltiptext">formula incomplete</span></font>'
convError = '<font style="color:red" class="tooltip">&#9888;<span class="tooltiptext">LaTeX-convert-error</span></font>'

def convert(mdtex, extensions=[], splitParagraphs=True, continuousSentence=False):
    ''' converts recursively the Markdown-LaTeX-mixture to HTML with MathML '''
    found = False
    # render table of contents before splitting it up:
    if 'toc' in extensions and splitParagraphs and '[toc]' in mdtex:
        md = Markdown(extensions=['toc'])
        md.convert(mdtex)
        mdtex = mdtex.replace('[toc]', md.toc)
    # entirely skip code-blocks:
    parts = re.split('```', mdtex, 2)
    if len(parts)>1:
        found = True
        result = convert(parts[0], extensions, splitParagraphs=False)+'\n'
        result += md2html('```'+parts[1]+'```', extensions=extensions)+'\n'
        if len(parts)==3:
            result += convert(parts[2], extensions, splitParagraphs=False)
        return result
    # handle all paragraphs separately (prevents follow-up rendering errors)
    if splitParagraphs:
        parts = re.split("\n\n", mdtex)
        result = ''
        for part in parts:
            result += convert(part, extensions, splitParagraphs=False)
        return result
    # skip code-spans:
    parts = re.split('`', mdtex, 2)
    if len(parts)>1:
        found = True
        codehtml = md2html('`'+parts[1]+'`', extensions=extensions)
        codehtml = re.sub('^<[a-z]+>', '', codehtml) # remove opening tag
        codehtml = re.sub('</[a-z]+>$', '', codehtml) # remove closing tag
        ranString = ''.join(random.choice(string.ascii_letters) for i in range(16))
        if len(parts)==3:
            result = convert(parts[0]+'CoDeRePlAcEmEnT'+ranString+parts[2], extensions, splitParagraphs=False)
        else:
            result = convert(parts[0]+'CoDeRePlAcEmEnT'+ranString, extensions, splitParagraphs=False)
        result = result.replace('CoDeRePlAcEmEnT'+ranString, codehtml)
    # find 
    else:
    # find first $$-formula:
        parts = re.split('\${2}', mdtex, 2)
    if len(parts)>1 and not found:
        found = True
        debug_logger.debug(f"parts: {parts}")
        w_newline = parts[1].startswith('\n')
        debug_logger.debug(f"keep1: {continuousSentence}")
        debug_logger.debug(f"parts[0]: {parts[0]}")
        if not continuousSentence and len(parts[0]) > 0:
            parts[0] = "<p>" + parts[0]
            parts[2] = parts[2] + "</p>"
            result = convert(parts[0], extensions, splitParagraphs=False)
        else:
            result = convert(parts[0], extensions, splitParagraphs=False, continuousSentence=True)
        debug_logger.debug(f"result1: {result}")
        debug_logger.debug(f"parts1: {parts}")
        if w_newline:
            result += '<p>'
        try:
            result += tex2mathml(parts[1]) + '\n'
            debug_logger.debug(f"result2: {result}")
            if parts[1].endswith('\n'):
                result += '</p>'
        except:
            result += '<div class="blockformula">'+convError+'</div>'
        if len(parts)==3:
            result += convert(parts[2], extensions, splitParagraphs=False, continuousSentence=True)
        else:
            result += '<div class="blockformula">'+incomplete+'</div>'
    # else find first $-formulas, excluding \$:
    else:
        parts = re.split(r'(?<!\\)\${1}', mdtex, 2)
        debug_logger.debug(f"parts2: {parts}")
    if len(parts)>1 and not found:
        found = True
        try:
            mathml = tex2mathml(parts[1])
        except:
            mathml = convError
        if parts[0].endswith('\n') or parts[0]=='': # make sure textblock starts before formula!
            parts[0]=parts[0]+'&#x200b;'
        if len(parts)==3:
            result = convert(parts[0]+mathml+parts[2], extensions, splitParagraphs=False)
        else:
            result = convert(parts[0]+mathml+incomplete, extensions, splitParagraphs=False)
    # else find first \[..\]-equation:
    else:
        mdtex = mdtex.replace(r'\$', '$')
    if not found:
        # no more formulas found
        debug_logger.debug(f"keep2: {continuousSentence}")
        debug_logger.debug(f"mdtex: {mdtex}")
        if not continuousSentence:
            if mdtex.startswith("<p>"):
                result = mdtex + '\n'
            else:
                result = md2html(mdtex, extensions=extensions) + '\n'
        else:
            result = mdtex + '\n'
    
    return result
