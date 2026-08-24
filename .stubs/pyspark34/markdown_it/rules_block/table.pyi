from ..common.utils import charStrAt as charStrAt, isStrSpace as isStrSpace
from .state_block import StateBlock as StateBlock
from _typeshed import Incomplete

headerLineRe: Incomplete
enclosingPipesRe: Incomplete

def getLine(state: StateBlock, line: int) -> str: ...
def escapedSplit(string: str) -> list[str]: ...
def table(state: StateBlock, startLine: int, endLine: int, silent: bool) -> bool: ...
