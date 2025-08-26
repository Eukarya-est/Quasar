import os
import markdown
import datetime as time

import properties.validation_type
import properties.path as path
import data_pipe
import data_store
from properties.sql_query import SqlQuery
from logger import debug_logger, info_logger, warning_logger, error_logger

def convert_md_to_html(directory, file):

    TYPE = validation_type()

    try:
        # Read Markdown from file
        with open(f"{path.MARKDOWN}/{directory}/{file}", "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()
    except FileNotFoundError as e:
        error_logger.error(f"File {file} not found in directory {directory}: {e}")
        return TYPE.ERROR
        
    # Convert to HTML
    html_content = markdown.markdown(markdown_content)

    try:
        with open(f"{path.HTMLS}/{directory}/{file}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as html_file:
            html_file.write(html_content)
    except Exception as e:
        error_logger.error(f"Error writing HTML file for {file} in directory {directory}: {e}")
        return TYPE.ERROR
    
    info_logger.info(f"{file} in {directory} has been converted to HTML")
    return TYPE.SUCCESS
    
def get_timestamp():
    return time.datetime.strftime(time.datetime.now(), "%Y-%m-%d %H:%M:%S")

def validation_type():
    return properties.validation_type.Type