from _typeshed import Incomplete

__all__ = ['tunnel_connection', 'ssh_tunnel', 'openssh_tunnel', 'paramiko_tunnel', 'try_passwordless_ssh']

class SSHException(Exception): ...

def try_passwordless_ssh(server, keyfile, paramiko: Incomplete | None = None):
    """Attempt to make an ssh connection without a password.
    This is mainly used for requiring password input only once
    when many tunnels may be connected to the same server.

    If paramiko is None, the default for the platform is chosen.
    """
def tunnel_connection(socket, addr, server, keyfile: Incomplete | None = None, password: Incomplete | None = None, paramiko: Incomplete | None = None, timeout: int = 60):
    """Connect a socket to an address via an ssh tunnel.

    This is a wrapper for socket.connect(addr), when addr is not accessible
    from the local machine.  It simply creates an ssh tunnel using the remaining args,
    and calls socket.connect('tcp://localhost:lport') where lport is the randomly
    selected local port of the tunnel.

    """
def openssh_tunnel(lport, rport, server, remoteip: str = '127.0.0.1', keyfile: Incomplete | None = None, password: Incomplete | None = None, timeout: int = 60):
    """Create an ssh tunnel using command-line ssh that connects port lport
    on this machine to localhost:rport on server.  The tunnel
    will automatically close when not in use, remaining open
    for a minimum of timeout seconds for an initial connection.

    This creates a tunnel redirecting `localhost:lport` to `remoteip:rport`,
    as seen from `server`.

    keyfile and password may be specified, but ssh config is checked for defaults.

    Parameters
    ----------

    lport : int
        local port for connecting to the tunnel from this machine.
    rport : int
        port on the remote machine to connect to.
    server : str
        The ssh server to connect to. The full ssh server string will be parsed.
        user@server:port
    remoteip : str [Default: 127.0.0.1]
        The remote ip, specifying the destination of the tunnel.
        Default is localhost, which means that the tunnel would redirect
        localhost:lport on this machine to localhost:rport on the *server*.

    keyfile : str; path to public key file
        This specifies a key to be used in ssh login, default None.
        Regular default ssh keys will be used without specifying this argument.
    password : str;
        Your ssh password to the ssh server. Note that if this is left None,
        you will be prompted for it if passwordless key based login is unavailable.
    timeout : int [default: 60]
        The time (in seconds) after which no activity will result in the tunnel
        closing.  This prevents orphaned tunnels from running forever.
    """
def paramiko_tunnel(lport, rport, server, remoteip: str = '127.0.0.1', keyfile: Incomplete | None = None, password: Incomplete | None = None, timeout: int = 60):
    """launch a tunner with paramiko in a subprocess. This should only be used
    when shell ssh is unavailable (e.g. Windows).

    This creates a tunnel redirecting `localhost:lport` to `remoteip:rport`,
    as seen from `server`.

    If you are familiar with ssh tunnels, this creates the tunnel:

    ssh server -L localhost:lport:remoteip:rport

    keyfile and password may be specified, but ssh config is checked for defaults.


    Parameters
    ----------

    lport : int
        local port for connecting to the tunnel from this machine.
    rport : int
        port on the remote machine to connect to.
    server : str
        The ssh server to connect to. The full ssh server string will be parsed.
        user@server:port
    remoteip : str [Default: 127.0.0.1]
        The remote ip, specifying the destination of the tunnel.
        Default is localhost, which means that the tunnel would redirect
        localhost:lport on this machine to localhost:rport on the *server*.

    keyfile : str; path to public key file
        This specifies a key to be used in ssh login, default None.
        Regular default ssh keys will be used without specifying this argument.
    password : str;
        Your ssh password to the ssh server. Note that if this is left None,
        you will be prompted for it if passwordless key based login is unavailable.
    timeout : int [default: 60]
        The time (in seconds) after which no activity will result in the tunnel
        closing.  This prevents orphaned tunnels from running forever.

    """
ssh_tunnel = openssh_tunnel
