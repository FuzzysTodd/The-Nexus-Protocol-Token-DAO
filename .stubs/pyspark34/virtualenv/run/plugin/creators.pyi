from .base import ComponentBuilder
from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['CreatorSelector', 'CreatorInfo']

class CreatorInfo(NamedTuple):
    key_to_class: Incomplete
    key_to_meta: Incomplete
    describe: Incomplete
    builtin_key: Incomplete

class CreatorSelector(ComponentBuilder):
    def __init__(self, interpreter, parser) -> None: ...
    @classmethod
    def for_interpreter(cls, interpreter): ...
    def add_selector_arg_parse(self, name, choices): ...
    def populate_selected_argparse(self, selected, app_data) -> None: ...
    def create(self, options): ...

# Names in __all__ with no definition:
#   CreatorInfo
