import os
import sys

from main import main

# Add the parent directory to sys.path to allow imports from the main codebase
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import properties.sql_query as SqlQuery
import properties.db_table as TABLE
import properties.path as PATH

from db_manager import DBManager as DBManager
from logger import debug_logger, info_logger, warning_logger, error_logger

def it():
    DB = DBManager.get_instance()
    try:
        info_logger.info("Table initialization")
        DB.init_table(SqlQuery.init_F1.format(TABLE.FILES_TEST))
        DB.init_table(SqlQuery.init_D1.format(TABLE.DIR_TEST))
    except Exception as e:
        info_logger.info(f"Table initialization failed: {e}")
        error_logger.error(f"Table initialization failed: {e}")

    info_logger.info("Table initialized")

    try:
        dir_os = os.listdir(PATH.TEST_RESULT)
        debug_logger.debug(dir_os)
        if(type(dir_os) == str):
            temp = []
            temp.append(dir_os)
            dir_os = temp
        for dir in dir_os:
            os.rmdir(dir)
    except Exception as e:
        info_logger.info(f"Directories removals failed: {e}")
        error_logger.error(f"Directories removals failed: {e}")    

    main()

if __name__ == "__main__":
    info_logger.info("!=== Interation TEST START ===!")
    warning_logger.warning("!=== Interation TEST START ===!")
    error_logger.error("!=== Interation TEST START ===!")
    it()