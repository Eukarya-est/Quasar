import os
import datetime as time

import properties.validation_type
import properties.path as path
import data_pipe
import db_controller
import v_and_v as vv
import md_changer
from logger import debug_logger, info_logger, warning_logger, error_logger

def main():

    """Main function to manage Markdown and HTML files"""

    TYPE = validation_type()

    #List directories up from MARKDOWN path
    dir_os = os.listdir(path.MARKDOWN)

    #List directories up from database (for updating deleted directories)
    dir_db = db_controller.select_all_dir()

    for directory in dir_os:

        # Verify directory
        verified = vv.verify_dir(directory)

        # If directory is not verified, remove it from database if it exists
        if not verified:
            if dir_db is not None and directory in dir_db:
                info_logger.info(f"Directory {directory} has been removed from the filesystem. Updating database.")
                db_controller.update_dir(TYPE.INVALID, directory)
                file_db = db_controller.select_all_files(directory)
                if file_db is not None and len(file_db) > 0:
                    for file in file_db:
                        info_logger.info(f"File {file} in directory {directory} has been removed from the filesystem. Updating database.")
                        db_controller.update_file(TYPE.INVALID, directory, file)
                continue
        # If directory is verified, Validate directory
        else:
            valid = vv.validate_dir(directory)

        # If directory is valid, proceed with conversion
        if valid:
            #List files in a directory up
            file_list = os.listdir(f"{path.MARKDOWN}/{directory}")
            dir_db.remove(directory)
            
            for file in file_list:

                # List files up from database (for updating deleted files)
                file_db = db_controller.select_all_files(directory)

                # Validate file
                verified = vv.verify_file(file)

                # If file is not valid, Skip it
                if not verified:
                    info_logger.info(f"File {file} in directory {directory} has been removed from the filesystem. Updating database.")
                    db_controller.update_file(TYPE.INVALID, directory, file)
                    continue
                # If file is valid, proceed to validate it
                else:
                    store = data_pipe.set_file_info(directory, f"{path.MARKDOWN}/{directory}/{file}")
                    valid = vv.validate_file(store)

                # If file is not valid, Skip it
                if not valid:
                    continue
                # If file is valid, proceed with conversion
                if valid == TYPE.NEW:
                    completed = md_changer.convert_md_to_html(directory, file)
                    if completed:
                        num = db_controller.select_file_num(directory)
                        if num is None:
                            num = 1
                        else:
                            store.num = num + 1
                        store.revision = 1
                        db_controller.insert_new_file(store)
                        file_db.remove(file)
                    else:
                        error_logger.error(f"Failed to convert {file} in {directory} to HTML")
                        continue
                elif valid == TYPE.UPDATE:
                    completed = md_changer.convert_md_to_html(directory, file)
                    if completed:
                        store.num = db_controller.select_file_max_num(directory)
                        store.revision = db_controller.select_file_max_rev(directory, file) + 1
                        db_controller.update_file(TYPE.VALID, store)
                        file_db.remove(file)
                    else:
                        error_logger.error(f"Failed to convert {file} in {directory} to HTML")
                        continue
                # If file is not valid , Skip it
                else:
                    continue

    finish_off()

def finish_off():
    
    """Finish off file number."""

    dir_db = db_controller.select_all_dir()

    for directory in dir_db:

        file_list = os.listdir(f"{path.MARKDOWN}/{directory}")

        file_count = 1

        for file in file_list:

            db_controller.finish_off_numbering(file_count, directory, file)
            file_count += 1

def validation_type():

    return properties.validation_type.Type

if __name__ == "__main__":
    main()