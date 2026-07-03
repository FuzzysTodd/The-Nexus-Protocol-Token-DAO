from _typeshed import Incomplete

class TmpFileManager:
    """
    A class to track record of every temporary files created by the tests.
    """
    tmp_files: Incomplete
    tmp_folders: Incomplete
    @classmethod
    def tmp_file(cls, name: str = ''): ...
    @classmethod
    def tmp_folder(cls, name: str = ''): ...
    @classmethod
    def cleanup(cls) -> None: ...

def cleanup_tmp_files(test_func):
    """
    A decorator to help test codes remove temporary files after the tests.
    """
