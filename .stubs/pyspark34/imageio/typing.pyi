from io import BytesIO
from numpy import ndarray as ArrayLike
from pathlib import Path
from typing import BinaryIO

__all__ = ['ArrayLike', 'ImageResource']

ImageResource = str | BytesIO | Path | BinaryIO
