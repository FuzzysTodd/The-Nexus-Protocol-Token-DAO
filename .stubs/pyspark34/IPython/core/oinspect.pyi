from IPython.utils.colorable import Colorable
from IPython.utils.coloransi import TermColors
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict

__all__ = ['Inspector', 'InspectColors']

@dataclass
class OInfo:
    ismagic: bool
    isalias: bool
    found: bool
    namespace: str | None
    parent: Any
    obj: Any
    def get(self, field):
        """Get a field from the object for backward compatibility with before 8.12

        see https://github.com/h5py/h5py/issues/2253
        """
    def __init__(self, ismagic, isalias, found, namespace, parent, obj) -> None: ...
Colors = TermColors
InspectColors: Incomplete

class Inspector(Colorable):
    color_table: Incomplete
    parser: Incomplete
    format: Incomplete
    str_detail_level: Incomplete
    def __init__(self, color_table=..., code_color_table=..., scheme: Incomplete | None = None, str_detail_level: int = 0, parent: Incomplete | None = None, config: Incomplete | None = None) -> None: ...
    def set_active_scheme(self, scheme) -> None: ...
    def noinfo(self, msg, oname) -> None:
        """Generic message when no information is found."""
    def pdef(self, obj, oname: str = '') -> None:
        """Print the call signature for any callable object.

        If the object is a class, print the constructor information."""
    def pdoc(self, obj, oname: str = '', formatter: Incomplete | None = None) -> None:
        """Print the docstring for any object.

        Optional:
        -formatter: a function to run the docstring through for specially
        formatted docstrings.

        Examples
        --------
        In [1]: class NoInit:
           ...:     pass

        In [2]: class NoDoc:
           ...:     def __init__(self):
           ...:         pass

        In [3]: %pdoc NoDoc
        No documentation found for NoDoc

        In [4]: %pdoc NoInit
        No documentation found for NoInit

        In [5]: obj = NoInit()

        In [6]: %pdoc obj
        No documentation found for obj

        In [5]: obj2 = NoDoc()

        In [6]: %pdoc obj2
        No documentation found for obj2
        """
    def psource(self, obj, oname: str = '') -> None:
        """Print the source code for an object."""
    def pfile(self, obj, oname: str = '') -> None:
        """Show the whole file where an object was defined."""
    def format_mime(self, bundle: UnformattedBundle) -> Bundle:
        """Format a mimebundle being created by _make_info_unformatted into a real mimebundle"""
    def pinfo(self, obj, oname: str = '', formatter: Incomplete | None = None, info: OInfo | None = None, detail_level: int = 0, enable_html_pager: bool = True, omit_sections=()):
        """Show detailed information about an object.

        Optional arguments:

        - oname: name of the variable pointing to the object.

        - formatter: callable (optional)
              A special formatter for docstrings.

              The formatter is a callable that takes a string as an input
              and returns either a formatted string or a mime type bundle
              in the form of a dictionary.

              Although the support of custom formatter returning a string
              instead of a mime type bundle is deprecated.

        - info: a structure with some information fields which may have been
          precomputed already.

        - detail_level: if set to 1, more information is given.

        - omit_sections: set of section keys and titles to omit
        """
    def info(self, obj, oname: str = '', info: Incomplete | None = None, detail_level: int = 0) -> Dict[str, Any]:
        """Compute a dict with detailed information about an object.

        Parameters
        ----------
        obj : any
            An object to find information about
        oname : str (default: '')
            Name of the variable pointing to `obj`.
        info : (default: None)
            A struct (dict like with attr access) with some information fields
            which may have been precomputed already.
        detail_level : int (default:0)
            If set to 1, more information is given.

        Returns
        -------
        An object info dict with known fields from `info_fields`. Keys are
        strings, values are string or None.
        """
    def psearch(self, pattern, ns_table, ns_search=[], ignore_case: bool = False, show_all: bool = False, *, list_types: bool = False) -> None:
        """Search namespaces with wildcards for objects.

        Arguments:

        - pattern: string containing shell-like wildcards to use in namespace
          searches and optionally a type specification to narrow the search to
          objects of that type.

        - ns_table: dict of name->namespaces for search.

        Optional arguments:

          - ns_search: list of namespace names to include in search.

          - ignore_case(False): make the search case-insensitive.

          - show_all(False): show all names, including those starting with
            underscores.

          - list_types(False): list all available object types for object matching.
        """
