from _typeshed import Incomplete

__all__ = ['copy', 'execute', 'kill', 'getpid', 'getppid', 'getchild', 'serve', 'connect', 'randomport']

def copy(source, destination: Incomplete | None = None, **kwds):
    """copy source to (possibly) remote destination

Execute a copy, and return the copier. Use 'kill' to kill the copier, and 
'pid' to get the process id for the copier.

Args:
    source      -- path string of source 'file'
    destination -- path string for destination target
  """
def execute(command, host: Incomplete | None = None, bg: bool = True, **kwds):
    """execute a command (possibly) on a remote host

Execute a process, and return the launcher. Use 'response' to retrieve the
response from the executed command. Use 'kill' to kill the launcher, and 'pid'
to get the process id for the launcher.

Args:
    command -- command string to be executed
    host    -- hostname of execution target  [default = None (i.e. run locally)]
    bg      -- run as background process?  [default = True]
  """
def kill(pid, host: Incomplete | None = None, **kwds):
    """kill a process (possibly) on a remote host

Args:
    pid   -- process id
    host  -- hostname where process is running [default = None (i.e. locally)]
  """
def getpid(target: Incomplete | None = None, host: Incomplete | None = None, all: bool = False, **kwds):
    """get the process id for a target process (possibly) running on remote host

This method should only be used as a last-ditch effort to find a process id.
This method __may__ work when a child has been spawned and the pid was not
registered... but there's no guarantee.

If target is None, then get the process id of the __main__  python instance.

Args:
    target -- string name of target process
    host   -- hostname where process is running
    all    -- get all resulting lines from query?  [default = False]
  """
def getppid(pid: Incomplete | None = None, host: Incomplete | None = None, group: bool = False):
    """get parent process id (ppid) for the given process

If pid is None, the pid of the __main__  python instance will be used.

Args:
    pid    -- process id
    host   -- hostname where process is running
    group  -- get parent group id (pgid) instead of direct parent id?
  """
def getchild(pid: Incomplete | None = None, host: Incomplete | None = None, group: bool = False):
    """get all child process ids for the given parent process id (ppid)

If pid is None, the pid of the __main__  python instance will be used.

Args:
    pid    -- parent process id
    host   -- hostname where process is running
    group  -- get process ids for the parent group id (pgid) instead?
  """
def randomport(host: Incomplete | None = None):
    """select a open port on a (possibly) remote host

Args:
    host -- hostname on which to select a open port
  """
def connect(host, port: Incomplete | None = None, through: Incomplete | None = None):
    """establish a secure tunnel connection to a remote host at the given port

Args:
    host     -- hostname to which a tunnel should be established
    port     -- port number (on host) to connect the tunnel to
    through  -- 'tunnel-through' hostname  [default = None]
  """
def serve(server, host: Incomplete | None = None, port: Incomplete | None = None, profile: str = '.bash_profile'):
    """begin serving RPC requests

Args:
    server: name of RPC server  (i.e. 'ppserver')
    host: hostname on which a server should be launched
    port: port number (on host) that server will accept request at
    profile: file to configure the user's environment [default='.bash_profile']
  """
