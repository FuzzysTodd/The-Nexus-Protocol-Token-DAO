from .api.client import APIClient as APIClient
from .constants import DEFAULT_MAX_POOL_SIZE as DEFAULT_MAX_POOL_SIZE, DEFAULT_TIMEOUT_SECONDS as DEFAULT_TIMEOUT_SECONDS
from .models.configs import ConfigCollection as ConfigCollection
from .models.containers import ContainerCollection as ContainerCollection
from .models.images import ImageCollection as ImageCollection
from .models.networks import NetworkCollection as NetworkCollection
from .models.nodes import NodeCollection as NodeCollection
from .models.plugins import PluginCollection as PluginCollection
from .models.secrets import SecretCollection as SecretCollection
from .models.services import ServiceCollection as ServiceCollection
from .models.swarm import Swarm as Swarm
from .models.volumes import VolumeCollection as VolumeCollection
from .utils import kwargs_from_env as kwargs_from_env
from _typeshed import Incomplete

class DockerClient:
    """
    A client for communicating with a Docker server.

    Example:

        >>> import docker
        >>> client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    Args:
        base_url (str): URL to the Docker server. For example,
            ``unix:///var/run/docker.sock`` or ``tcp://127.0.0.1:1234``.
        version (str): The version of the API to use. Set to ``auto`` to
            automatically detect the server's version. Default: ``1.35``
        timeout (int): Default timeout for API calls, in seconds.
        tls (bool or :py:class:`~docker.tls.TLSConfig`): Enable TLS. Pass
            ``True`` to enable it with default options, or pass a
            :py:class:`~docker.tls.TLSConfig` object to use custom
            configuration.
        user_agent (str): Set a custom user agent for requests to the server.
        credstore_env (dict): Override environment variables when calling the
            credential store process.
        use_ssh_client (bool): If set to `True`, an ssh connection is made
            via shelling out to the ssh client. Ensure the ssh client is
            installed and configured on the host.
        max_pool_size (int): The maximum number of connections
            to save in the pool.
    """
    api: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def from_env(cls, **kwargs):
        """
        Return a client configured from environment variables.

        The environment variables used are the same as those used by the
        Docker command-line client. They are:

        .. envvar:: DOCKER_HOST

            The URL to the Docker host.

        .. envvar:: DOCKER_TLS_VERIFY

            Verify the host against a CA certificate.

        .. envvar:: DOCKER_CERT_PATH

            A path to a directory containing TLS certificates to use when
            connecting to the Docker host.

        Args:
            version (str): The version of the API to use. Set to ``auto`` to
                automatically detect the server's version. Default: ``auto``
            timeout (int): Default timeout for API calls, in seconds.
            max_pool_size (int): The maximum number of connections
                to save in the pool.
            ssl_version (int): A valid `SSL version`_.
            assert_hostname (bool): Verify the hostname of the server.
            environment (dict): The environment to read environment variables
                from. Default: the value of ``os.environ``
            credstore_env (dict): Override environment variables when calling
                the credential store process.
            use_ssh_client (bool): If set to `True`, an ssh connection is
                made via shelling out to the ssh client. Ensure the ssh
                client is installed and configured on the host.

        Example:

            >>> import docker
            >>> client = docker.from_env()

        .. _`SSL version`:
            https://docs.python.org/3.5/library/ssl.html#ssl.PROTOCOL_TLSv1
        """
    @property
    def configs(self):
        """
        An object for managing configs on the server. See the
        :doc:`configs documentation <configs>` for full details.
        """
    @property
    def containers(self):
        """
        An object for managing containers on the server. See the
        :doc:`containers documentation <containers>` for full details.
        """
    @property
    def images(self):
        """
        An object for managing images on the server. See the
        :doc:`images documentation <images>` for full details.
        """
    @property
    def networks(self):
        """
        An object for managing networks on the server. See the
        :doc:`networks documentation <networks>` for full details.
        """
    @property
    def nodes(self):
        """
        An object for managing nodes on the server. See the
        :doc:`nodes documentation <nodes>` for full details.
        """
    @property
    def plugins(self):
        """
        An object for managing plugins on the server. See the
        :doc:`plugins documentation <plugins>` for full details.
        """
    @property
    def secrets(self):
        """
        An object for managing secrets on the server. See the
        :doc:`secrets documentation <secrets>` for full details.
        """
    @property
    def services(self):
        """
        An object for managing services on the server. See the
        :doc:`services documentation <services>` for full details.
        """
    @property
    def swarm(self):
        """
        An object for managing a swarm on the server. See the
        :doc:`swarm documentation <swarm>` for full details.
        """
    @property
    def volumes(self):
        """
        An object for managing volumes on the server. See the
        :doc:`volumes documentation <volumes>` for full details.
        """
    def events(self, *args, **kwargs): ...
    def df(self): ...
    def info(self, *args, **kwargs): ...
    def login(self, *args, **kwargs): ...
    def ping(self, *args, **kwargs): ...
    def version(self, *args, **kwargs): ...
    def close(self): ...
    def __getattr__(self, name) -> None: ...

from_env: Incomplete
