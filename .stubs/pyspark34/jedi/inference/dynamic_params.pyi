from jedi import debug as debug, settings as settings
from jedi.inference import recursion as recursion
from jedi.inference.arguments import TreeArguments as TreeArguments
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.helpers import is_stdlib_path as is_stdlib_path
from jedi.inference.param import get_executed_param_names as get_executed_param_names
from jedi.inference.references import get_module_contexts_containing_name as get_module_contexts_containing_name
from jedi.inference.utils import to_list as to_list
from jedi.inference.value import instance as instance
from jedi.parser_utils import get_parent_scope as get_parent_scope

MAX_PARAM_SEARCHES: int

def dynamic_param_lookup(function_value, param_index):
    '''
    A dynamic search for param values. If you try to complete a type:

    >>> def func(foo):
    ...     foo
    >>> func(1)
    >>> func("")

    It is not known what the type ``foo`` without analysing the whole code. You
    have to look for all calls to ``func`` to find out what ``foo`` possibly
    is.
    '''
