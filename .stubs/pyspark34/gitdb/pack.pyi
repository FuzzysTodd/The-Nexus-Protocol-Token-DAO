from _typeshed import Incomplete
from gitdb.util import LazyMixin

__all__ = ['PackIndexFile', 'PackFile', 'PackEntity']

class IndexWriter:
    """Utility to cache index information, allowing to write all information later
    in one go to the given stream
    **Note:** currently only writes v2 indices"""
    def __init__(self) -> None: ...
    def append(self, binsha, crc, offset) -> None:
        """Append one piece of object information"""
    def write(self, pack_sha, write):
        """Write the index file using the given write method
        :param pack_sha: binary sha over the whole pack that we index
        :return: sha1 binary sha over all index file contents"""

class PackIndexFile(LazyMixin):
    """A pack index provides offsets into the corresponding pack, allowing to find
    locations for offsets faster."""
    index_v2_signature: bytes
    index_version_default: int
    def __init__(self, indexpath) -> None: ...
    def close(self) -> None: ...
    def version(self): ...
    def size(self):
        """:return: amount of objects referred to by this index"""
    def path(self):
        """:return: path to the packindexfile"""
    def packfile_checksum(self):
        """:return: 20 byte sha representing the sha1 hash of the pack file"""
    def indexfile_checksum(self):
        """:return: 20 byte sha representing the sha1 hash of this index file"""
    def offsets(self):
        """:return: sequence of all offsets in the order in which they were written

        **Note:** return value can be random accessed, but may be immmutable"""
    def sha_to_index(self, sha):
        """
        :return: index usable with the ``offset`` or ``entry`` method, or None
            if the sha was not found in this pack index
        :param sha: 20 byte sha to lookup"""
    def partial_sha_to_index(self, partial_bin_sha, canonical_length):
        """
        :return: index as in `sha_to_index` or None if the sha was not found in this
            index file
        :param partial_bin_sha: an at least two bytes of a partial binary sha as bytes
        :param canonical_length: length of the original hexadecimal representation of the
            given partial binary sha
        :raise AmbiguousObjectName:"""
    def sha_to_index(self, sha): ...

class PackFile(LazyMixin):
    """A pack is a file written according to the Version 2 for git packs

    As we currently use memory maps, it could be assumed that the maximum size of
    packs therefore is 32 bit on 32 bit systems. On 64 bit systems, this should be
    fine though.

    **Note:** at some point, this might be implemented using streams as well, or
    streams are an alternate path in the case memory maps cannot be created
    for some reason - one clearly doesn't want to read 10GB at once in that
    case"""
    pack_signature: int
    pack_version_default: int
    first_object_offset: Incomplete
    footer_size: int
    def __init__(self, packpath) -> None: ...
    def close(self) -> None: ...
    def size(self):
        """:return: The amount of objects stored in this pack"""
    def version(self):
        """:return: the version of this pack"""
    def data(self):
        """
        :return: read-only data of this pack. It provides random access and usually
            is a memory map.
        :note: This method is unsafe as it returns a window into a file which might be larger than than the actual window size"""
    def checksum(self):
        """:return: 20 byte sha1 hash on all object sha's contained in this file"""
    def path(self):
        """:return: path to the packfile"""
    def collect_streams(self, offset):
        """
        :return: list of pack streams which are required to build the object
            at the given offset. The first entry of the list is the object at offset,
            the last one is either a full object, or a REF_Delta stream. The latter
            type needs its reference object to be locked up in an ODB to form a valid
            delta chain.
            If the object at offset is no delta, the size of the list is 1.
        :param offset: specifies the first byte of the object within this pack"""
    def info(self, offset):
        """Retrieve information about the object at the given file-absolute offset

        :param offset: byte offset
        :return: OPackInfo instance, the actual type differs depending on the type_id attribute"""
    def stream(self, offset):
        """Retrieve an object at the given file-relative offset as stream along with its information

        :param offset: byte offset
        :return: OPackStream instance, the actual type differs depending on the type_id attribute"""
    def stream_iter(self, start_offset: int = 0):
        """
        :return: iterator yielding OPackStream compatible instances, allowing
            to access the data in the pack directly.
        :param start_offset: offset to the first object to iterate. If 0, iteration
            starts at the very first object in the pack.

        **Note:** Iterating a pack directly is costly as the datastream has to be decompressed
        to determine the bounds between the objects"""

class PackEntity(LazyMixin):
    """Combines the PackIndexFile and the PackFile into one, allowing the
    actual objects to be resolved and iterated"""
    IndexFileCls = PackIndexFile
    PackFileCls = PackFile
    def __init__(self, pack_or_index_path) -> None:
        """Initialize ourselves with the path to the respective pack or index file"""
    def close(self) -> None: ...
    def info(self, sha):
        """Retrieve information about the object identified by the given sha

        :param sha: 20 byte sha1
        :raise BadObject:
        :return: OInfo instance, with 20 byte sha"""
    def stream(self, sha):
        """Retrieve an object stream along with its information as identified by the given sha

        :param sha: 20 byte sha1
        :raise BadObject:
        :return: OStream instance, with 20 byte sha"""
    def info_at_index(self, index):
        """As ``info``, but uses a PackIndexFile compatible index to refer to the object"""
    def stream_at_index(self, index):
        """As ``stream``, but uses a PackIndexFile compatible index to refer to the
        object"""
    def pack(self):
        """:return: the underlying pack file instance"""
    def index(self):
        """:return: the underlying pack index file instance"""
    def is_valid_stream(self, sha, use_crc: bool = False):
        """
        Verify that the stream at the given sha is valid.

        :param use_crc: if True, the index' crc is run over the compressed stream of
            the object, which is much faster than checking the sha1. It is also
            more prone to unnoticed corruption or manipulation.
        :param sha: 20 byte sha1 of the object whose stream to verify
            whether the compressed stream of the object is valid. If it is
            a delta, this only verifies that the delta's data is valid, not the
            data of the actual undeltified object, as it depends on more than
            just this stream.
            If False, the object will be decompressed and the sha generated. It must
            match the given sha

        :return: True if the stream is valid
        :raise UnsupportedOperation: If the index is version 1 only
        :raise BadObject: sha was not found"""
    def info_iter(self):
        """
        :return: Iterator over all objects in this pack. The iterator yields
            OInfo instances"""
    def stream_iter(self):
        """
        :return: iterator over all objects in this pack. The iterator yields
            OStream instances"""
    def collect_streams_at_offset(self, offset):
        """
        As the version in the PackFile, but can resolve REF deltas within this pack
        For more info, see ``collect_streams``

        :param offset: offset into the pack file at which the object can be found"""
    def collect_streams(self, sha):
        """
        As ``PackFile.collect_streams``, but takes a sha instead of an offset.
        Additionally, ref_delta streams will be resolved within this pack.
        If this is not possible, the stream will be left alone, hence it is adivsed
        to check for unresolved ref-deltas and resolve them before attempting to
        construct a delta stream.

        :param sha: 20 byte sha1 specifying the object whose related streams you want to collect
        :return: list of streams, first being the actual object delta, the last being
            a possibly unresolved base object.
        :raise BadObject:"""
    @classmethod
    def write_pack(cls, object_iter, pack_write, index_write: Incomplete | None = None, object_count: Incomplete | None = None, zlib_compression=...):
        """
        Create a new pack by putting all objects obtained by the object_iterator
        into a pack which is written using the pack_write method.
        The respective index is produced as well if index_write is not Non.

        :param object_iter: iterator yielding odb output objects
        :param pack_write: function to receive strings to write into the pack stream
        :param indx_write: if not None, the function writes the index file corresponding
            to the pack.
        :param object_count: if you can provide the amount of objects in your iteration,
            this would be the place to put it. Otherwise we have to pre-iterate and store
            all items into a list to get the number, which uses more memory than necessary.
        :param zlib_compression: the zlib compression level to use
        :return: tuple(pack_sha, index_binsha) binary sha over all the contents of the pack
            and over all contents of the index. If index_write was None, index_binsha will be None

        **Note:** The destination of the write functions is up to the user. It could
        be a socket, or a file for instance

        **Note:** writes only undeltified objects"""
    @classmethod
    def create(cls, object_iter, base_dir, object_count: Incomplete | None = None, zlib_compression=...):
        """Create a new on-disk entity comprised of a properly named pack file and a properly named
        and corresponding index file. The pack contains all OStream objects contained in object iter.
        :param base_dir: directory which is to contain the files
        :return: PackEntity instance initialized with the new pack

        **Note:** for more information on the other parameters see the write_pack method"""
