import os

import properties.validation_type as TYPE
import properties.path as PATH
import properties.db_table as TABLE
from logger import debug_logger, info_logger, warning_logger, error_logger
import machine_controller

def process(md_path, html_path, directory, title):
    """
    Convert a markdown file to HTML and save it to the HTML directory.
    """

    try:
        # Read Markdown from file
        with open(f"{md_path}/{directory}/{title}.html", "r", encoding="utf-8") as read_file:
            contents = read_file.read()
    except Exception as e:
        info_logger.info(f"File {title} not found in directory {directory}: {e}")
        error_logger.error(f"File {title} not found in directory {directory}: {e}")
        return TYPE.ERROR
    
    # Convert Markdown and LaTeX to HTML
    final_content = machine_controller.operate(directory, contents)

    try:
        if not os.path.isdir(f"{html_path}/{directory}"):
            os.mkdir(f"{html_path}/{directory}")
        with open(f"{html_path}/{directory}/{title}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as write_file:
            write_file.write(final_content)  
    except Exception as e:
        info_logger.info(f"Error converting Markdown in {title} in directory {directory}: {e}")
        error_logger.error(f"Error converting Markdown in {title} in directory {directory}: {e}")
        return TYPE.ERROR
        
    
    info_logger.info(f"{title} in {directory} has been converted to HTML")
    return TYPE.SUCCESS
    