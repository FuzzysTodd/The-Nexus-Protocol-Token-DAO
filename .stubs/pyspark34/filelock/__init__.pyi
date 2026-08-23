from ._api import AcquireReturnProxy as AcquireReturnProxy, BaseFileLock as BaseFileLock
from ._error import Timeout as Timeout
from ._soft import SoftFileLock as SoftFileLock
from ._unix import UnixFileLock as UnixFileLock
from ._windows import WindowsFileLock as WindowsFileLock

__all__ = ['__version__', 'FileLock', 'SoftFileLock', 'Timeout', 'UnixFileLock', 'WindowsFileLock', 'BaseFileLock', 'AcquireReturnProxy']

__version__: str
FileLock = SoftFileLock
