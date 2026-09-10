import torch
from _typeshed import Incomplete
from nni.common.graph_utils import NodePyGroup
from nni.compression.pytorch.speedup import ModelSpeedup
from typing import Any, Callable, Dict, List

__all__ = ['getattr_python', 'jit_to_python_function', 'num2tensor_python', 'parse_constant', 'slice_python', 'translate_list', 'tupleunpack_python', 'arg_trans_dtype', 'arg_trans_memory_format', 'arg_trans_layout']

def translate_list(list_node: torch._C.Value, speedup: ModelSpeedup = None) -> List:
    """
    Get the list of values from the list construct node.

    Parameters
    ----------
    list_node
        The cpp node of the target list.
    speedup
        The Module speedup module.

    Returns
    -------
    values
        The list of values in the target cpp list node.
    """
def parse_constant(cvalue: torch._C.Value, speedup: ModelSpeedup) -> Any:
    """
    Parse the constant values from this Node

    Parameters
    ----------
    cvalue
        The cpp node of the target constant value.
    speedup
        The Model speedup module.

    Returns
    -------
    value
        The constant values parsed from the node.
    """
def slice_python(node: NodePyGroup, speedup: ModelSpeedup): ...
def tupleunpack_python(_node: NodePyGroup, _speedup: ModelSpeedup) -> Callable | None: ...
def num2tensor_python(_node: NodePyGroup, _speedup: ModelSpeedup): ...
def getattr_python(node: NodePyGroup, _speedup: ModelSpeedup):
    """
    Note: Ops started with Prim:: is not taken as the key node,
    so we directly pass the Cpp node into this funciton.

    Parameters
    ----------
    node
        The cpp node of prim::Getattr
    speedup
        The corresponding speedup object.
    """

class FuncAdapter:
    """
    A function adapter which can reorder arguments.
    It can be initialate with constant argument, and positions of each non-constant
    argument. When called, it can put arguments into correct position, then call the
    function.

    Attributes
    ----------
    func
        The function or method to be called.
    positional
        Positional arguments values. The placeholder is None if it's non-constant.
    keyword
        Keyword arguments values. The placeholder is None if it's non-constant.
    undetermined
        A list of the right positions of arguments.
        Position is an int in positional or a str in keyword.
    special_treat
        A Dict of the positions and methods.
        The values of these positions should be treat by those methods.

    """
    func: Incomplete
    positional: Incomplete
    keyword: Incomplete
    undetermined: Incomplete
    special_treat: Incomplete
    def __init__(self, func: Callable, positional: List[Any], keyword: Dict[str, Any], undetermined: List[int | str], special_treat: Dict[int | str, Callable]) -> None: ...
    def __call__(self, *args): ...

def arg_trans_dtype(ivalue: int | torch.dtype):
    """
    Special process for dtype.
    Torch will transform dtype to an enum in cpp, so the value of dtype we get in jit is an int.
    This function is used to recover the int to torch.dtype in python.

    Parameters
    ----------
    ivalue
        The value of dtype or method to be recovered.

    """
def arg_trans_memory_format(ivalue: int | torch.memory_format):
    """
    Special process for memory_format.
    Torch will transform memory_format to an enum in cpp, so the value of memory_format we get in jit is an int.
    This function is used to recover the int to torch.memory_format in python.

    Parameters
    ----------
    ivalue
        The value of memory_format or method to be recovered.

    """
def arg_trans_layout(ivalue: int | torch.layout):
    """
    Special process for layout.
    Torch will transform layout to an enum in cpp, so the value of layout we get in jit is an int.
    This function is used to recover the int to torch.layout in python.

    Parameters
    ----------
    ivalue
        The value of layout or method to be recovered.

    """
def jit_to_python_function(node: NodePyGroup, speedup: ModelSpeedup) -> FuncAdapter:
    """
    Return a callable object to inference the mask according to the node.op_type.

    Parameters
    ---------
    node
        The target node to inference the mask
    speedup
        The speedup object of the target model.

    Returns
    ------
    func
        Return the translated function that used to inference the mask
        , if current op_type is not supported, then we return None.
    """
