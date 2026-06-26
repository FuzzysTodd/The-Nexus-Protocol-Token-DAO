from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src.lib import xla_client

__all__ = ['fft', 'fft_p']

def fft(x, fft_type: xla_client.FftType | str, fft_lengths: Sequence[int]): ...

fft_p: Incomplete
