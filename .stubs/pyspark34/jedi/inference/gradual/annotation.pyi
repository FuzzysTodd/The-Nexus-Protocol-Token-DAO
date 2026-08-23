from jedi import debug as debug, parser_utils as parser_utils
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.compiled import builtin_from_name as builtin_from_name
from jedi.inference.gradual.base import DefineGenericBaseClass as DefineGenericBaseClass, GenericClass as GenericClass
from jedi.inference.gradual.generics import TupleGenericManager as TupleGenericManager
from jedi.inference.gradual.type_var import TypeVar as TypeVar
from jedi.inference.helpers import is_string as is_string
from jedi.inference.param import get_executed_param_names as get_executed_param_names

def infer_annotation(context, annotation):
    """
    Inferes an annotation node. This means that it inferes the part of
    `int` here:

        foo: int = 3

    Also checks for forward references (strings)
    """
def infer_param(function_value, param, ignore_stars: bool = False): ...
def py__annotations__(funcdef): ...
def resolve_forward_references(context, all_annotations): ...
def infer_return_types(function, arguments):
    """
    Infers the type of a function's return value,
    according to type annotations.
    """
def infer_type_vars_for_execution(function, arguments, annotation_dict):
    """
    Some functions use type vars that are not defined by the class, but rather
    only defined in the function. See for example `iter`. In those cases we
    want to:

    1. Search for undefined type vars.
    2. Infer type vars with the execution state we have.
    3. Return the union of all type vars that have been found.
    """
def infer_return_for_callable(arguments, param_values, result_values): ...
def merge_type_var_dicts(base_dict, new_dict) -> None: ...
def merge_pairwise_generics(annotation_value, annotated_argument_class):
    """
    Match up the generic parameters from the given argument class to the
    target annotation.

    This walks the generic parameters immediately within the annotation and
    argument's type, in order to determine the concrete values of the
    annotation's parameters for the current case.

    For example, given the following code:

        def values(mapping: Mapping[K, V]) -> List[V]: ...

        for val in values({1: 'a'}):
            val

    Then this function should be given representations of `Mapping[K, V]`
    and `Mapping[int, str]`, so that it can determine that `K` is `int and
    `V` is `str`.

    Note that it is responsibility of the caller to traverse the MRO of the
    argument type as needed in order to find the type matching the
    annotation (in this case finding `Mapping[int, str]` as a parent of
    `Dict[int, str]`).

    Parameters
    ----------

    `annotation_value`: represents the annotation to infer the concrete
        parameter types of.

    `annotated_argument_class`: represents the annotated class of the
        argument being passed to the object annotated by `annotation_value`.
    """
def find_type_from_comment_hint_for(context, node, name): ...
def find_type_from_comment_hint_with(context, node, name): ...
def find_type_from_comment_hint_assign(context, node, name): ...
def find_unknown_type_vars(context, node): ...
