from _typeshed import Incomplete
from jedi.inference.helpers import is_big_annoying_library as is_big_annoying_library
from jedi.inference.recursion import execution_allowed as execution_allowed
from jedi.parser_utils import get_flow_branch_keyword as get_flow_branch_keyword, get_parent_scope as get_parent_scope, is_scope as is_scope
from typing import Dict

class Status:
    lookup_table: Dict[bool | None, 'Status']
    def __init__(self, value: bool | None, name: str) -> None: ...
    def invert(self): ...
    def __and__(self, other): ...

REACHABLE: Incomplete
UNREACHABLE: Incomplete
UNSURE: Incomplete

def reachability_check(context, value_scope, node, origin_scope: Incomplete | None = None): ...
