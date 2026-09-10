from .na import AppDataDisabled as AppDataDisabled
from .read_only import ReadOnlyAppData as ReadOnlyAppData
from .via_disk_folder import AppDataDiskFolder as AppDataDiskFolder
from .via_tempdir import TempAppData as TempAppData

__all__ = ['AppDataDisabled', 'AppDataDiskFolder', 'ReadOnlyAppData', 'TempAppData', 'make_app_data']

def make_app_data(folder, **kwargs): ...
