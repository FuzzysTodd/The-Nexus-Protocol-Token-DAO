from .config import BaseConfig as BaseConfig
from .errors import ConfigError as ConfigError
from .fields import ModelField as ModelField
from .types import ModelOrDc as ModelOrDc
from .typing import AnyCallable as AnyCallable, AnyClassMethod as AnyClassMethod
from .utils import ROOT_KEY as ROOT_KEY, in_ipython as in_ipython
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Iterable, List, Tuple, Type, overload

class Validator:
    func: Incomplete
    pre: Incomplete
    each_item: Incomplete
    always: Incomplete
    check_fields: Incomplete
    skip_on_failure: Incomplete
    def __init__(self, func: AnyCallable, pre: bool = False, each_item: bool = False, always: bool = False, check_fields: bool = False, skip_on_failure: bool = False) -> None: ...
ValidatorCallable = Callable[[ModelOrDc | None, Any, Dict[str, Any], ModelField, Type[BaseConfig]], Any]
ValidatorsList = List[ValidatorCallable]
ValidatorListDict = Dict[str, List[Validator]]
VALIDATOR_CONFIG_KEY: str
ROOT_VALIDATOR_CONFIG_KEY: str

def validator(*fields: str, pre: bool = False, each_item: bool = False, always: bool = False, check_fields: bool = True, whole: bool | None = None, allow_reuse: bool = False) -> Callable[[AnyCallable], 'AnyClassMethod']:
    """
    Decorate methods on the class indicating that they should be used to validate fields
    :param fields: which field(s) the method should be called on
    :param pre: whether or not this validator should be called before the standard validators (else after)
    :param each_item: for complex objects (sets, lists etc.) whether to validate individual elements rather than the
      whole object
    :param always: whether this method and other validators should be called even if the value is missing
    :param check_fields: whether to check that the fields actually exist on the model
    :param allow_reuse: whether to track and raise an error if another validator refers to the decorated function
    """
@overload
def root_validator(_func: AnyCallable) -> AnyClassMethod: ...
@overload
def root_validator(*, pre: bool = False, allow_reuse: bool = False, skip_on_failure: bool = False) -> Callable[[AnyCallable], 'AnyClassMethod']: ...

class ValidatorGroup:
    validators: Incomplete
    used_validators: Incomplete
    def __init__(self, validators: ValidatorListDict) -> None: ...
    def get_validators(self, name: str) -> Dict[str, Validator] | None: ...
    def check_for_unused(self) -> None: ...

def extract_validators(namespace: Dict[str, Any]) -> Dict[str, List[Validator]]: ...
def extract_root_validators(namespace: Dict[str, Any]) -> Tuple[List[AnyCallable], List[Tuple[bool, AnyCallable]]]: ...
def inherit_validators(base_validators: ValidatorListDict, validators: ValidatorListDict) -> ValidatorListDict: ...
def make_generic_validator(validator: AnyCallable) -> ValidatorCallable:
    '''
    Make a generic function which calls a validator with the right arguments.

    Unfortunately other approaches (eg. return a partial of a function that builds the arguments) is slow,
    hence this laborious way of doing things.

    It\'s done like this so validators don\'t all need **kwargs in their signature, eg. any combination of
    the arguments "values", "fields" and/or "config" are permitted.
    '''
def prep_validators(v_funcs: Iterable[AnyCallable]) -> ValidatorsList: ...

all_kwargs: Incomplete

def gather_all_validators(type_: ModelOrDc) -> Dict[str, 'AnyClassMethod']: ...
