__all__ = ['count_blocks', 'estimate_blocksize']

def estimate_blocksize(A, efficiency: float = 0.7):
    """Attempt to determine the blocksize of a sparse matrix

    Returns a blocksize=(r,c) such that
        - A.nnz / A.tobsr( (r,c) ).nnz > efficiency
    """
def count_blocks(A, blocksize):
    """For a given blocksize=(r,c) count the number of occupied
    blocks in a sparse matrix A
    """
