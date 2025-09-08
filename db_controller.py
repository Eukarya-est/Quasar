# db_controller.py
from db_manager import DBManager as DBManager
import properties.sql_query as SqlQuery
from logger import debug_logger, info_logger, warning_logger, error_logger

def insert_dir(table, *args):
    """Inserts a new directory into the database."""

    if not table:
        info_logger.info("Table name is missing for insert_dir")
        error_logger.error("No table name provided for insert_dir")
        return None
    
    if not args:
        info_logger.info("No table name provided for insert_dir")
        error_logger.error("No arguments provided for insert_dir")
        return None

    DB = DBManager.get_instance()
    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    try:
        result = DB.insert_query(SqlQuery.insert_D1.format(table), args)
        if result == 1:
            info_logger.info(f"{args} is inserted successfully")
        else:
            info_logger.info(f"insert_dir is anomaly; result: {result} args: {args}")
            warning_logger.warning.error(f"insert_dir is anomaly; result: {result} args: {args}")
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during insert_dir: {e}")
        error_logger.error(f"Exception occurred during insert_dir: {e}")
        return None

def select_dir1(table, *args):
    """select data in the database."""
    if not args:
        info_logger.info("No arguments provided for select_dir1")
        error_logger.error("No arguments provided for select_dir1")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_D1.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_dir1: {e}")
        error_logger.error(f"Exception occurred during select_dir1: {e}")
        return None

def select_dir2(table, *args):
    """select data in the database."""
    if not args:
        info_logger.info("No arguments provided for select_dir1")
        error_logger.error("No arguments provided for select_dir1")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_D2.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_dir2: {e}")
        error_logger.error(f"Exception occurred during select_dir2: {e}")
        return None

def select_dir3(table, *args):
    """select data in the database."""
    if not args:
        info_logger.info("No arguments provided for select_row_dir")
        error_logger.error("No arguments provided for select_row_dir")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_D3.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_dir3: {e}")
        error_logger.error(f"Exception occurred during select_dir3: {e}")
        return None
    
def select_dir4(table, *args):
    """select data in the database."""
    if not args:
        info_logger.info("No arguments provided for select_row_dir")
        error_logger.error("No arguments provided for select_row_dir")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_D4.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_dir4: {e}")
        error_logger.error(f"Exception occurred during select_dir4: {e}")
        return None    

def update_dir(table, *args):
    """Update a directory in the database."""

    if not args:
        info_logger.info("No arguments provided for update_dir")
        error_logger.error("No arguments provided for update_dir")
        return None
    
    DB = DBManager.get_instance()
    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    try:
        result = DB.update_query(SqlQuery.update_D1.format(table), args)
        if result == 1:
            info_logger.info(f"{args} is updated successfully")
        else:
            info_logger.info(f"update_dir is anomaly; result: {result} args: {args}")
            warning_logger.warning.error(f"update_dir is anomaly; result: {result} args: {args}")
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during update_dir: {e}")
        error_logger.error(f"Exception occurred during update_dir: {e}")
        return None

def insert_new_file(table, *args):
    """Inserts a new directory into the database."""
    if not args:
        info_logger.info("No arguments provided for insert_dir")
        error_logger.error("No arguments provided for insert_dir")
        return None
    
    DB = DBManager.get_instance()
    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.insert_query(SqlQuery.insert_F1.format(table), args)
        if result == 1:
            info_logger.info(f"{args} is inserted successfully")
        else:
            info_logger.info(f"insert_new_file is anomaly; result: {result} args: {args}")
            warning_logger.warning(f"insert_new_file is anomaly; result: {result} args: {args}")
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during insert_new_file: {e}")
        error_logger.error(f"Exception occurred during insert_new_file: {e}")
        return None


def select_all_files(table, *args):
    """select a directory in the database."""
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    try:
        result = DB.select_query(SqlQuery.select_F1.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_all_files: {e}")
        error_logger.error(f"Exception occurred during select_all_files: {e}")
        return None

def select_file(table, *args):
    """select a file in the database."""
    if not args:
        info_logger.info("No arguments provided for select_file")
        error_logger.error("No arguments provided for select_file")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_F2.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_file: {e}")
        error_logger.error(f"Exception occurred during select_file: {e}")
        return None

def select_file_revised(table, *args):
    """select a file in the database."""
    if not args:
        info_logger.info("No arguments provided for select_file_revised")
        error_logger.error("No arguments provided for select_file_revised")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_F3.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_file_revised: {e}")
        error_logger.error(f"Exception occurred during select_file_revised: {e}")
        return None

def select_file_max_num(table, *args):
    """select a file in the database."""
    if not args:
        info_logger.info("No arguments provided for select_file_max_num")
        error_logger.error("No arguments provided for select_file_max_num")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_F4.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_file_max_num: {e}")
        error_logger.error(f"Exception occurred during select_file_max_num: {e}")
        return None

def select_file_max_rev(table, *args):
    """select a file in the database."""
    if not args:
        info_logger.info("No arguments provided for select_file_max_rev")
        error_logger.error("No arguments provided for select_file_max_rev")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.select_query(SqlQuery.select_F5.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_file_max_rev: {e}")
        error_logger.error(f"Exception occurred during select_file_max_rev: {e}")
        return None

def select_file_flag(table, *args):
    """select a file in the database."""
    if not args:
        info_logger.info("No arguments provided for select_file_max_rev")
        error_logger.error("No arguments provided for select_file_max_rev")
        return None
    
    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:    
        result = DB.select_query(SqlQuery.select_F6.format(table), args)
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during select_file_flag: {e}")
        error_logger.error(f"Exception occurred during select_file_flag: {e}")
        return None

def update_file(table, *args):
    """Update a directory in the database."""

    if not args:
        info_logger.info("No arguments provided for update_file")
        error_logger.error("No arguments provided for update_file")
        return None
    
    DB = DBManager.get_instance()
    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None

    try:
        result = DB.update_query(SqlQuery.update_F1.format(table), args)
        if result == 1:
            info_logger.info(f"{args} is updated successfully")
        else:
            info_logger.info(f"update_file is anomaly; result: {result} args: {args}")
            warning_logger.warning(f"update_file is anomaly; result: {result} args: {args}")
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during update_file: {e}")
        error_logger.error(f"Exception occurred during update_file: {e}")
        return None

def finish_off_numbering(table, *args):
    """Scale the number of files in each directory."""

    DB = DBManager.get_instance()

    if DB is None:
        info_logger.info("Database connection is not established")
        error_logger.error("Database connection is not established")
        return None
    
    try:
        result = DB.update_query(SqlQuery.update_F2.format(table), args)
        if result == 1:
            info_logger.info("numbering finish off executed successfully")
        else:
            info_logger.info(f"finish_off_numbering is anomaly; result: {result} args: {args}")
            warning_logger.warning(f"finish_off_numbering is anomaly; result: {result} args: {args}")
        return handling_result(result)
    except Exception as e:
        info_logger.info(f"Exception occurred during finish_off_numbering: {e}")
        error_logger.error(f"Exception occurred during finish_off_numbering: {e}")
        return None

def handling_result(result):
    if(type(result) == list):
        if(result is None):
            return None
        elif(len(result) == 0):
            return None
        elif(len(result) == 1):
            if(type(result[0]) == tuple):
                if(len(result[0]) > 1):
                    return result[0]
                else:
                    return result[0][0]
            else:
                return result[0]
        else:
            return result
    else:
        return result