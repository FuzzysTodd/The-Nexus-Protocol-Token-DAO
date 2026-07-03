from _typeshed import Incomplete

torch_float_dtype: Incomplete
torch_integer_dtype: Incomplete

def get_module_by_name(model, module_name):
    """
    Get a module specified by its module name

    Parameters
    ----------
    model : pytorch model
        the pytorch model from which to get its module
    module_name : str
        the name of the required module

    Returns
    -------
    module, module
        the parent module of the required module, the required module
    """
def rand_like_with_shape(shape, ori_t):
    """
    Return a new random tensor like the original
    tensor.
    """
def randomize_tensor(tensor, start: int = 1, end: int = 100) -> None:
    """
    Randomize the target tensor according to the given
    range.
    """

jit_python_code_replacement: Incomplete

def translate_jit_code(code): ...
def python_slice_replace(funcstr):
    """
    translate the torch.slice to the appropriate python str that can be replace
    in the forward function string.

    Parameters
    ----------
    funcstr: str
        the str that calling the torch.slice, for example:
        _8 = torch.slice(attention_mask, 0, 0, 9223372036854775807, 1)

    Returns:
    new_str: str
        the string that should replace the original one
    """
