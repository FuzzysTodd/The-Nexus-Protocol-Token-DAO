from .clr_error import ClrError as ClrError
from typing import Dict

def get_coreclr_error(hresult: int) -> ClrError | None: ...

Comment: Dict[int, str]
SymbolicName: Dict[int, str]
Message: Dict[int, str]
