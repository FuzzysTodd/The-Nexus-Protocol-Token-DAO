from .constants import PRUNER_DICT as PRUNER_DICT, QUANTIZER_DICT as QUANTIZER_DICT
from _typeshed import Incomplete
from typing import Any

class AutoCompressionSearchSpaceGenerator:
    """
    For convenient generation of search space that can be used by tuner.
    """
    algorithm_choice_list: Incomplete
    def __init__(self) -> None: ...
    def add_config(self, algorithm_name: str, config_list: list, **algo_kwargs):
        """
        This function used for distinguish algorithm type is pruning or quantization.
        Then call `self._add_pruner_config()` or `self._add_quantizer_config()`.
        """
    def dumps(self) -> dict:
        """
        Dump the search space as a dict.
        """
    @classmethod
    def loads(cls, search_space: dict):
        """
        Return a AutoCompressionSearchSpaceGenerator instance load from a search space dict.
        """

def import_(target: str, allow_none: bool = False) -> Any: ...
