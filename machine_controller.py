import os

from logger import debug_logger, info_logger, warning_logger, error_logger
import machine

def operate(directory, contents):

    try:
        # Convert Typora html to HTML
        contents = machine.extract(contents)
        contents = machine.label(directory, contents)
    except Exception as e:
        error_logger.error(f"Fail to operation; {e}")

    return contents
    