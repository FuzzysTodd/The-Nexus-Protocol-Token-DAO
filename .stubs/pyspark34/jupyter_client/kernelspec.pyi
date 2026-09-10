import typing as t
from _typeshed import Incomplete
from traitlets import HasTraits
from traitlets.config import LoggingConfigurable

pjoin: Incomplete
NATIVE_KERNEL_NAME: str

class KernelSpec(HasTraits):
    """A kernel spec model object."""
    argv: Incomplete
    name: Incomplete
    mimetype: Incomplete
    display_name: Incomplete
    language: Incomplete
    env: Incomplete
    resource_dir: Incomplete
    interrupt_mode: Incomplete
    metadata: Incomplete
    @classmethod
    def from_resource_dir(cls, resource_dir: str) -> KernelSpec:
        """Create a KernelSpec object by reading kernel.json

        Pass the path to the *directory* containing kernel.json.
        """
    def to_dict(self) -> dict[str, t.Any]:
        """Convert the kernel spec to a dict."""
    def to_json(self) -> str:
        """Serialise this kernelspec to a JSON object.

        Returns a string.
        """

class NoSuchKernel(KeyError):
    """An error raised when there is no kernel of a give name."""
    name: Incomplete
    def __init__(self, name: str) -> None:
        """Initialize the error."""

class KernelSpecManager(LoggingConfigurable):
    """A manager for kernel specs."""
    kernel_spec_class: Incomplete
    ensure_native_kernel: Incomplete
    data_dir: Incomplete
    user_kernel_dir: Incomplete
    whitelist: Incomplete
    allowed_kernelspecs: Incomplete
    kernel_dirs: Incomplete
    def find_kernel_specs(self) -> dict[str, str]:
        """Returns a dict mapping kernel names to resource directories."""
    def get_kernel_spec(self, kernel_name: str) -> KernelSpec:
        """Returns a :class:`KernelSpec` instance for the given kernel_name.

        Raises :exc:`NoSuchKernel` if the given kernel name is not found.
        """
    def get_all_specs(self) -> dict[str, t.Any]:
        '''Returns a dict mapping kernel names to kernelspecs.

        Returns a dict of the form::

            {
              \'kernel_name\': {
                \'resource_dir\': \'/path/to/kernel_name\',
                \'spec\': {"the spec itself": ...}
              },
              ...
            }
        '''
    def remove_kernel_spec(self, name: str) -> str:
        """Remove a kernel spec directory by name.

        Returns the path that was deleted.
        """
    def install_kernel_spec(self, source_dir: str, kernel_name: str | None = None, user: bool = False, replace: bool | None = None, prefix: str | None = None) -> str:
        """Install a kernel spec by copying its directory.

        If ``kernel_name`` is not given, the basename of ``source_dir`` will
        be used.

        If ``user`` is False, it will attempt to install into the systemwide
        kernel registry. If the process does not have appropriate permissions,
        an :exc:`OSError` will be raised.

        If ``prefix`` is given, the kernelspec will be installed to
        PREFIX/share/jupyter/kernels/KERNEL_NAME. This can be sys.prefix
        for installation inside virtual or conda envs.
        """
    def install_native_kernel_spec(self, user: bool = False) -> None:
        """DEPRECATED: Use ipykernel.kernelspec.install"""

def find_kernel_specs() -> dict[str, str]:
    """Returns a dict mapping kernel names to resource directories."""
def get_kernel_spec(kernel_name: str) -> KernelSpec:
    """Returns a :class:`KernelSpec` instance for the given kernel_name.

    Raises KeyError if the given kernel name is not found.
    """
def install_kernel_spec(source_dir: str, kernel_name: str | None = None, user: bool = False, replace: bool | None = False, prefix: str | None = None) -> str:
    """Install a kernel spec in a given directory."""
def install_native_kernel_spec(user: bool = False) -> None:
    """Install the native kernel spec."""
