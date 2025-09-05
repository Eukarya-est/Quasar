import os

import properties.validation_type as TYPE
import properties.path as PATH
import properties.db_table as TABLE
import data_manager
import db_controller
import v_and_v as vv
import md_changer
from logger import debug_logger, info_logger, warning_logger, error_logger

def main():

    """Main function to manage Markdown and HTML files"""

    #List directories up from MARKDOWN path
    dir_os = os.listdir(PATH.MARKDOWN)

    #List directories up from database (for updating deleted directories)
    dir_db = db_controller.select_col_dir(TABLE.DIR, TYPE.VALID)

    for directory in dir_os:

        # Verify directory
        verified = vv.verify_dir(PATH.MARKDOWN, directory)

        # If directory is not verified, remove it from database if it exists
        if not verified:
            if dir_db is not None and directory in dir_db:
                info_logger.info(f"Directory {directory} has been removed from the filesystem. Updating database.")
                db_controller.update_dir(TABLE.DIR, TYPE.INVALID, directory)
                cd = db_controller.select_row_dir3(TABLE.DIR, directory)
                # Also, remove all files in the directory from database
                file_db = db_controller.select_all_files(TABLE.DIR, cd)
                if file_db is not None and len(file_db) > 0:
                    for file in file_db:
                        info_logger.info(f"File {file} in directory {directory} has been removed from the filesystem. Updating database.")
                        db_controller.update_file(TABLE.DIR, TYPE.INVALID, directory, file)
                continue
        # If directory is verified, Validate directory
        else:
            valid = vv.validate_dir(PATH.MARKDOWN, directory)

        # If directory is valid, proceed with conversion
        if valid:
            #List files in a directory up
            file_list = os.listdir(f"{PATH.MARKDOWN}/{directory}")
            dir_db.remove(directory)
            
            for file in file_list:

                # List files up from database (for updating deleted files)
                file_db = db_controller.select_all_files(TABLE.FILES, directory)

                # Validate file
                verified = vv.verify_file(file)

                # If file is not valid, Skip it
                if not verified:
                    info_logger.info(f"File {file} in directory {directory} has been removed from the filesystem. Updating database.")
                    db_controller.update_file(TABLE.FILES, TYPE.INVALID, directory, file)
                    continue
                # If file is valid, proceed to validate it
                else:
                    store = data_manager.set_file_info_init(TABLE.FILES, f"{PATH.MARKDOWN}/{directory}/{file}")
                    valid = vv.validate_file(store)

                # If file is not valid, Skip it
                if not valid:
                    continue
                # If file is valid, proceed with conversion
                if valid == TYPE.NEW:
                    completed = md_changer.convert_md_to_html(directory, file)
                    if completed:
                        cover = db_controller.select_row_dir3(TABLE.DIR, directory)
                        num = db_controller.select_row_A3(TABLE.FILES, directory)
                        revision = db_controller.select_row_A4(TABLE.FILES, directory, file)
                        store._cover = data_manager.get_cover(cover)
                        store._num = data_manager.get_num(num)
                        store._revision = data_manager.get_revision(revision)
                        db_controller.insert_new_file(TABLE.FILES, TYPE.VALID, store.cover, store.number, store.revision, store.created, store.revised, store.title, store.file)
                        file_db.remove(file)
                    else:
                        error_logger.error(f"Failed to convert {file} in {directory} to HTML")
                        continue
                elif valid == TYPE.UPDATE:
                    completed = md_changer.convert_md_to_html(directory, file)
                    if completed:
                        cover = db_controller.select_row_dir3(TABLE.DIR, directory)
                        num = db_controller.select_row_A3(TABLE.FILES, directory)
                        revision = db_controller.select_row_A4(TABLE.FILES, directory, file)
                        store._cover = data_manager.get_cover(cover)
                        store._num = data_manager.get_num(num)
                        store._revision = data_manager.get_revision(revision)
                        db_controller.update_file(TABLE.FILES, TYPE.VALID, store.cover, store.title)
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

    dir_db = db_controller.select_col_dir(TABLE.DIR, TYPE.VALID)

    for directory in dir_db:

        file_list = os.listdir(f"{PATH.MARKDOWN}/{directory}")

        file_count = 1

        for file in file_list:

            db_controller.finish_off_numbering(TABLE.FILES, file_count, directory, file)
            file_count += 1

if __name__ == "__main__":
    main()