from _typeshed import Incomplete

__all__ = ['Library', 'impl', 'define']

class Library:
    '''
    A class to create libraries that can be used to register new operators or
    override operators in existing libraries from Python.
    A user can optionally pass in a dispatch keyname if they only want to register
    kernels corresponding to only one specific dispatch key.

    To create a library to override operators in an existing library (with name ns), set the kind to "IMPL".
    To create a new library (with name ns) to register new operators, set the kind to "DEF".
    Args:
        ns: library name
        kind: "DEF", "IMPL" (default: "IMPL")
        dispatch_key: PyTorch dispatch key (default: "")
    '''
    m: Incomplete
    ns: Incomplete
    kind: Incomplete
    dispatch_key: Incomplete
    def __init__(self, ns, kind, dispatch_key: str = '') -> None: ...
    def define(self, schema, alias_analysis: str = ''):
        '''Defines a new operator and its semantics in the ns namespace.

        Args:
            schema: function schema to define a new operator.
            alias_analysis (optional): Indicates if the aliasing properties of the operator arguments can be
                                       inferred from the schema (default behavior) or not ("CONSERVATIVE").
        Returns:
            name of the operator as inferred from the schema.

        Example::
            >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_LIBRARY)
            >>> my_lib = Library("foo", "DEF")
            >>> my_lib.define("sum(Tensor self) -> Tensor")
        '''
    def impl(self, op_name, fn, dispatch_key: str = '') -> None:
        '''Registers the function implementation for an operator defined in the library.

        Args:
            op_name: operator name (along with the overload) or OpOverload object.
            fn: function that\'s the operator implementation for the input dispatch key.
            dispatch_key: dispatch key that the input function should be registered for. By default, it uses
                          the dispatch key that the library was created with.

        Example::
            >>> # xdoctest: +SKIP
            >>> my_lib = Library("aten", "IMPL")
            >>> def div_cpu(self, other):
            >>>     return self * (1 / other)
            >>> my_lib.impl("div.Tensor", "CPU")
        '''
    def __del__(self) -> None: ...

def impl(lib, name, dispatch_key: str = ''): ...
def define(lib, schema, alias_analysis: str = ''): ...
