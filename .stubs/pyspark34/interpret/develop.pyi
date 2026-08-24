from _typeshed import Incomplete

def print_debug_info(file: Incomplete | None = None) -> None:
    """This function varies version-by-version, prints debug info as a pretty string.

    Args:
        file: File to print to (default goes to sys.stdout).

    Returns:
        None
    """
def debug_info():
    """This function varies version-by-version, designed to help the authors of this package when there's an issue.

    Returns:
        A dictionary that contains debug info across the interpret package.
    """
def dynamic_system_info():
    """Provides dynamic system information (available memory etc.) as a dictionary.

    Returns:
        A dictionary containing dynamic system information.
    """
def static_system_info():
    """Provides static system information (machine architecture etc.) as a dictionary.

    Returns:
        A dictionary containing static system information.
    """
def debug_mode(log_filename: str = 'log.txt', log_level: str = 'INFO', native_debug: bool = True, simd: bool = True):
    '''Sets package into debug mode.

    Args:
        log_filename: A string that is the filepath to log to, or sys.stderr/sys.stdout.
        log_level: Logging level. For example, "DEBUG".
        native_debug: Load debug versions of native libraries if True.

    Returns:
        Logging handler.
    '''
def register_log(filename, level: str = 'DEBUG'):
    '''Registers file to have logs written to.

    Args:
        filename: A string that is the filepath to log to, or sys.stderr/sys.stdout.
        level: Logging level. For example, "DEBUG".

    Returns:
        Logging handler.
    '''
