import sys
import unit_db_controller
import unit_vv
from logger import debug_logger, info_logger, warning_logger, error_logger

def main(*args):
    print("Running tests...;", args[0][1], args[0][2])
    module_name = "unit_" + args[0][1]
    function_name = args[0][2]

    if function_name in dir(sys.modules[module_name]):
        debug_logger.debug(f"{module_name} / {function_name}")
        getattr(sys.modules[module_name], function_name)()
    else:
        error_logger.error(f"Function {function_name} not found in module {args[0][1]}")
        print(f"Function {function_name} not found in module {args[0][1]}")
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv)