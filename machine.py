#!/usr/bin/python3

import re, random, string

from logger import debug_logger, info_logger


def extract(contents):
    """Create html from typora-export-content for Note-stacks"""
    found = False
    search_string = "<div class='typora-export-content'>\n"
    split_1 = re.split(rf'{search_string}', contents)
    
    if len(split_1) > 1 and not found:
        found = True
        search_string = "</body>"
        split_2 = re.split(rf'{search_string}', split_1[1])

        result = split_2[0]
        
        # if len(split_1) > 1:
        #     replace = re.sub(r'\>', '>\n', split_2[0])
        #     result = replace
    else:
        result = contents
    
    return result

def manage_pre(contents):
    """"""
    found = False
    start_string = r'<pre(.*?)>'
    end_string = r'</pre>'
    result = ''
    parts_start = re.split(start_string, contents, 1)

    if len(parts_start) > 1 and not found:
        found = True
        result += re.sub(r'\>', '>\n', parts_start[0])
        result += f'<pre{parts_start[1]} >'
        result += ''
        if len(parts_start) == 3:
            parts_end = re.split(end_string, parts_start[2], 1)
            result += parts_end[0] + '<pre>'
            result += manage_pre(parts_end[1])
            return result
        else:
            return result

    if not found:
        result = contents
    
    return result

def label(directory, contents):
    """Label Image Path for Note-stacks"""

    search_string = r'src=".\\imgs'
    replace_string = rf'src="\\server\\{directory}\\imgs'
    replace = re.sub(rf'{search_string}', f'{replace_string}', contents)
    result = replace

    return result

