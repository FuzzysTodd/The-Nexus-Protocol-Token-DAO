import inspect
from .typing_utils import get_args as get_args, issubtype as issubtype
from typing import Dict

def ensure_signature_is_compatible(super_callable: _WrappedMethod, sub_callable: _WrappedMethod2, is_static: bool = False) -> None:
    """Ensure that the signature of `sub_callable` is compatible with the signature of `super_callable`.

    Guarantees that any call to `super_callable` will work on `sub_callable` by checking the following criteria:

    1. The return type of `sub_callable` is a subtype of the return type of `super_callable`.
    2. All parameters of `super_callable` are present in `sub_callable`, unless `sub_callable`
       declares `*args` or `**kwargs`.
    3. All positional parameters of `super_callable` appear in the same order in `sub_callable`.
    4. All parameters of `super_callable` are a subtype of the corresponding parameters of `sub_callable`.
    5. All required parameters of `sub_callable` are present in `super_callable`, unless `super_callable`
       declares `*args` or `**kwargs`.

    :param super_callable: Function to check compatibility with.
    :param sub_callable: Function to check compatibility of.
    :param is_static: True if staticmethod and should check first argument.
    """
def ensure_all_kwargs_defined_in_sub(super_sig: inspect.Signature, sub_sig: inspect.Signature, super_type_hints: Dict, sub_type_hints: Dict, check_first_parameter: bool, method_name: str): ...
def ensure_all_positional_args_defined_in_sub(super_sig: inspect.Signature, sub_sig: inspect.Signature, super_type_hints: Dict, sub_type_hints: Dict, check_first_parameter: bool, is_same_main_module: bool, method_name: str): ...
def is_param_defined_in_sub(name: str, sub_has_var_args: bool, sub_has_var_kwargs: bool, sub_sig: inspect.Signature, super_param: inspect.Parameter) -> bool: ...
def ensure_no_extra_args_in_sub(super_sig: inspect.Signature, sub_sig: inspect.Signature, check_first_parameter: bool, method_name: str) -> None: ...
def ensure_return_type_compatibility(super_type_hints: Dict, sub_type_hints: Dict, method_name: str): ...
