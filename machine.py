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

def label(directory, contents):
    """Label Image Path for Note-stacks"""

    search_string = r'src=".\\imgs'
    replace_string = rf'src="\\server\\{directory}\\imgs'
    replace = re.sub(rf'{search_string}', f'{replace_string}', contents)
    result = replace

    return result

# def manage_pre(contents):
#     """"""
#     found = False
#     start_string = r'<pre(.*?)>'
#     start_string_2 = r'<pre'    
#     end_string = r'</pre>'
#     result = ''
#     # Ex) ...<pre class = "abc"><p>ef</p></pre>... => ['...', ' class="abc"', <p>ef</p></pre>...]
#     parts_start = re.split(start_string, contents, 1)

#     if len(parts_start) > 1 and not found:
#         found = True
#         result += re.sub(r'\>', '>\n', parts_start[0])
#         result += f'<pre{parts_start[1]} >'
#         result += ''
#         # Handling nested pre tag
#         indices_s = []
#         indices_e = []
#         matches =  re.finditer(start_string, parts_start[2])
#         for match in matches:
#             indices_s.append(match.start())
#         matches =  re.finditer(end_string, parts_start[2])
#         for match in matches:
#             indices_e.append(match.start())
#         count = 0
#         try: 
#             while count > -1:
#                 found_index = parts_start[2].find(start_string_2, start_index)
#                 debug_logger.debug(found_index)
#                 if found_index != -1:
#                     indices.append(found_index)
#                     count += 1
#                     debug_logger.debug(count)                    
#                 found_index = parts_start[2].find(end_string, found_index)
#                 debug_logger.debug(found_index)
#                 if found_index != -1:
#                     indices.append(found_index + len(end_string))
#                     count -= 1
#                     start_index = found_index
#                     debug_logger.debug(count)      
#                 else:
#                     raise Exception("manage_pre is anomaly")
#         except Exception as e:
#             raise
        
#         debug_logger.debug(indices)
#         result += parts_start[2][0:max(indices)]
#         debug_logger.debug(result)
#         end_index = max(indices) + 1
#         result += manage_pre(parts_start[2][end_index:])
#         return result

#     if not found:
#         result = contents
    
#     return result
