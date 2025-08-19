import os
import markdown
import datetime as time

import properties.validation_type as validation_type
import properties.path as path
import db_controller
from logger import debug_logger, info_logger, warning_logger, error_logger

def verify_dir(directory):

    """
    Verify the directory and return True it is truly direcotry or not '.git', False other wise.
    """
    
    # Check if the directory is '.git' directory
    if directory == path.GIT:
        info_logger.info(f"{directory} is a git directory, skipping")
        return False
    
    # Check if the 'directory' is a directory
    if not os.path.isdir(f"{path.MARKDOWN}/{directory}"):
        error_logger.error(f"{directory} is not a directory")
        return False
    
    return True

def validate_dir(directory):

    """
    Validate the directory and return True if files exist, False other wise.
    """

    # Verify the directory on database

    file_list = os.listdir(f"{path.MARKDOWN}/{directory}")

    # Check if the directory is already in the database
    try:
        result=db_controller.select_dir(directory)
    except Exception as e:
        error_logger.error(f"db_controller.select_dir failed: {e}")
        return False

    # Check if the directory is empty
    if len(file_list) == 0 and result is None:
        info_logger.info(f"{directory} is empty and not in the database")
        warning_logger.warning(f"{directory} is empty and not in the database")
        return False
    elif len(file_list) == 0 and result is not None:
        info_logger.info(f"{directory} is empty")
        warning_logger.warning(f"{directory} is empty")
        db_controller.update_dir(directory, False)
        return False
    # Verify files in the directory on these cases
    # 1. file_list > 0 && result is None 
    # 2. file_list > 0 && result is not None    
    else:
        # Check if the directory contatins at least one valid markdown file
        file_verified = False
        for file in file_list:
            
            file_verified = validate_file(file)
            if file_verified:
                break; 

        if not file_verified:
            info_logger.info(f"{directory} does not contain valid markdown files")
            warning_logger.warning(f"{directory} does not contain valid markdown files")
            db_controller.update_dir(directory, False)
            return False

        # If the directory is not found in the database, insert it.
        ## NEW COVER ##
        if result is None:
            info_logger.info(f"NEW directory:{directory}")
            try:
                db_controller.insert_dir(directory)
                return True
            except Exception as e:
                error_logger.error(f"db_controller.insert_dir failed: {e}")
                return False
        else:
            info_logger.info(f"Directory {directory} already exists in the database")
            return True    

def verify_file(file):

    """
    Verify the file and return True if file is valid, False other wise.
    """

    # Check if the file is a valid file
    if not os.path.isfile(file):
        error_logger.error(f"{file} is not a file")
        return False
    
    # Check if the file is a markdown file
    if not file.endswith('.md'):
        error_logger.error(f"{file} is not a markdown file")
        return False
    
    return True

def validate_file(file):

    """
    Validate the file and return True if file is valid, False other wise.
    """

    # Verify the file on database
    try:
        result = db_controller.select_file(file)
    except Exception as e:
        error_logger.error(f"db_controller.select_file failed: {e}")
        return validation_type.Type.INVALID
    
    # Check if the file is already in the database
    if result is None:
        info_logger.info(f"NEW file: {file}")
        return validation_type.Type.NEW
    else:
        if result.revised_time != file.revised:
            info_logger.info(f"{file} is already in the database and up to date")
            return validation_type.Type.UPDATE
        else:
            info_logger.info(f"{file} is already in the database but not up to date")
            return validation_type.Type.INVALID
        
    
    

