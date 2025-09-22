import os

from logger import debug_logger, info_logger, warning_logger, error_logger
import machine

def operate(directory, contents):

    # Convert Typora html to HTML
    contents = machine.extract(contents)
    contents = machine.manage_pre(contents)
    contents = machine.label(directory, contents)

    return contents
    