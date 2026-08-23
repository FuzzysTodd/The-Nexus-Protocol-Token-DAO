import requests
from .. import auth as auth
from ..constants import DEFAULT_MAX_POOL_SIZE as DEFAULT_MAX_POOL_SIZE, DEFAULT_NUM_POOLS as DEFAULT_NUM_POOLS, DEFAULT_NUM_POOLS_SSH as DEFAULT_NUM_POOLS_SSH, DEFAULT_TIMEOUT_SECONDS as DEFAULT_TIMEOUT_SECONDS, DEFAULT_USER_AGENT as DEFAULT_USER_AGENT, IS_WINDOWS_PLATFORM as IS_WINDOWS_PLATFORM, MINIMUM_DOCKER_API_VERSION as MINIMUM_DOCKER_API_VERSION, STREAM_HEADER_SIZE_BYTES as STREAM_HEADER_SIZE_BYTES
from ..errors import DockerException as DockerException, InvalidVersion as InvalidVersion, TLSParameterError as TLSParameterError, create_api_error_from_http_exception as create_api_error_from_http_exception
from ..tls import TLSConfig as TLSConfig
from ..transport import NpipeHTTPAdapter as NpipeHTTPAdapter, SSHHTTPAdapter as SSHHTTPAdapter, SSLHTTPAdapter as SSLHTTPAdapter, UnixHTTPAdapter as UnixHTTPAdapter
from ..utils import check_resource as check_resource, config as config, update_headers as update_headers, utils as utils
from ..utils.json_stream import json_stream as json_stream
from ..utils.proxy import ProxyConfig as ProxyConfig
from ..utils.socket import consume_socket_output as consume_socket_output, demux_adaptor as demux_adaptor, frames_iter as frames_iter
from .build import BuildApiMixin as BuildApiMixin
from .config import ConfigApiMixin as ConfigApiMixin
from .container import ContainerApiMixin as ContainerApiMixin
from .daemon import DaemonApiMixin as DaemonApiMixin
from .exec_api import ExecApiMixin as ExecApiMixin
from .image import ImageApiMixin as ImageApiMixin
from .network import NetworkApiMixin as NetworkApiMixin
from .plugin import PluginApiMixin as PluginApiMixin
from .secret import SecretApiMixin as SecretApiMixin
from .service import ServiceApiMixin as ServiceApiMixin
from .swarm import SwarmApiMixin as SwarmApiMixin
from .volume import VolumeApiMixin as VolumeApiMixin
from _typeshed import Incomplete

class APIClient(requests.Session, BuildApiMixin, ConfigApiMixin, ContainerApiMixin, DaemonApiMixin, ExecApiMixin, ImageApiMixin, NetworkApiMixin, PluginApiMixin, SecretApiMixin, ServiceApiMixin, SwarmApiMixin, VolumeApiMixin):
    """
    A low-level client for the Docker Engine API.

    Example:

        >>> import docker
        >>> client = docker.APIClient(base_url='unix://var/run/docker.sock')
        >>> client.version()
        {u'ApiVersion': u'1.33',
         u'Arch': u'amd64',
         u'BuildTime': u'2017-11-19T18:46:37.000000000+00:00',
         u'GitCommit': u'f4ffd2511c',
         u'GoVersion': u'go1.9.2',
         u'KernelVersion': u'4.14.3-1-ARCH',
         u'MinAPIVersion': u'1.12',
         u'Os': u'linux',
         u'Version': u'17.10.0-ce'}

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
    __attrs__: Incomplete
    base_url: Incomplete
    timeout: Incomplete
    credstore_env: Incomplete
    def __init__(self, base_url: Incomplete | None = None, version: Incomplete | None = None, timeout=..., tls: bool = False, user_agent=..., num_pools: Incomplete | None = None, credstore_env: Incomplete | None = None, use_ssh_client: bool = False, max_pool_size=...) -> None: ...
    def get_adapter(self, url): ...
    @property
    def api_version(self): ...
    def reload_config(self, dockercfg_path: Incomplete | None = None) -> None:
        """
        Force a reload of the auth configuration

        Args:
            dockercfg_path (str): Use a custom path for the Docker config file
                (default ``$HOME/.docker/config.json`` if present,
                otherwise ``$HOME/.dockercfg``)

        Returns:
            None
        """
