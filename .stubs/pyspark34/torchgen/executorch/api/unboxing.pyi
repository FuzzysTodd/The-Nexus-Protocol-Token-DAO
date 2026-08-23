from dataclasses import dataclass
from torchgen.api.types import Binding as Binding, CType as CType, NamedCType as NamedCType
from torchgen.model import Argument as Argument, BaseTy as BaseTy, BaseType as BaseType, ListType as ListType, NativeFunction as NativeFunction, OptionalType as OptionalType, Type as Type
from typing import Callable, List, Sequence, Tuple

connector: str

def name(f: NativeFunction) -> str: ...

@dataclass(frozen=True)
class Unboxing:
    '''
    Takes a sequence of Bindings and unbox EValues to these Bindings. Return generated code that performs correct unboxing.
    A sample generated code:
    // aten::mul.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!)
    void mul_out(EValue** stack) {
        EValue& self = *stack[0];
        EValue& other = *stack[1];
        EValue& out = *stack[2];
        const torch::executor::Tensor & self_base = self.to<torch::executor::Tensor>();
        const torch::executor::Tensor & other_base = other.to<torch::executor::Tensor>();
        torch::executor::Tensor & out_base = out.to<torch::executor::Tensor>();

        EXECUTORCH_SCOPE_PROF("native_call_mul.out");
        torch::executor::mul_outf(self_base, other_base, out_base);


    }
    '''
    argument_type_gen: Callable[..., NamedCType]
    def convert_arguments(self, args: Sequence[Binding]) -> Tuple[List[Binding], List[str]]: ...
    def argumenttype_evalue_convert(self, t: Type, arg_name: str, *, mutable: bool = False) -> Tuple[str, CType, List[str], List[str]]:
        """
        Takes in the type, name and mutability corresponding to an argument, and generates a tuple of:
        (1) the C++ code necessary to unbox the argument
        (2) A Binding corresponding to the newly created unboxed variable, including variable name and its CType
        :param t: a `Type` of an argument
        :param arg_name: argument name
        :param mutable: boolean for whether this argument type is mutable
        :return: unboxed result
        """
    def __init__(self, argument_type_gen) -> None: ...
