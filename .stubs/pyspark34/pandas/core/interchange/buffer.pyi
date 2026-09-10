import numpy as np
from pandas.core.interchange.dataframe_protocol import Buffer as Buffer, DlpackDeviceType as DlpackDeviceType
from pandas.util.version import Version as Version

class PandasBuffer(Buffer):
    """
    Data in the buffer is guaranteed to be contiguous in memory.
    """
    def __init__(self, x: np.ndarray, allow_copy: bool = True) -> None:
        """
        Handle only regular columns (= numpy arrays) for now.
        """
    @property
    def bufsize(self) -> int:
        """
        Buffer size in bytes.
        """
    @property
    def ptr(self) -> int:
        """
        Pointer to start of the buffer as an integer.
        """
    def __dlpack__(self):
        """
        Represent this structure as DLPack interface.
        """
    def __dlpack_device__(self) -> tuple[DlpackDeviceType, int | None]:
        """
        Device type and device ID for where the data in the buffer resides.
        """
