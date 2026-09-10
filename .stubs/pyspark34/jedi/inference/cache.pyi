from jedi import debug as debug

def inference_state_function_cache(default=...): ...
def inference_state_method_cache(default=...): ...
def inference_state_as_method_param_cache(): ...

class CachedMetaClass(type):
    """
    This is basically almost the same than the decorator above, it just caches
    class initializations. Either you do it this way or with decorators, but
    with decorators you lose class access (isinstance, etc).
    """
    def __call__(self, *args, **kwargs): ...

def inference_state_method_generator_cache():
    """
    This is a special memoizer. It memoizes generators and also checks for
    recursion errors and returns no further iterator elemends in that case.
    """
