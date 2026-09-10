from .clr_error import ClrError

__all__ = ['get_hostfxr_error']

def get_hostfxr_error(hresult: int) -> ClrError | None: ...
