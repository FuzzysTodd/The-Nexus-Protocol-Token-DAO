import abc
from _typeshed import Incomplete

ABC = abc.ABC
logger: Incomplete

class PersistenceError(IOError):
    """The base exception for persistence."""
    def __init__(self, err_no: Incomplete | None = None, message: Incomplete | None = None, location: Incomplete | None = None) -> None: ...

class PersistenceNotFound(PersistenceError):
    """This happens when attempting BasePersistence.load() on a non-existent persistence instance"""
    def __init__(self, err_no: Incomplete | None = None, message: Incomplete | None = None, location: Incomplete | None = None) -> None: ...

class PersistenceEncryptionError(PersistenceError):
    """This could be raised by persistence.save()"""
class PersistenceDecryptionError(PersistenceError):
    """This could be raised by persistence.load()"""

def build_encrypted_persistence(location):
    """Build a suitable encrypted persistence instance based your current OS.

    If you do not need encryption, then simply use ``FilePersistence`` constructor.
    """

class BasePersistence(ABC, metaclass=abc.ABCMeta):
    """An abstract persistence defining the common interface of this family"""
    is_encrypted: bool
    @abc.abstractmethod
    def save(self, content: str) -> None:
        """Save the content into this persistence"""
    @abc.abstractmethod
    def load(self) -> str:
        """Load content from this persistence.

        Could raise PersistenceNotFound if no save() was called before.
        """
    @abc.abstractmethod
    def time_last_modified(self):
        """Get the last time when this persistence has been modified.

        Could raise PersistenceNotFound if no save() was called before.
        """
    @abc.abstractmethod
    def get_location(self):
        """Return the file path which this persistence stores (meta)data into"""

class FilePersistence(BasePersistence):
    """A generic persistence, storing data in a plain-text file"""
    def __init__(self, location) -> None: ...
    def save(self, content: str) -> None:
        """Save the content into this persistence"""
    def load(self) -> str:
        """Load content from this persistence"""
    def time_last_modified(self): ...
    def touch(self) -> None:
        """To touch this file-based persistence without writing content into it"""
    def get_location(self): ...

class FilePersistenceWithDataProtection(FilePersistence):
    """A generic persistence with data stored in a file,
    protected by Win32 encryption APIs on Windows"""
    is_encrypted: bool
    def __init__(self, location, entropy: str = '') -> None:
        """Initialization could fail due to unsatisfied dependency"""
    def save(self, content: str) -> None: ...
    def load(self) -> str: ...

class KeychainPersistence(BasePersistence):
    """A generic persistence with data stored in,
    and protected by native Keychain libraries on OSX"""
    is_encrypted: bool
    def __init__(self, signal_location, service_name: Incomplete | None = None, account_name: Incomplete | None = None) -> None:
        """Initialization could fail due to unsatisfied dependency.

        :param signal_location: See :func:`persistence.LibsecretPersistence.__init__`
        """
    def save(self, content) -> None: ...
    def load(self): ...
    def time_last_modified(self): ...
    def get_location(self): ...

class LibsecretPersistence(BasePersistence):
    """A generic persistence with data stored in,
    and protected by native libsecret libraries on Linux"""
    is_encrypted: bool
    def __init__(self, signal_location, schema_name: Incomplete | None = None, attributes: Incomplete | None = None, **kwargs) -> None:
        """Initialization could fail due to unsatisfied dependency.

        :param string signal_location:
            Besides saving the real payload into encrypted storage,
            this class will also touch this signal file.
            Applications may listen a FileSystemWatcher.Changed event for reload.
            https://docs.microsoft.com/en-us/dotnet/api/system.io.filesystemwatcher.changed?view=netframework-4.8#remarks
        :param string schema_name: See :func:`libsecret.LibSecretAgent.__init__`
        :param dict attributes: See :func:`libsecret.LibSecretAgent.__init__`
        """
    def save(self, content) -> None: ...
    def load(self): ...
    def time_last_modified(self): ...
    def get_location(self): ...
