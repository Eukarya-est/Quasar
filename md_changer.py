import os
import markdown
import datetime as time

import properties.path as path
import data_pipe
import data_store
from properties.sql_query import SqlQuery
from logger import debug_logger, info_logger, warning_logger, error_logger

def convert_md_to_html():
    #List direcories up
    dir_list = os.listdir(path.MARKDOWN)

    dir_count = 1
    for directory in dir_list:

        if(directory == path.GIT):
            continue
        
        #List files in a directory up
        file_list = os.listdir(f"{path.MARKDOWN}/{directory}")
        
        file_count = 1
        for file in file_list:

            extension = list(os.path.splitext(file))

            data_pipe.set_file_info(f"{path.MARKDOWN}/{directory}/{file}", directory)
            modified_time = data_store.DataStore.revised_time

            if(extension[1].lower() == '.md'):

                # Read Markdown from file
                with open(f"{path.MARKDOWN}/{directory}/{file}", "r", encoding="utf-8") as md_file:
                    markdown_content = md_file.read()
                    # Convert to HTML
                html_content = markdown.markdown(markdown_content)

                if not os.path.isdir(f"{path.HTMLS}/{directory}"):
                    os.mkdir(f"{path.HTMLS}/{directory}")

                # Save HTML to file
                if not os.path.exists(f"{path.HTMLS}/{directory}/{extension[0]}.html"):
                    with open(f"{path.HTMLS}/{directory}/{extension[0]}.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as html_file:
                        html_file.write(html_content)
                    
                    info_logger.info(f"{file} in {directory} has been converted {file_count} / {len(file_list)}")
                    print(f"[{get_timestamp()}]: {file} in {directory} has been converted {file_count} / {len(file_list)}")
                else:
                    info_logger.info(f"{file} in {directory} already has been exist {file_count} / {len(file_list)}")
                    print(f"[{get_timestamp()}]: {file} in {directory} already has been exist {file_count} / {len(file_list)}")
                         
                file_count += 1

        info_logger.info(f"{directory} has been completed. {dir_count} / {len(dir_list)}")
        print(f"[{get_timestamp()}]: {directory} has been completed. {dir_count} / {len(dir_list)}")
        dir_count += 1

    info_logger.info("===== Markdown has been converted and saved to html =====")
    print(f"[{get_timestamp()}]: Markdown has been converted and saved to html")

def get_timestamp():
    return time.datetime.strftime(time.datetime.now(), "%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    convert_md_to_html()