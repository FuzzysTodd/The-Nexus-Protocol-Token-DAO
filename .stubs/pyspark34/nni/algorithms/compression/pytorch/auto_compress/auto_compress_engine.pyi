from .constants import PRUNER_DICT as PRUNER_DICT, QUANTIZER_DICT as QUANTIZER_DICT
from .interface import AbstractAutoCompressionModule as AbstractAutoCompressionModule, BaseAutoCompressionEngine as BaseAutoCompressionEngine
from .utils import import_ as import_
from torch.nn import Module as Module

class AutoCompressionEngine(BaseAutoCompressionEngine):
    @classmethod
    def trial_execute_compress(cls, module_name) -> None: ...
