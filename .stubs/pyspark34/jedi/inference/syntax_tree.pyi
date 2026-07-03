from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug, parser_utils as parser_utils
from jedi.inference import analysis as analysis, arguments as arguments, compiled as compiled, imports as imports, recursion as recursion
from jedi.inference.base_value import ContextualizedNode as ContextualizedNode, NO_VALUES as NO_VALUES, ValueSet as ValueSet, iterate_values as iterate_values, iterator_to_value_set as iterator_to_value_set
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.compiled.access import COMPARISON_OPERATORS as COMPARISON_OPERATORS
from jedi.inference.context import CompForContext as CompForContext
from jedi.inference.gradual import annotation as annotation
from jedi.inference.gradual.stub_value import VersionInfo as VersionInfo
from jedi.inference.helpers import get_names_of_node as get_names_of_node, is_big_annoying_library as is_big_annoying_library, is_literal as is_literal, is_number as is_number, is_string as is_string
from jedi.inference.lazy_value import LazyTreeValue as LazyTreeValue
from jedi.inference.names import TreeNameDefinition as TreeNameDefinition
from jedi.inference.value import ClassValue as ClassValue, FunctionValue as FunctionValue, TreeInstance as TreeInstance, iterable as iterable
from jedi.inference.value.decorator import Decoratee as Decoratee
from jedi.inference.value.dynamic_arrays import DictModification as DictModification, ListModification as ListModification
from jedi.plugins import plugin_manager as plugin_manager

operator_to_magic_method: Incomplete
reverse_operator_to_magic_method: Incomplete

def infer_node(context, element): ...
def infer_trailer(context, atom_values, trailer): ...
def infer_atom(context, atom):
    """
    Basically to process ``atom`` nodes. The parser sometimes doesn't
    generate the node (because it has just one child). In that case an atom
    might be a name or a literal as well.
    """
def infer_expr_stmt(context, stmt, seek_name: Incomplete | None = None): ...
def infer_or_test(context, or_test): ...
def infer_factor(value_set, operator) -> Generator[Incomplete, None, None]:
    """
    Calculates `+`, `-`, `~` and `not` prefixes.
    """
def tree_name_to_values(inference_state, context, tree_name): ...
def check_tuple_assignments(name, value_set):
    """
    Checks if tuples are assigned.
    """

class ContextualizedSubscriptListNode(ContextualizedNode):
    def infer(self): ...
