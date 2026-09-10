import types
from typing import Any, Dict, Iterable, List, NamedTuple, Sequence, Set
from xml.dom import minidom as minidom

disclaim_module_ids: Set[int]
SPECIAL_FLAGS: Any
FLAGS_MODULE: types.ModuleType

class _ModuleObjectAndName(NamedTuple):
    """Module object and name.

  Fields:
  - module: object, module object.
  - module_name: str, module name.
  """
    module: types.ModuleType
    module_name: str

def get_module_object_and_name(globals_dict: Dict[str, Any]) -> _ModuleObjectAndName:
    """Returns the module that defines a global environment, and its name.

  Args:
    globals_dict: A dictionary that should correspond to an environment
      providing the values of the globals.

  Returns:
    _ModuleObjectAndName - pair of module object & module name.
    Returns (None, None) if the module could not be identified.
  """
def get_calling_module_object_and_name() -> _ModuleObjectAndName:
    """Returns the module that's calling into this module.

  We generally use this function to get the name of the module calling a
  DEFINE_foo... function.

  Returns:
    The module object that called into this one.

  Raises:
    AssertionError: Raised when no calling module could be identified.
  """
def get_calling_module() -> str:
    """Returns the name of the module that's calling into this module."""
def create_xml_dom_element(doc: minidom.Document, name: str, value: Any) -> minidom.Element:
    """Returns an XML DOM element with name and text value.

  Args:
    doc: minidom.Document, the DOM document it should create nodes from.
    name: str, the tag of XML element.
    value: object, whose string representation will be used
        as the value of the XML element. Illegal or highly discouraged xml 1.0
        characters are stripped.

  Returns:
    An instance of minidom.Element.
  """
def get_help_width() -> int:
    """Returns the integer width of help lines that is used in TextWrap."""
def get_flag_suggestions(attempt: str | None, longopt_list: Sequence[str]) -> List[str]:
    """Returns helpful similar matches for an invalid flag."""
def text_wrap(text: str, length: int | None = None, indent: str = '', firstline_indent: str | None = None) -> str:
    """Wraps a given text to a maximum line length and returns it.

  It turns lines that only contain whitespace into empty lines, keeps new lines,
  and expands tabs using 4 spaces.

  Args:
    text: str, text to wrap.
    length: int, maximum length of a line, includes indentation.
        If this is None then use get_help_width()
    indent: str, indent for all but first line.
    firstline_indent: str, indent for first line; if None, fall back to indent.

  Returns:
    str, the wrapped text.

  Raises:
    ValueError: Raised if indent or firstline_indent not shorter than length.
  """
def flag_dict_to_args(flag_map: Dict[str, Any], multi_flags: Set[str] | None = None) -> Iterable[str]:
    """Convert a dict of values into process call parameters.

  This method is used to convert a dictionary into a sequence of parameters
  for a binary that parses arguments using this module.

  Args:
    flag_map: dict, a mapping where the keys are flag names (strings).
        values are treated according to their type:

        * If value is ``None``, then only the name is emitted.
        * If value is ``True``, then only the name is emitted.
        * If value is ``False``, then only the name prepended with 'no' is
          emitted.
        * If value is a string then ``--name=value`` is emitted.
        * If value is a collection, this will emit
          ``--name=value1,value2,value3``, unless the flag name is in
          ``multi_flags``, in which case this will emit
          ``--name=value1 --name=value2 --name=value3``.
        * Everything else is converted to string an passed as such.

    multi_flags: set, names (strings) of flags that should be treated as
        multi-flags.
  Yields:
    sequence of string suitable for a subprocess execution.
  """
def trim_docstring(docstring: str) -> str:
    """Removes indentation from triple-quoted strings.

  This is the function specified in PEP 257 to handle docstrings:
  https://www.python.org/dev/peps/pep-0257/.

  Args:
    docstring: str, a python docstring.

  Returns:
    str, docstring with indentation removed.
  """
def doc_to_help(doc: str) -> str:
    """Takes a __doc__ string and reformats it as help."""
