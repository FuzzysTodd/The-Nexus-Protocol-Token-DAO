from _typeshed import Incomplete
from collections.abc import Generator

class VendorImporter:
    """
    A PEP 302 meta path importer for finding optionally-vendored
    or otherwise naturally-installed packages from root_name.
    """
    root_name: Incomplete
    vendored_names: Incomplete
    vendor_pkg: Incomplete
    def __init__(self, root_name, vendored_names=(), vendor_pkg: Incomplete | None = None) -> None: ...
    @property
    def search_path(self) -> Generator[Incomplete, None, None]:
        """
        Search first the vendor package then as a natural package.
        """
    def load_module(self, fullname):
        """
        Iterate over the search path to locate and load fullname.
        """
    def create_module(self, spec): ...
    def exec_module(self, module) -> None: ...
    def find_spec(self, fullname, path: Incomplete | None = None, target: Incomplete | None = None):
        """Return a module spec for vendored names."""
    def install(self) -> None:
        """
        Install this importer into sys.meta_path if not already present.
        """

names: Incomplete
