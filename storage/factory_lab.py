import os

import properties.validation_type as TYPE
import properties.path as PATH
import properties.db_table as TABLE
from logger import debug_logger, info_logger, warning_logger, error_logger
import mdtex2html
import markdown

def process(md_path, html_path, directory, title):
    """
    Convert a markdown file to HTML and save it to the HTML directory.
    """

    try:
        # Read Markdown from file
        with open(f"{md_path}/{directory}/{title}.md", "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()
    except Exception as e:
        info_logger.info(f"File {title} not found in directory {directory}: {e}")
        error_logger.error(f"File {title} not found in directory {directory}: {e}")
        return TYPE.ERROR
    
    # Convert Markdown and LaTeX to HTML
    inter_content = markdown.markdown(markdown_content)

    try:
        if not os.path.isdir(f"{html_path}/{directory}"):
            os.mkdir(f"{html_path}/{directory}")
        with open(f"{html_path}/{directory}/{title}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as inter_file:
            inter_file.write(inter_content)  
    except Exception as e:
        info_logger.info(f"Error converting Markdown in {title} in directory {directory}: {e}")
        error_logger.error(f"Error converting Markdown in {title} in directory {directory}: {e}")
        return TYPE.ERROR
    
    inter_content_2 = mdtex2html.convert(inter_content)

    try:
        if not os.path.isdir(f"test_converter/{directory}"):
            os.mkdir(f"test_converter/{directory}")
        with open(f"test_converter/{directory}/{title}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as inter_file:
            inter_file.write(inter_content_2)  
    except Exception as e:
        info_logger.info(f"Error converting Markdown in {title} in directory {directory}: {e}")
        error_logger.error(f"Error converting Markdown in {title} in directory {directory}: {e}")
        return TYPE.ERROR
        
    
    info_logger.info(f"{title} in {directory} has been converted to HTML")
    return TYPE.SUCCESS
    