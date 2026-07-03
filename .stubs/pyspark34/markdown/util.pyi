from _typeshed import Incomplete
from typing import NamedTuple

BLOCK_LEVEL_ELEMENTS: Incomplete
STX: str
ETX: str
INLINE_PLACEHOLDER_PREFIX: Incomplete
INLINE_PLACEHOLDER: Incomplete
INLINE_PLACEHOLDER_RE: Incomplete
AMP_SUBSTITUTE: Incomplete
HTML_PLACEHOLDER: Incomplete
HTML_PLACEHOLDER_RE: Incomplete
TAG_PLACEHOLDER: Incomplete
RTL_BIDI_RANGES: Incomplete

def get_installed_extensions(): ...
def deprecated(message, stacklevel: int = 2):
    '''
    Raise a `DeprecationWarning` when wrapped function/method is called.

    Usage:
        @deprecated("This method will be removed in version X; use Y instead.")
        def some_method()"
            pass
    '''
def parseBoolValue(value, fail_on_errors: bool = True, preserve_none: bool = False):
    """Parses a string representing boolean value. If parsing was successful,
       returns True or False. If `preserve_none=True`, returns `True`, `False`,
       or `None`. If parsing was not successful, raises `ValueError`, or, if
       `fail_on_errors=False`, returns `None`."""
def code_escape(text):
    """Escape code."""
def nearing_recursion_limit():
    """Return true if current stack depth is within 100 of maximum limit."""

class AtomicString(str):
    """A string which should not be further processed."""

class Processor:
    md: Incomplete
    def __init__(self, md: Incomplete | None = None) -> None: ...

class HtmlStash:
    """
    This class is used for stashing HTML objects that we extract
    in the beginning and replace with place-holders.
    """
    html_counter: int
    rawHtmlBlocks: Incomplete
    tag_counter: int
    tag_data: Incomplete
    def __init__(self) -> None:
        """ Create an `HtmlStash`. """
    def store(self, html):
        """
        Saves an HTML segment for later reinsertion.  Returns a
        placeholder string that needs to be inserted into the
        document.

        Keyword arguments:

        * `html`: an html segment

        Returns : a placeholder string

        """
    def reset(self) -> None: ...
    def get_placeholder(self, key): ...
    def store_tag(self, tag, attrs, left_index, right_index):
        """Store tag data and return a placeholder."""

class _PriorityItem(NamedTuple):
    name: Incomplete
    priority: Incomplete

class Registry:
    '''
    A priority sorted registry.

    A `Registry` instance provides two public methods to alter the data of the
    registry: `register` and `deregister`. Use `register` to add items and
    `deregister` to remove items. See each method for specifics.

    When registering an item, a "name" and a "priority" must be provided. All
    items are automatically sorted by "priority" from highest to lowest. The
    "name" is used to remove ("deregister") and get items.

    A `Registry` instance it like a list (which maintains order) when reading
    data. You may iterate over the items, get an item and get a count (length)
    of all items. You may also check that the registry contains an item.

    When getting an item you may use either the index of the item or the
    string-based "name". For example:

        registry = Registry()
        registry.register(SomeItem(), \'itemname\', 20)
        # Get the item by index
        item = registry[0]
        # Get the item by name
        item = registry[\'itemname\']

    When checking that the registry contains an item, you may use either the
    string-based "name", or a reference to the actual item. For example:

        someitem = SomeItem()
        registry.register(someitem, \'itemname\', 20)
        # Contains the name
        assert \'itemname\' in registry
        # Contains the item instance
        assert someitem in registry

    The method `get_index_for_name` is also available to obtain the index of
    an item using that item\'s assigned "name".
    '''
    def __init__(self) -> None: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...
    def get_index_for_name(self, name):
        """
        Return the index of the given name.
        """
    def register(self, item, name, priority) -> None:
        '''
        Add an item to the registry with the given name and priority.

        Parameters:

        * `item`: The item being registered.
        * `name`: A string used to reference the item.
        * `priority`: An integer or float used to sort against all items.

        If an item is registered with a "name" which already exists, the
        existing item is replaced with the new item. Treat carefully as the
        old item is lost with no way to recover it. The new item will be
        sorted according to its priority and will **not** retain the position
        of the old item.
        '''
    def deregister(self, name, strict: bool = True) -> None:
        """
        Remove an item from the registry.

        Set `strict=False` to fail silently.
        """
