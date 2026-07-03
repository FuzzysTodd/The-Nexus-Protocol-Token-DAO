import dataclasses
import types
from .bytecode_transformation import Instruction as Instruction, create_instruction as create_instruction, create_jump_absolute as create_jump_absolute, transform_code_object as transform_code_object
from .codegen import PyCodegen as PyCodegen
from .utils import ExactWeakKeyDictionary as ExactWeakKeyDictionary
from _typeshed import Incomplete
from typing import List, Tuple

CO_OPTIMIZED: int
CO_NEWLOCALS: int
CO_VARARGS: int
CO_VARKEYWORDS: int
CO_NESTED: int
CO_GENERATOR: int
CO_NOFREE: int
CO_COROUTINE: int
CO_ITERABLE_COROUTINE: int
CO_ASYNC_GENERATOR: int

@dataclasses.dataclass(frozen=True)
class ReenterWith:
    stack_index: int = ...
    target_values: Tuple | None = ...
    def __call__(self, code_options, cleanup): ...
    def __init__(self, stack_index, target_values) -> None: ...

@dataclasses.dataclass
class ResumeFunctionMetadata:
    code: types.CodeType
    instructions: List[Instruction] = ...
    def __init__(self, code, instructions) -> None: ...

class ContinueExecutionCache:
    cache: Incomplete
    generated_code_metadata: Incomplete
    @classmethod
    def lookup(cls, code, lineno, *key): ...
    @classmethod
    def generate(cls, code, lineno, offset: int, nstack: int, argnames: List[str], setup_fns: List[ReenterWith]): ...
    @staticmethod
    def unreachable_codes(code_options):
        """Codegen a `raise None` to make analysis work for unreachable code"""
    @classmethod
    def generate_based_on_original_code_object(cls, code, lineno, offset: int, *args):
        """
        This handles the case of generating a resume into code generated
        to resume something else.  We want to always generate starting
        from the original code object so that if control flow paths
        converge we only generated 1 resume function (rather than 2^n
        resume functions).
        """
