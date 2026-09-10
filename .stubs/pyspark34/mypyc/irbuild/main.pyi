from _typeshed import Incomplete
from mypy.build import Graph as Graph
from mypy.nodes import Expression as Expression, MypyFile as MypyFile
from mypy.types import Type as Type
from mypyc.analysis.attrdefined import analyze_always_defined_attrs as analyze_always_defined_attrs
from mypyc.common import TOP_LEVEL_NAME as TOP_LEVEL_NAME
from mypyc.errors import Errors as Errors
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR, FuncSignature as FuncSignature
from mypyc.ir.module_ir import ModuleIR as ModuleIR, ModuleIRs as ModuleIRs
from mypyc.ir.rtypes import none_rprimitive as none_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.mapper import Mapper as Mapper
from mypyc.irbuild.prebuildvisitor import PreBuildVisitor as PreBuildVisitor
from mypyc.irbuild.prepare import build_type_map as build_type_map, find_singledispatch_register_impls as find_singledispatch_register_impls
from mypyc.irbuild.visitor import IRBuilderVisitor as IRBuilderVisitor
from mypyc.irbuild.vtable import compute_vtable as compute_vtable
from mypyc.options import CompilerOptions as CompilerOptions
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])
strict_optional_dec: Incomplete

def build_ir(modules: list[MypyFile], graph: Graph, types: dict[Expression, Type], mapper: Mapper, options: CompilerOptions, errors: Errors) -> ModuleIRs:
    """Build basic IR for a set of modules that have been type-checked by mypy.

    The returned IR is not complete and requires additional
    transformations, such as the insertion of refcount handling.
    """
def transform_mypy_file(builder: IRBuilder, mypyfile: MypyFile) -> None:
    """Generate IR for a single module."""
