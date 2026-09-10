from _typeshed import Incomplete
from collections.abc import Generator
from gitdb.db.base import FileDBBase, ObjectDBR, ObjectDBW
from gitdb.fun import chunk_size

__all__ = ['LooseObjectDB']

class LooseObjectDB(FileDBBase, ObjectDBR, ObjectDBW):
    """A database which operates on loose object files"""
    stream_chunk_size = chunk_size
    new_objects_mode: Incomplete
    def __init__(self, root_path) -> None: ...
    def object_path(self, hexsha):
        """
        :return: path at which the object with the given hexsha would be stored,
            relative to the database root"""
    def readable_db_object_path(self, hexsha):
        """
        :return: readable object path to the object identified by hexsha
        :raise BadObject: If the object file does not exist"""
    def partial_to_complete_sha_hex(self, partial_hexsha):
        """:return: 20 byte binary sha1 string which matches the given name uniquely
        :param name: hexadecimal partial name (bytes or ascii string)
        :raise AmbiguousObjectName:
        :raise BadObject: """
    def set_ostream(self, stream):
        """:raise TypeError: if the stream does not support the Sha1Writer interface"""
    def info(self, sha): ...
    def stream(self, sha): ...
    def has_object(self, sha): ...
    def store(self, istream):
        """note: The sha we produce will be hex by nature"""
    def sha_iter(self) -> Generator[Incomplete, None, None]: ...
    def size(self): ...
