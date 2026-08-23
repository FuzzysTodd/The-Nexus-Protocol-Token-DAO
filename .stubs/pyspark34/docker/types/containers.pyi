from .. import errors as errors
from ..utils.utils import convert_port_bindings as convert_port_bindings, convert_tmpfs_mounts as convert_tmpfs_mounts, convert_volume_binds as convert_volume_binds, format_environment as format_environment, format_extra_hosts as format_extra_hosts, normalize_links as normalize_links, parse_bytes as parse_bytes, parse_devices as parse_devices, split_command as split_command, version_gte as version_gte, version_lt as version_lt
from .base import DictType as DictType
from .healthcheck import Healthcheck as Healthcheck
from _typeshed import Incomplete

class LogConfigTypesEnum:
    JSON: Incomplete
    SYSLOG: Incomplete
    JOURNALD: Incomplete
    GELF: Incomplete
    FLUENTD: Incomplete
    NONE: Incomplete

class LogConfig(DictType):
    """
    Configure logging for a container, when provided as an argument to
    :py:meth:`~docker.api.container.ContainerApiMixin.create_host_config`.
    You may refer to the
    `official logging driver documentation <https://docs.docker.com/config/containers/logging/configure/>`_
    for more information.

    Args:
        type (str): Indicate which log driver to use. A set of valid drivers
            is provided as part of the :py:attr:`LogConfig.types`
            enum. Other values may be accepted depending on the engine version
            and available logging plugins.
        config (dict): A driver-dependent configuration dictionary. Please
            refer to the driver's documentation for a list of valid config
            keys.

    Example:

        >>> from docker.types import LogConfig
        >>> lc = LogConfig(type=LogConfig.types.JSON, config={
        ...   'max-size': '1g',
        ...   'labels': 'production_status,geo'
        ... })
        >>> hc = client.create_host_config(log_config=lc)
        >>> container = client.create_container('busybox', 'true',
        ...    host_config=hc)
        >>> client.inspect_container(container)['HostConfig']['LogConfig']
        {'Type': 'json-file', 'Config': {'labels': 'production_status,geo', 'max-size': '1g'}}
    """
    types = LogConfigTypesEnum
    def __init__(self, **kwargs) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, value) -> None: ...
    @property
    def config(self): ...
    def set_config_value(self, key, value) -> None:
        """ Set a the value for ``key`` to ``value`` inside the ``config``
            dict.
        """
    def unset_config(self, key) -> None:
        """ Remove the ``key`` property from the ``config`` dict. """

class Ulimit(DictType):
    """
    Create a ulimit declaration to be used with
    :py:meth:`~docker.api.container.ContainerApiMixin.create_host_config`.

    Args:

        name (str): Which ulimit will this apply to. The valid names can be
            found in '/etc/security/limits.conf' on a gnu/linux system.
        soft (int): The soft limit for this ulimit. Optional.
        hard (int): The hard limit for this ulimit. Optional.

    Example:

        >>> nproc_limit = docker.types.Ulimit(name='nproc', soft=1024)
        >>> hc = client.create_host_config(ulimits=[nproc_limit])
        >>> container = client.create_container(
                'busybox', 'true', host_config=hc
            )
        >>> client.inspect_container(container)['HostConfig']['Ulimits']
        [{'Name': 'nproc', 'Hard': 0, 'Soft': 1024}]

    """
    def __init__(self, **kwargs) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value) -> None: ...
    @property
    def soft(self): ...
    @soft.setter
    def soft(self, value) -> None: ...
    @property
    def hard(self): ...
    @hard.setter
    def hard(self, value) -> None: ...

class DeviceRequest(DictType):
    """
    Create a device request to be used with
    :py:meth:`~docker.api.container.ContainerApiMixin.create_host_config`.

    Args:

        driver (str): Which driver to use for this device. Optional.
        count (int): Number or devices to request. Optional.
            Set to -1 to request all available devices.
        device_ids (list): List of strings for device IDs. Optional.
            Set either ``count`` or ``device_ids``.
        capabilities (list): List of lists of strings to request
            capabilities. Optional. The global list acts like an OR,
            and the sub-lists are AND. The driver will try to satisfy
            one of the sub-lists.
            Available capabilities for the ``nvidia`` driver can be found
            `here <https://github.com/NVIDIA/nvidia-container-runtime>`_.
        options (dict): Driver-specific options. Optional.
    """
    def __init__(self, **kwargs) -> None: ...
    @property
    def driver(self): ...
    @driver.setter
    def driver(self, value) -> None: ...
    @property
    def count(self): ...
    @count.setter
    def count(self, value) -> None: ...
    @property
    def device_ids(self): ...
    @device_ids.setter
    def device_ids(self, value) -> None: ...
    @property
    def capabilities(self): ...
    @capabilities.setter
    def capabilities(self, value) -> None: ...
    @property
    def options(self): ...
    @options.setter
    def options(self, value) -> None: ...

class HostConfig(dict):
    def __init__(self, version, binds: Incomplete | None = None, port_bindings: Incomplete | None = None, lxc_conf: Incomplete | None = None, publish_all_ports: bool = False, links: Incomplete | None = None, privileged: bool = False, dns: Incomplete | None = None, dns_search: Incomplete | None = None, volumes_from: Incomplete | None = None, network_mode: Incomplete | None = None, restart_policy: Incomplete | None = None, cap_add: Incomplete | None = None, cap_drop: Incomplete | None = None, devices: Incomplete | None = None, extra_hosts: Incomplete | None = None, read_only: Incomplete | None = None, pid_mode: Incomplete | None = None, ipc_mode: Incomplete | None = None, security_opt: Incomplete | None = None, ulimits: Incomplete | None = None, log_config: Incomplete | None = None, mem_limit: Incomplete | None = None, memswap_limit: Incomplete | None = None, mem_reservation: Incomplete | None = None, kernel_memory: Incomplete | None = None, mem_swappiness: Incomplete | None = None, cgroup_parent: Incomplete | None = None, group_add: Incomplete | None = None, cpu_quota: Incomplete | None = None, cpu_period: Incomplete | None = None, blkio_weight: Incomplete | None = None, blkio_weight_device: Incomplete | None = None, device_read_bps: Incomplete | None = None, device_write_bps: Incomplete | None = None, device_read_iops: Incomplete | None = None, device_write_iops: Incomplete | None = None, oom_kill_disable: bool = False, shm_size: Incomplete | None = None, sysctls: Incomplete | None = None, tmpfs: Incomplete | None = None, oom_score_adj: Incomplete | None = None, dns_opt: Incomplete | None = None, cpu_shares: Incomplete | None = None, cpuset_cpus: Incomplete | None = None, userns_mode: Incomplete | None = None, uts_mode: Incomplete | None = None, pids_limit: Incomplete | None = None, isolation: Incomplete | None = None, auto_remove: bool = False, storage_opt: Incomplete | None = None, init: Incomplete | None = None, init_path: Incomplete | None = None, volume_driver: Incomplete | None = None, cpu_count: Incomplete | None = None, cpu_percent: Incomplete | None = None, nano_cpus: Incomplete | None = None, cpuset_mems: Incomplete | None = None, runtime: Incomplete | None = None, mounts: Incomplete | None = None, cpu_rt_period: Incomplete | None = None, cpu_rt_runtime: Incomplete | None = None, device_cgroup_rules: Incomplete | None = None, device_requests: Incomplete | None = None, cgroupns: Incomplete | None = None) -> None: ...

def host_config_type_error(param, param_value, expected): ...
def host_config_version_error(param, version, less_than: bool = True): ...
def host_config_value_error(param, param_value): ...
def host_config_incompatible_error(param, param_value, incompatible_param): ...

class ContainerConfig(dict):
    def __init__(self, version, image, command, hostname: Incomplete | None = None, user: Incomplete | None = None, detach: bool = False, stdin_open: bool = False, tty: bool = False, ports: Incomplete | None = None, environment: Incomplete | None = None, volumes: Incomplete | None = None, network_disabled: bool = False, entrypoint: Incomplete | None = None, working_dir: Incomplete | None = None, domainname: Incomplete | None = None, host_config: Incomplete | None = None, mac_address: Incomplete | None = None, labels: Incomplete | None = None, stop_signal: Incomplete | None = None, networking_config: Incomplete | None = None, healthcheck: Incomplete | None = None, stop_timeout: Incomplete | None = None, runtime: Incomplete | None = None) -> None: ...
