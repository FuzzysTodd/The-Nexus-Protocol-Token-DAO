import subprocess
from .util import LazyMixin
from _typeshed import Incomplete
from git.types import Literal, PathLike
from typing import Any, Dict, IO, Iterator, List, Sequence, Tuple, overload

__all__ = ['Git']

class Git(LazyMixin):
    """
    The Git class manages communication with the Git binary.

    It provides a convenient interface to calling the Git binary, such as in::

     g = Git( git_dir )
     g.init()                   # calls 'git init' program
     rval = g.ls_files()        # calls 'git ls-files' program

    ``Debugging``
        Set the GIT_PYTHON_TRACE environment variable print each invocation
        of the command to stdout.
        Set its value to 'full' to see details about the returned values.
    """
    re_unsafe_protocol: Incomplete
    git_exec_name: str
    GIT_PYTHON_TRACE: Incomplete
    USE_SHELL: bool
    GIT_PYTHON_GIT_EXECUTABLE: Incomplete
    @classmethod
    def refresh(cls, path: None | PathLike = None) -> bool:
        """This gets called by the refresh function (see the top level __init__)."""
    @classmethod
    def is_cygwin(cls) -> bool: ...
    @overload
    @classmethod
    def polish_url(cls, url: str, is_cygwin: Literal[False] = ...) -> str: ...
    @overload
    @classmethod
    def polish_url(cls, url: str, is_cygwin: None | bool = None) -> str: ...
    @classmethod
    def check_unsafe_protocols(cls, url: str) -> None:
        '''
        Check for unsafe protocols.

        Apart from the usual protocols (http, git, ssh),
        Git allows "remote helpers" that have the form ``<transport>::<address>``,
        one of these helpers (``ext::``) can be used to invoke any arbitrary command.

        See:

        - https://git-scm.com/docs/gitremote-helpers
        - https://git-scm.com/docs/git-remote-ext
        '''
    @classmethod
    def check_unsafe_options(cls, options: List[str], unsafe_options: List[str]) -> None:
        """
        Check for unsafe options.

        Some options that are passed to `git <command>` can be used to execute
        arbitrary commands, this are blocked by default.
        """
    class AutoInterrupt:
        """Kill/Interrupt the stored process instance once this instance goes out of scope. It is
        used to prevent processes piling up in case iterators stop reading.
        Besides all attributes are wired through to the contained process object.

        The wait method was overridden to perform automatic status code checking
        and possibly raise."""
        proc: Incomplete
        args: Incomplete
        status: Incomplete
        def __init__(self, proc: None | subprocess.Popen, args: Any) -> None: ...
        def __del__(self) -> None: ...
        def __getattr__(self, attr: str) -> Any: ...
        def wait(self, stderr: None | str | bytes = b'') -> int:
            """Wait for the process and return its status code.

            :param stderr: Previously read value of stderr, in case stderr is already closed.
            :warn: May deadlock if output or error pipes are used and not handled separately.
            :raise GitCommandError: if the return status is not 0"""
    class CatFileContentStream:
        """Object representing a sized read-only stream returning the contents of
        an object.
        It behaves like a stream, but counts the data read and simulates an empty
        stream once our sized content region is empty.
        If not all data is read to the end of the object's lifetime, we read the
        rest to assure the underlying stream continues to work."""
        def __init__(self, size: int, stream: IO[bytes]) -> None: ...
        def read(self, size: int = -1) -> bytes: ...
        def readline(self, size: int = -1) -> bytes: ...
        def readlines(self, size: int = -1) -> List[bytes]: ...
        def __iter__(self) -> Git.CatFileContentStream: ...
        def __next__(self) -> bytes: ...
        next = __next__
        def __del__(self) -> None: ...
    cat_file_header: Incomplete
    cat_file_all: Incomplete
    def __init__(self, working_dir: None | PathLike = None) -> None:
        """Initialize this instance with:

        :param working_dir:
           Git directory we should work in. If None, we always work in the current
           directory as returned by os.getcwd().
           It is meant to be the working tree directory if available, or the
           .git directory in case of bare repositories."""
    def __getattr__(self, name: str) -> Any:
        """A convenience method as it allows to call the command as if it was
        an object.

        :return: Callable object that will execute call _call_process with your arguments."""
    def set_persistent_git_options(self, **kwargs: Any) -> None:
        """Specify command line options to the git executable
        for subsequent subcommand calls.

        :param kwargs:
            is a dict of keyword arguments.
            These arguments are passed as in _call_process
            but will be passed to the git command rather than
            the subcommand.
        """
    @property
    def working_dir(self) -> None | PathLike:
        """:return: Git directory we are working on"""
    @property
    def version_info(self) -> Tuple[int, int, int, int]:
        """
        :return: tuple(int, int, int, int) tuple with integers representing the major, minor
            and additional version numbers as parsed from git version.
            This value is generated on demand and is cached."""
    @overload
    def execute(self, command: str | Sequence[Any], *, as_process: Literal[True]) -> AutoInterrupt: ...
    @overload
    def execute(self, command: str | Sequence[Any], *, as_process: Literal[False] = False, stdout_as_string: Literal[True]) -> str | Tuple[int, str, str]: ...
    @overload
    def execute(self, command: str | Sequence[Any], *, as_process: Literal[False] = False, stdout_as_string: Literal[False] = False) -> bytes | Tuple[int, bytes, str]: ...
    @overload
    def execute(self, command: str | Sequence[Any], *, with_extended_output: Literal[False], as_process: Literal[False], stdout_as_string: Literal[True]) -> str: ...
    @overload
    def execute(self, command: str | Sequence[Any], *, with_extended_output: Literal[False], as_process: Literal[False], stdout_as_string: Literal[False]) -> bytes: ...
    def environment(self) -> Dict[str, str]: ...
    def update_environment(self, **kwargs: Any) -> Dict[str, str | None]:
        """
        Set environment variables for future git invocations. Return all changed
        values in a format that can be passed back into this function to revert
        the changes:

        ``Examples``::

            old_env = self.update_environment(PWD='/tmp')
            self.update_environment(**old_env)

        :param kwargs: environment variables to use for git processes
        :return: dict that maps environment variables to their old values
        """
    def custom_environment(self, **kwargs: Any) -> Iterator[None]:
        """
        A context manager around the above ``update_environment`` method to restore the
        environment back to its previous state after operation.

        ``Examples``::

            with self.custom_environment(GIT_SSH='/bin/ssh_wrapper'):
                repo.remotes.origin.fetch()

        :param kwargs: see update_environment
        """
    def transform_kwarg(self, name: str, value: Any, split_single_char_options: bool) -> List[str]: ...
    def transform_kwargs(self, split_single_char_options: bool = True, **kwargs: Any) -> List[str]:
        """Transforms Python style kwargs into git command line options."""
    def __call__(self, **kwargs: Any) -> Git:
        """Specify command line options to the git executable
        for a subcommand call.

        :param kwargs:
            is a dict of keyword arguments.
            these arguments are passed as in _call_process
            but will be passed to the git command rather than
            the subcommand.

        ``Examples``::
            git(work_tree='/tmp').difftool()"""
    def get_object_header(self, ref: str) -> Tuple[str, str, int]:
        """Use this method to quickly examine the type and size of the object behind
        the given ref.

        :note: The method will only suffer from the costs of command invocation
            once and reuses the command in subsequent calls.

        :return: (hexsha, type_string, size_as_int)"""
    def get_object_data(self, ref: str) -> Tuple[str, str, int, bytes]:
        """As get_object_header, but returns object data as well.

        :return: (hexsha, type_string, size_as_int, data_string)
        :note: not threadsafe"""
    def stream_object_data(self, ref: str) -> Tuple[str, str, int, 'Git.CatFileContentStream']:
        """As get_object_header, but returns the data as a stream.

        :return: (hexsha, type_string, size_as_int, stream)
        :note: This method is not threadsafe, you need one independent Command instance per thread to be safe!"""
    def clear_cache(self) -> Git:
        """Clear all kinds of internal caches to release resources.

        Currently persistent commands will be interrupted.

        :return: self"""
