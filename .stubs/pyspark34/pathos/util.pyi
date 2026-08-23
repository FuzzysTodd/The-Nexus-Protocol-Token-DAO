def print_exc_info():
    """thread-safe return of string from print_exception call"""
def spawn(onParent, onChild):
    """a unidirectional fork wrapper

Calls onParent(pid, fromchild) in parent process,
      onChild(pid, toparent) in child process.
    """
def spawn2(onParent, onChild):
    """a bidirectional fork wrapper

Calls onParent(pid, fromchild, tochild) in parent process,
      onChild(pid, fromparent, toparent) in child process.
    """
