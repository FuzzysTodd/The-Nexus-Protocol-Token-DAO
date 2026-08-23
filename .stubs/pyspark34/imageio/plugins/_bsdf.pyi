import struct
from _typeshed import Incomplete

logger: Incomplete
VERSION: Incomplete
__version__: Incomplete
PY3: Incomplete
text_type = str
string_types = str
unicode_types = str
integer_types = int
classtypes = type
spack = struct.pack
strunpack = struct.unpack

def lencode(x):
    """Encode an unsigned integer into a variable sized blob of bytes."""
def lendecode(f):
    """Decode an unsigned integer from a file."""
def encode_type_id(b, ext_id):
    """Encode the type identifier, with or without extension id."""

class BsdfSerializer:
    '''Instances of this class represent a BSDF encoder/decoder.

    It acts as a placeholder for a set of extensions and encoding/decoding
    options. Use this to predefine extensions and options for high
    performance encoding/decoding. For general use, see the functions
    `save()`, `encode()`, `load()`, and `decode()`.

    This implementation of BSDF supports streaming lists (keep adding
    to a list after writing the main file), lazy loading of blobs, and
    in-place editing of blobs (for streams opened with a+).

    Options for encoding:

    * compression (int or str): ``0`` or "no" for no compression (default),
      ``1`` or "zlib" for Zlib compression (same as zip files and PNG), and
      ``2`` or "bz2" for Bz2 compression (more compact but slower writing).
      Note that some BSDF implementations (e.g. JavaScript) may not support
      compression.
    * use_checksum (bool): whether to include a checksum with binary blobs.
    * float64 (bool): Whether to write floats as 64 bit (default) or 32 bit.

    Options for decoding:

    * load_streaming (bool): if True, and the final object in the structure was
      a stream, will make it available as a stream in the decoded object.
    * lazy_blob (bool): if True, bytes are represented as Blob objects that can
      be used to lazily access the data, and also overwrite the data if the
      file is open in a+ mode.
    '''
    def __init__(self, extensions: Incomplete | None = None, **options) -> None: ...
    def add_extension(self, extension_class):
        """Add an extension to this serializer instance, which must be
        a subclass of Extension. Can be used as a decorator.
        """
    def remove_extension(self, name) -> None:
        """Remove a converted by its unique name."""
    def encode(self, ob):
        """Save the given object to bytes."""
    def save(self, f, ob) -> None:
        """Write the given object to the given file object."""
    def decode(self, bb):
        """Load the data structure that is BSDF-encoded in the given bytes."""
    def load(self, f):
        """Load a BSDF-encoded object from the given file object."""

class BaseStream:
    """Base class for streams."""
    def __init__(self, mode: str = 'w') -> None: ...
    @property
    def mode(self):
        """The mode of this stream: 'r' or 'w'."""

class ListStream(BaseStream):
    """A streamable list object used for writing or reading.
    In read mode, it can also be iterated over.
    """
    @property
    def count(self):
        """The number of elements in the stream (can be -1 for unclosed
        streams in read-mode).
        """
    @property
    def index(self):
        """The current index of the element to read/write."""
    def append(self, item) -> None:
        """Append an item to the streaming list. The object is immediately
        serialized and written to the underlying file.
        """
    def close(self, unstream: bool = False) -> None:
        """Close the stream, marking the number of written elements. New
        elements may still be appended, but they won't be read during decoding.
        If ``unstream`` is False, the stream is turned into a regular list
        (not streaming).
        """
    def next(self):
        """Read and return the next element in the streaming list.
        Raises StopIteration if the stream is exhausted.
        """
    def __iter__(self): ...
    def __next__(self): ...

class Blob:
    """Object to represent a blob of bytes. When used to write a BSDF file,
    it's a wrapper for bytes plus properties such as what compression to apply.
    When used to read a BSDF file, it can be used to read the data lazily, and
    also modify the data if reading in 'r+' mode and the blob isn't compressed.
    """
    compressed: Incomplete
    compression: Incomplete
    allocated_size: Incomplete
    use_checksum: Incomplete
    def __init__(self, bb, compression: int = 0, extra_size: int = 0, use_checksum: bool = False) -> None: ...
    def seek(self, p) -> None:
        """Seek to the given position (relative to the blob start)."""
    def tell(self):
        """Get the current file pointer position (relative to the blob start)."""
    def write(self, bb):
        """Write bytes to the blob."""
    def read(self, n):
        """Read n bytes from the blob."""
    def get_bytes(self):
        """Get the contents of the blob as bytes."""
    def update_checksum(self) -> None:
        """Reset the blob's checksum if present. Call this after modifying
        the data.
        """

def encode(ob, extensions: Incomplete | None = None, **options):
    """Save (BSDF-encode) the given object to bytes.
    See `BSDFSerializer` for details on extensions and options.
    """
def save(f, ob, extensions: Incomplete | None = None, **options):
    """Save (BSDF-encode) the given object to the given filename or
    file object. See` BSDFSerializer` for details on extensions and options.
    """
def decode(bb, extensions: Incomplete | None = None, **options):
    """Load a (BSDF-encoded) structure from bytes.
    See `BSDFSerializer` for details on extensions and options.
    """
def load(f, extensions: Incomplete | None = None, **options):
    """Load a (BSDF-encoded) structure from the given filename or file object.
    See `BSDFSerializer` for details on extensions and options.
    """
loads = decode
dumps = encode

class Extension:
    """Base class to implement BSDF extensions for special data types.

    Extension classes are provided to the BSDF serializer, which
    instantiates the class. That way, the extension can be somewhat dynamic:
    e.g. the NDArrayExtension exposes the ndarray class only when numpy
    is imported.

    A extension instance must have two attributes. These can be attribiutes of
    the class, or of the instance set in ``__init__()``:

    * name (str): the name by which encoded values will be identified.
    * cls (type): the type (or list of types) to match values with.
      This is optional, but it makes the encoder select extensions faster.

    Further, it needs 3 methods:

    * `match(serializer, value) -> bool`: return whether the extension can
      convert the given value. The default is ``isinstance(value, self.cls)``.
    * `encode(serializer, value) -> encoded_value`: the function to encode a
      value to more basic data types.
    * `decode(serializer, encoded_value) -> value`: the function to decode an
      encoded value back to its intended representation.

    """
    name: str
    cls: Incomplete
    def match(self, s, v): ...
    def encode(self, s, v) -> None: ...
    def decode(self, s, v) -> None: ...

class ComplexExtension(Extension):
    name: str
    cls = complex
    def encode(self, s, v): ...
    def decode(self, s, v): ...

class NDArrayExtension(Extension):
    name: str
    cls: Incomplete
    def __init__(self) -> None: ...
    def match(self, s, v): ...
    def encode(self, s, v): ...
    def decode(self, s, v): ...

standard_extensions: Incomplete
