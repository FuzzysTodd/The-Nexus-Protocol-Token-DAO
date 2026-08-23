from azure.core import CaseInsensitiveEnumMeta
from enum import Enum

class LeaseAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LeaseAction."""
    ACQUIRE: str
    AUTO_RENEW: str
    RELEASE: str
    ACQUIRE_RELEASE: str

class ListBlobsIncludeItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListBlobsIncludeItem."""
    COPY: str
    DELETED: str
    METADATA: str
    SNAPSHOTS: str
    UNCOMMITTEDBLOBS: str
    VERSIONS: str
    TAGS: str

class PathExpiryOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathExpiryOptions."""
    NEVER_EXPIRE: str
    RELATIVE_TO_CREATION: str
    RELATIVE_TO_NOW: str
    ABSOLUTE: str

class PathGetPropertiesAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathGetPropertiesAction."""
    GET_ACCESS_CONTROL: str
    GET_STATUS: str

class PathLeaseAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathLeaseAction."""
    ACQUIRE: str
    BREAK: str
    CHANGE: str
    RENEW: str
    RELEASE: str

class PathRenameMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathRenameMode."""
    LEGACY: str
    POSIX: str

class PathResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathResourceType."""
    DIRECTORY: str
    FILE: str

class PathSetAccessControlRecursiveMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathSetAccessControlRecursiveMode."""
    SET: str
    MODIFY: str
    REMOVE: str

class PathUpdateAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PathUpdateAction."""
    APPEND: str
    FLUSH: str
    SET_PROPERTIES: str
    SET_ACCESS_CONTROL: str
    SET_ACCESS_CONTROL_RECURSIVE: str
