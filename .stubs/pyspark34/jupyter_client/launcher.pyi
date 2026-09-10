from subprocess import Popen
from typing import Any, Dict, List

__all__ = ['launch_kernel']

def launch_kernel(cmd: List[str], stdin: int | None = None, stdout: int | None = None, stderr: int | None = None, env: Dict[str, str] | None = None, independent: bool = False, cwd: str | None = None, **kw: Any) -> Popen:
    """Launches a localhost kernel, binding to the specified ports.

    Parameters
    ----------
    cmd : Popen list,
        A string of Python code that imports and executes a kernel entry point.

    stdin, stdout, stderr : optional (default None)
        Standards streams, as defined in subprocess.Popen.

    env: dict, optional
        Environment variables passed to the kernel

    independent : bool, optional (default False)
        If set, the kernel process is guaranteed to survive if this process
        dies. If not set, an effort is made to ensure that the kernel is killed
        when this process dies. Note that in this case it is still good practice
        to kill kernels manually before exiting.

    cwd : path, optional
        The working dir of the kernel process (default: cwd of this process).

    **kw: optional
        Additional arguments for Popen

    Returns
    -------

    Popen instance for the kernel subprocess
    """
