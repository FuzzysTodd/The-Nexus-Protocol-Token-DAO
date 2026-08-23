from typing import NamedTuple
from typing_extensions import Literal

__all__ = ['AlgoMeta']

class AlgoMeta(NamedTuple):
    name: str
    alias: str | None
    class_name: str | None
    accept_class_args: bool
    class_args: dict | None
    validator_class_name: str | None
    algo_type: Literal['tuner', 'assessor']
    is_advisor: bool
    is_builtin: bool
    nni_version: str | None
    @staticmethod
    def load(meta: dict, algo_type: Literal['tuner', 'assessor', 'advisor'] | None = None) -> AlgoMeta: ...
    def dump(self) -> dict: ...
