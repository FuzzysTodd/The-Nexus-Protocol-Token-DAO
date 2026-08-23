__all__ = ['_main', 'freeze_support', 'set_executable', 'get_executable', 'get_preparation_data', 'get_command_line', 'import_main_path']

def set_executable(exe) -> None: ...
def get_executable(): ...
def freeze_support() -> None:
    """
    Run code for process object if this in not the main process
    """
def get_command_line(**kwds):
    """
    Returns prefix of command line used for spawning a child process
    """
def _main(fd, parent_sentinel): ...
def get_preparation_data(name):
    """
    Return info about parent needed by child to unpickle process object
    """
def import_main_path(main_path) -> None:
    """
    Set sys.modules['__main__'] to module at main_path
    """
