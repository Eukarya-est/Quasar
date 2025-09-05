import os
import sys
import datetime as time

# Add the parent directory to sys.path to allow imports from the main codebase
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import properties.db_table as TABLE
import properties.validation_type as TYPE
import properties.path as PATH
import v_and_v as vv
from logger import debug_logger, info_logger, warning_logger, error_logger

def test_verify_dir():
    test_count = 0
    pass_count = 0
    try:
        #Test1: Valid directory 
        test_count += 1
        path = PATH.TEST
        directory = "valid_case"
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print("Test1 Passed")

        #Test2: Invalid directory
        test_count += 1
        path = PATH.TEST
        directory = "invalid_case"
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print("Test2 Passed")

        #Test3: Mix directory
        test_count += 1
        path = PATH.TEST
        directory = "mix_case"
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print("Test3 Passed")

        #Test4: empty directory
        test_count += 1
        path = PATH.TEST
        directory = "empty_case"
        result = vv.verify_dir(path, directory)
        debug_logger.debug(result)
        assert result == TYPE.VERIFIED
        pass_count += 1
        print("Test4 Passed")

        #Test5: .git directory
        test_count += 1
        directory = PATH.GIT
        result = vv.verify_dir(None, directory)
        debug_logger.debug(result)
        assert result == TYPE.UNVERIFIED
        pass_count += 1
        print("Test5 Passed")

        #Final test result
        debug_logger.debug(f"test_count: {test_count} / pass_count: {pass_count}")
        assert pass_count == test_count
        print(f"Test Passed All; {pass_count} / {test_count}")
    except AssertionError:
        print(f"Test Failed; Test {test_count}")
    except Exception as e:
        print("Test Error")
        error_logger.error(e)

