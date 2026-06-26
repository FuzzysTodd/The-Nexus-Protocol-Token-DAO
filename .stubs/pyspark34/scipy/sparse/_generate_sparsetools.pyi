from _typeshed import Incomplete

BSR_ROUTINES: str
CSC_ROUTINES: str
CSR_ROUTINES: str
OTHER_ROUTINES: str
COMPILATION_UNITS: Incomplete
I_TYPES: Incomplete
T_TYPES: Incomplete
THUNK_TEMPLATE: str
METHOD_TEMPLATE: str
GET_THUNK_CASE_TEMPLATE: str

def newer(source, target):
    """
    Return true if 'source' exists and is more recently modified than
    'target', or if 'source' exists and 'target' doesn't.  Return false if
    both exist and 'target' is the same age or younger than 'source'.
    """
def get_thunk_type_set():
    """
    Get a list containing cartesian product of data types, plus a getter routine.

    Returns
    -------
    i_types : list [(j, I_typenum, None, I_type, None), ...]
         Pairing of index type numbers and the corresponding C++ types,
         and an unique index `j`. This is for routines that are parameterized
         only by I but not by T.
    it_types : list [(j, I_typenum, T_typenum, I_type, T_type), ...]
         Same as `i_types`, but for routines parameterized both by T and I.
    getter_code : str
         C++ code for a function that takes I_typenum, T_typenum and returns
         the unique index corresponding to the lists, or -1 if no match was
         found.

    """
def parse_routine(name, args, types):
    """
    Generate thunk and method code for a given routine.

    Parameters
    ----------
    name : str
        Name of the C++ routine
    args : str
        Argument list specification (in format explained above)
    types : list
        List of types to instantiate, as returned `get_thunk_type_set`

    """
def main() -> None: ...
def write_autogen_blurb(stream) -> None: ...
