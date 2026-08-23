from gitdb.util import to_hex_sha as to_hex_sha

__all__ = ['AmbiguousObjectName', 'BadName', 'BadObject', 'BadObjectType', 'InvalidDBRoot', 'ODBError', 'ParseError', 'UnsupportedOperation', 'to_hex_sha']

class ODBError(Exception):
    """All errors thrown by the object database"""
class InvalidDBRoot(ODBError):
    """Thrown if an object database cannot be initialized at the given path"""
class BadObject(ODBError):
    """The object with the given SHA does not exist. Instantiate with the
    failed sha"""
class BadName(ODBError):
    """A name provided to rev_parse wasn't understood"""
class ParseError(ODBError):
    """Thrown if the parsing of a file failed due to an invalid format"""
class AmbiguousObjectName(ODBError):
    """Thrown if a possibly shortened name does not uniquely represent a single object
    in the database"""
class BadObjectType(ODBError):
    """The object had an unsupported type"""
class UnsupportedOperation(ODBError):
    """Thrown if the given operation cannot be supported by the object database"""
