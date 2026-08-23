from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet, iterator_to_value_set as iterator_to_value_set
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.lazy_value import LazyKnownValues as LazyKnownValues

DOCSTRING_PARAM_PATTERNS: Incomplete
DOCSTRING_RETURN_PATTERNS: Incomplete
REST_ROLE_PATTERN: Incomplete

def infer_param(function_value, param): ...
def infer_return_types(function_value) -> Generator[Incomplete, Incomplete, None]: ...
