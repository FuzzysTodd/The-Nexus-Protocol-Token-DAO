import ctypes
from _typeshed import Incomplete

LPDWORD: Incomplete
LPHANDLE: Incomplete
ULONG_PTR: Incomplete

class SECURITY_ATTRIBUTES(ctypes.Structure): ...

LPSECURITY_ATTRIBUTES: Incomplete

class STARTUPINFO(ctypes.Structure): ...

LPSTARTUPINFO: Incomplete

class PROCESS_INFORMATION(ctypes.Structure): ...

LPPROCESS_INFORMATION: Incomplete
ERROR_HANDLE_EOF: int
ERROR_BROKEN_PIPE: int
ERROR_NO_DATA: int
HANDLE_FLAG_INHERIT: int
STARTF_USESTDHANDLES: int
CREATE_SUSPENDED: int
CREATE_NEW_CONSOLE: int
CREATE_NO_WINDOW: int
STILL_ACTIVE: int
WAIT_TIMEOUT: int
WAIT_FAILED: int
INFINITE: int
DUPLICATE_SAME_ACCESS: int
ENABLE_ECHO_INPUT: int
ENABLE_LINE_INPUT: int
ENABLE_PROCESSED_INPUT: int
GetLastError: Incomplete
CreateFile: Incomplete
CreatePipe: Incomplete
CreateProcess: Incomplete
GetExitCodeProcess: Incomplete
GetCurrentProcess: Incomplete
ResumeThread: Incomplete
ReadFile: Incomplete
WriteFile: Incomplete
GetConsoleMode: Incomplete
SetConsoleMode: Incomplete
FlushConsoleInputBuffer: Incomplete
WaitForSingleObject: Incomplete
DuplicateHandle: Incomplete
SetHandleInformation: Incomplete
CloseHandle: Incomplete
CommandLineToArgvW: Incomplete
LocalFree: Incomplete

class AvoidUNCPath:
    '''A context manager to protect command execution from UNC paths.

    In the Win32 API, commands can\'t be invoked with the cwd being a UNC path.
    This context manager temporarily changes directory to the \'C:\' drive on
    entering, and restores the original working directory on exit.

    The context manager returns the starting working directory *if* it made a
    change and None otherwise, so that users can apply the necessary adjustment
    to their system calls in the event of a change.

    Examples
    --------
    ::
        cmd = \'dir\'
        with AvoidUNCPath() as path:
            if path is not None:
                cmd = \'"pushd %s &&"%s\' % (path, cmd)
            os.system(cmd)
    '''
    path: Incomplete
    is_unc_path: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class Win32ShellCommandController:
    """Runs a shell command in a 'with' context.

    This implementation is Win32-specific.

    Example:
        # Runs the command interactively with default console stdin/stdout
        with ShellCommandController('python -i') as scc:
            scc.run()

        # Runs the command using the provided functions for stdin/stdout
        def my_stdout_func(s):
            # print or save the string 's'
            write_to_stdout(s)
        def my_stdin_func():
            # If input is available, return it as a string.
            if input_available():
                return get_input()
            # If no input available, return None after a short delay to
            # keep from blocking.
            else:
                time.sleep(0.01)
                return None
      
        with ShellCommandController('python -i') as scc:
            scc.run(my_stdout_func, my_stdin_func)
    """
    cmd: Incomplete
    mergeout: Incomplete
    def __init__(self, cmd, mergeout: bool = True) -> None:
        """Initializes the shell command controller.

        The cmd is the program to execute, and mergeout is
        whether to blend stdout and stderr into one output
        in stdout. Merging them together in this fashion more
        reliably keeps stdout and stderr in the correct order
        especially for interactive shell usage.
        """
    piProcInfo: Incomplete
    hstdin: Incomplete
    hstdout: Incomplete
    hstderr: Incomplete
    def __enter__(self): ...
    def run(self, stdout_func: Incomplete | None = None, stdin_func: Incomplete | None = None, stderr_func: Incomplete | None = None):
        """Runs the process, using the provided functions for I/O.

        The function stdin_func should return strings whenever a
        character or characters become available.
        The functions stdout_func and stderr_func are called whenever
        something is printed to stdout or stderr, respectively.
        These functions are called from different threads (but not
        concurrently, because of the GIL).
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def system(cmd) -> None:
    """Win32 version of os.system() that works with network shares.

    Note that this implementation returns None, as meant for use in IPython.

    Parameters
    ----------
    cmd : str
        A command to be executed in the system shell.

    Returns
    -------
    None : we explicitly do NOT return the subprocess status code, as this
    utility is meant to be used extensively in IPython, where any return value
    would trigger : func:`sys.displayhook` calls.
    """
