# db_controller.py
from db_manager import DBManager as DBManager
import properties.sql_query as SqlQuery
from logger import debug_logger, info_logger, warning_logger, error_logger

def insert_dir(table, *args):
    """Inserts a new directory into the database."""

    if not table:
        error_logger.error("No table name provided for insert_dir")
        return
    if not args:
        error_logger.error("No arguments provided for insert_dir")
        return

    DB = DBManager.get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.insert_query(SqlQuery.insert_row_B.format(table), args)
    if result == 1:
        info_logger.info(f"Directory {args[0]} inserted successfully")
    else:
        warning_logger.warning(f"Insert directory is anomaly; {args[0]}")
    return handling_result(result)

def select_col_dir(table, *args):
    """select a directory in the database."""
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_col_B1.format(table), args)
    return handling_result(result)

def select_row_dir(table, *args):
    """select a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for select_row_dir")
        return
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_row_B1.format(table), args)
    return handling_result(result)

def select_row_dir2(table, *args):
    """select a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for select_row_dir")
        return
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_row_B2.format(table), args)
    return handling_result(result)

def select_row_dir3(table, *args):
    """select a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for select_row_dir")
        return
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_row_B3.format(table), args)
    return handling_result(result)
    
def update_dir(table, *args):
    """Update a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for update_dir")
        return
    
    DB = DBManager.get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.update_query(SqlQuery.update_row_B1.format(table), args)
    if result == 1:
        info_logger.info(f"Directory {args[0]} updated successfully")
    else:
        warning_logger.warning(f"Update directory is anomaly; {args[0]}")
    return handling_result(result)

def insert_new_file(table, *args):
    """Inserts a new directory into the database."""
    if not args:
        error_logger.error("No arguments provided for insert_dir")
        return
    
    DB = DBManager.get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return

    result = DB.insert_query(SqlQuery.insert_row_A.format(table), args)
    if result == 1:
        info_logger.info(f"File {args[0]} inserted successfully")
    else:
        warning_logger.warning(f"Update file is anomaly; {args[0]}")
    return handling_result(result)

def select_all_files(table, *args):
    """select a directory in the database."""
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_col_A1.format(table), args)
    return handling_result(result)

def select_file(table, *args):
    """select a file in the database."""
    if not args:
        error_logger.error("No arguments provided for select_file")
        return
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_row_A2.format(table), args)
    return handling_result(result)

def select_file_max_num(table, *args):
    """select a file in the database."""
    if not args:
        error_logger.error("No arguments provided for select_file_max_num")
        return
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_max_A1.format(table), args)
    return handling_result(result)

def select_file_max_rev(table, *args):
    """select a file in the database."""
    if not args:
        error_logger.error("No arguments provided for select_file_max_rev")
        return
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_max_A2.format(table), args)
    return handling_result(result)
    
def update_file(table, *args):
    """Update a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for update_file")
        return
    
    DB = DBManager.get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return

    result = DB.update_query(SqlQuery.update_row_A1.format(table), args)
    if result == 1:
        info_logger.info(f"file {args[2]} updated successfully")
    else:
        warning_logger.warning(f"Update file is anomaly; {args[2]}")
    return handling_result(result)

def finish_off_numbering(table, *args):
    """Scale the number of files in each directory."""
    
    DB = DBManager.get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.update_query(SqlQuery.update_row_A2.format(table), args)
    if result == 1:
        info_logger.info("numbering finish off executed successfully")
    else:
        warning_logger.warning("finish_off_numbering is anomaly")
    return handling_result(result)

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