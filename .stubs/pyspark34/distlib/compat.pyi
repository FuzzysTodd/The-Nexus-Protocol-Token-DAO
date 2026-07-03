import os
from _typeshed import Incomplete
from cgi import escape as escape
from collections import MutableMapping
from collections.abc import Generator
from html import unescape as unescape
from html.parser import HTMLParser as HTMLParser
from importlib.util import cache_from_source as cache_from_source
from io import StringIO as StringIO
from itertools import filterfalse as filterfalse
from logging.config import BaseConfigurator as BaseConfigurator
from platform import python_implementation as python_implementation
from shutil import which as which
from ssl import match_hostname as match_hostname
from tokenize import detect_encoding as detect_encoding
from urllib.error import ContentTooShortError as ContentTooShortError, HTTPError as HTTPError, URLError as URLError
from urllib.parse import quote as quote, splittype as splittype, unquote as unquote, urljoin as urljoin, urlparse as urlparse, urlsplit as urlsplit, urlunparse as urlunparse, urlunsplit as urlunsplit
from urllib.request import HTTPBasicAuthHandler as HTTPBasicAuthHandler, HTTPHandler as HTTPHandler, HTTPPasswordMgr as HTTPPasswordMgr, HTTPRedirectHandler as HTTPRedirectHandler, HTTPSHandler as HTTPSHandler, Request as Request, build_opener as build_opener, pathname2url as pathname2url, url2pathname as url2pathname, urlopen as urlopen, urlretrieve as urlretrieve
from zipfile import ZipExtFile as BaseZipExtFile, ZipFile as BaseZipFile

string_types: Incomplete
text_type = str
raw_input = input
filter = filter

class CertificateError(ValueError): ...

class Container:
    """
        A generic container for when multiple values need to be returned
        """
    def __init__(self, **kwargs) -> None: ...
ZipFile = BaseZipFile

class ZipExtFile(BaseZipExtFile):
    def __init__(self, base) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...

class ZipFile(BaseZipFile):
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...
    def open(self, *args, **kwargs): ...
callable = callable
fsencode = os.fsencode
fsdecode = os.fsdecode
cookie_re: Incomplete

class ChainMap(MutableMapping):
    """ A ChainMap groups multiple dicts (or other mappings) together
        to create a single, updateable view.

        The underlying mappings are stored in a list.  That list is public and can
        accessed or updated using the *maps* attribute.  There is no other state.

        Lookups search the underlying mappings successively until a key is found.
        In contrast, writes, updates, and deletions only operate on the first
        mapping.

        """
    maps: Incomplete
    def __init__(self, *maps) -> None:
        """Initialize a ChainMap by setting *maps* to the given mappings.
            If no mappings are provided, a single empty dictionary is used.

            """
    def __missing__(self, key) -> None: ...
    def __getitem__(self, key): ...
    def get(self, key, default: Incomplete | None = None): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __contains__(self, key) -> bool: ...
    def __bool__(self) -> bool: ...
    @classmethod
    def fromkeys(cls, iterable, *args):
        """Create a ChainMap with a single dict created from the iterable."""
    def copy(self):
        """New ChainMap or subclass with a new copy of maps[0] and refs to maps[1:]"""
    __copy__ = copy
    def new_child(self):
        """New ChainMap with a new dict followed by all previous maps."""
    @property
    def parents(self):
        """New ChainMap from maps[1:]."""
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def popitem(self):
        """Remove and return an item pair from maps[0]. Raise KeyError is maps[0] is empty."""
    def pop(self, key, *args):
        """Remove *key* from maps[0] and return its value. Raise KeyError if *key* not in maps[0]."""
    def clear(self) -> None:
        """Clear maps[0], leaving maps[1:] intact."""

class OrderedDict(dict):
    """Dictionary that remembers insertion order"""
    def __init__(self, *args, **kwds) -> None:
        """Initialize an ordered dictionary.  Signature is the same as for
            regular dictionaries, but keyword arguments are not recommended
            because their insertion order is arbitrary.

            """
    def __setitem__(self, key, value, dict_setitem=...) -> None:
        """od.__setitem__(i, y) <==> od[i]=y"""
    def __delitem__(self, key, dict_delitem=...) -> None:
        """od.__delitem__(y) <==> del od[y]"""
    def __iter__(self):
        """od.__iter__() <==> iter(od)"""
    def __reversed__(self) -> Generator[Incomplete, None, None]:
        """od.__reversed__() <==> reversed(od)"""
    def clear(self) -> None:
        """od.clear() -> None.  Remove all items from od."""
    def popitem(self, last: bool = True):
        """od.popitem() -> (k, v), return and remove a (key, value) pair.
            Pairs are returned in LIFO order if last is true or FIFO order if false.

            """
    def keys(self):
        """od.keys() -> list of keys in od"""
    def values(self):
        """od.values() -> list of values in od"""
    def items(self):
        """od.items() -> list of (key, value) pairs in od"""
    def iterkeys(self):
        """od.iterkeys() -> an iterator over the keys in od"""
    def itervalues(self) -> Generator[Incomplete, None, None]:
        """od.itervalues -> an iterator over the values in od"""
    def iteritems(self) -> Generator[Incomplete, None, None]:
        """od.iteritems -> an iterator over the (key, value) items in od"""
    def update(*args, **kwds) -> None:
        """od.update(E, **F) -> None.  Update od from dict/iterable E and F.

            If E is a dict instance, does:           for k in E: od[k] = E[k]
            If E has a .keys() method, does:         for k in E.keys(): od[k] = E[k]
            Or if E is an iterable of items, does:   for k, v in E: od[k] = v
            In either case, this is followed by:     for k, v in F.items(): od[k] = v

            """
    def pop(self, key, default=...):
        """od.pop(k[,d]) -> v, remove specified key and return the corresponding value.
            If key is not found, d is returned if given, otherwise KeyError is raised.

            """
    def setdefault(self, key, default: Incomplete | None = None):
        """od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od"""
    def __reduce__(self):
        """Return state information for pickling"""
    def copy(self):
        """od.copy() -> a shallow copy of od"""
    @classmethod
    def fromkeys(cls, iterable, value: Incomplete | None = None):
        """OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S
            and values equal to v (which defaults to None).

            """
    def __eq__(self, other):
        """od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
            while comparison to a regular mapping is order-insensitive.

            """
    def __ne__(self, other): ...
    def viewkeys(self):
        """od.viewkeys() -> a set-like object providing a view on od's keys"""
    def viewvalues(self):
        """od.viewvalues() -> an object providing a view on od's values"""
    def viewitems(self):
        """od.viewitems() -> a set-like object providing a view on od's items"""

IDENTIFIER: Incomplete

class ConvertingDict(dict):
    """A converting dictionary wrapper."""
    def __getitem__(self, key): ...
    def get(self, key, default: Incomplete | None = None): ...

def pop(self, key, default: Incomplete | None = None): ...

class ConvertingList(list):
    """A converting list wrapper."""
    def __getitem__(self, key): ...
    def pop(self, idx: int = -1): ...

class ConvertingTuple(tuple):
    """A converting tuple wrapper."""
    def __getitem__(self, key): ...

class BaseConfigurator:
    """
        The configurator base class which defines some useful defaults.
        """
    CONVERT_PATTERN: Incomplete
    WORD_PATTERN: Incomplete
    DOT_PATTERN: Incomplete
    INDEX_PATTERN: Incomplete
    DIGIT_PATTERN: Incomplete
    value_converters: Incomplete
    importer: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def resolve(self, s):
        """
            Resolve strings to objects using standard import and attribute
            syntax.
            """
    def ext_convert(self, value):
        """Default converter for the ext:// protocol."""
    def cfg_convert(self, value):
        """Default converter for the cfg:// protocol."""
    def convert(self, value):
        """
            Convert values to an appropriate type. dicts, lists and tuples are
            replaced by their converting alternatives. Strings are checked to
            see if they have a conversion format and are converted if they do.
            """
    def configure_custom(self, config):
        """Configure an object with a user-supplied factory."""
    def as_tuple(self, value):
        """Utility function which converts lists to tuples."""
