from _typeshed import Incomplete
from collections.abc import Generator
from typing import List

UFUNCS_EXTRA_CODE_COMMON: str
UFUNCS_EXTRA_CODE: str
UFUNCS_EXTRA_CODE_BOTTOM: str
CYTHON_SPECIAL_PXD: str
CYTHON_SPECIAL_PYX: str
STUBS: str
BASE_DIR: Incomplete
add_newdocs: Incomplete
CY_TYPES: Incomplete
C_TYPES: Incomplete
TYPE_NAMES: Incomplete
CYTHON_SPECIAL_BENCHFUNCS: Incomplete

def underscore(arg): ...
def cast_order(c): ...

DANGEROUS_DOWNCAST: Incomplete
NAN_VALUE: Incomplete

def generate_loop(func_inputs, func_outputs, func_retval, ufunc_inputs, ufunc_outputs):
    """
    Generate a UFunc loop function that calls a function given as its
    data parameter with the specified input and output arguments and
    return value.

    This function can be passed to PyUFunc_FromFuncAndData.

    Parameters
    ----------
    func_inputs, func_outputs, func_retval : str
        Signature of the function to call, given as type codes of the
        input, output and return value arguments. These 1-character
        codes are given according to the CY_TYPES and TYPE_NAMES
        lists above.

        The corresponding C function signature to be called is:

            retval func(intype1 iv1, intype2 iv2, ..., outtype1 *ov1, ...);

        If len(ufunc_outputs) == len(func_outputs)+1, the return value
        is treated as the first output argument. Otherwise, the return
        value is ignored.

    ufunc_inputs, ufunc_outputs : str
        Ufunc input and output signature.

        This does not have to exactly match the function signature,
        as long as the type casts work out on the C level.

    Returns
    -------
    loop_name
        Name of the generated loop function.
    loop_body
        Generated C code for the loop.

    """
def generate_fused_type(codes):
    """
    Generate name of and cython code for a fused type.

    Parameters
    ----------
    codes : str
        Valid inputs to CY_TYPES (i.e. f, d, g, ...).

    """
def generate_bench(name, codes): ...
def generate_doc(name, specs): ...
def npy_cdouble_from_double_complex(var):
    """Cast a Cython double complex to a NumPy cdouble."""
def double_complex_from_npy_cdouble(var):
    """Cast a NumPy cdouble to a Cython double complex."""
def iter_variants(inputs, outputs) -> Generator[Incomplete, None, None]:
    """
    Generate variants of UFunc signatures, by changing variable types,
    within the limitation that the corresponding C types casts still
    work out.

    This does not generate all possibilities, just the ones required
    for the ufunc to work properly with the most common data types.

    Parameters
    ----------
    inputs, outputs : str
        UFunc input and output signature strings

    Yields
    ------
    new_input, new_output : str
        Modified input and output strings.
        Also the original input/output pair is yielded.

    """

class Func:
    """
    Base class for Ufunc and FusedFunc.

    """
    name: Incomplete
    signatures: Incomplete
    function_name_overrides: Incomplete
    def __init__(self, name, signatures) -> None: ...
    def get_prototypes(self, nptypes_for_h: bool = False): ...
    def cython_func_name(self, c_name, specialized: bool = False, prefix: str = '_func_', override: bool = True): ...

class Ufunc(Func):
    """
    Ufunc signature, restricted format suitable for special functions.

    Parameters
    ----------
    name
        Name of the ufunc to create
    signature
        String of form 'func: fff*ff->f, func2: ddd->*i' describing
        the C-level functions and types of their input arguments
        and return values.

        The syntax is 'function_name: inputparams*outputparams->output_retval*ignored_retval'

    Attributes
    ----------
    name : str
        Python name for the Ufunc
    signatures : list of (func_name, inarg_spec, outarg_spec, ret_spec, header_name)
        List of parsed signatures
    doc : str
        Docstring, obtained from add_newdocs
    function_name_overrides : dict of str->str
        Overrides for the function names in signatures

    """
    doc: Incomplete
    def __init__(self, name, signatures) -> None: ...
    def generate(self, all_loops): ...

class FusedFunc(Func):
    """
    Generate code for a fused-type special function that can be
    cimported in Cython.

    """
    doc: Incomplete
    fused_types: Incomplete
    def __init__(self, name, signatures) -> None: ...
    def generate(self): ...

def get_declaration(ufunc, c_name, c_proto, cy_proto, header, proto_h_filename):
    """
    Construct a Cython declaration of a function coming either from a
    pxd or a header file. Do sufficient tricks to enable compile-time
    type checking against the signature expected by the ufunc.

    """
def generate_ufuncs(fn_prefix, cxx_fn_prefix, ufuncs): ...
def generate_fused_funcs(modname, ufunc_fn_prefix, fused_funcs) -> None: ...
def generate_ufuncs_type_stubs(module_name: str, ufuncs: List[Ufunc]): ...
def unique(lst):
    """
    Return a list without repeated entries (first occurrence is kept),
    preserving order.
    """
def newer(source, target):
    """
    Return true if 'source' exists and is more recently modified than
    'target', or if 'source' exists and 'target' doesn't.  Return false if
    both exist and 'target' is the same age or younger than 'source'.
    """
def all_newer(src_files, dst_files): ...
def main(outdir) -> None: ...
