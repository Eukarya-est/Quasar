import os

import properties.validation_type as TYPE
import properties.path as PATH
import db_controller
from logger import debug_logger, info_logger, warning_logger, error_logger

def verify_dir(path, directory):

    """
    Verify the directory and return True it is truly direcotry or not '.git', False other wise.
    """
    
    # Check if the directory is '.git' directory
    if directory == PATH.GIT:
        info_logger.info(f"{directory} is a git directory, skipping")
        warning_logger.warning(f"{directory} is a git directory, skipping")
        return TYPE.UNVERIFIED
    
    # Check if the 'directory' is a directory
    if not os.path.isdir(f"{path}/{directory}"):
        info_logger.error(f"{directory} is not a directory")
        warning_logger.warning(f"{directory} is not a directory")
        return TYPE.UNVERIFIED
    
    return TYPE.VERIFIED

def validate_dir(db_table, path, directory):

    """
    Validate the directory and return True if files exist, False other wise.
    """

    # Verify the directory on database
    file_list = os.listdir(f"{path}/{directory}")

    # Check if the directory is already in the database
    try:
        result = db_controller.select_dir2(db_table, directory)
    except Exception as e:
        error_logger.error(f"db_controller.select_dir2 failed: {e}")
        return TYPE.INVALID

    # Check if the directory is empty
    if len(file_list) == 0 and result is None:
        info_logger.info(f"{directory} is empty and not in the database")
        warning_logger.warning(f"{directory} is empty and not in the database")
        return TYPE.INVALID
    elif len(file_list) == 0 and result is not None:
        info_logger.info(f"{directory} is empty")
        warning_logger.warning(f"{directory} is empty")
        db_controller.update_dir(db_table, TYPE.INVALID, directory)
        return TYPE.INVALID
    # Verify files in the directory on these cases
    # 1. file_list > 0 && result is None 
    # 2. file_list > 0 && result is not None    
    else:
        # Check if the directory contatins at least one valid markdown file
        file_verified = False
        for file in file_list:
            
            file_verified = verify_file(f"{path}/{directory}/{file}")
            if file_verified:
                break; 

        if file_verified == TYPE.UNVERIFIED:
            info_logger.info(f"{directory} does not contain valid markdown files")
            warning_logger.warning(f"{directory} does not contain valid markdown files")
            # If the directory is not valid, remove it from the database
            if result is not None:
                info_logger.info(f"Removing {directory} from the database")
                warning_logger.warning(f"Removing {directory} from the database")
                db_controller.update_dir(db_table, TYPE.INVALID, directory)
                return TYPE.INVALID
            else:
                info_logger.info(f"{directory} is not valid and not in the database")
                warning_logger.warning(f"{directory} is not valid and not in the database")
                return TYPE.INVALID
                
        # If the directory is not found in the database, insert it.
        ## NEW COVER ##
        if result is None:
            info_logger.info(f"NEW directory:{directory}")
            try:
                db_controller.insert_dir(db_table, directory, TYPE.VALID)
                return TYPE.VALID
            except Exception as e:
                error_logger.error(f"db_controller.insert_dir failed: {e}")
                return TYPE.INVALID
        else:
            info_logger.info(f"Directory {directory} already exists in the database")
            return TYPE.VALID    

def verify_file(file):

    """
    Verify the file and return True if file is valid, False other wise.
    """ 

    # Check if the file is a valid file
    if not os.path.isfile(file):
        info_logger.error(f"{file} is not a file")
        warning_logger.warning(f"{file} is not a file")
        return TYPE.UNVERIFIED
    
    # # Check if the file is a markdown file
    # if not file.endswith('.md'):
    #     info_logger.error(f"{file} is not a markdown file")
    #     warning_logger.warning(f"{file} is not a markdown file")
    #     return TYPE.UNVERIFIED
    
    # Check if the file is a markdown file
    if not file.endswith('.html'):
        info_logger.error(f"{file} is not a html file")
        warning_logger.warning(f"{file} is not a html file")
        return TYPE.UNVERIFIED

    # Check if the file is a directory
    if os.path.isdir(file):
        info_logger.error(f"{file} is a directory")
        warning_logger.warning(f"{file} is a directory")
        return TYPE.UNVERIFIED
    
    return TYPE.VERIFIED

def validate_file(db_table, file_info):

    """
    Validate the file and return True if file is valid, False other wise.
    """

    # Verify the file on database
    try:
        result = db_controller.select_file(db_table, file_info.cover, file_info.title)
        revised_time = db_controller.select_file_revised(db_table, file_info.cover, file_info.title)
    except Exception as e:
        info_logger.info(f"db_controller.select_file failed: {e}")
        error_logger.error(f"db_controller.select_file failed: {e}")
        return TYPE.INVALID
    
    # Check if the file is already in the database
    if result is None:
        info_logger.info(f"NEW file: {file_info.title}")
        return TYPE.NEW
    else:
        if str(revised_time) != str(file_info.revised):
            info_logger.info(f"{file_info.title} is already in the database and up to date")
            return TYPE.UPDATE
        else:
            info_logger.info(f"{file_info.title} is already in the database but not up to date")
            return TYPE.NOACTION
