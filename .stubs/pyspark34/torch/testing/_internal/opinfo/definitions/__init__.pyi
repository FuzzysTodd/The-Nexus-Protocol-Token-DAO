from torch.testing._internal.opinfo.core import OpInfo as OpInfo
from torch.testing._internal.opinfo.definitions import fft as fft, linalg as linalg, signal as signal, special as special
from typing import List

op_db: List[OpInfo]
python_ref_db: List[OpInfo]
