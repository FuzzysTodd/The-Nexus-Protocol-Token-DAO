import pyarrow as pa
from .. import config as config
from ..download.download_config import DownloadConfig as DownloadConfig
from ..download.streaming_download_manager import xopen as xopen, xsplitext as xsplitext
from ..table import array_cast as array_cast
from ..utils.py_utils import no_op_if_value_is_null as no_op_if_value_is_null, string_to_dict as string_to_dict
from .features import FeatureType as FeatureType
from dataclasses import dataclass
from typing import Any, ClassVar, Dict

@dataclass
class Audio:
    '''Audio [`Feature`] to extract audio data from an audio file.

    Input: The Audio feature accepts as input:
    - A `str`: Absolute path to the audio file (i.e. random access is allowed).
    - A `dict` with the keys:

        - `path`: String with relative path of the audio file to the archive file.
        - `bytes`: Bytes content of the audio file.

      This is useful for archived files with sequential access.

    - A `dict` with the keys:

        - `path`: String with relative path of the audio file to the archive file.
        - `array`: Array containing the audio sample
        - `sampling_rate`: Integer corresponding to the sampling rate of the audio sample.

      This is useful for archived files with sequential access.

    Args:
        sampling_rate (`int`, *optional*):
            Target sampling rate. If `None`, the native sampling rate is used.
        mono (`bool`, defaults to `True`):
            Whether to convert the audio signal to mono by averaging samples across
            channels.
        decode (`bool`, defaults to `True`):
            Whether to decode the audio data. If `False`,
            returns the underlying dictionary in the format `{"path": audio_path, "bytes": audio_bytes}`.

    Example:

    ```py
    >>> from datasets import load_dataset, Audio
    >>> ds = load_dataset("PolyAI/minds14", name="en-US", split="train")
    >>> ds = ds.cast_column("audio", Audio(sampling_rate=16000))
    >>> ds[0]["audio"]
    {\'array\': array([ 2.3443763e-05,  2.1729663e-04,  2.2145823e-04, ...,
         3.8356509e-05, -7.3497440e-06, -2.1754686e-05], dtype=float32),
     \'path\': \'/root/.cache/huggingface/datasets/downloads/extracted/f14948e0e84be638dd7943ac36518a4cf3324e8b7aa331c5ab11541518e9368c/en-US~JOINT_ACCOUNT/602ba55abb1e6d0fbce92065.wav\',
     \'sampling_rate\': 16000}
    ```
    '''
    sampling_rate: int | None = ...
    mono: bool = ...
    decode: bool = ...
    id: str | None = ...
    dtype: ClassVar[str] = ...
    pa_type: ClassVar[Any] = ...
    def __call__(self): ...
    def encode_example(self, value: str | bytes | dict) -> dict:
        """Encode example into a format for Arrow.

        Args:
            value (`str` or `dict`):
                Data passed as input to Audio feature.

        Returns:
            `dict`
        """
    def decode_example(self, value: dict, token_per_repo_id: Dict[str, str | bool | None] | None = None) -> dict:
        """Decode example audio file into audio data.

        Args:
            value (`dict`):
                A dictionary with keys:

                - `path`: String with relative audio file path.
                - `bytes`: Bytes of the audio file.
            token_per_repo_id (`dict`, *optional*):
                To access and decode
                audio files from private repositories on the Hub, you can pass
                a dictionary repo_id (`str`) -> token (`bool` or `str`)

        Returns:
            `dict`
        """
    def flatten(self) -> FeatureType | Dict[str, 'FeatureType']:
        """If in the decodable state, raise an error, otherwise flatten the feature into a dictionary."""
    def cast_storage(self, storage: pa.StringArray | pa.StructArray) -> pa.StructArray:
        '''Cast an Arrow array to the Audio arrow storage type.
        The Arrow types that can be converted to the Audio pyarrow storage type are:

        - `pa.string()` - it must contain the "path" data
        - `pa.binary()` - it must contain the audio bytes
        - `pa.struct({"bytes": pa.binary()})`
        - `pa.struct({"path": pa.string()})`
        - `pa.struct({"bytes": pa.binary(), "path": pa.string()})`  - order doesn\'t matter

        Args:
            storage (`Union[pa.StringArray, pa.StructArray]`):
                PyArrow array to cast.

        Returns:
            `pa.StructArray`: Array in the Audio arrow storage type, that is
                `pa.struct({"bytes": pa.binary(), "path": pa.string()})`
        '''
    def embed_storage(self, storage: pa.StructArray) -> pa.StructArray:
        '''Embed audio files into the Arrow array.

        Args:
            storage (`pa.StructArray`):
                PyArrow array to embed.

        Returns:
            `pa.StructArray`: Array in the Audio arrow storage type, that is
                `pa.struct({"bytes": pa.binary(), "path": pa.string()})`.
        '''
    def __init__(self, sampling_rate, mono, decode, id) -> None: ...
