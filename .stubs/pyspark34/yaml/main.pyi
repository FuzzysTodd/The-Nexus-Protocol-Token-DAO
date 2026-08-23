from ruamel.yaml.tokens import *
from ruamel.yaml.events import *
from ruamel.yaml.nodes import *
from _typeshed import Incomplete
from pathlib import Path
from ruamel.yaml.compat import StreamTextType as StreamTextType, StreamType as StreamType, VersionType as VersionType, nprintf as nprintf
from ruamel.yaml.constructor import Constructor
from ruamel.yaml.error import YAMLError as YAMLError
from ruamel.yaml.representer import Representer
from ruamel.yaml.resolver import VersionedResolver as VersionedResolver
from types import TracebackType
from typing import Any, List, Text, Type

class YAML:
    typ: Incomplete
    pure: Incomplete
    plug_ins: Incomplete
    Resolver: Incomplete
    allow_unicode: bool
    Reader: Incomplete
    Representer: Incomplete
    Constructor: Incomplete
    Scanner: Incomplete
    Serializer: Incomplete
    default_flow_style: Incomplete
    comment_handling: Incomplete
    Emitter: Incomplete
    Parser: Incomplete
    Composer: Incomplete
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
    preserve_quotes: Incomplete
    allow_duplicate_keys: bool
    encoding: str
    explicit_start: Incomplete
    explicit_end: Incomplete
    tags: Incomplete
    default_style: Incomplete
    top_level_block_style_scalar_no_indent_error_1_1: bool
    scalar_after_indicator: Incomplete
    brace_single_entry_mapping_in_flow_sequence: bool
    def __init__(self, *, typ: List[Text] | Text | None = None, pure: Any = False, output: Any = None, plug_ins: Any = None) -> None:
        """
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
    def scan(self, stream: StreamTextType) -> Any:
        """
        Scan a YAML stream and produce scanning tokens.
        """
    def parse(self, stream: StreamTextType) -> Any:
        """
        Parse a YAML stream and produce parsing events.
        """
    def compose(self, stream: Path | StreamTextType) -> Any:
        """
        Parse the first YAML document in a stream
        and produce the corresponding representation tree.
        """
    def compose_all(self, stream: Path | StreamTextType) -> Any:
        """
        Parse all YAML documents in a stream
        and produce corresponding representation trees.
        """
    def load(self, stream: Path | StreamTextType) -> Any:
        """
        at this point you either have the non-pure Parser (which has its own reader and
        scanner) or you have the pure Parser.
        If the pure Parser is set, then set the Reader and Scanner, if not already set.
        If either the Scanner or Reader are set, you cannot use the non-pure Parser,
            so reset it to the pure parser and set the Reader resp. Scanner if necessary
        """
    def load_all(self, stream: Path | StreamTextType) -> Any: ...
    def get_constructor_parser(self, stream: StreamTextType) -> Any:
        """
        the old cyaml needs special setup, and therefore the stream
        """
    def emit(self, events: Any, stream: Any) -> None:
        """
        Emit YAML parsing events into a stream.
        If stream is None, return the produced string instead.
        """
    def serialize(self, node: Any, stream: StreamType | None) -> Any:
        """
        Serialize a representation tree into a YAML stream.
        If stream is None, return the produced string instead.
        """
    def serialize_all(self, nodes: Any, stream: StreamType | None) -> Any:
        """
        Serialize a sequence of representation trees into a YAML stream.
        If stream is None, return the produced string instead.
        """
    def dump(self, data: Path | StreamType, stream: Any = None, *, transform: Any = None) -> Any: ...
    def dump_all(self, documents: Any, stream: Path | StreamType, *, transform: Any = None) -> Any: ...
    def Xdump_all(self, documents: Any, stream: Any, *, transform: Any = None) -> Any:
        """
        Serialize a sequence of Python objects into a YAML stream.
        """
    def get_serializer_representer_emitter(self, stream: StreamType, tlca: Any) -> Any: ...
    def map(self, **kw: Any) -> Any: ...
    def seq(self, *args: Any) -> Any: ...
    def official_plug_ins(self) -> Any:
        """search for list of subdirs that are plug-ins, if __file__ is not available, e.g.
        single file installers that are not properly emulating a file-system (issue 324)
        no plug-ins will be found. If any are packaged, you know which file that are
        and you can explicitly provide it during instantiation:
            yaml = ruamel.yaml.YAML(plug_ins=['ruamel/yaml/jinja2/__plug_in__'])
        """
    def register_class(self, cls: Any) -> Any:
        """
        register a class for dumping/loading
        - if it has attribute yaml_tag use that to register, else use class name
        - if it has methods to_yaml/from_yaml use those to dump/load else dump attributes
          as mapping
        """
    def __enter__(self) -> Any: ...
    def __exit__(self, typ: Type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    @property
    def version(self) -> Any | None: ...
    @version.setter
    def version(self, val: VersionType | None) -> None: ...
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
    def __init__(self, yaml: Any, transform: Any = None) -> None: ...
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
def warn_deprecation(fun: Any, method: Any, arg: str = '') -> None: ...
def error_deprecation(fun: Any, method: Any, arg: str = '') -> None: ...
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
def load(stream: Any, Loader: Any = None, version: Any = None, preserve_quotes: Any = None) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    """
def load_all(stream: Any, Loader: Any = None, version: Any = None, preserve_quotes: Any = None) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    """
def safe_load(stream: StreamTextType, version: VersionType | None = None) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    Resolve only basic YAML tags.
    """
def safe_load_all(stream: StreamTextType, version: VersionType | None = None) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    Resolve only basic YAML tags.
    """
def round_trip_load(stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> Any:
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    Resolve only basic YAML tags.
    """
def round_trip_load_all(stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None) -> Any:
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    Resolve only basic YAML tags.
    """
def emit(events: Any, stream: StreamType | None = None, Dumper: Any = ..., canonical: bool | None = None, indent: int | None = None, width: int | None = None, allow_unicode: bool | None = None, line_break: Any = None) -> Any:
    """
    Emit YAML parsing events into a stream.
    If stream is None, return the produced string instead.
    """

enc: Incomplete

def serialize_all(nodes: Any, stream: StreamType | None = None, Dumper: Any = ..., canonical: Any = None, indent: int | None = None, width: int | None = None, allow_unicode: bool | None = None, line_break: Any = None, encoding: Any = ..., explicit_start: bool | None = None, explicit_end: bool | None = None, version: VersionType | None = None, tags: Any = None) -> Any:
    """
    Serialize a sequence of representation trees into a YAML stream.
    If stream is None, return the produced string instead.
    """
def serialize(node: Any, stream: StreamType | None = None, Dumper: Any = ..., **kwds: Any) -> Any:
    """
    Serialize a representation tree into a YAML stream.
    If stream is None, return the produced string instead.
    """
def dump_all(documents: Any, stream: StreamType | None = None, Dumper: Any = ..., default_style: Any = None, default_flow_style: Any = None, canonical: bool | None = None, indent: int | None = None, width: int | None = None, allow_unicode: bool | None = None, line_break: Any = None, encoding: Any = ..., explicit_start: bool | None = None, explicit_end: bool | None = None, version: Any = None, tags: Any = None, block_seq_indent: Any = None, top_level_colon_align: Any = None, prefix_colon: Any = None) -> Any:
    """
    Serialize a sequence of Python objects into a YAML stream.
    If stream is None, return the produced string instead.
    """
def dump(data: Any, stream: StreamType | None = None, Dumper: Any = ..., default_style: Any = None, default_flow_style: Any = None, canonical: bool | None = None, indent: int | None = None, width: int | None = None, allow_unicode: bool | None = None, line_break: Any = None, encoding: Any = ..., explicit_start: bool | None = None, explicit_end: bool | None = None, version: VersionType | None = None, tags: Any = None, block_seq_indent: Any = None) -> Any:
    '''
    Serialize a Python object into a YAML stream.
    If stream is None, return the produced string instead.

    default_style ∈ None, \'\', \'"\', "\'", \'|\', \'>\'

    '''
def safe_dump(data: Any, stream: StreamType | None = None, **kwds: Any) -> Any:
    """
    Serialize a Python object into a YAML stream.
    Produce only basic YAML tags.
    If stream is None, return the produced string instead.
    """
def round_trip_dump(data: Any, stream: StreamType | None = None, Dumper: Any = ..., default_style: Any = None, default_flow_style: Any = None, canonical: bool | None = None, indent: int | None = None, width: int | None = None, allow_unicode: bool | None = None, line_break: Any = None, encoding: Any = ..., explicit_start: bool | None = None, explicit_end: bool | None = None, version: VersionType | None = None, tags: Any = None, block_seq_indent: Any = None, top_level_colon_align: Any = None, prefix_colon: Any = None) -> Any: ...
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
