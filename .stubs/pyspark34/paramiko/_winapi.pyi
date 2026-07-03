import builtins
import ctypes
from _typeshed import Incomplete
from paramiko.util import u as u

def format_system_message(errno):
    """
    Call FormatMessage with a system error number to retrieve
    the descriptive error message.
    """

class WindowsError(builtins.WindowsError):
    """more info about errors at
    http://msdn.microsoft.com/en-us/library/ms681381(VS.85).aspx"""
    def __init__(self, value: Incomplete | None = None) -> None: ...
    @property
    def message(self): ...
    @property
    def code(self): ...

def handle_nonzero_success(result) -> None: ...

GMEM_MOVEABLE: int
GlobalAlloc: Incomplete
GlobalLock: Incomplete
GlobalUnlock: Incomplete
GlobalSize: Incomplete
CreateFileMapping: Incomplete
MapViewOfFile: Incomplete
UnmapViewOfFile: Incomplete
RtlMoveMemory: Incomplete

class MemoryMap:
    """
    A memory map object which can have security attributes overridden.
    """
    name: Incomplete
    length: Incomplete
    security_attributes: Incomplete
    pos: int
    def __init__(self, name, length, security_attributes: Incomplete | None = None) -> None: ...
    filemap: Incomplete
    view: Incomplete
    def __enter__(self): ...
    def seek(self, pos) -> None: ...
    def write(self, msg) -> None: ...
    def read(self, n):
        """
        Read n bytes from mapped view.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, tb: types.TracebackType | None) -> None: ...

READ_CONTROL: int
STANDARD_RIGHTS_REQUIRED: int
STANDARD_RIGHTS_READ = READ_CONTROL
STANDARD_RIGHTS_WRITE = READ_CONTROL
STANDARD_RIGHTS_EXECUTE = READ_CONTROL
STANDARD_RIGHTS_ALL: int
POLICY_VIEW_LOCAL_INFORMATION: int
POLICY_VIEW_AUDIT_INFORMATION: int
POLICY_GET_PRIVATE_INFORMATION: int
POLICY_TRUST_ADMIN: int
POLICY_CREATE_ACCOUNT: int
POLICY_CREATE_SECRET: int
POLICY_CREATE_PRIVILEGE: int
POLICY_SET_DEFAULT_QUOTA_LIMITS: int
POLICY_SET_AUDIT_REQUIREMENTS: int
POLICY_AUDIT_LOG_ADMIN: int
POLICY_SERVER_ADMIN: int
POLICY_LOOKUP_NAMES: int
POLICY_NOTIFICATION: int
POLICY_ALL_ACCESS: Incomplete
POLICY_READ: Incomplete
POLICY_WRITE: Incomplete
POLICY_EXECUTE: Incomplete

class TokenAccess:
    TOKEN_QUERY: int

class TokenInformationClass:
    TokenUser: int

class TOKEN_USER(ctypes.Structure):
    num: int

class SECURITY_DESCRIPTOR(ctypes.Structure):
    """
    typedef struct _SECURITY_DESCRIPTOR
        {
        UCHAR Revision;
        UCHAR Sbz1;
        SECURITY_DESCRIPTOR_CONTROL Control;
        PSID Owner;
        PSID Group;
        PACL Sacl;
        PACL Dacl;
        }   SECURITY_DESCRIPTOR;
    """
    SECURITY_DESCRIPTOR_CONTROL: Incomplete
    REVISION: int

class SECURITY_ATTRIBUTES(ctypes.Structure):
    """
    typedef struct _SECURITY_ATTRIBUTES {
        DWORD  nLength;
        LPVOID lpSecurityDescriptor;
        BOOL   bInheritHandle;
    } SECURITY_ATTRIBUTES;
    """
    nLength: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def descriptor(self): ...
    lpSecurityDescriptor: Incomplete
    @descriptor.setter
    def descriptor(self, value) -> None: ...

def GetTokenInformation(token, information_class):
    """
    Given a token, get the token information for it.
    """
def OpenProcessToken(proc_handle, access): ...
def get_current_user():
    """
    Return a TOKEN_USER for the owner of this process.
    """
def get_security_attributes_for_user(user: Incomplete | None = None):
    """
    Return a SECURITY_ATTRIBUTES structure with the SID set to the
    specified user (uses current user if none is specified).
    """
