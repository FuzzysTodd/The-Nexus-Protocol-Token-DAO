import ctypes
from paramiko.common import zero_byte as zero_byte
from paramiko.util import b as b

win32con_WM_COPYDATA: int

def can_talk_to_agent():
    '''
    Check to see if there is a "Pageant" agent we can talk to.

    This checks both if we have the required libraries (win32all or ctypes)
    and if there is a Pageant currently running.
    '''
ULONG_PTR = ctypes.c_uint64
ULONG_PTR = ctypes.c_uint32

class COPYDATASTRUCT(ctypes.Structure):
    """
    ctypes implementation of
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms649010%28v=vs.85%29.aspx
    """

class PageantConnection:
    '''
    Mock "connection" to an agent which roughly approximates the behavior of
    a unix local-domain socket (as used by Agent).  Requests are sent to the
    pageant daemon via special Windows magick, and responses are buffered back
    for subsequent reads.
    '''
    def __init__(self) -> None: ...
    def send(self, data) -> None: ...
    def recv(self, n): ...
    def close(self) -> None: ...
