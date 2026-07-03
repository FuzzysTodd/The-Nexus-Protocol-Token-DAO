from ..types import StrOrPath
from .find import find_dotnet_root as find_dotnet_root

__all__ = ['check_result', 'find_dotnet_root', 'path_as_string', 'optional_path_as_string']

def optional_path_as_string(path: StrOrPath | None) -> str | None: ...
def path_as_string(path: StrOrPath) -> str: ...
def check_result(err_code: int) -> None:
    """Check the error code of a .NET hosting API function and raise a
    converted exception.

    :raises ClrError: If the error code is `< 0`
    """
