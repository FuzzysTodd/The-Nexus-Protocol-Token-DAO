import dataclasses as dc
from collections.abc import Callable as Callable, MutableMapping
from markdown_it._compat import DATACLASS_KWARGS as DATACLASS_KWARGS
from typing import Any, Literal

def convert_attrs(value: Any) -> Any:
    """Convert Token.attrs set as ``None`` or ``[[key, value], ...]`` to a dict.

    This improves compatibility with upstream markdown-it.
    """

@dc.dataclass(**DATACLASS_KWARGS)
class Token:
    type: str
    tag: str
    nesting: Literal[-1, 0, 1]
    attrs: dict[str, str | int | float] = ...
    map: list[int] | None = ...
    level: int = ...
    children: list[Token] | None = ...
    content: str = ...
    markup: str = ...
    info: str = ...
    meta: dict[Any, Any] = ...
    block: bool = ...
    hidden: bool = ...
    def __post_init__(self) -> None: ...
    def attrIndex(self, name: str) -> int: ...
    def attrItems(self) -> list[tuple[str, str | int | float]]:
        """Get (key, value) list of attrs."""
    def attrPush(self, attrData: tuple[str, str | int | float]) -> None:
        """Add `[ name, value ]` attribute to list. Init attrs if necessary."""
    def attrSet(self, name: str, value: str | int | float) -> None:
        """Set `name` attribute to `value`. Override old value if exists."""
    def attrGet(self, name: str) -> None | str | int | float:
        """Get the value of attribute `name`, or null if it does not exist."""
    def attrJoin(self, name: str, value: str) -> None:
        """Join value to existing attribute via space.
        Or create new attribute if not exists.
        Useful to operate with token classes.
        """
    def copy(self, **changes: Any) -> Token:
        """Return a shallow copy of the instance."""
    def as_dict(self, *, children: bool = True, as_upstream: bool = True, meta_serializer: Callable[[dict[Any, Any]], Any] | None = None, filter: Callable[[str, Any], bool] | None = None, dict_factory: Callable[..., MutableMapping[str, Any]] = ...) -> MutableMapping[str, Any]:
        """Return the token as a dictionary.

        :param children: Also convert children to dicts
        :param as_upstream: Ensure the output dictionary is equal to that created by markdown-it
            For example, attrs are converted to null or lists
        :param meta_serializer: hook for serializing ``Token.meta``
        :param filter: A callable whose return code determines whether an
            attribute or element is included (``True``) or dropped (``False``).
            Is called with the (key, value) pair.
        :param dict_factory: A callable to produce dictionaries from.
            For example, to produce ordered dictionaries instead of normal Python
            dictionaries, pass in ``collections.OrderedDict``.

        """
    @classmethod
    def from_dict(cls, dct: MutableMapping[str, Any]) -> Token:
        """Convert a dict to a Token."""
    def __init__(self, type, tag, nesting, attrs, map, level, children, content, markup, info, meta, block, hidden) -> None: ...
