def kill_process_tree(process, use_psutil: bool = True) -> None:
    """Terminate process and its descendants with SIGKILL"""
def recursive_terminate(process, use_psutil: bool = True) -> None: ...
def get_exitcodes_terminated_worker(processes):
    """Return a formatted string with the exitcodes of terminated workers.

    If necessary, wait (up to .25s) for the system to correctly set the
    exitcode of one terminated worker.
    """
