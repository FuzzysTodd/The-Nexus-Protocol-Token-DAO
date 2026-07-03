from .constants import INPUT as INPUT, LABEL2ID as LABEL2ID, OUTPUT as OUTPUT

def nasbench_format_to_architecture_repr(adjacency_matrix, labeling):
    """
    Computes a graph-invariance MD5 hash of the matrix and label pair.
    Imported from NAS-Bench-101 repo.

    Parameters
    ----------
    adjacency_matrix : np.ndarray
        A 2D array of shape NxN, where N is the number of vertices.
        ``matrix[u][v]`` is 1 if there is a direct edge from `u` to `v`,
        otherwise it will be 0.
    labeling : list of str
        A list of str that starts with input and ends with output. The intermediate
        nodes are chosen from candidate operators.

    Returns
    -------
    tuple and int and dict
        Converted number of vertices and architecture.
    """
def infer_num_vertices(architecture):
    """
    Infer number of vertices from an architecture dict.

    Parameters
    ----------
    architecture : dict
        Architecture in NNI format.

    Returns
    -------
    int
        Number of vertices.
    """
def hash_module(architecture, vertices):
    """
    Computes a graph-invariance MD5 hash of the matrix and label pair.
    This snippet is modified from code in NAS-Bench-101 repo.

    Parameters
    ----------
    matrix : np.ndarray
        Square upper-triangular adjacency matrix.
    labeling : list of int
        Labels of length equal to both dimensions of matrix.

    Returns
    -------
    str
        MD5 hash of the matrix and labeling.
    """
