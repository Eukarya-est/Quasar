import mysql.connector
from mysql.connector import Error

from properties.db_config import DBconfig
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
                user=DBconfig.user.value,
                password=DBconfig.password.value,
                host=DBconfig.host.value, # name of the mysql service as set in the docker compose file
                database=DBconfig.database.value,
                port=DBconfig.port.value,            
            )
        except Error as e:
            error_logger.error(f"Error connecting to the database: {e}")
            self.connection = None
        info_logger.info("Successfully connected to the database")

    def insert_query(self, query, values):
        """Executes an insert query."""
        result = None
        if not self.connection or not self.connection.is_connected():
            info_logger.info("No active database connection for insert_query")
            error_logger.error("No active database connection for insert_query")
            return result
        
        cursor = self.connection.cursor()

        try:
            cursor.execute(query, values)
            self.connection.commit()
            result = cursor.rowcount
            info_logger.info("Query executed successfully; insert_query")
        except Error as e:
            info_logger.info(f"Error insert_query: {e}")
            error_logger.error(f"Error insert_query: {e}")
            self.connection.rollback()
            raise e
        finally:
            cursor.close()
            return result

    def select_query(self, query, values):
        """Executes a select query and returns the result."""
        result = None
        if not self.connection or not self.connection.is_connected():
            info_logger.info("No active database connection for select_query")
            error_logger.error("No active database connection for select_query")
            return result
        
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            info_logger.info("Query executed successfully; select_query")
        except Error as e:
            info_logger.info(f"Error select_query: {e}")
            error_logger.error(f"Error select_query: {e}")
            self.connection.rollback()
            raise e
        finally:
            cursor.close()
            return result
    
    def update_query(self, query, values):
        """Executes an update query."""
        result = None
        if not self.connection or not self.connection.is_connected():
            info_logger.info("No active database connection for select_query")
            error_logger.error("No active database connection for select_query")
            return result
        
        cursor = self.connection.cursor()

        try:
            cursor.execute(query, values)
            self.connection.commit()
            result = cursor.rowcount
            info_logger.info("Query executed successfully; update_query")
        except Error as e:
            info_logger.info(f"Error update_query: {e}")
            error_logger.error(f"Error update_query: {e}")
            self.connection.rollback()
            raise e
        finally:
            cursor.close()
            return result

    def close_connection(self):
        """Closes the database connection."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            info_logger.info("Database connection closed")
        else:
            info_logger.info("No active database connection to close")
            warning_logger.warning("No active database connection to close")
        self.connection = None
        self.cursor = None

    @staticmethod
    def get_instance():
        """Returns a singleton instance of DBManager."""
        if not hasattr(DBManager, "_instance"):
            DBManager._instance = DBManager()
        return DBManager._instance
    
