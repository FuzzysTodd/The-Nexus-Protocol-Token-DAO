from ..spec import AbstractBufferedFile as AbstractBufferedFile, AbstractFileSystem as AbstractFileSystem
from ..utils import infer_storage_options as infer_storage_options, tokenize as tokenize
from _typeshed import Incomplete

logger: Incomplete

class WebHDFS(AbstractFileSystem):
    '''
    Interface to HDFS over HTTP using the WebHDFS API. Supports also HttpFS gateways.

    Three auth mechanisms are supported:

    insecure: no auth is done, and the user is assumed to be whoever they
        say they are (parameter ``user``), or a predefined value such as
        "dr.who" if not given
    spnego: when kerberos authentication is enabled, auth is negotiated by
        requests_kerberos https://github.com/requests/requests-kerberos .
        This establishes a session based on existing kinit login and/or
        specified principal/password; parameters are passed with ``kerb_kwargs``
    token: uses an existing Hadoop delegation token from another secured
        service. Indeed, this client can also generate such tokens when
        not insecure. Note that tokens expire, but can be renewed (by a
        previously specified user) and may allow for proxying.

    '''
    tempdir: Incomplete
    protocol: Incomplete
    url: Incomplete
    kerb: Incomplete
    kerb_kwargs: Incomplete
    pars: Incomplete
    proxy: Incomplete
    def __init__(self, host, port: int = 50070, kerberos: bool = False, token: Incomplete | None = None, user: Incomplete | None = None, proxy_to: Incomplete | None = None, kerb_kwargs: Incomplete | None = None, data_proxy: Incomplete | None = None, use_https: bool = False, **kwargs) -> None:
        """
        Parameters
        ----------
        host: str
            Name-node address
        port: int
            Port for webHDFS
        kerberos: bool
            Whether to authenticate with kerberos for this connection
        token: str or None
            If given, use this token on every call to authenticate. A user
            and user-proxy may be encoded in the token and should not be also
            given
        user: str or None
            If given, assert the user name to connect with
        proxy_to: str or None
            If given, the user has the authority to proxy, and this value is
            the user in who's name actions are taken
        kerb_kwargs: dict
            Any extra arguments for HTTPKerberosAuth, see
            `<https://github.com/requests/requests-kerberos/blob/master/requests_kerberos/kerberos_.py>`_
        data_proxy: dict, callable or None
            If given, map data-node addresses. This can be necessary if the
            HDFS cluster is behind a proxy, running on Docker or otherwise has
            a mismatch between the host-names given by the name-node and the
            address by which to refer to them from the client. If a dict,
            maps host names ``host->data_proxy[host]``; if a callable, full
            URLs are passed, and function must conform to
            ``url->data_proxy(url)``.
        use_https: bool
            Whether to connect to the Name-node using HTTPS instead of HTTP
        kwargs
        """
    @property
    def fsid(self): ...
    def info(self, path): ...
    def ls(self, path, detail: bool = False): ...
    def content_summary(self, path):
        """Total numbers of files, directories and bytes under path"""
    def ukey(self, path):
        """Checksum info of file, giving method and result"""
    def home_directory(self):
        """Get user's home directory"""
    def get_delegation_token(self, renewer: Incomplete | None = None):
        """Retrieve token which can give the same authority to other uses

        Parameters
        ----------
        renewer: str or None
            User who may use this token; if None, will be current user
        """
    def renew_delegation_token(self, token):
        """Make token live longer. Returns new expiry time"""
    def cancel_delegation_token(self, token) -> None:
        """Stop the token from being useful"""
    def chmod(self, path, mod) -> None:
        """Set the permission at path

        Parameters
        ----------
        path: str
            location to set (file or directory)
        mod: str or int
            posix epresentation or permission, give as oct string, e.g, '777'
            or 0o777
        """
    def chown(self, path, owner: Incomplete | None = None, group: Incomplete | None = None) -> None:
        """Change owning user and/or group"""
    def set_replication(self, path, replication) -> None:
        """
        Set file replication factor

        Parameters
        ----------
        path: str
            File location (not for directories)
        replication: int
            Number of copies of file on the cluster. Should be smaller than
            number of data nodes; normally 3 on most systems.
        """
    def mkdir(self, path, **kwargs) -> None: ...
    def makedirs(self, path, exist_ok: bool = False) -> None: ...
    def mv(self, path1, path2, **kwargs) -> None: ...
    def rm(self, path, recursive: bool = False, **kwargs) -> None: ...
    def rm_file(self, path, **kwargs) -> None: ...
    def cp_file(self, lpath, rpath, **kwargs) -> None: ...

class WebHDFile(AbstractBufferedFile):
    """A file living in HDFS over webHDFS"""
    permissions: Incomplete
    target: Incomplete
    path: Incomplete
    def __init__(self, fs, path, **kwargs) -> None: ...
    def commit(self) -> None: ...
    def discard(self) -> None: ...
