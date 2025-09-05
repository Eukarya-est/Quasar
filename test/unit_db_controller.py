import os
import sys
import datetime as time

# Add the parent directory to sys.path to allow imports from the main codebase
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import properties.db_table as TABLE
import properties.validation_type as TYPE
import db_controller
import data_manager
from logger import debug_logger, info_logger, warning_logger, error_logger

def test_insert_dir():
    try:
        current_datetime = time.datetime.now()
        now = time.datetime.strftime(current_datetime, "%Y%m%d%H%M%S")

        result = db_controller.insert_dir(TABLE.DIR_TEST, f"TEST DIR {now}", TYPE.VALID)
        debug_logger.debug(result)
        
        assert result == 1
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_col_dir():
    try:
        result = db_controller.select_col_dir(TABLE.DIR_TEST, TYPE.VALID)
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_row_dir():
    try:
        result = db_controller.select_row_dir(TABLE.DIR_TEST, "test_directory")
        debug_logger.debug(result)
        
        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_row_dir2():
    try:
        result = db_controller.select_row_dir2(TABLE.DIR_TEST, "test_directory")
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_row_dir3():
    try: 
        directory = "TEST DIR 20250903224106"
        result = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_update_dir():
    try: 
        directory = "TEST DIR 20250903224106"
        case = db_controller.select_row_dir2(TABLE.DIR_TEST, directory)
        debug_logger.debug(case)
        if(case == TYPE.INVALID):
            result = db_controller.update_dir(TABLE.DIR_TEST, TYPE.VALID, directory)
        else:
            result = db_controller.update_dir(TABLE.DIR_TEST, TYPE.INVALID, directory)
        debug_logger.debug(result)
        
        assert result == 1
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_insert_file():
    try:
        directory = "TEST DIR 20250904080517"
        path = "./test_case/valid_case"
        file_list = os.listdir(f"{path}")
        len_file = len(file_list)
        count = 0
        debug_logger.debug(file_list)
        for file in file_list:
            store = data_manager.set_file_info_init(f"{path}/{file}")
            cover = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
            num = db_controller.select_file_max_num(TABLE.FILES_TEST, directory)
            revision = db_controller.select_file_max_rev(TABLE.FILES_TEST, directory, file)
            debug_logger.debug(cover)
            debug_logger.debug(num)
            debug_logger.debug(revision)
            store._cover = data_manager.get_cover(cover)
            store._num = data_manager.get_num(num)
            store._revision = data_manager.get_revision(revision)
            db_controller.update_file(TABLE.FILES_TEST, TYPE.VALID, store.cover, store.title)

            result = db_controller.insert_new_file(TABLE.FILES_TEST, store.cover, store.number, store.revision, store.created, store.revised, store.title, store.file_name, TYPE.VALID)
            debug_logger.debug(result)
            count += result

        assert count == len_file
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_all_files():
    try:
        directory = "TEST DIR 20250904080517"
        cd = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(cd)
        result = db_controller.select_all_files(TABLE.FILES_TEST, cd)
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_file():
    try:
        directory = "TEST DIR 20250904080517"
        file = "valid_2.md"
        cd = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(cd)
        result = db_controller.select_file(TABLE.FILES_TEST, cd, file)
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_file_max_num():
    try:
        directory = "TEST DIR 20250904080517"
        cd = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(cd)
        result = db_controller.select_file_max_num(TABLE.FILES_TEST, cd)
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_select_file_max_rev():
    try:
        directory = "TEST DIR 20250904080517"
        file = "valid_2.md"
        cd = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(cd)
        result = db_controller.select_file_max_rev(TABLE.FILES_TEST, cd, file)
        debug_logger.debug(result)

        assert result is not None
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_update_file():
    try:
        directory = "TEST DIR 20250904080517"
        file = "valid_2.md"
        cd = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(cd)
        case = db_controller.select_file(TABLE.FILES_TEST, cd, file)
        debug_logger.debug(case)
        if(case == TYPE.INVALID):
            result = db_controller.update_file(TABLE.FILES_TEST, TYPE.VALID, cd, file)
        else:
            result = db_controller.update_file(TABLE.FILES_TEST, TYPE.INVALID, cd, file)
        debug_logger.debug(result)

        assert result == 1
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_finish_off_numbering():
    try:
        directory = "TEST DIR 20250904080517"
        file = "valid_2.md"
        num = 2
        cd = db_controller.select_row_dir3(TABLE.DIR_TEST, directory)
        debug_logger.debug(cd)
        result = db_controller.finish_off_numbering(TABLE.FILES_TEST, num, cd, file)
        debug_logger.debug(result)

        assert result == 1
        print("Test Passed")
    except AssertionError:
        print("Test Failed")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)
