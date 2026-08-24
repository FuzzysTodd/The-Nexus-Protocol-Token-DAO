from typing import Any
from typing_extensions import Literal

__all__ = ['create_builtin_class_instance', 'create_customized_class_instance']

def create_builtin_class_instance(builtin_name: str, input_class_args: dict, algo_type: Literal['tuners', 'assessors']) -> Any:
    """Create instance of builtin algorithms

    Parameters
    ----------
    builtin_name: str
        builtin name.
    input_class_args: dict
        kwargs for builtin class constructor
    algo_type: str
        can be one of 'tuners', 'assessors'

    Returns: object
    -------
        Returns builtin class instance.
    """
def create_customized_class_instance(class_params):
    """Create instance of customized algorithms

    Parameters
    ----------
    class_params: dict
        class_params should contains following keys:
            codeDirectory: code directory
            className: qualified class name
            classArgs (optional): kwargs pass to class constructor

    Returns: object
    -------
        Returns customized class instance.
    """
