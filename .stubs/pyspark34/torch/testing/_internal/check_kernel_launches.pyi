from _typeshed import Incomplete

__all__ = ['check_code_for_cuda_kernel_launches', 'check_cuda_kernel_launches']

def check_code_for_cuda_kernel_launches(code, filename: Incomplete | None = None):
    """Checks code for CUDA kernel launches without cuda error checks.

    Args:
        filename - Filename of file containing the code. Used only for display
                   purposes, so you can put anything here.
        code     - The code to check

    Returns:
        The number of unsafe kernel launches in the code
    """
def check_cuda_kernel_launches():
    """Checks all pytorch code for CUDA kernel launches without cuda error checks

    Returns:
        The number of unsafe kernel launches in the codebase
    """
