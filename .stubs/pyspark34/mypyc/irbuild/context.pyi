from _typeshed import Incomplete
from mypy.nodes import FuncItem as FuncItem
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import INVALID_FUNC_DEF as INVALID_FUNC_DEF
from mypyc.ir.ops import BasicBlock as BasicBlock, Value as Value
from mypyc.irbuild.targets import AssignmentTarget as AssignmentTarget

class FuncInfo:
    """Contains information about functions as they are generated."""
    fitem: Incomplete
    name: Incomplete
    class_name: Incomplete
    ns: Incomplete
    is_nested: Incomplete
    contains_nested: Incomplete
    is_decorated: Incomplete
    in_non_ext: Incomplete
    add_nested_funcs_to_env: Incomplete
    def __init__(self, fitem: FuncItem = ..., name: str = '', class_name: str | None = None, namespace: str = '', is_nested: bool = False, contains_nested: bool = False, is_decorated: bool = False, in_non_ext: bool = False, add_nested_funcs_to_env: bool = False) -> None: ...
    def namespaced_name(self) -> str: ...
    @property
    def is_generator(self) -> bool: ...
    @property
    def is_coroutine(self) -> bool: ...
    @property
    def callable_class(self) -> ImplicitClass: ...
    @callable_class.setter
    def callable_class(self, cls: ImplicitClass) -> None: ...
    @property
    def env_class(self) -> ClassIR: ...
    @env_class.setter
    def env_class(self, ir: ClassIR) -> None: ...
    @property
    def generator_class(self) -> GeneratorClass: ...
    @generator_class.setter
    def generator_class(self, cls: GeneratorClass) -> None: ...
    @property
    def curr_env_reg(self) -> Value: ...

class ImplicitClass:
    """Contains information regarding implicitly generated classes.

    Implicit classes are generated for nested functions and generator
    functions. They are not explicitly defined in the source code.

    NOTE: This is both a concrete class and used as a base class.
    """
    ir: Incomplete
    def __init__(self, ir: ClassIR) -> None: ...
    @property
    def self_reg(self) -> Value: ...
    @self_reg.setter
    def self_reg(self, reg: Value) -> None: ...
    @property
    def curr_env_reg(self) -> Value: ...
    @curr_env_reg.setter
    def curr_env_reg(self, reg: Value) -> None: ...
    @property
    def prev_env_reg(self) -> Value: ...
    @prev_env_reg.setter
    def prev_env_reg(self, reg: Value) -> None: ...

class GeneratorClass(ImplicitClass):
    """Contains information about implicit generator function classes."""
    exc_regs: Incomplete
    send_arg_reg: Incomplete
    switch_block: Incomplete
    continuation_blocks: Incomplete
    def __init__(self, ir: ClassIR) -> None: ...
    @property
    def next_label_reg(self) -> Value: ...
    @next_label_reg.setter
    def next_label_reg(self, reg: Value) -> None: ...
    @property
    def next_label_target(self) -> AssignmentTarget: ...
    @next_label_target.setter
    def next_label_target(self, target: AssignmentTarget) -> None: ...
