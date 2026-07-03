import PIL.Image
import numpy as np
import pyarrow as pa
from .. import config as config
from ..download.download_config import DownloadConfig as DownloadConfig
from ..download.streaming_download_manager import xopen as xopen
from ..table import array_cast as array_cast
from ..utils.file_utils import is_local_path as is_local_path
from ..utils.py_utils import first_non_null_value as first_non_null_value, no_op_if_value_is_null as no_op_if_value_is_null, string_to_dict as string_to_dict
from .features import FeatureType as FeatureType
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, ClassVar, Dict, List

@dataclass
class Image:
    '''Image [`Feature`] to read image data from an image file.

    Input: The Image feature accepts as input:
    - A `str`: Absolute path to the image file (i.e. random access is allowed).
    - A `dict` with the keys:

        - `path`: String with relative path of the image file to the archive file.
        - `bytes`: Bytes of the image file.

      This is useful for archived files with sequential access.

    - An `np.ndarray`: NumPy array representing an image.
    - A `PIL.Image.Image`: PIL image object.

    Args:
        decode (`bool`, defaults to `True`):
            Whether to decode the image data. If `False`,
            returns the underlying dictionary in the format `{"path": image_path, "bytes": image_bytes}`.

    Examples:

    ```py
    >>> from datasets import load_dataset, Image
    >>> ds = load_dataset("beans", split="train")
    >>> ds.features["image"]
    Image(decode=True, id=None)
    >>> ds[0]["image"]
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=500x500 at 0x15E52E7F0>
    >>> ds = ds.cast_column(\'image\', Image(decode=False))
    {\'bytes\': None,
     \'path\': \'/root/.cache/huggingface/datasets/downloads/extracted/b0a21163f78769a2cf11f58dfc767fb458fc7cea5c05dccc0144a2c0f0bc1292/train/healthy/healthy_train.85.jpg\'}
    ```
    '''
    decode: bool = ...
    id: str | None = ...
    dtype: ClassVar[str] = ...
    pa_type: ClassVar[Any] = ...
    def __call__(self): ...
    def encode_example(self, value: str | bytes | dict | np.ndarray | PIL.Image.Image) -> dict:
        '''Encode example into a format for Arrow.

        Args:
            value (`str`, `np.ndarray`, `PIL.Image.Image` or `dict`):
                Data passed as input to Image feature.

        Returns:
            `dict` with "path" and "bytes" fields
        '''
    def decode_example(self, value: dict, token_per_repo_id: Incomplete | None = None) -> PIL.Image.Image:
        """Decode example image file into image data.

        Args:
            value (`str` or `dict`):
                A string with the absolute image file path, a dictionary with
                keys:

                - `path`: String with absolute or relative image file path.
                - `bytes`: The bytes of the image file.
            token_per_repo_id (`dict`, *optional*):
                To access and decode
                image files from private repositories on the Hub, you can pass
                a dictionary repo_id (`str`) -> token (`bool` or `str`).

        Returns:
            `PIL.Image.Image`
        """
    def flatten(self) -> FeatureType | Dict[str, 'FeatureType']:
        """If in the decodable state, return the feature itself, otherwise flatten the feature into a dictionary."""
    def cast_storage(self, storage: pa.StringArray | pa.StructArray | pa.ListArray) -> pa.StructArray:
        '''Cast an Arrow array to the Image arrow storage type.
        The Arrow types that can be converted to the Image pyarrow storage type are:

        - `pa.string()` - it must contain the "path" data
        - `pa.binary()` - it must contain the image bytes
        - `pa.struct({"bytes": pa.binary()})`
        - `pa.struct({"path": pa.string()})`
        - `pa.struct({"bytes": pa.binary(), "path": pa.string()})`  - order doesn\'t matter
        - `pa.list(*)` - it must contain the image array data

        Args:
            storage (`Union[pa.StringArray, pa.StructArray, pa.ListArray]`):
                PyArrow array to cast.

        Returns:
            `pa.StructArray`: Array in the Image arrow storage type, that is
                `pa.struct({"bytes": pa.binary(), "path": pa.string()})`.
        '''
    def embed_storage(self, storage: pa.StructArray) -> pa.StructArray:
        '''Embed image files into the Arrow array.

        Args:
            storage (`pa.StructArray`):
                PyArrow array to embed.

        Returns:
            `pa.StructArray`: Array in the Image arrow storage type, that is
                `pa.struct({"bytes": pa.binary(), "path": pa.string()})`.
        '''
    def __init__(self, decode, id) -> None: ...

def list_image_compression_formats() -> List[str]: ...
def image_to_bytes(image: PIL.Image.Image) -> bytes:
    """Convert a PIL Image object to bytes using native compression if possible, otherwise use PNG/TIFF compression."""
def encode_pil_image(image: PIL.Image.Image) -> dict: ...
def encode_np_array(array: np.ndarray) -> dict: ...
def objects_to_list_of_image_dicts(objs: List[str] | List[dict] | List[np.ndarray] | List['PIL.Image.Image']) -> List[dict]:
    """Encode a list of objects into a format suitable for creating an extension array of type `ImageExtensionType`."""
