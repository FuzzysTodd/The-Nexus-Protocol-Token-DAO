def create_pass_manager_builder(opt: int = 2, loop_vectorize: bool = False, slp_vectorize: bool = False):
    """
    Create an LLVM pass manager with the desired optimisation level and options.
    """
