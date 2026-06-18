import ctypes
from _typeshed import Incomplete

objc: Incomplete
void_p = ctypes.c_void_p
msg: Incomplete

def n(name):
    """create a selector name (for ObjC methods)"""
def C(classname):
    """get an ObjC Class by name"""

CoreFoundation: Incomplete
CFFileDescriptorCreate: Incomplete
CFFileDescriptorGetNativeDescriptor: Incomplete
CFFileDescriptorEnableCallBacks: Incomplete
CFFileDescriptorCreateRunLoopSource: Incomplete
CFRunLoopGetCurrent: Incomplete
CFRunLoopAddSource: Incomplete
CFRelease: Incomplete
CFFileDescriptorInvalidate: Incomplete
kCFFileDescriptorReadCallBack: int
kCFRunLoopCommonModes: Incomplete

def inputhook(context) -> None:
    """Inputhook for Cocoa (NSApp)"""
