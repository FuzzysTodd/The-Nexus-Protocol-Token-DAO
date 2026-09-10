from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug
from jedi.inference import analysis as analysis
from jedi.inference.base_value import ContextualizedNode as ContextualizedNode, NO_VALUES as NO_VALUES, ValueSet as ValueSet
from jedi.inference.cache import inference_state_as_method_param_cache as inference_state_as_method_param_cache
from jedi.inference.lazy_value import LazyKnownValue as LazyKnownValue, LazyKnownValues as LazyKnownValues, LazyTreeValue as LazyTreeValue, get_merged_lazy_value as get_merged_lazy_value
from jedi.inference.names import AnonymousParamName as AnonymousParamName, ParamName as ParamName, TreeNameDefinition as TreeNameDefinition
from jedi.inference.utils import PushBackIterator as PushBackIterator
from jedi.inference.value import iterable as iterable

def try_iter_content(types, depth: int = 0) -> None:
    """Helper method for static analysis."""

class ParamIssue(Exception): ...

def repack_with_argument_clinic(clinic_string):
    """
    Transforms a function or method with arguments to the signature that is
    given as an argument clinic notation.

    Argument clinic is part of CPython and used for all the functions that are
    implemented in C (Python 3.7):

        str.split.__text_signature__
        # Results in: '($self, /, sep=None, maxsplit=-1)'
    """
def iterate_argument_clinic(inference_state, arguments, clinic_string) -> Generator[Incomplete, None, None]:
    """Uses a list with argument clinic information (see PEP 436)."""

class _AbstractArgumentsMixin:
    def unpack(self, funcdef: Incomplete | None = None) -> None: ...
    def get_calling_nodes(self): ...

class AbstractArguments(_AbstractArgumentsMixin):
    context: Incomplete
    argument_node: Incomplete
    trailer: Incomplete

def unpack_arglist(arglist) -> Generator[Incomplete, None, None]: ...

class TreeArguments(AbstractArguments):
    argument_node: Incomplete
    context: Incomplete
    trailer: Incomplete
    def __init__(self, inference_state, context, argument_node, trailer: Incomplete | None = None) -> None:
        """
        :param argument_node: May be an argument_node or a list of nodes.
        """
    @classmethod
    def create_cached(cls, *args, **kwargs): ...
    def unpack(self, funcdef: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
    def iter_calling_names_with_star(self) -> Generator[Incomplete, None, None]: ...
    def get_calling_nodes(self): ...

class ValuesArguments(AbstractArguments):
    def __init__(self, values_list) -> None: ...
    def unpack(self, funcdef: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...

class TreeArgumentsWrapper(_AbstractArgumentsMixin):
    def __init__(self, arguments) -> None: ...
    @property
    def context(self): ...
    @property
    def argument_node(self): ...
    @property
    def trailer(self): ...
    def unpack(self, func: Incomplete | None = None) -> None: ...
    def get_calling_nodes(self): ...
