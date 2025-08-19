import mysql.connector
from mysql.connector import Error
import time

from properties.db_config import DbConfig
from logger import debug_logger, info_logger, warning_logger, error_logger

class DBManager:
    """
    This class manages the database connection and operttions.
    It uses the mysql.connector library to connect to a MySQL database.
    """

    def __init__(self):
        """Establishes a connection to the database."""
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                user=DbConfig.user.value,
                password=DbConfig.password.value,
                host=DbConfig.host.value, # name of the mysql service as set in the docker compose file
                database=DbConfig.database.value,
                port=DbConfig.port.value,            
            )
            if self.connection.is_connected():
                info_logger.info("Successfully connected to the database")
                self.cursor = self.connection.cursor()
        except Error as e:
            error_logger.error(f"Error connecting to the database: {e}")

    def select_query(self, query, values):
        """Executes a select query and returns the result."""
        result = None
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            info_logger.info("Query executed successfully; select_query")
        except Error as e:
            error_logger.error(f"Error select_query: {e}")
        finally:
            if self.cursor:
                self.cursor.close()
        return result
    
    def insert_query(self, query, values):
        """Executes an insert query."""
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            info_logger.info("Query executed successfully; insert_query")
        except Error as e:
            error_logger.error(f"Error insert_query: {e}")
            self.connection.rollback()
        finally:
            if self.cursor:
                self.cursor.close()
    
    def update_query(self, query, values):
        """Executes an update query."""
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            info_logger.info("Query executed successfully; update_query")
        except Error as e:
            error_logger.error(f"Error update_query: {e}")
            self.connection.rollback()
        finally:
            if self.cursor:
                self.cursor.close()

    def close_connection(self):
        """Closes the database connection."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            info_logger.info("Database connection closed")
        else:
            warning_logger.warning("No active database connection to close")
        self.connection = None
        self.cursor = None

    @staticmethod
    def get_instance():
        """Returns a singleton instance of DBManager."""
        if not hasattr(DBManager, "_instance"):
            DBManager._instance = DBManager()
        return DBManager._instance
    
