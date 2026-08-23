from ._typing import get_args as get_args, get_origin as get_origin
from .models import ArgumentInfo as ArgumentInfo, OptionInfo as OptionInfo, ParamMeta as ParamMeta, ParameterInfo as ParameterInfo
from typing import Any, Callable, Dict, Type

class AnnotatedParamWithDefaultValueError(Exception):
    argument_name: str
    param_type: Type[ParameterInfo]
    def __init__(self, argument_name: str, param_type: Type[ParameterInfo]) -> None: ...

class MixedAnnotatedAndDefaultStyleError(Exception):
    argument_name: str
    annotated_param_type: Type[ParameterInfo]
    default_param_type: Type[ParameterInfo]
    def __init__(self, argument_name: str, annotated_param_type: Type[ParameterInfo], default_param_type: Type[ParameterInfo]) -> None: ...

class MultipleTyperAnnotationsError(Exception):
    argument_name: str
    def __init__(self, argument_name: str) -> None: ...

class DefaultFactoryAndDefaultValueError(Exception):
    argument_name: str
    param_type: Type[ParameterInfo]
    def __init__(self, argument_name: str, param_type: Type[ParameterInfo]) -> None: ...

def get_params_from_function(func: Callable[..., Any]) -> Dict[str, ParamMeta]: ...
