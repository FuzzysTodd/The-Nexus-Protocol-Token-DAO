from _typeshed import Incomplete
from typing import Iterable

class NameGenerator:
    """Utility for generating distinct C names from Python names.

    Since C names can't use '.' (or unicode), some care is required to
    make C names generated from Python names unique. Also, we want to
    avoid generating overly long C names since they make the generated
    code harder to read.

    Note that we don't restrict ourselves to a 32-character distinguishing
    prefix guaranteed by the C standard since all the compilers we care
    about at the moment support longer names without issues.

    For names that are exported in a shared library (not static) use
    exported_name() instead.

    Summary of the approach:

    * Generate a unique name prefix from suffix of fully-qualified
      module name used for static names. If only compiling a single
      module, this can be empty. For example, if the modules are
      'foo.bar' and 'foo.baz', the prefixes can be 'bar_' and 'baz_',
      respectively. If the modules are 'bar.foo' and 'baz.foo', the
      prefixes will be 'bar_foo_' and 'baz_foo_'.

    * Replace '.' in the Python name with '___' in the C name. (And
      replace the unlikely but possible '___' with '___3_'. This
      collides '___' with '.3_', but this is OK because names
      may not start with a digit.)

    The generated should be internal to a build and thus the mapping is
    arbitrary. Just generating names '1', '2', ... would be correct,
    though not very usable.
    """
    module_map: Incomplete
    translations: Incomplete
    used_names: Incomplete
    def __init__(self, groups: Iterable[list[str]]) -> None:
        """Initialize with a list of modules in each compilation group.

        The names of modules are used to shorten names referring to
        modules, for convenience. Arbitrary module
        names are supported for generated names, but uncompiled modules
        will use long names.
        """
    def private_name(self, module: str, partial_name: str | None = None) -> str:
        """Return a C name usable for a static definition.

        Return a distinct result for each (module, partial_name) pair.

        The caller should add a suitable prefix to the name to avoid
        conflicts with other C names. Only ensure that the results of
        this function are unique, not that they aren't overlapping with
        arbitrary names.

        If a name is not specific to any module, the module argument can
        be an empty string.
        """

def exported_name(fullname: str) -> str:
    """Return a C name usable for an exported definition.

    This is like private_name(), but the output only depends on the
    'fullname' argument, so the names are distinct across multiple
    builds.
    """
def make_module_translation_map(names: list[str]) -> dict[str, str]: ...
def candidate_suffixes(fullname: str) -> list[str]: ...
