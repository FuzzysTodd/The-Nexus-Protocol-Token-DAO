from .external.docscrape import NumpyDocString as NumpyDocString
from _typeshed import Incomplete

class DocstringComponents:
    regexp: Incomplete
    entries: Incomplete
    def __init__(self, comp_dict, strip_whitespace: bool = True) -> None:
        """Read entries from a dict, optionally stripping outer whitespace."""
    def __getattr__(self, attr):
        """Provide dot access to entries for clean raw docstrings."""
    @classmethod
    def from_nested_components(cls, **kwargs):
        """Add multiple sub-sets of components."""
    @classmethod
    def from_function_params(cls, func):
        """Use the numpydoc parser to extract components from existing func."""
