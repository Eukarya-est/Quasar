import datetime as time

import data_manager
import data_store
from logger import debug_logger, info_logger, warning_logger, error_logger

def set_file_info(directory, file):

    cover = data_manager.get_cover(directory)
    num = data_manager.get_num()
    revision = data_manager.get_revision()    
    created_time = data_manager.get_created_time(file)
    revised_time = data_manager.get_modified_time(file)
    title = data_manager.get_title(file)
    file_name = data_manager.get_file_name(file)

    return data_store.DataStore(cover, num, revision, created_time, revised_time, title, file_name)