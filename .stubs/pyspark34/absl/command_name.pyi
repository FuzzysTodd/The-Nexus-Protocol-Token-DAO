def make_process_name_useful() -> None:
    """Sets the process name to something better than 'python' if possible."""
def set_kernel_process_name(name) -> None:
    """Changes the Kernel's /proc/self/status process name on Linux.

  The kernel name is NOT what will be shown by the ps or top command.
  It is a 15 character string stored in the kernel's process table that
  is included in the kernel log when a process is OOM killed.
  The first 15 bytes of name are used.  Non-ASCII unicode is replaced with '?'.

  Does nothing if /proc/self/comm cannot be written or prctl() fails.

  Args:
    name: bytes|unicode, the Linux kernel's command name to set.
  """
