from .pre_build_helpers import compile_test_program as compile_test_program

def get_openmp_flag(): ...
def check_openmp_support():
    """Check whether OpenMP test code can be compiled and run"""
