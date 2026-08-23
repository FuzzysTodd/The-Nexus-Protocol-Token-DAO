from .convert_slow_tokenizer import SLOW_TO_FAST_CONVERTERS as SLOW_TO_FAST_CONVERTERS
from .utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
TOKENIZER_CLASSES: Incomplete

def convert_slow_checkpoint_to_fast(tokenizer_name, checkpoint_name, dump_path, force_download) -> None: ...
