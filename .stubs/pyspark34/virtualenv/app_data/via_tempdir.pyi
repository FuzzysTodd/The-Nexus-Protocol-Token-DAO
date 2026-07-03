from .via_disk_folder import AppDataDiskFolder

__all__ = ['TempAppData']

class TempAppData(AppDataDiskFolder):
    transient: bool
    can_update: bool
    def __init__(self) -> None: ...
    def reset(self) -> None:
        """This is a temporary folder, is already empty to start with."""
    def close(self) -> None: ...
    def embed_update_log(self, distribution, for_py_version) -> None: ...
