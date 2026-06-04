from ._tokenizer import DEFAULT_RULES as DEFAULT_RULES, Tokenizer as Tokenizer
from _typeshed import Incomplete
from typing import Any, List, NamedTuple, Tuple

class Node:
    value: Incomplete
    def __init__(self, value: str) -> None: ...
    def serialize(self) -> str: ...

class Variable(Node):
    def serialize(self) -> str: ...

class Value(Node):
    def serialize(self) -> str: ...

class Op(Node):
    def serialize(self) -> str: ...
MarkerVar = Variable | Value
MarkerItem = Tuple[MarkerVar, Op, MarkerVar]
MarkerAtom = Any
MarkerList = List[Any]

class ParsedRequirement(NamedTuple):
    name: str
    url: str
    extras: List[str]
    specifier: str
    marker: MarkerList | None

def parse_requirement(source: str) -> ParsedRequirement: ...
def parse_marker(source: str) -> MarkerList: ...
def process_env_var(env_var: str) -> Variable: ...
def process_python_str(python_str: str) -> Value: ...
