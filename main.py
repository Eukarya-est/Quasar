import os
import markdown
import datetime as time

import properties.validation_type as validation_type
import properties.path as path
import data_pipe
import data_store
import db_controller
import v_and_v as vv
from logger import debug_logger, info_logger, warning_logger, error_logger

def main():

    """Main function to manage Markdown and HTML files"""

    #List directories up
    dir_list = os.listdir(path.MARKDOWN)

    dir_count = 1
    for directory in dir_list:

        # Verify directory
        verified = vv.verify_dir(directory)

        # If directory is not verified, Skip it
        if not verified:
            continue
        # If directory is verified, Validate directory
        else:
            valid =  vv.validate_dir(directory)

        # If directory is valid, proceed with conversion
        if valid:
            #List files in a directory up
            file_list = os.listdir(f"{path.MARKDOWN}/{directory}")
            
            file_count = 1
            for file in file_list:

                # Validate file
                verified = vv.verify_file(file)

                # If file is not valid, Skip it
                if not verified:
                    continue
                # If file is valid, proceed to validate it
                else:
                    store=data_pipe.set_file_info(directory, f"{path.MARKDOWN}/{directory}/{file}")

                valid = vv.validate_file(store)
                
                # If file is not valid, Skip it
                if valid == validation_type.Type.INVALID:
                    continue
                # If file is valid, proceed with conversion
                elif valid == validation_type.Type.NEW:
                    db_controller.insert_new_file(store)
                elif valid == validation_type.Type.UPDATE:
                    db_controller.update_dir(store)

if __name__ == "__main__":
    main()