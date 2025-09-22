#!/usr/bin/python3
import os
import sys

# Add the parent directory to sys.path to allow imports from the main codebase
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import properties.validation_type as TYPE
import properties.path as PATH
import properties.db_table as TABLE
import data_manager
import db_controller
import v_and_v as vv
import factory
#import md_changer_lab as md_changer
from logger import debug_logger, info_logger, warning_logger, error_logger

def main():

    """Main function to manage Markdown and HTML files"""

    #List directories up from MARKDOWN path
    dir_os = os.listdir(PATH.TEST_CASE)
    dir_list = sorted(dir_os, reverse=False)

    #List directories up from database (for updating deleted directories)
    dir_db = db_controller.select_dir1(TABLE.DIR_TEST, TYPE.VALID)

    for directory in dir_list:
        info_logger.info(f"[!] Processing directory: {directory}")

        # Verify directory
        verified = vv.verify_dir(PATH.TEST_CASE, directory)
        info_logger.info(f"Directory {directory} verification result: {verified}")
        cd = db_controller.select_dir3(TABLE.DIR_TEST, directory)
        valid = TYPE.INVALID

        # If directory is not verified, remove it from database if it exists
        if not verified:
            if dir_db is not None and directory in dir_db:
                info_logger.info(f"Directory {directory} has been removed from the filesystem. Updating database.")
                db_controller.update_dir(TABLE.DIR_TEST, TYPE.INVALID, directory)
                # Also, remove all files in the directory from database
                file_db = db_controller.select_all_files(TABLE.DIR_TEST, cd)
                if file_db is not None and len(file_db) > 0:
                    for file in file_db:
                        info_logger.info(f"File {file} in directory {directory} has been removed from the filesystem. Updating database.")
                        revision = db_controller.select_file_max_rev(TABLE.FILES_TEST, directory, data_manager.parse_path(file))
                        db_controller.update_file(TABLE.DIR_TEST, TYPE.INVALID, directory, data_manager.parse_path(file), revision)
                continue
        # If directory is verified, Validate directory
        else:
            valid = vv.validate_dir(TABLE.DIR_TEST, PATH.TEST_CASE, directory)
            info_logger.info(f"Directory {directory} validation result: {valid}")

        # If directory is valid, proceed with conversion
        if valid == TYPE.VALID:
            #List files in a directory up
            file_os = os.listdir(f"{PATH.TEST_CASE}/{directory}")
            file_list = sorted(file_os, reverse=False)
            
            if dir_db is not None and directory in dir_db:
                dir_db.remove(directory)
            
            for file in file_list:
                info_logger.info(f"Processing file: {file} in directory: {directory}")

                # List files up from database (for updating deleted files)
                file_db = db_controller.select_all_files(TABLE.FILES_TEST, cd)

                # Validate file
                verified = vv.verify_file(f"{PATH.TEST_CASE}/{directory}/{file}")
                info_logger.info(f"File {file} verification result: {verified}")

                # If file is not verified, Skip it
                if not verified:
                    info_logger.info(f"File {file} in directory {directory} has been removed from the filesystem. Updating database if file data exist.")
                    revision = db_controller.select_file_max_rev(TABLE.FILES_TEST, directory, data_manager.parse_path(file))
                    if revision is not None:
                        db_controller.update_file(TABLE.FILES_TEST, TYPE.INVALID, directory, file, revision)
                    continue
                # If file is verified, proceed to validate it
                else:
                    store = data_manager.set_file_info_init(f"{PATH.TEST_CASE}/{directory}/{file}")
                    cd = db_controller.select_dir3(TABLE.DIR_TEST, directory)
                    store._cover = data_manager.get_cover(cd)
                    valid = vv.validate_file(TABLE.FILES_TEST, store)
                    debug_logger.debug(f"File {file} validation result: {valid}")

                # If file is not valid, Skip it
                if not valid:
                    continue

                # If file is valid, proceed with conversion
                if valid == TYPE.NEW:
                    completed = factory.process(PATH.TEST_CASE, PATH.TEST_RESULT, directory, store.title)
                    if completed:
                        num = db_controller.select_file_max_num(TABLE.FILES_TEST, store.cover)
                        revision = db_controller.select_file_max_rev(TABLE.FILES_TEST, store.cover, store.title)
                        store._num = data_manager.get_num(num)
                        store._revision = data_manager.get_revision(revision)
                        db_controller.insert_new_file(TABLE.FILES_TEST, store.cover, store.number, store.revision, store.created, store.revised, store.title, store.title)
                        if file_db is not None and file in file_db:
                            file_db.remove(file)
                    else:
                        info_logger.info(f"File {file} in directory {directory} could not be converted.")
                        error_logger.error(f"Failed to convert {file} in {directory} to HTML")
                        continue
                elif valid == TYPE.UPDATE:
                    completed = factory.process(PATH.TEST_CASE, PATH.TEST_RESULT, directory, store.title)
                    if completed:
                        num = db_controller.select_file_max_num(TABLE.FILES_TEST, store.cover)
                        revision = db_controller.select_file_max_rev(TABLE.FILES_TEST, store.cover, file)
                        store._num = data_manager.get_num(num)
                        store._revision = data_manager.get_revision(revision)
                        db_controller.update_file(TABLE.FILES_TEST, TYPE.INVALID, store.cover, store.title, revision)
                        db_controller.insert_new_file(TABLE.FILES_TEST, store.cover, store.number, store.revision, store.created, store.revised, store.title, store.title)
                        if file_db is not None and file in file_db:
                            file_db.remove(file)
                    else:
                        info_logger.info(f"File {file} in directory {directory} could not be converted.")
                        error_logger.error(f"Failed to convert {file} in {directory} to HTML")
                        continue
                else:
                    continue

    finish_off()

def finish_off():
    
    """Finish off file number."""

    dir_db = db_controller.select_dir1(TABLE.DIR_TEST, TYPE.VALID)
    if dir_db is None or len(dir_db) == 0:
        info_logger.info("No valid directory found in the database")
        warning_logger.warning("No valid directory found in the database")
        return
    else:
        if(type(dir_db) == str):
            temp = []
            temp.append(dir_db)
            dir_db = temp
        for directory in dir_db:
            if type(directory) == tuple:
                directory = directory[0]

            file_os = os.listdir(f"{PATH.TEST_CASE}/{directory}")
            file_list = sorted(file_os, reverse=False)

            file_count = 1

            for file in file_list:

                verified = vv.verify_file(f"{PATH.TEST_CASE}/{directory}/{file}")

                cd = db_controller.select_dir3(TABLE.DIR_TEST, directory)

                if verified == TYPE.VERIFIED:
                    db_controller.finish_off_numbering(TABLE.FILES_TEST, file_count, cd, data_manager.parse_path(file))
                    file_count += 1

    info_logger.info("*=== Process END ===*")
    warning_logger.warning("*=== Process END ===*")
    error_logger.error("*=== Process END ===*")

if __name__ == "__main__":
    info_logger.info("!=== Process START ===!")
    warning_logger.warning("!=== Process START ===!")
    error_logger.error("!=== Process START ===!")
    main()