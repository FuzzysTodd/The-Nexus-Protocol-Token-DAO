import threading
from _typeshed import Incomplete
from paramiko.common import byte_chr as byte_chr, io_sleep as io_sleep
from paramiko.message import Message as Message
from paramiko.pkey import PKey as PKey, UnknownKeyType as UnknownKeyType
from paramiko.ssh_exception import AuthenticationException as AuthenticationException, SSHException as SSHException
from paramiko.util import asbytes as asbytes, get_logger as get_logger

cSSH2_AGENTC_REQUEST_IDENTITIES: Incomplete
SSH2_AGENT_IDENTITIES_ANSWER: int
cSSH2_AGENTC_SIGN_REQUEST: Incomplete
SSH2_AGENT_SIGN_RESPONSE: int
SSH_AGENT_RSA_SHA2_256: int
SSH_AGENT_RSA_SHA2_512: int
ALGORITHM_FLAG_MAP: Incomplete

class AgentSSH:
    def __init__(self) -> None: ...
    def get_keys(self):
        """
        Return the list of keys available through the SSH agent, if any.  If
        no SSH agent was running (or it couldn't be contacted), an empty list
        will be returned.

        This method performs no IO, just returns the list of keys retrieved
        when the connection was made.

        :return:
            a tuple of `.AgentKey` objects representing keys available on the
            SSH agent
        """

class AgentProxyThread(threading.Thread):
    """
    Class in charge of communication between two channels.
    """
    def __init__(self, agent) -> None: ...
    def run(self) -> None: ...

class AgentLocalProxy(AgentProxyThread):
    """
    Class to be used when wanting to ask a local SSH Agent being
    asked from a remote fake agent (so use a unix socket for ex.)
    """
    def __init__(self, agent) -> None: ...
    def get_connection(self):
        """
        Return a pair of socket object and string address.

        May block!
        """

class AgentRemoteProxy(AgentProxyThread):
    """
    Class to be used when wanting to ask a remote SSH Agent
    """
    def __init__(self, agent, chan) -> None: ...
    def get_connection(self): ...

def get_agent_connection():
    """
    Returns some SSH agent object, or None if none were found/supported.

    .. versionadded:: 2.10
    """

class AgentClientProxy:
    """
    Class proxying request as a client:

    #. client ask for a request_forward_agent()
    #. server creates a proxy and a fake SSH Agent
    #. server ask for establishing a connection when needed,
       calling the forward_agent_handler at client side.
    #. the forward_agent_handler launch a thread for connecting
       the remote fake agent and the local agent
    #. Communication occurs ...
    """
    thread: Incomplete
    def __init__(self, chanRemote) -> None: ...
    def __del__(self) -> None: ...
    def connect(self) -> None:
        """
        Method automatically called by ``AgentProxyThread.run``.
        """
    def close(self) -> None:
        """
        Close the current connection and terminate the agent
        Should be called manually
        """

class AgentServerProxy(AgentSSH):
    """
    Allows an SSH server to access a forwarded agent.

    This also creates a unix domain socket on the system to allow external
    programs to also access the agent. For this reason, you probably only want
    to create one of these.

    :meth:`connect` must be called before it is usable. This will also load the
    list of keys the agent contains. You must also call :meth:`close` in
    order to clean up the unix socket and the thread that maintains it.
    (:class:`contextlib.closing` might be helpful to you.)

    :param .Transport t: Transport used for SSH Agent communication forwarding

    :raises: `.SSHException` -- mostly if we lost the agent
    """
    thread: Incomplete
    def __init__(self, t) -> None: ...
    def __del__(self) -> None: ...
    def connect(self) -> None: ...
    def close(self) -> None:
        """
        Terminate the agent, clean the files, close connections
        Should be called manually
        """
    def get_env(self):
        """
        Helper for the environment under unix

        :return:
            a dict containing the ``SSH_AUTH_SOCK`` environment variables
        """

class AgentRequestHandler:
    '''
    Primary/default implementation of SSH agent forwarding functionality.

    Simply instantiate this class, handing it a live command-executing session
    object, and it will handle forwarding any local SSH agent processes it
    finds.

    For example::

        # Connect
        client = SSHClient()
        client.connect(host, port, username)
        # Obtain session
        session = client.get_transport().open_session()
        # Forward local agent
        AgentRequestHandler(session)
        # Commands executed after this point will see the forwarded agent on
        # the remote end.
        session.exec_command("git clone https://my.git.repository/")
    '''
    def __init__(self, chanClient) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...

class Agent(AgentSSH):
    """
    Client interface for using private keys from an SSH agent running on the
    local machine.  If an SSH agent is running, this class can be used to
    connect to it and retrieve `.PKey` objects which can be used when
    attempting to authenticate to remote SSH servers.

    Upon initialization, a session with the local machine's SSH agent is
    opened, if one is running. If no agent is running, initialization will
    succeed, but `get_keys` will return an empty tuple.

    :raises: `.SSHException` --
        if an SSH agent is found, but speaks an incompatible protocol

    .. versionchanged:: 2.10
        Added support for native openssh agent on windows (extending previous
        putty pageant support)
    """
    def __init__(self) -> None: ...
    def close(self) -> None:
        """
        Close the SSH agent connection.
        """

class AgentKey(PKey):
    """
    Private key held in a local SSH agent.  This type of key can be used for
    authenticating to a remote server (signing).  Most other key operations
    work as expected.

    .. versionchanged:: 3.2
        Added the ``comment`` kwarg and attribute.

    .. versionchanged:: 3.2
        Added the ``.inner_key`` attribute holding a reference to the 'real'
        key instance this key is a proxy for, if one was obtainable, else None.
    """
    agent: Incomplete
    blob: Incomplete
    comment: Incomplete
    name: Incomplete
    inner_key: Incomplete
    def __init__(self, agent, blob, comment: str = '') -> None: ...
    def log(self, *args, **kwargs): ...
    def asbytes(self): ...
    def get_name(self): ...
    def get_bits(self): ...
    def __getattr__(self, name):
        """
        Proxy any un-implemented methods/properties to the inner_key.
        """
    def sign_ssh_data(self, data, algorithm: Incomplete | None = None): ...
