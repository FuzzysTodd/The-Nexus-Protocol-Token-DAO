import threading
from _typeshed import Incomplete
from paramiko import util as util
from paramiko.auth_handler import AuthHandler as AuthHandler, AuthOnlyHandler as AuthOnlyHandler
from paramiko.channel import Channel as Channel
from paramiko.common import CONNECTION_FAILED_CODE as CONNECTION_FAILED_CODE, DEBUG as DEBUG, DEFAULT_MAX_PACKET_SIZE as DEFAULT_MAX_PACKET_SIZE, DEFAULT_WINDOW_SIZE as DEFAULT_WINDOW_SIZE, ERROR as ERROR, HIGHEST_USERAUTH_MESSAGE_ID as HIGHEST_USERAUTH_MESSAGE_ID, INFO as INFO, MAX_WINDOW_SIZE as MAX_WINDOW_SIZE, MIN_PACKET_SIZE as MIN_PACKET_SIZE, MIN_WINDOW_SIZE as MIN_WINDOW_SIZE, MSG_CHANNEL_CLOSE as MSG_CHANNEL_CLOSE, MSG_CHANNEL_DATA as MSG_CHANNEL_DATA, MSG_CHANNEL_EOF as MSG_CHANNEL_EOF, MSG_CHANNEL_EXTENDED_DATA as MSG_CHANNEL_EXTENDED_DATA, MSG_CHANNEL_FAILURE as MSG_CHANNEL_FAILURE, MSG_CHANNEL_OPEN as MSG_CHANNEL_OPEN, MSG_CHANNEL_OPEN_FAILURE as MSG_CHANNEL_OPEN_FAILURE, MSG_CHANNEL_OPEN_SUCCESS as MSG_CHANNEL_OPEN_SUCCESS, MSG_CHANNEL_REQUEST as MSG_CHANNEL_REQUEST, MSG_CHANNEL_SUCCESS as MSG_CHANNEL_SUCCESS, MSG_CHANNEL_WINDOW_ADJUST as MSG_CHANNEL_WINDOW_ADJUST, MSG_DEBUG as MSG_DEBUG, MSG_DISCONNECT as MSG_DISCONNECT, MSG_EXT_INFO as MSG_EXT_INFO, MSG_GLOBAL_REQUEST as MSG_GLOBAL_REQUEST, MSG_IGNORE as MSG_IGNORE, MSG_KEXINIT as MSG_KEXINIT, MSG_NAMES as MSG_NAMES, MSG_NEWKEYS as MSG_NEWKEYS, MSG_REQUEST_FAILURE as MSG_REQUEST_FAILURE, MSG_REQUEST_SUCCESS as MSG_REQUEST_SUCCESS, MSG_SERVICE_ACCEPT as MSG_SERVICE_ACCEPT, MSG_UNIMPLEMENTED as MSG_UNIMPLEMENTED, OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED as OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED, OPEN_SUCCEEDED as OPEN_SUCCEEDED, WARNING as WARNING, byte_ord as byte_ord, cMSG_CHANNEL_OPEN as cMSG_CHANNEL_OPEN, cMSG_CHANNEL_OPEN_FAILURE as cMSG_CHANNEL_OPEN_FAILURE, cMSG_CHANNEL_OPEN_SUCCESS as cMSG_CHANNEL_OPEN_SUCCESS, cMSG_EXT_INFO as cMSG_EXT_INFO, cMSG_GLOBAL_REQUEST as cMSG_GLOBAL_REQUEST, cMSG_IGNORE as cMSG_IGNORE, cMSG_KEXINIT as cMSG_KEXINIT, cMSG_NEWKEYS as cMSG_NEWKEYS, cMSG_REQUEST_FAILURE as cMSG_REQUEST_FAILURE, cMSG_REQUEST_SUCCESS as cMSG_REQUEST_SUCCESS, cMSG_SERVICE_REQUEST as cMSG_SERVICE_REQUEST, cMSG_UNIMPLEMENTED as cMSG_UNIMPLEMENTED, xffffffff as xffffffff
from paramiko.compress import ZlibCompressor as ZlibCompressor, ZlibDecompressor as ZlibDecompressor
from paramiko.dsskey import DSSKey as DSSKey
from paramiko.ecdsakey import ECDSAKey as ECDSAKey
from paramiko.ed25519key import Ed25519Key as Ed25519Key
from paramiko.kex_curve25519 import KexCurve25519 as KexCurve25519
from paramiko.kex_ecdh_nist import KexNistp256 as KexNistp256, KexNistp384 as KexNistp384, KexNistp521 as KexNistp521
from paramiko.kex_gex import KexGex as KexGex, KexGexSHA256 as KexGexSHA256
from paramiko.kex_group1 import KexGroup1 as KexGroup1
from paramiko.kex_group14 import KexGroup14 as KexGroup14, KexGroup14SHA256 as KexGroup14SHA256
from paramiko.kex_group16 import KexGroup16SHA512 as KexGroup16SHA512
from paramiko.kex_gss import KexGSSGex as KexGSSGex, KexGSSGroup1 as KexGSSGroup1, KexGSSGroup14 as KexGSSGroup14
from paramiko.message import Message as Message
from paramiko.packet import NeedRekeyException as NeedRekeyException, Packetizer as Packetizer
from paramiko.primes import ModulusPack as ModulusPack
from paramiko.rsakey import RSAKey as RSAKey
from paramiko.server import ServerInterface as ServerInterface
from paramiko.sftp_client import SFTPClient as SFTPClient
from paramiko.ssh_exception import BadAuthenticationType as BadAuthenticationType, ChannelException as ChannelException, IncompatiblePeer as IncompatiblePeer, ProxyCommandFailure as ProxyCommandFailure, SSHException as SSHException
from paramiko.ssh_gss import GSSAuth as GSSAuth
from paramiko.util import ClosingContextManager as ClosingContextManager, b as b, clamp_value as clamp_value

class Transport(threading.Thread, ClosingContextManager):
    """
    An SSH Transport attaches to a stream (usually a socket), negotiates an
    encrypted session, authenticates, and then creates stream tunnels, called
    `channels <.Channel>`, across the session.  Multiple channels can be
    multiplexed across a single session (and often are, in the case of port
    forwardings).

    Instances of this class may be used as context managers.
    """
    active: bool
    hostname: Incomplete
    server_extensions: Incomplete
    daemon: bool
    sock: Incomplete
    packetizer: Incomplete
    local_version: Incomplete
    remote_version: str
    local_cipher: str
    local_kex_init: Incomplete
    local_mac: Incomplete
    local_compression: Incomplete
    session_id: Incomplete
    host_key_type: Incomplete
    host_key: Incomplete
    use_gss_kex: Incomplete
    gss_kex_used: bool
    kexgss_ctxt: Incomplete
    gss_host: Incomplete
    kex_engine: Incomplete
    H: Incomplete
    K: Incomplete
    initial_kex_done: bool
    in_kex: bool
    authenticated: bool
    lock: Incomplete
    channel_events: Incomplete
    channels_seen: Incomplete
    default_max_packet_size: Incomplete
    default_window_size: Incomplete
    saved_exception: Incomplete
    clear_to_send: Incomplete
    clear_to_send_lock: Incomplete
    clear_to_send_timeout: float
    log_name: str
    logger: Incomplete
    auth_handler: Incomplete
    global_response: Incomplete
    completion_event: Incomplete
    banner_timeout: int
    handshake_timeout: int
    auth_timeout: int
    channel_timeout: Incomplete
    disabled_algorithms: Incomplete
    server_sig_algs: Incomplete
    server_mode: bool
    server_object: Incomplete
    server_key_dict: Incomplete
    server_accepts: Incomplete
    server_accept_cv: Incomplete
    subsystem_table: Incomplete
    def __init__(self, sock, default_window_size=..., default_max_packet_size=..., gss_kex: bool = False, gss_deleg_creds: bool = True, disabled_algorithms: Incomplete | None = None, server_sig_algs: bool = True) -> None:
        '''
        Create a new SSH session over an existing socket, or socket-like
        object.  This only creates the `.Transport` object; it doesn\'t begin
        the SSH session yet.  Use `connect` or `start_client` to begin a client
        session, or `start_server` to begin a server session.

        If the object is not actually a socket, it must have the following
        methods:

        - ``send(bytes)``: Writes from 1 to ``len(bytes)`` bytes, and returns
          an int representing the number of bytes written.  Returns
          0 or raises ``EOFError`` if the stream has been closed.
        - ``recv(int)``: Reads from 1 to ``int`` bytes and returns them as a
          string.  Returns 0 or raises ``EOFError`` if the stream has been
          closed.
        - ``close()``: Closes the socket.
        - ``settimeout(n)``: Sets a (float) timeout on I/O operations.

        For ease of use, you may also pass in an address (as a tuple) or a host
        string as the ``sock`` argument.  (A host string is a hostname with an
        optional port (separated by ``":"``) which will be converted into a
        tuple of ``(hostname, port)``.)  A socket will be connected to this
        address and used for communication.  Exceptions from the ``socket``
        call may be thrown in this case.

        .. note::
            Modifying the the window and packet sizes might have adverse
            effects on your channels created from this transport. The default
            values are the same as in the OpenSSH code base and have been
            battle tested.

        :param socket sock:
            a socket or socket-like object to create the session over.
        :param int default_window_size:
            sets the default window size on the transport. (defaults to
            2097152)
        :param int default_max_packet_size:
            sets the default max packet size on the transport. (defaults to
            32768)
        :param bool gss_kex:
            Whether to enable GSSAPI key exchange when GSSAPI is in play.
            Default: ``False``.
        :param bool gss_deleg_creds:
            Whether to enable GSSAPI credential delegation when GSSAPI is in
            play. Default: ``True``.
        :param dict disabled_algorithms:
            If given, must be a dictionary mapping algorithm type to an
            iterable of algorithm identifiers, which will be disabled for the
            lifetime of the transport.

            Keys should match the last word in the class\' builtin algorithm
            tuple attributes, such as ``"ciphers"`` to disable names within
            ``_preferred_ciphers``; or ``"kex"`` to disable something defined
            inside ``_preferred_kex``. Values should exactly match members of
            the matching attribute.

            For example, if you need to disable
            ``diffie-hellman-group16-sha512`` key exchange (perhaps because
            your code talks to a server which implements it differently from
            Paramiko), specify ``disabled_algorithms={"kex":
            ["diffie-hellman-group16-sha512"]}``.
        :param bool server_sig_algs:
            Whether to send an extra message to compatible clients, in server
            mode, with a list of supported pubkey algorithms. Default:
            ``True``.

        .. versionchanged:: 1.15
            Added the ``default_window_size`` and ``default_max_packet_size``
            arguments.
        .. versionchanged:: 1.15
            Added the ``gss_kex`` and ``gss_deleg_creds`` kwargs.
        .. versionchanged:: 2.6
            Added the ``disabled_algorithms`` kwarg.
        .. versionchanged:: 2.9
            Added the ``server_sig_algs`` kwarg.
        '''
    @property
    def preferred_ciphers(self): ...
    @property
    def preferred_macs(self): ...
    @property
    def preferred_keys(self): ...
    @property
    def preferred_pubkeys(self): ...
    @property
    def preferred_kex(self): ...
    @property
    def preferred_compression(self): ...
    def atfork(self) -> None:
        """
        Terminate this Transport without closing the session.  On posix
        systems, if a Transport is open during process forking, both parent
        and child will share the underlying socket, but only one process can
        use the connection (without corrupting the session).  Use this method
        to clean up a Transport object without disrupting the other process.

        .. versionadded:: 1.5.3
        """
    def get_security_options(self):
        """
        Return a `.SecurityOptions` object which can be used to tweak the
        encryption algorithms this transport will permit (for encryption,
        digest/hash operations, public keys, and key exchanges) and the order
        of preference for them.
        """
    def set_gss_host(self, gss_host, trust_dns: bool = True, gssapi_requested: bool = True) -> None:
        """
        Normalize/canonicalize ``self.gss_host`` depending on various factors.

        :param str gss_host:
            The explicitly requested GSS-oriented hostname to connect to (i.e.
            what the host's name is in the Kerberos database.) Defaults to
            ``self.hostname`` (which will be the 'real' target hostname and/or
            host portion of given socket object.)
        :param bool trust_dns:
            Indicates whether or not DNS is trusted; if true, DNS will be used
            to canonicalize the GSS hostname (which again will either be
            ``gss_host`` or the transport's default hostname.)
            (Defaults to True due to backwards compatibility.)
        :param bool gssapi_requested:
            Whether GSSAPI key exchange or authentication was even requested.
            If not, this is a no-op and nothing happens
            (and ``self.gss_host`` is not set.)
            (Defaults to True due to backwards compatibility.)
        :returns: ``None``.
        """
    def start_client(self, event: Incomplete | None = None, timeout: Incomplete | None = None) -> None:
        """
        Negotiate a new SSH2 session as a client.  This is the first step after
        creating a new `.Transport`.  A separate thread is created for protocol
        negotiation.

        If an event is passed in, this method returns immediately.  When
        negotiation is done (successful or not), the given ``Event`` will
        be triggered.  On failure, `is_active` will return ``False``.

        (Since 1.4) If ``event`` is ``None``, this method will not return until
        negotiation is done.  On success, the method returns normally.
        Otherwise an SSHException is raised.

        After a successful negotiation, you will usually want to authenticate,
        calling `auth_password <Transport.auth_password>` or
        `auth_publickey <Transport.auth_publickey>`.

        .. note:: `connect` is a simpler method for connecting as a client.

        .. note::
            After calling this method (or `start_server` or `connect`), you
            should no longer directly read from or write to the original socket
            object.

        :param .threading.Event event:
            an event to trigger when negotiation is complete (optional)

        :param float timeout:
            a timeout, in seconds, for SSH2 session negotiation (optional)

        :raises:
            `.SSHException` -- if negotiation fails (and no ``event`` was
            passed in)
        """
    def start_server(self, event: Incomplete | None = None, server: Incomplete | None = None) -> None:
        """
        Negotiate a new SSH2 session as a server.  This is the first step after
        creating a new `.Transport` and setting up your server host key(s).  A
        separate thread is created for protocol negotiation.

        If an event is passed in, this method returns immediately.  When
        negotiation is done (successful or not), the given ``Event`` will
        be triggered.  On failure, `is_active` will return ``False``.

        (Since 1.4) If ``event`` is ``None``, this method will not return until
        negotiation is done.  On success, the method returns normally.
        Otherwise an SSHException is raised.

        After a successful negotiation, the client will need to authenticate.
        Override the methods `get_allowed_auths
        <.ServerInterface.get_allowed_auths>`, `check_auth_none
        <.ServerInterface.check_auth_none>`, `check_auth_password
        <.ServerInterface.check_auth_password>`, and `check_auth_publickey
        <.ServerInterface.check_auth_publickey>` in the given ``server`` object
        to control the authentication process.

        After a successful authentication, the client should request to open a
        channel.  Override `check_channel_request
        <.ServerInterface.check_channel_request>` in the given ``server``
        object to allow channels to be opened.

        .. note::
            After calling this method (or `start_client` or `connect`), you
            should no longer directly read from or write to the original socket
            object.

        :param .threading.Event event:
            an event to trigger when negotiation is complete.
        :param .ServerInterface server:
            an object used to perform authentication and create `channels
            <.Channel>`

        :raises:
            `.SSHException` -- if negotiation fails (and no ``event`` was
            passed in)
        """
    def add_server_key(self, key) -> None:
        """
        Add a host key to the list of keys used for server mode.  When behaving
        as a server, the host key is used to sign certain packets during the
        SSH2 negotiation, so that the client can trust that we are who we say
        we are.  Because this is used for signing, the key must contain private
        key info, not just the public half.  Only one key of each type (RSA or
        DSS) is kept.

        :param .PKey key:
            the host key to add, usually an `.RSAKey` or `.DSSKey`.
        """
    def get_server_key(self):
        """
        Return the active host key, in server mode.  After negotiating with the
        client, this method will return the negotiated host key.  If only one
        type of host key was set with `add_server_key`, that's the only key
        that will ever be returned.  But in cases where you have set more than
        one type of host key (for example, an RSA key and a DSS key), the key
        type will be negotiated by the client, and this method will return the
        key of the type agreed on.  If the host key has not been negotiated
        yet, ``None`` is returned.  In client mode, the behavior is undefined.

        :return:
            host key (`.PKey`) of the type negotiated by the client, or
            ``None``.
        """
    @staticmethod
    def load_server_moduli(filename: Incomplete | None = None):
        '''
        (optional)
        Load a file of prime moduli for use in doing group-exchange key
        negotiation in server mode.  It\'s a rather obscure option and can be
        safely ignored.

        In server mode, the remote client may request "group-exchange" key
        negotiation, which asks the server to send a random prime number that
        fits certain criteria.  These primes are pretty difficult to compute,
        so they can\'t be generated on demand.  But many systems contain a file
        of suitable primes (usually named something like ``/etc/ssh/moduli``).
        If you call `load_server_moduli` and it returns ``True``, then this
        file of primes has been loaded and we will support "group-exchange" in
        server mode.  Otherwise server mode will just claim that it doesn\'t
        support that method of key negotiation.

        :param str filename:
            optional path to the moduli file, if you happen to know that it\'s
            not in a standard location.
        :return:
            True if a moduli file was successfully loaded; False otherwise.

        .. note:: This has no effect when used in client mode.
        '''
    def close(self) -> None:
        """
        Close this session, and any open channels that are tied to it.
        """
    def get_remote_server_key(self):
        """
        Return the host key of the server (in client mode).

        .. note::
            Previously this call returned a tuple of ``(key type, key
            string)``. You can get the same effect by calling `.PKey.get_name`
            for the key type, and ``str(key)`` for the key string.

        :raises: `.SSHException` -- if no session is currently active.

        :return: public key (`.PKey`) of the remote server
        """
    def is_active(self):
        """
        Return true if this session is active (open).

        :return:
            True if the session is still active (open); False if the session is
            closed
        """
    def open_session(self, window_size: Incomplete | None = None, max_packet_size: Incomplete | None = None, timeout: Incomplete | None = None):
        '''
        Request a new channel to the server, of type ``"session"``.  This is
        just an alias for calling `open_channel` with an argument of
        ``"session"``.

        .. note:: Modifying the the window and packet sizes might have adverse
            effects on the session created. The default values are the same
            as in the OpenSSH code base and have been battle tested.

        :param int window_size:
            optional window size for this session.
        :param int max_packet_size:
            optional max packet size for this session.

        :return: a new `.Channel`

        :raises:
            `.SSHException` -- if the request is rejected or the session ends
            prematurely

        .. versionchanged:: 1.13.4/1.14.3/1.15.3
            Added the ``timeout`` argument.
        .. versionchanged:: 1.15
            Added the ``window_size`` and ``max_packet_size`` arguments.
        '''
    def open_x11_channel(self, src_addr: Incomplete | None = None):
        '''
        Request a new channel to the client, of type ``"x11"``.  This
        is just an alias for ``open_channel(\'x11\', src_addr=src_addr)``.

        :param tuple src_addr:
            the source address (``(str, int)``) of the x11 server (port is the
            x11 port, ie. 6010)
        :return: a new `.Channel`

        :raises:
            `.SSHException` -- if the request is rejected or the session ends
            prematurely
        '''
    def open_forward_agent_channel(self):
        '''
        Request a new channel to the client, of type
        ``"auth-agent@openssh.com"``.

        This is just an alias for ``open_channel(\'auth-agent@openssh.com\')``.

        :return: a new `.Channel`

        :raises: `.SSHException` --
            if the request is rejected or the session ends prematurely
        '''
    def open_forwarded_tcpip_channel(self, src_addr, dest_addr):
        """
        Request a new channel back to the client, of type ``forwarded-tcpip``.

        This is used after a client has requested port forwarding, for sending
        incoming connections back to the client.

        :param src_addr: originator's address
        :param dest_addr: local (server) connected address
        """
    def open_channel(self, kind, dest_addr: Incomplete | None = None, src_addr: Incomplete | None = None, window_size: Incomplete | None = None, max_packet_size: Incomplete | None = None, timeout: Incomplete | None = None):
        '''
        Request a new channel to the server. `Channels <.Channel>` are
        socket-like objects used for the actual transfer of data across the
        session. You may only request a channel after negotiating encryption
        (using `connect` or `start_client`) and authenticating.

        .. note:: Modifying the the window and packet sizes might have adverse
            effects on the channel created. The default values are the same
            as in the OpenSSH code base and have been battle tested.

        :param str kind:
            the kind of channel requested (usually ``"session"``,
            ``"forwarded-tcpip"``, ``"direct-tcpip"``, or ``"x11"``)
        :param tuple dest_addr:
            the destination address (address + port tuple) of this port
            forwarding, if ``kind`` is ``"forwarded-tcpip"`` or
            ``"direct-tcpip"`` (ignored for other channel types)
        :param src_addr: the source address of this port forwarding, if
            ``kind`` is ``"forwarded-tcpip"``, ``"direct-tcpip"``, or ``"x11"``
        :param int window_size:
            optional window size for this session.
        :param int max_packet_size:
            optional max packet size for this session.
        :param float timeout:
            optional timeout opening a channel, default 3600s (1h)

        :return: a new `.Channel` on success

        :raises:
            `.SSHException` -- if the request is rejected, the session ends
            prematurely or there is a timeout opening a channel

        .. versionchanged:: 1.15
            Added the ``window_size`` and ``max_packet_size`` arguments.
        '''
    def request_port_forward(self, address, port, handler: Incomplete | None = None):
        """
        Ask the server to forward TCP connections from a listening port on
        the server, across this SSH session.

        If a handler is given, that handler is called from a different thread
        whenever a forwarded connection arrives.  The handler parameters are::

            handler(
                channel,
                (origin_addr, origin_port),
                (server_addr, server_port),
            )

        where ``server_addr`` and ``server_port`` are the address and port that
        the server was listening on.

        If no handler is set, the default behavior is to send new incoming
        forwarded connections into the accept queue, to be picked up via
        `accept`.

        :param str address: the address to bind when forwarding
        :param int port:
            the port to forward, or 0 to ask the server to allocate any port
        :param callable handler:
            optional handler for incoming forwarded connections, of the form
            ``func(Channel, (str, int), (str, int))``.

        :return: the port number (`int`) allocated by the server

        :raises:
            `.SSHException` -- if the server refused the TCP forward request
        """
    def cancel_port_forward(self, address, port) -> None:
        """
        Ask the server to cancel a previous port-forwarding request.  No more
        connections to the given address & port will be forwarded across this
        ssh connection.

        :param str address: the address to stop forwarding
        :param int port: the port to stop forwarding
        """
    def open_sftp_client(self):
        """
        Create an SFTP client channel from an open transport.  On success, an
        SFTP session will be opened with the remote host, and a new
        `.SFTPClient` object will be returned.

        :return:
            a new `.SFTPClient` referring to an sftp session (channel) across
            this transport
        """
    def send_ignore(self, byte_count: Incomplete | None = None) -> None:
        '''
        Send a junk packet across the encrypted link.  This is sometimes used
        to add "noise" to a connection to confuse would-be attackers.  It can
        also be used as a keep-alive for long lived connections traversing
        firewalls.

        :param int byte_count:
            the number of random bytes to send in the payload of the ignored
            packet -- defaults to a random number from 10 to 41.
        '''
    def renegotiate_keys(self) -> None:
        """
        Force this session to switch to new keys.  Normally this is done
        automatically after the session hits a certain number of packets or
        bytes sent or received, but this method gives you the option of forcing
        new keys whenever you want.  Negotiating new keys causes a pause in
        traffic both ways as the two sides swap keys and do computations.  This
        method returns when the session has switched to new keys.

        :raises:
            `.SSHException` -- if the key renegotiation failed (which causes
            the session to end)
        """
    def set_keepalive(self, interval):
        '''
        Turn on/off keepalive packets (default is off).  If this is set, after
        ``interval`` seconds without sending any data over the connection, a
        "keepalive" packet will be sent (and ignored by the remote host).  This
        can be useful to keep connections alive over a NAT, for example.

        :param int interval:
            seconds to wait before sending a keepalive packet (or
            0 to disable keepalives).
        '''
    def global_request(self, kind, data: Incomplete | None = None, wait: bool = True):
        """
        Make a global request to the remote host.  These are normally
        extensions to the SSH2 protocol.

        :param str kind: name of the request.
        :param tuple data:
            an optional tuple containing additional data to attach to the
            request.
        :param bool wait:
            ``True`` if this method should not return until a response is
            received; ``False`` otherwise.
        :return:
            a `.Message` containing possible additional data if the request was
            successful (or an empty `.Message` if ``wait`` was ``False``);
            ``None`` if the request was denied.
        """
    def accept(self, timeout: Incomplete | None = None):
        """
        Return the next channel opened by the client over this transport, in
        server mode.  If no channel is opened before the given timeout,
        ``None`` is returned.

        :param int timeout:
            seconds to wait for a channel, or ``None`` to wait forever
        :return: a new `.Channel` opened by the client
        """
    def connect(self, hostkey: Incomplete | None = None, username: str = '', password: Incomplete | None = None, pkey: Incomplete | None = None, gss_host: Incomplete | None = None, gss_auth: bool = False, gss_kex: bool = False, gss_deleg_creds: bool = True, gss_trust_dns: bool = True) -> None:
        """
        Negotiate an SSH2 session, and optionally verify the server's host key
        and authenticate using a password or private key.  This is a shortcut
        for `start_client`, `get_remote_server_key`, and
        `Transport.auth_password` or `Transport.auth_publickey`.  Use those
        methods if you want more control.

        You can use this method immediately after creating a Transport to
        negotiate encryption with a server.  If it fails, an exception will be
        thrown.  On success, the method will return cleanly, and an encrypted
        session exists.  You may immediately call `open_channel` or
        `open_session` to get a `.Channel` object, which is used for data
        transfer.

        .. note::
            If you fail to supply a password or private key, this method may
            succeed, but a subsequent `open_channel` or `open_session` call may
            fail because you haven't authenticated yet.

        :param .PKey hostkey:
            the host key expected from the server, or ``None`` if you don't
            want to do host key verification.
        :param str username: the username to authenticate as.
        :param str password:
            a password to use for authentication, if you want to use password
            authentication; otherwise ``None``.
        :param .PKey pkey:
            a private key to use for authentication, if you want to use private
            key authentication; otherwise ``None``.
        :param str gss_host:
            The target's name in the kerberos database. Default: hostname
        :param bool gss_auth:
            ``True`` if you want to use GSS-API authentication.
        :param bool gss_kex:
            Perform GSS-API Key Exchange and user authentication.
        :param bool gss_deleg_creds:
            Whether to delegate GSS-API client credentials.
        :param gss_trust_dns:
            Indicates whether or not the DNS is trusted to securely
            canonicalize the name of the host being connected to (default
            ``True``).

        :raises: `.SSHException` -- if the SSH2 negotiation fails, the host key
            supplied by the server is incorrect, or authentication fails.

        .. versionchanged:: 2.3
            Added the ``gss_trust_dns`` argument.
        """
    def get_exception(self):
        """
        Return any exception that happened during the last server request.
        This can be used to fetch more specific error information after using
        calls like `start_client`.  The exception (if any) is cleared after
        this call.

        :return:
            an exception, or ``None`` if there is no stored exception.

        .. versionadded:: 1.1
        """
    def set_subsystem_handler(self, name, handler, *args, **kwargs) -> None:
        """
        Set the handler class for a subsystem in server mode.  If a request
        for this subsystem is made on an open ssh channel later, this handler
        will be constructed and called -- see `.SubsystemHandler` for more
        detailed documentation.

        Any extra parameters (including keyword arguments) are saved and
        passed to the `.SubsystemHandler` constructor later.

        :param str name: name of the subsystem.
        :param handler:
            subclass of `.SubsystemHandler` that handles this subsystem.
        """
    def is_authenticated(self):
        """
        Return true if this session is active and authenticated.

        :return:
            True if the session is still open and has been authenticated
            successfully; False if authentication failed and/or the session is
            closed.
        """
    def get_username(self):
        """
        Return the username this connection is authenticated for.  If the
        session is not authenticated (or authentication failed), this method
        returns ``None``.

        :return: username that was authenticated (a `str`), or ``None``.
        """
    def get_banner(self):
        """
        Return the banner supplied by the server upon connect. If no banner is
        supplied, this method returns ``None``.

        :returns: server supplied banner (`str`), or ``None``.

        .. versionadded:: 1.13
        """
    def auth_none(self, username):
        '''
        Try to authenticate to the server using no authentication at all.
        This will almost always fail.  It may be useful for determining the
        list of authentication types supported by the server, by catching the
        `.BadAuthenticationType` exception raised.

        :param str username: the username to authenticate as
        :return:
            list of auth types permissible for the next stage of
            authentication (normally empty)

        :raises:
            `.BadAuthenticationType` -- if "none" authentication isn\'t allowed
            by the server for this user
        :raises:
            `.SSHException` -- if the authentication failed due to a network
            error

        .. versionadded:: 1.5
        '''
    def auth_password(self, username, password, event: Incomplete | None = None, fallback: bool = True):
        '''
        Authenticate to the server using a password.  The username and password
        are sent over an encrypted link.

        If an ``event`` is passed in, this method will return immediately, and
        the event will be triggered once authentication succeeds or fails.  On
        success, `is_authenticated` will return ``True``.  On failure, you may
        use `get_exception` to get more detailed error information.

        Since 1.1, if no event is passed, this method will block until the
        authentication succeeds or fails.  On failure, an exception is raised.
        Otherwise, the method simply returns.

        Since 1.5, if no event is passed and ``fallback`` is ``True`` (the
        default), if the server doesn\'t support plain password authentication
        but does support so-called "keyboard-interactive" mode, an attempt
        will be made to authenticate using this interactive mode.  If it fails,
        the normal exception will be thrown as if the attempt had never been
        made.  This is useful for some recent Gentoo and Debian distributions,
        which turn off plain password authentication in a misguided belief
        that interactive authentication is "more secure".  (It\'s not.)

        If the server requires multi-step authentication (which is very rare),
        this method will return a list of auth types permissible for the next
        step.  Otherwise, in the normal case, an empty list is returned.

        :param str username: the username to authenticate as
        :param basestring password: the password to authenticate with
        :param .threading.Event event:
            an event to trigger when the authentication attempt is complete
            (whether it was successful or not)
        :param bool fallback:
            ``True`` if an attempt at an automated "interactive" password auth
            should be made if the server doesn\'t support normal password auth
        :return:
            list of auth types permissible for the next stage of
            authentication (normally empty)

        :raises:
            `.BadAuthenticationType` -- if password authentication isn\'t
            allowed by the server for this user (and no event was passed in)
        :raises:
            `.AuthenticationException` -- if the authentication failed (and no
            event was passed in)
        :raises: `.SSHException` -- if there was a network error
        '''
    def auth_publickey(self, username, key, event: Incomplete | None = None):
        """
        Authenticate to the server using a private key.  The key is used to
        sign data from the server, so it must include the private part.

        If an ``event`` is passed in, this method will return immediately, and
        the event will be triggered once authentication succeeds or fails.  On
        success, `is_authenticated` will return ``True``.  On failure, you may
        use `get_exception` to get more detailed error information.

        Since 1.1, if no event is passed, this method will block until the
        authentication succeeds or fails.  On failure, an exception is raised.
        Otherwise, the method simply returns.

        If the server requires multi-step authentication (which is very rare),
        this method will return a list of auth types permissible for the next
        step.  Otherwise, in the normal case, an empty list is returned.

        :param str username: the username to authenticate as
        :param .PKey key: the private key to authenticate with
        :param .threading.Event event:
            an event to trigger when the authentication attempt is complete
            (whether it was successful or not)
        :return:
            list of auth types permissible for the next stage of
            authentication (normally empty)

        :raises:
            `.BadAuthenticationType` -- if public-key authentication isn't
            allowed by the server for this user (and no event was passed in)
        :raises:
            `.AuthenticationException` -- if the authentication failed (and no
            event was passed in)
        :raises: `.SSHException` -- if there was a network error
        """
    def auth_interactive(self, username, handler, submethods: str = ''):
        """
        Authenticate to the server interactively.  A handler is used to answer
        arbitrary questions from the server.  On many servers, this is just a
        dumb wrapper around PAM.

        This method will block until the authentication succeeds or fails,
        periodically calling the handler asynchronously to get answers to
        authentication questions.  The handler may be called more than once
        if the server continues to ask questions.

        The handler is expected to be a callable that will handle calls of the
        form: ``handler(title, instructions, prompt_list)``.  The ``title`` is
        meant to be a dialog-window title, and the ``instructions`` are user
        instructions (both are strings).  ``prompt_list`` will be a list of
        prompts, each prompt being a tuple of ``(str, bool)``.  The string is
        the prompt and the boolean indicates whether the user text should be
        echoed.

        A sample call would thus be:
        ``handler('title', 'instructions', [('Password:', False)])``.

        The handler should return a list or tuple of answers to the server's
        questions.

        If the server requires multi-step authentication (which is very rare),
        this method will return a list of auth types permissible for the next
        step.  Otherwise, in the normal case, an empty list is returned.

        :param str username: the username to authenticate as
        :param callable handler: a handler for responding to server questions
        :param str submethods: a string list of desired submethods (optional)
        :return:
            list of auth types permissible for the next stage of
            authentication (normally empty).

        :raises: `.BadAuthenticationType` -- if public-key authentication isn't
            allowed by the server for this user
        :raises: `.AuthenticationException` -- if the authentication failed
        :raises: `.SSHException` -- if there was a network error

        .. versionadded:: 1.5
        """
    def auth_interactive_dumb(self, username, handler: Incomplete | None = None, submethods: str = ''):
        """
        Authenticate to the server interactively but dumber.
        Just print the prompt and / or instructions to stdout and send back
        the response. This is good for situations where partial auth is
        achieved by key and then the user has to enter a 2fac token.
        """
    def auth_gssapi_with_mic(self, username, gss_host, gss_deleg_creds):
        """
        Authenticate to the Server using GSS-API / SSPI.

        :param str username: The username to authenticate as
        :param str gss_host: The target host
        :param bool gss_deleg_creds: Delegate credentials or not
        :return: list of auth types permissible for the next stage of
                 authentication (normally empty)
        :raises: `.BadAuthenticationType` -- if gssapi-with-mic isn't
            allowed by the server (and no event was passed in)
        :raises:
            `.AuthenticationException` -- if the authentication failed (and no
            event was passed in)
        :raises: `.SSHException` -- if there was a network error
        """
    def auth_gssapi_keyex(self, username):
        """
        Authenticate to the server with GSS-API/SSPI if GSS-API kex is in use.

        :param str username: The username to authenticate as.
        :returns:
            a list of auth types permissible for the next stage of
            authentication (normally empty)
        :raises: `.BadAuthenticationType` --
            if GSS-API Key Exchange was not performed (and no event was passed
            in)
        :raises: `.AuthenticationException` --
            if the authentication failed (and no event was passed in)
        :raises: `.SSHException` -- if there was a network error
        """
    def set_log_channel(self, name) -> None:
        '''
        Set the channel for this transport\'s logging.  The default is
        ``"paramiko.transport"`` but it can be set to anything you want. (See
        the `.logging` module for more info.)  SSH Channels will log to a
        sub-channel of the one specified.

        :param str name: new channel name for logging

        .. versionadded:: 1.1
        '''
    def get_log_channel(self):
        """
        Return the channel name used for this transport's logging.

        :return: channel name as a `str`

        .. versionadded:: 1.2
        """
    def set_hexdump(self, hexdump) -> None:
        """
        Turn on/off logging a hex dump of protocol traffic at DEBUG level in
        the logs.  Normally you would want this off (which is the default),
        but if you are debugging something, it may be useful.

        :param bool hexdump:
            ``True`` to log protocol traffix (in hex) to the log; ``False``
            otherwise.
        """
    def get_hexdump(self):
        """
        Return ``True`` if the transport is currently logging hex dumps of
        protocol traffic.

        :return: ``True`` if hex dumps are being logged, else ``False``.

        .. versionadded:: 1.4
        """
    def use_compression(self, compress: bool = True) -> None:
        """
        Turn on/off compression.  This will only have an affect before starting
        the transport (ie before calling `connect`, etc).  By default,
        compression is off since it negatively affects interactive sessions.

        :param bool compress:
            ``True`` to ask the remote client/server to compress traffic;
            ``False`` to refuse compression

        .. versionadded:: 1.5.2
        """
    def getpeername(self):
        '''
        Return the address of the remote side of this Transport, if possible.

        This is effectively a wrapper around ``getpeername`` on the underlying
        socket.  If the socket-like object has no ``getpeername`` method, then
        ``("unknown", 0)`` is returned.

        :return:
            the address of the remote host, if known, as a ``(str, int)``
            tuple.
        '''
    def stop_thread(self) -> None: ...
    sys: Incomplete
    def run(self) -> None: ...

class SecurityOptions:
    """
    Simple object containing the security preferences of an ssh transport.
    These are tuples of acceptable ciphers, digests, key types, and key
    exchange algorithms, listed in order of preference.

    Changing the contents and/or order of these fields affects the underlying
    `.Transport` (but only if you change them before starting the session).
    If you try to add an algorithm that paramiko doesn't recognize,
    ``ValueError`` will be raised.  If you try to assign something besides a
    tuple to one of the fields, ``TypeError`` will be raised.
    """
    def __init__(self, transport) -> None: ...
    @property
    def ciphers(self):
        """Symmetric encryption ciphers"""
    @ciphers.setter
    def ciphers(self, x) -> None: ...
    @property
    def digests(self):
        """Digest (one-way hash) algorithms"""
    @digests.setter
    def digests(self, x) -> None: ...
    @property
    def key_types(self):
        """Public-key algorithms"""
    @key_types.setter
    def key_types(self, x) -> None: ...
    @property
    def kex(self):
        """Key exchange algorithms"""
    @kex.setter
    def kex(self, x) -> None: ...
    @property
    def compression(self):
        """Compression algorithms"""
    @compression.setter
    def compression(self, x) -> None: ...

class ChannelMap:
    def __init__(self) -> None: ...
    def put(self, chanid, chan) -> None: ...
    def get(self, chanid): ...
    def delete(self, chanid) -> None: ...
    def values(self): ...
    def __len__(self) -> int: ...

class ServiceRequestingTransport(Transport):
    """
    Transport, but also handling service requests, like it oughtta!

    .. versionadded:: 3.2
    """
    def __init__(self, *args, **kwargs) -> None: ...
    auth_handler: Incomplete
    def ensure_session(self) -> None: ...
    def get_auth_handler(self): ...
    def auth_none(self, username): ...
    def auth_password(self, username, password, fallback: bool = True): ...
    def auth_publickey(self, username, key): ...
    def auth_interactive(self, username, handler, submethods: str = ''): ...
    def auth_interactive_dumb(self, username, handler: Incomplete | None = None, submethods: str = ''): ...
    def auth_gssapi_with_mic(self, username, gss_host, gss_deleg_creds): ...
    def auth_gssapi_keyex(self, username): ...
