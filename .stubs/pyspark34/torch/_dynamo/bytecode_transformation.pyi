import dataclasses
import dis
import types
from .bytecode_analysis import propagate_line_nums as propagate_line_nums, remove_extra_line_nums as remove_extra_line_nums, stacksize_analysis as stacksize_analysis
from _typeshed import Incomplete
from typing import Any, Dict, List, Tuple

@dataclasses.dataclass
class Instruction:
    """A mutable version of dis.Instruction"""
    opcode: int
    opname: str
    arg: int | None
    argval: Any
    offset: int | None = ...
    starts_line: int | None = ...
    is_jump_target: bool = ...
    target: Instruction | None = ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __init__(self, opcode, opname, arg, argval, offset, starts_line, is_jump_target, target) -> None: ...

def convert_instruction(i: dis.Instruction): ...

class _NotProvided: ...

def create_instruction(name, arg: Incomplete | None = None, argval=..., target: Incomplete | None = None): ...
def create_jump_absolute(target): ...
def create_dup_top(): ...
def create_rot_n(n):
    '''
    Returns a "simple" sequence of instructions that rotates TOS to the n-th
    position in the stack. For Python < 3.11, returns a single ROT_*
    instruction. If no such instruction exists, an error is raised and the
    caller is expected to generate an equivalent sequence of instructions.
    For Python >= 3.11, any rotation can be expressed as a simple sequence of
    swaps.
    '''
def lnotab_writer(lineno, byteno: int = 0):
    """
    Used to create typing.CodeType.co_lnotab
    See https://github.com/python/cpython/blob/main/Objects/lnotab_notes.txt
    This is the internal format of the line number table if Python < 3.10
    """
def linetable_writer(first_lineno):
    """
    Used to create typing.CodeType.co_linetable
    See https://github.com/python/cpython/blob/main/Objects/lnotab_notes.txt
    This is the internal format of the line number table if Python >= 3.10
    """
def assemble(instructions: List[Instruction], firstlineno):
    """Do the opposite of dis.get_instructions()"""
def virtualize_jumps(instructions) -> None:
    """Replace jump targets with pointers to make editing easier"""
def flip_jump_direction(instruction) -> None: ...
def devirtualize_jumps(instructions) -> None:
    """Fill in args for virtualized jump target after instructions may have moved"""
def strip_extended_args(instructions: List[Instruction]): ...
def remove_load_call_method(instructions: List[Instruction]):
    """LOAD_METHOD puts a NULL on the stack which causes issues, so remove it"""
def explicit_super(code: types.CodeType, instructions: List[Instruction]):
    """convert super() with no args into explict arg form"""
def fix_extended_args(instructions: List[Instruction]):
    """Fill in correct argvals for EXTENDED_ARG ops"""
def instruction_size(inst): ...
def check_offsets(instructions) -> None: ...
def update_offsets(instructions) -> None: ...
def debug_bytes(*args): ...
def debug_checks(code) -> None:
    """Make sure our assembler produces same bytes as we start with"""

HAS_LOCAL: Incomplete
HAS_NAME: Incomplete

def fix_vars(instructions: List[Instruction], code_options): ...
def transform_code_object(code, transformations, safe: bool = False): ...
def clean_and_assemble_instructions(instructions: List[Instruction], keys: List[str], code_options: Dict[str, Any]) -> Tuple[List[Instruction], types.CodeType]: ...
def cleaned_instructions(code, safe: bool = False): ...
def unique_id(name): ...
def is_generator(code: types.CodeType): ...
