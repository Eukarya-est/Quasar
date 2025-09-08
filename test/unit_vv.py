import os
import sys
import datetime as time

# Add the parent directory to sys.path to allow imports from the main codebase
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import properties.db_table as TABLE
import properties.validation_type as TYPE
import properties.path as PATH
import properties.test as TESTCASE
import v_and_v as vv
import db_controller
import data_manager
from logger import debug_logger, info_logger, warning_logger, error_logger

def test_verify_dir():
    test_count = 0
    pass_count = 0
    try:
        # Test 1: Valid directory 
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.VALID
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 2: Invalid directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INVALID
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 3: Mix directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.MIX
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 4: empty directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.EMPTY
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 5: Not directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.NOT_DIR
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.UNVERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        #T Test 6: Inner directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INNER_DIR
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 7: .git directory
        test_count += 1
        directory = PATH.GIT
        result = vv.verify_dir(None, directory)
        debug_logger.debug(result)
        assert result == TYPE.UNVERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Final test result
        debug_logger.debug(f"test_count: {test_count} / pass_count: {pass_count}")
        assert pass_count == test_count
        print(f"Test Passed All; {pass_count} / {test_count}")
    except AssertionError:
        print(f"Test Failed; Test {test_count}")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_validate_dir():
    test_count = 0
    pass_count = 0
    try:
        # Test 1: Valid directory 
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.VALID
        result = vv.validate_dir(TABLE.DIR_TEST, path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VALID
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 2: Invalid directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INVALID
        result = vv.validate_dir(TABLE.DIR_TEST, path, directory)
        debug_logger.debug(result)
        assert result == TYPE.INVALID
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 3: Mix directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.MIX
        result = vv.validate_dir(TABLE.DIR_TEST, path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VALID
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 4: Empty directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.EMPTY
        result = vv.validate_dir(TABLE.DIR_TEST, path, directory)
        debug_logger.debug(result)
        assert result == TYPE.INVALID
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 5: Inner directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INNER_DIR
        result = vv.validate_dir(TABLE.DIR_TEST, path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VALID
        pass_count += 1
        print(f"Test {test_count} Passed")

        #Final test result
        debug_logger.debug(f"test_count: {test_count} / pass_count: {pass_count}")
        assert pass_count == test_count
        print(f"Test Passed All; {pass_count} / {test_count}")
    except AssertionError:
        print(f"Test Failed; Test {test_count}")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_verify_file():
    test_count = 0
    pass_count = 0
    try:
        # Test 1: Markdown file 
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INNER_DIR
        file = "valid.md"
        result = vv.verify_file(f"{path}/{directory}/{file}")
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 2: Non-Markdown file
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INNER_DIR
        file = "invalid.txt"
        result = vv.verify_file(f"{path}/{directory}/{file}")
        debug_logger.debug(result)
        assert result == TYPE.UNVERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 3: Inner directory
        test_count += 1
        path = PATH.TEST
        directory = TESTCASE.INNER_DIR
        file = "inner_dir"
        result = vv.verify_file(f"{path}/{directory}/{file}")
        debug_logger.debug(result)
        assert result == TYPE.UNVERIFIED
        pass_count += 1
        print(f"Test {test_count} Passed")

        #Final test result
        debug_logger.debug(f"test_count: {test_count} / pass_count: {pass_count}")
        assert pass_count == test_count
        print(f"Test Passed All; {pass_count} / {test_count}")
    except AssertionError:
        print(f"Test Failed; Test {test_count}")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

def test_validate_file():
    test_count = 0
    pass_count = 0
    try:
        # Test 1: TYPE.NEW
        test_count += 1
        directory = "TEST DIR 20250903223735"
        file = "./test_case/valid_case/valid.md"
        store = data_manager.set_file_info_init(f"{file}")
        cd = db_controller.select_dir3(TABLE.DIR_TEST, directory)
        store._cover = data_manager.get_cover(cd) 
        result = vv.validate_file(TABLE.FILES_TEST, store)
        debug_logger.debug(result)
        assert result == TYPE.NEW
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 2: TYPE.UPDATE
        test_count += 1
        directory = "TEST DIR 20250903223525"
        file = "./test_case/valid_case/valid_2.md"
        store = data_manager.set_file_info_init(f"{file}")
        cd = db_controller.select_dir3(TABLE.DIR_TEST, directory)
        store._cover = data_manager.get_cover(cd) 
        result = vv.validate_file(TABLE.FILES_TEST, store)
        debug_logger.debug(result)
        assert result == TYPE.UPDATE
        pass_count += 1
        print(f"Test {test_count} Passed")

        # Test 3: TYPE.NOACTION
        test_count += 1
        directory = "TEST DIR 20250904080517"
        file = "./test_case/valid_case/valid.md"
        store = data_manager.set_file_info_init(f"{file}")
        cd = db_controller.select_dir3(TABLE.DIR_TEST, directory)
        store._cover = data_manager.get_cover(cd) 
        result = vv.validate_file(TABLE.FILES_TEST, store)
        debug_logger.debug(result)
        assert result == TYPE.NOACTION
        pass_count += 1
        print(f"Test {test_count} Passed")

        #Final test result
        debug_logger.debug(f"test_count: {test_count} / pass_count: {pass_count}")
        assert pass_count == test_count
        print(f"Test Passed All; {pass_count} / {test_count}")
    except AssertionError:
        print(f"Test Failed; Test {test_count}")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)