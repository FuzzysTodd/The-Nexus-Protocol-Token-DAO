from .provisioner_base import KernelProvisionerBase as KernelProvisionerBase
from _typeshed import Incomplete
from importlib.metadata import EntryPoint
from traitlets.config import SingletonConfigurable
from typing import Any, Dict

class KernelProvisionerFactory(SingletonConfigurable):
    '''
    :class:`KernelProvisionerFactory` is responsible for creating provisioner instances.

    A singleton instance, `KernelProvisionerFactory` is also used by the :class:`KernelSpecManager`
    to validate `kernel_provisioner` references found in kernel specifications to confirm their
    availability (in cases where the kernel specification references a kernel provisioner that has
    not been installed into the current Python environment).

    It\'s ``default_provisioner_name`` attribute can be used to specify the default provisioner
    to use when a kernel_spec is found to not reference a provisioner.  It\'s value defaults to
    `"local-provisioner"` which identifies the local provisioner implemented by
    :class:`LocalProvisioner`.
    '''
    GROUP_NAME: str
    provisioners: Dict[str, EntryPoint]
    default_provisioner_name_env: str
    default_provisioner_name: Incomplete
    def __init__(self, **kwargs: Any) -> None:
        """Initialize a kernel provisioner factory."""
    def is_provisioner_available(self, kernel_spec: Any) -> bool:
        """
        Reads the associated ``kernel_spec`` to determine the provisioner and returns whether it
        exists as an entry_point (True) or not (False).  If the referenced provisioner is not
        in the current cache or cannot be loaded via entry_points, a warning message is issued
        indicating it is not available.
        """
    def create_provisioner_instance(self, kernel_id: str, kernel_spec: Any, parent: Any) -> KernelProvisionerBase:
        """
        Reads the associated ``kernel_spec`` to see if it has a `kernel_provisioner` stanza.
        If one exists, it instantiates an instance.  If a kernel provisioner is not
        specified in the kernel specification, a default provisioner stanza is fabricated
        and instantiated corresponding to the current value of ``default_provisioner_name`` trait.
        The instantiated instance is returned.

        If the provisioner is found to not exist (not registered via entry_points),
        `ModuleNotFoundError` is raised.
        """
    def get_provisioner_entries(self) -> Dict[str, str]:
        """
        Returns a dictionary of provisioner entries.

        The key is the provisioner name for its entry point.  The value is the colon-separated
        string of the entry point's module name and object name.
        """
