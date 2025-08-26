from properties.db_table import DBtable as TABLE
import db_manager
from logger import debug_logger, info_logger, warning_logger, error_logger
from properties.sql_query import SqlQuery

def select_all_dir():
    """select a directory in the database."""
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = DB.select_query(SqlQuery.select_all_B1.format(TABLE.directories))
    return result

def select_dir(*args):
    """select a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for select_dir")
        return
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.select_query(SqlQuery.select_row_B1.format(TABLE.directories), args)
    return result

def insert_dir(*args):
    """Inserts a new directory into the database."""
    if not args:
        error_logger.error("No arguments provided for insert_dir")
        return
    
    DB = db_manager.DBManager().get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.insert_query(SqlQuery.insert_row_B1.format(TABLE.directories), args)
    if result == 1:
        info_logger.info(f"Directory {args[0]} inserted successfully")
    else:
        warning_logger.warning(f"Insert directory is anomaly; {args[0]}")
    return result
    
def update_dir(cd, *args):
    """Update a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for update_dir")
        return
    
    DB = db_manager.DBManager().get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.update_query(SqlQuery.update_row_B1.format(TABLE.directories), cd, args)
    if result == 1:
        info_logger.info(f"Directory {args[0]} updated successfully")
    else:
        warning_logger.warning(f"Update directory is anomaly; {args[0]}")
    return result

def select_all_files(*args):
    """select a directory in the database."""
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.select_query(SqlQuery.select_all_A1.format(TABLE.files), args)
    return result

def select_file(*args):
    """select a file in the database."""
    if not args:
        error_logger.error("No arguments provided for select_dir")
        return
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.select_query(SqlQuery.select_row_A2, args)
    return result

def select_file_max_num(*args):
    """select a file in the database."""
    if not args:
        error_logger.error("No arguments provided for select_dir")
        return
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.select_query(SqlQuery.select_max_num_A, args)
    return result

def select_file_max_rev(*args):
    """select a file in the database."""
    if not args:
        error_logger.error("No arguments provided for select_dir")
        return
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.select_query(SqlQuery.select_max_rev_A, args)
    return result

def insert_new_file(*args):
    """Inserts a new directory into the database."""
    if not args:
        error_logger.error("No arguments provided for insert_dir")
        return
    
    DB = db_manager.DBManager().get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.insert_query(SqlQuery.insert_row_A, args)
    if result == 1:
        info_logger.info(f"File {args[0]} inserted successfully")
    else:
        warning_logger.warning(f"Update file is anomaly; {args[0]}")
    return result
    
def update_file(cd, *args):
    """Update a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for update_dir")
        return
    
    DB = db_manager.DBManager().get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.update_query(SqlQuery.update_row_A1, cd, args)
    if result == 1:
        info_logger.info(f"file {args[3]} updated successfully")
    else:
        warning_logger.warning(f"Update file is anomaly; {args[3]}")
    return result

def finish_off_numbering(number, *args):
    """Scale the number of files in each directory."""
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    result = db_manager.DBManager.update_query(SqlQuery.update_row_A2, number, args)
    if result == 1:
        info_logger.info("numbering finish off executed successfully")
    else:
        warning_logger.warning("finish_off_numbering is anomaly")
    return result