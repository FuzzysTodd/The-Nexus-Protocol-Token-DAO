from ruamel_yaml.tokens import *
from ruamel_yaml.events import *
from ruamel_yaml.nodes import *
from _ruamel_yaml import CEmitter as CEmitter, CParser as CParser
from _typeshed import Incomplete
from pathlib import Path
from ruamel_yaml.compat import BytesIO as BytesIO, PY3 as PY3, StreamTextType as StreamTextType, StreamType as StreamType, StringIO as StringIO, VersionType as VersionType, nprint as nprint, with_metaclass as with_metaclass
from ruamel_yaml.constructor import BaseConstructor as BaseConstructor, Constructor as Constructor, RoundTripConstructor as RoundTripConstructor, SafeConstructor as SafeConstructor
from ruamel_yaml.dumper import BaseDumper as BaseDumper, Dumper as Dumper, RoundTripDumper as RoundTripDumper, SafeDumper as SafeDumper
from ruamel_yaml.error import UnsafeLoaderWarning as UnsafeLoaderWarning, YAMLError as YAMLError
from ruamel_yaml.loader import BaseLoader as BaseLoader, Loader as Loader, RoundTripLoader as RoundTripLoader, SafeLoader as SafeLoader
from ruamel_yaml.representer import BaseRepresenter as BaseRepresenter, Representer as Representer, RoundTripRepresenter as RoundTripRepresenter, SafeRepresenter as SafeRepresenter
from ruamel_yaml.resolver import Resolver as Resolver, VersionedResolver as VersionedResolver
from typing import Any, Callable

enforce: Incomplete

class YAML:
    typ: Incomplete
    pure: Incomplete
    plug_ins: Incomplete
    Resolver: Incomplete
    allow_unicode: bool
    Reader: Incomplete
    Scanner: Incomplete
    Serializer: Incomplete
    default_flow_style: Incomplete
    Emitter: Incomplete
    Representer: Incomplete
    Parser: Incomplete
    Composer: Incomplete
    Constructor: Incomplete
    stream: Incomplete
    canonical: Incomplete
    old_indent: Incomplete
    width: Incomplete
    line_break: Incomplete
    map_indent: Incomplete
    sequence_indent: Incomplete
    sequence_dash_offset: int
    compact_seq_seq: Incomplete
    compact_seq_map: Incomplete
    sort_base_mapping_type_on_output: Incomplete
    top_level_colon_align: Incomplete
    prefix_colon: Incomplete
    version: Incomplete
    preserve_quotes: Incomplete
    allow_duplicate_keys: bool
    encoding: str
    explicit_start: Incomplete
    explicit_end: Incomplete
    tags: Incomplete
    default_style: Incomplete
    top_level_block_style_scalar_no_indent_error_1_1: bool
    brace_single_entry_mapping_in_flow_sequence: bool
    def __init__(self, _kw: Any = ..., typ: Optional[Text] = None, pure: Any = False, output: Any = None, plug_ins: Any = None) -> None:
        """
        _kw: not used, forces keyword arguments in 2.7 (in 3 you can do (*, safe_load=..)
        typ: 'rt'/None -> RoundTripLoader/RoundTripDumper,  (default)
             'safe'    -> SafeLoader/SafeDumper,
             'unsafe'  -> normal/unsafe Loader/Dumper
             'base'    -> baseloader
        pure: if True only use Python modules
        input/output: needed to work as context manager
        plug_ins: a list of plug-in files
        """
    @property
    def reader(self) -> Any: ...
    @property
    def scanner(self) -> Any: ...
    @property
    def parser(self) -> Any: ...
    @property
    def composer(self) -> Any: ...
    @property
    def constructor(self) -> Any: ...
    @property
    def resolver(self) -> Any: ...
    @property
    def emitter(self) -> Any: ...
    @property
    def serializer(self) -> Any: ...
    @property
    def representer(self) -> Any: ...
    def load(self, stream: Path | StreamTextType) -> Any:
        """
        at this point you either have the non-pure Parser (which has its own reader and
        scanner) or you have the pure Parser.
        If the pure Parser is set, then set the Reader and Scanner, if not already set.
        If either the Scanner or Reader are set, you cannot use the non-pure Parser,
            so reset it to the pure parser and set the Reader resp. Scanner if necessary
        """
    def load_all(self, stream: Path | StreamTextType, _kw: Any = ...) -> Any: ...
    def get_constructor_parser(self, stream: StreamTextType) -> Any:
        """
        the old cyaml needs special setup, and therefore the stream
        """
    def dump(self, data: Any, stream: Path | StreamType = None, _kw: Any = ..., transform: Any = None) -> Any: ...
    def dump_all(self, documents: Any, stream: Path | StreamType, _kw: Any = ..., transform: Any = None) -> Any: ...
    def Xdump_all(self, documents: Any, stream: Path | StreamType, _kw: Any = ..., transform: Any = None) -> Any:
        """
        Serialize a sequence of Python objects into a YAML stream.
        """
    def get_serializer_representer_emitter(self, stream: StreamType, tlca: Any) -> Any: ...
    def map(self, **kw: Any) -> Any: ...
    def seq(self, *args: Any) -> Any: ...
    def official_plug_ins(self) -> Any: ...
    def register_class(self, cls: Any) -> Any:
        """
        register a class for dumping loading
        - if it has attribute yaml_tag use that to register, else use class name
        - if it has methods to_yaml/from_yaml use those to dump/load else dump attributes
          as mapping
        """
    def parse(self, stream: StreamTextType) -> Any:
        """
        Parse a YAML stream and produce parsing events.
        """
    def __enter__(self) -> Any: ...
    def __exit__(self, typ: Any, value: Any, traceback: Any) -> None: ...
    @property
    def indent(self) -> Any: ...
    @indent.setter
    def indent(self, val: Any) -> None: ...
    @property
    def block_seq_indent(self) -> Any: ...
    @block_seq_indent.setter
    def block_seq_indent(self, val: Any) -> None: ...
    def compact(self, seq_seq: Any = None, seq_map: Any = None) -> None: ...

class YAMLContextManager:
    def __init__(self, yaml: Any, transform: Optional[Callable] = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data: Any) -> None: ...
    def dump(self, data: Any) -> None: ...

def yaml_object(yml: Any) -> Any:
    """ decorator for classes that needs to dump/load objects
    The tag for such objects is taken from the class attribute yaml_tag (or the
    class name in lowercase in case unavailable)
    If methods to_yaml and/or from_yaml are available, these are called for dumping resp.
    loading, default routines (dumping a mapping of the attributes) used otherwise.
    """
def scan(stream: StreamTextType, Loader: Any = ...) -> Any:
    """
    Scan a YAML stream and produce scanning tokens.
    """
def parse(stream: StreamTextType, Loader: Any = ...) -> Any:
    """
    Parse a YAML stream and produce parsing events.
    """
def compose(stream: StreamTextType, Loader: Any = ...) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding representation tree.
    """
def compose_all(stream: StreamTextType, Loader: Any = ...) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding representation trees.
    """
def load(stream: StreamTextType, Loader: Any = None, version: Optional[VersionType] = None, preserve_quotes: Any = None) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    """
def load_all(stream: Optional[StreamTextType], Loader: Any = None, version: Optional[VersionType] = None, preserve_quotes: Optional[bool] = None) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    """
def safe_load(stream: StreamTextType, version: Optional[VersionType] = None) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    Resolve only basic YAML tags.
    """
def safe_load_all(stream: StreamTextType, version: Optional[VersionType] = None) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    Resolve only basic YAML tags.
    """
def round_trip_load(stream: StreamTextType, version: Optional[VersionType] = None, preserve_quotes: Optional[bool] = None) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    Resolve only basic YAML tags.
    """
def round_trip_load_all(stream: StreamTextType, version: Optional[VersionType] = None, preserve_quotes: Optional[bool] = None) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    Resolve only basic YAML tags.
    """
def emit(events: Any, stream: Optional[StreamType] = None, Dumper: Any = ..., canonical: Optional[bool] = None, indent: int | None = None, width: Optional[int] = None, allow_unicode: Optional[bool] = None, line_break: Any = None) -> Any:
    """
    Emit YAML parsing events into a stream.
    If stream is None, return the produced string instead.
    """

enc: Incomplete

def serialize_all(nodes: Any, stream: Optional[StreamType] = None, Dumper: Any = ..., canonical: Any = None, indent: Optional[int] = None, width: Optional[int] = None, allow_unicode: Optional[bool] = None, line_break: Any = None, encoding: Any = ..., explicit_start: Optional[bool] = None, explicit_end: Optional[bool] = None, version: Optional[VersionType] = None, tags: Any = None) -> Any:
    """
    Serialize a sequence of representation trees into a YAML stream.
    If stream is None, return the produced string instead.
    """
def serialize(node: Any, stream: Optional[StreamType] = None, Dumper: Any = ..., **kwds: Any) -> Any:
    """
    Serialize a representation tree into a YAML stream.
    If stream is None, return the produced string instead.
    """
def dump_all(documents: Any, stream: Optional[StreamType] = None, Dumper: Any = ..., default_style: Any = None, default_flow_style: Any = None, canonical: Optional[bool] = None, indent: Optional[int] = None, width: Optional[int] = None, allow_unicode: Optional[bool] = None, line_break: Any = None, encoding: Any = ..., explicit_start: Optional[bool] = None, explicit_end: Optional[bool] = None, version: Any = None, tags: Any = None, block_seq_indent: Any = None, top_level_colon_align: Any = None, prefix_colon: Any = None) -> Optional[str]:
    """
    Serialize a sequence of Python objects into a YAML stream.
    If stream is None, return the produced string instead.
    """
def dump(data: Any, stream: Optional[StreamType] = None, Dumper: Any = ..., default_style: Any = None, default_flow_style: Any = None, canonical: Optional[bool] = None, indent: Optional[int] = None, width: Optional[int] = None, allow_unicode: Optional[bool] = None, line_break: Any = None, encoding: Any = ..., explicit_start: Optional[bool] = None, explicit_end: Optional[bool] = None, version: Optional[VersionType] = None, tags: Any = None, block_seq_indent: Any = None) -> Optional[str]:
    '''
    Serialize a Python object into a YAML stream.
    If stream is None, return the produced string instead.

    default_style ∈ None, \'\', \'"\', "\'", \'|\', \'>\'

    '''
def safe_dump_all(documents: Any, stream: Optional[StreamType] = None, **kwds: Any) -> Optional[str]:
    """
    Serialize a sequence of Python objects into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    """
def safe_dump(data: Any, stream: Optional[StreamType] = None, **kwds: Any) -> Optional[str]:
    """
    Serialize a Python object into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    """
def round_trip_dump(data: Any, stream: Optional[StreamType] = None, Dumper: Any = ..., default_style: Any = None, default_flow_style: Any = None, canonical: Optional[bool] = None, indent: Optional[int] = None, width: Optional[int] = None, allow_unicode: Optional[bool] = None, line_break: Any = None, encoding: Any = ..., explicit_start: Optional[bool] = None, explicit_end: Optional[bool] = None, version: Optional[VersionType] = None, tags: Any = None, block_seq_indent: Any = None, top_level_colon_align: Any = None, prefix_colon: Any = None) -> Optional[str]: ...
def add_implicit_resolver(tag: Any, regexp: Any, first: Any = None, Loader: Any = None, Dumper: Any = None, resolver: Any = ...) -> None:
    """
    Add an implicit scalar detector.
    If an implicit scalar value matches the given regexp,
    the corresponding tag is assigned to the scalar.
    first is a sequence of possible initial characters or None.
    """
def add_path_resolver(tag: Any, path: Any, kind: Any = None, Loader: Any = None, Dumper: Any = None, resolver: Any = ...) -> None:
    """
    Add a path based resolver for the given tag.
    A path is a list of keys that forms a path
    to a node in the representation tree.
    Keys can be string values, integers, or None.
    """
def add_constructor(tag: Any, object_constructor: Any, Loader: Any = None, constructor: Any = ...) -> None:
    """
    Add an object constructor for the given tag.
    object_onstructor is a function that accepts a Loader instance
    and a node object and produces the corresponding Python object.
    """
def add_multi_constructor(tag_prefix: Any, multi_constructor: Any, Loader: Any = None, constructor: Any = ...) -> None:
    """
    Add a multi-constructor for the given tag prefix.
    Multi-constructor is called for a node if its tag starts with tag_prefix.
    Multi-constructor accepts a Loader instance, a tag suffix,
    and a node object and produces the corresponding Python object.
    """
def add_representer(data_type: Any, object_representer: Any, Dumper: Any = None, representer: Any = ...) -> None:
    """
    Add a representer for the given type.
    object_representer is a function accepting a Dumper instance
    and an instance of the given data type
    and producing the corresponding representation node.
    """
def add_multi_representer(data_type: Any, multi_representer: Any, Dumper: Any = None, representer: Any = ...) -> None:
    """
    Add a representer for the given type.
    multi_representer is a function accepting a Dumper instance
    and an instance of the given data type or subtype
    and producing the corresponding representation node.
    """

class YAMLObjectMetaclass(type):
    """
    The metaclass for YAMLObject.
    """
    def __init__(cls, name: Any, bases: Any, kwds: Any) -> None: ...

class YAMLObject(Incomplete):
    """
    An object that can dump itself to a YAML stream
    and load itself from a YAML stream.
    """
    yaml_constructor = Constructor
    yaml_representer = Representer
    yaml_tag: Any
    yaml_flow_style: Any
    @classmethod
    def from_yaml(cls, constructor: Any, node: Any) -> Any:
        """
        Convert a representation node to a Python object.
        """
    @classmethod
    def to_yaml(cls, representer: Any, data: Any) -> Any:
        """
        Convert a Python object to a representation node.
        """
