from ..util.typing import Literal as Literal
from .cache_key import CacheConst as CacheConst
from typing import Any, Dict, Tuple

class prefix_anon_map(Dict[str, str]):
    '''A map that creates new keys for missing key access.

    Considers keys of the form "<ident> <name>" to produce
    new symbols "<name>_<index>", where "index" is an incrementing integer
    corresponding to <name>.

    Inlines the approach taken by :class:`sqlalchemy.util.PopulateDict` which
    is otherwise usually used for this type of operation.

    '''
    def __missing__(self, key: str) -> str: ...

class cache_anon_map(Dict[int | 'Literal[CacheConst.NO_CACHE]', Literal[True] | str]):
    """A map that creates new keys for missing key access.

    Produces an incrementing sequence given a series of unique keys.

    This is similar to the compiler prefix_anon_map class although simpler.

    Inlines the approach taken by :class:`sqlalchemy.util.PopulateDict` which
    is otherwise usually used for this type of operation.

    """
    def get_anon(self, object_: Any) -> Tuple[str, bool]: ...
    def __missing__(self, key: int) -> str: ...
