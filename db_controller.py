import data_pipe
import db_manager
from logger import debug_logger, info_logger, warning_logger, error_logger
from properties.sql_query import SqlQuery

def select_dir(*args):
    """select a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for select_dir")
        return
    
    DB = db_manager.DBManager().get_instance()

    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    db_manager.DBManager.select_query(SqlQuery.select_row_B1, args)

def insert_dir(*args):
    """Inserts a new directory into the database."""
    if not args:
        error_logger.error("No arguments provided for insert_dir")
        return
    
    DB = db_manager.DBManager().get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    db_manager.DBManager.insert_query(SqlQuery.insert_row_B, args)
    
def update_dir(*args):
    """Update a directory in the database."""
    if not args:
        error_logger.error("No arguments provided for update_dir")
        return
    
    DB = db_manager.DBManager().get_instance()
    if DB is None:
        error_logger.error("Database connection is not established")
        return
    
    db_manager.DBManager.update_query(SqlQuery.update_row_B, args)

def insert_new_file(data):
    inquiry = db_manager.DBManager.select_query(data.cover, data.title)
    if inquiry is None :
        db_manager.DBManager.insert_query
    
def select_file(data):
    inquiry = db_manager.DBManager.select_query(data.cover, data.title)