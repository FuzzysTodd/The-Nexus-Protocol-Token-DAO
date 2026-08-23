from _typeshed import Incomplete

def is_data_frame(obj): ...
def is_design_matrix(obj): ...
def interpret_data(data, colnames: Incomplete | None = None, rownames: Incomplete | None = None):
    """
    Convert passed data structure to form required by estimation classes

    Parameters
    ----------
    data : array_like
    colnames : sequence or None
        May be part of data structure
    rownames : sequence or None

    Returns
    -------
    (values, colnames, rownames) : (homogeneous ndarray, list)
    """
def struct_to_ndarray(arr): ...
