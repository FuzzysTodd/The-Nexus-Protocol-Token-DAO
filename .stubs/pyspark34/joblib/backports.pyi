from _typeshed import Incomplete

class Version:
    """Backport from deprecated distutils

    We maintain this backport to avoid introducing a new dependency on
    `packaging`.

    We might rexplore this choice in the future if all major Python projects
    introduce a dependency on packaging anyway.
    """
    def __init__(self, vstring: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class LooseVersion(Version):
    """Backport from deprecated distutils

    We maintain this backport to avoid introducing a new dependency on
    `packaging`.

    We might rexplore this choice in the future if all major Python projects
    introduce a dependency on packaging anyway.
    """
    component_re: Incomplete
    def __init__(self, vstring: Incomplete | None = None) -> None: ...
    vstring: Incomplete
    version: Incomplete
    def parse(self, vstring) -> None: ...

def make_memmap(filename, dtype: str = 'uint8', mode: str = 'r+', offset: int = 0, shape: Incomplete | None = None, order: str = 'C', unlink_on_gc_collect: bool = False):
    """Custom memmap constructor compatible with numpy.memmap.

        This function:
        - is a backport the numpy memmap offset fix (See
          https://github.com/numpy/numpy/pull/8443 for more details.
          The numpy fix is available starting numpy 1.13)
        - adds ``unlink_on_gc_collect``, which specifies  explicitly whether
          the process re-constructing the memmap owns a reference to the
          underlying file. If set to True, it adds a finalizer to the
          newly-created memmap that sends a maybe_unlink request for the
          memmaped file to resource_tracker.
        """

access_denied_errors: Incomplete

def concurrency_safe_rename(src, dst) -> None:
    """Renames ``src`` into ``dst`` overwriting ``dst`` if it exists.

        On Windows os.replace can yield permission errors if executed by two
        different processes.
        """
