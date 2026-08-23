from _typeshed import Incomplete
from nni.algorithms.compression.v2.pytorch.utils.attr import get_nested_attr as get_nested_attr
from torch.nn import Module as Module
from typing import Tuple

TRANSFORMERS_INSTALLED: bool

def parser_factory(model: Module) -> HuggingfaceModelParser | None: ...

class HuggingfaceModelParser:
    TRANSFORMER_PREFIX: str
    QKV: Tuple[str, ...]
    QKVO: Tuple[str, ...]
    FFN1: Tuple[str, ...]
    FFN2: Tuple[str, ...]
    ATTENTION: Tuple[str, ...]
    @classmethod
    def is_huggingface_model(cls, model: Module): ...
    @classmethod
    def is_attention(cls, module_name: str, include_output: bool = True) -> bool: ...
    @classmethod
    def is_ffn(cls, module_name: str, ffn_num: int = 1) -> bool: ...
    @classmethod
    def get_num_heads(cls, module_name: str, model: Module) -> int: ...

class HuggingfaceBertParser(HuggingfaceModelParser):
    TRANSFORMER_PREFIX: str
    QKV: Incomplete
    QKVO: Incomplete
    FFN1: Incomplete
    FFN2: Incomplete
    ATTENTION: Incomplete

class HuggingfaceBartParser(HuggingfaceModelParser):
    TRANSFORMER_PREFIX: str
    QKV: Incomplete
    QKVO: Incomplete
    FFN1: Incomplete
    FFN2: Incomplete
    ATTENTION: Incomplete

class HuggingfaceT5Parser(HuggingfaceModelParser):
    TRANSFORMER_PREFIX: str
    QKV: Incomplete
    QKVO: Incomplete
    FFN1: Incomplete
    FFN2: Incomplete
    ATTENTION: Incomplete
