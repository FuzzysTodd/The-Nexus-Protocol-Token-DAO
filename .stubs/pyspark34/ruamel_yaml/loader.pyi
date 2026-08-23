from ruamel_yaml.compat import StreamTextType, VersionType
from ruamel_yaml.composer import Composer
from ruamel_yaml.constructor import BaseConstructor, Constructor, RoundTripConstructor, SafeConstructor
from ruamel_yaml.parser import Parser, RoundTripParser
from ruamel_yaml.reader import Reader
from ruamel_yaml.resolver import VersionedResolver
from ruamel_yaml.scanner import RoundTripScanner, Scanner

__all__ = ['BaseLoader', 'SafeLoader', 'Loader', 'RoundTripLoader']

class BaseLoader(Reader, Scanner, Parser, Composer, BaseConstructor, VersionedResolver):
    def __init__(self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> None: ...

class SafeLoader(Reader, Scanner, Parser, Composer, SafeConstructor, VersionedResolver):
    def __init__(self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> None: ...

class Loader(Reader, Scanner, Parser, Composer, Constructor, VersionedResolver):
    def __init__(self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> None: ...

class RoundTripLoader(Reader, RoundTripScanner, RoundTripParser, Composer, RoundTripConstructor, VersionedResolver):
    def __init__(self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> None: ...
