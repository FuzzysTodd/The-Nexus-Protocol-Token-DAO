import typing
from . import constants as constants, exceptions as exceptions

LockFlags = constants.LockFlags

def lock(file_: typing.IO | int, flags: LockFlags): ...
def unlock(file_: typing.IO): ...
