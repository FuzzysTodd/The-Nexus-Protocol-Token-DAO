from _typeshed import Incomplete

__all__ = ['convertCFFToCFF2', 'main']

class _NominalWidthUsedError(Exception):
    def __add__(self, other) -> None: ...
    def __radd__(self, other) -> None: ...

def convertCFFToCFF2(font) -> None: ...
def main(args: Incomplete | None = None) -> None:
    """Convert CFF OTF font to CFF2 OTF font"""
