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
CFAbsoluteTimeGetCurrent: Incomplete
CFRunLoopGetCurrent: Incomplete
CFRunLoopGetMain: Incomplete
CFRunLoopStop: Incomplete
CFRunLoopTimerCreate: Incomplete
CFRunLoopAddTimer: Incomplete
kCFRunLoopCommonModes: Incomplete

def stop(timer: Incomplete | None = None, loop: Incomplete | None = None) -> None:
    """Callback to fire when there's input to be read"""
def mainloop(duration: int = 1) -> None:
    """run the Cocoa eventloop for the specified duration (seconds)"""
