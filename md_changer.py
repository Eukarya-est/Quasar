import markdown
import os

import properties.validation_type as TYPE
import properties.path as PATH
import properties.db_table as TABLE
from logger import debug_logger, info_logger, warning_logger, error_logger

def convert_md_to_html(md_path, html_path, directory, file):
    """
    Convert a markdown file to HTML and save it to the HTML directory.
    """

    try:
        # Read Markdown from file
        with open(f"{md_path}/{directory}/{file}.md", "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()
    except FileNotFoundError as e:
        info_logger.info(f"File {file} not found in directory {directory}: {e}")
        error_logger.error(f"File {file} not found in directory {directory}: {e}")
        return TYPE.ERROR
        
    # Convert to HTML
    html_content = markdown.markdown(markdown_content)

    try:
        if not os.path.isdir(f"{html_path}/{directory}"):
            os.mkdir(f"{html_path}/{directory}")
        with open(f"{html_path}/{directory}/{file}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as html_file:
            html_file.write(html_content)
    except Exception as e:
        info_logger.info(f"Error writing HTML file for {file} in directory {directory}: {e}")
        error_logger.error(f"Error writing HTML file for {file} in directory {directory}: {e}")
        return TYPE.ERROR
    
    info_logger.info(f"{file} in {directory} has been converted to HTML")
    return TYPE.SUCCESS
    