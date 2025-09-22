import os
import sys

# Add the parent directory to sys.path to allow imports from the main codebase
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import machine
from logger import debug_logger, info_logger, warning_logger, error_logger

def main():
    with open(f"./test_case/valid_case/valid3.html", "r", encoding="utf-8") as f:
            content = f.read()
    extracted_content = machine.extract(content)
    labeled_content = machine.label(extracted_content, 'valid_case')
    managed_content = machine.manage_pre(extracted_content)
    debug_logger.debug(managed_content)
    final_content = managed_content


if __name__ == "__main__":
    main()