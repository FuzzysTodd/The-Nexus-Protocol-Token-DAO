from _typeshed import Incomplete
from toml.decoder import InlineTableDict as InlineTableDict

unicode = str

def dump(o, f, encoder: Incomplete | None = None):
    """Writes out dict as toml to a file

    Args:
        o: Object to dump into toml
        f: File descriptor where the toml should be stored
        encoder: The ``TomlEncoder`` to use for constructing the output string

    Returns:
        String containing the toml corresponding to dictionary

    Raises:
        TypeError: When anything other than file descriptor is passed
    """
def dumps(o, encoder: Incomplete | None = None):
    '''Stringifies input dict as toml

    Args:
        o: Object to dump into toml
        encoder: The ``TomlEncoder`` to use for constructing the output string

    Returns:
        String containing the toml corresponding to dict

    Examples:
        ```python
        >>> import toml
        >>> output = {
        ... \'a\': "I\'m a string",
        ... \'b\': ["I\'m", "a", "list"],
        ... \'c\': 2400
        ... }
        >>> toml.dumps(output)
        \'a = "I\'m a string"
b = [ "I\'m", "a", "list",]
c = 2400
\'
        ```
    '''

class TomlEncoder:
    preserve: Incomplete
    dump_funcs: Incomplete
    def __init__(self, _dict=..., preserve: bool = False) -> None: ...
    def get_empty_table(self): ...
    def dump_list(self, v): ...
    def dump_inline_table(self, section):
        """Preserve inline table in its compact syntax instead of expanding
        into subsection.

        https://github.com/toml-lang/toml#user-content-inline-table
        """
    def dump_value(self, v): ...
    def dump_sections(self, o, sup): ...

class TomlPreserveInlineDictEncoder(TomlEncoder):
    def __init__(self, _dict=...) -> None: ...

class TomlArraySeparatorEncoder(TomlEncoder):
    separator: Incomplete
    def __init__(self, _dict=..., preserve: bool = False, separator: str = ',') -> None: ...
    def dump_list(self, v): ...

class TomlNumpyEncoder(TomlEncoder):
    def __init__(self, _dict=..., preserve: bool = False) -> None: ...

class TomlPreserveCommentEncoder(TomlEncoder):
    def __init__(self, _dict=..., preserve: bool = False) -> None: ...

class TomlPathlibEncoder(TomlEncoder):
    def dump_value(self, v): ...
