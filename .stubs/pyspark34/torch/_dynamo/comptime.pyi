from .exc import unimplemented as unimplemented
from _typeshed import Incomplete

class ComptimeVar:
    """
    A ComptimeVar represents a Python value, at some particular point
    in time, in the Python code we are symbolically evaluating with
    torchdynamo.  This must be distinguished from a runtime value, as
    at compile-time there are some properties of the variable we
    do not know (for example, if the ComptimeVar represents a Tensor,
    we only know metadata about the tensor; we do NOT know what the
    actual data in the Tensor is.)
    """
    def __init__(self, v) -> None: ...
    def as_proxy(self):
        """
        Returns an fx.Proxy (or tuple/list of fx.Proxy) representing
        this variable in the FX graph we are assembling to pass
        to the user compiler.

        This method only works for variables we actually track in
        the FX graph, aka Tensors (and ints, if you are compiling
        with dynamic shapes).  In particular, if you have a list
        or tuple of tensors, you will get a list/tuple of proxies
        (not a single proxy representing the entire list/tuple).
        """
    def is_proxy(self):
        """
        Returns True if as_proxy() would succeed.
        """
    def as_fake(self):
        '''
        Returns a "fake" value (either a FakeTensor or a SymInt)
        representing the variable in question.  This only works
        for variables that denote Tensor or int.  You can use
        this to query metadata; e.g., v.as_fake().size(0) will
        tell you the compile-time known size of the tensor.

        WARNING: Do NOT mutate the returned tensor.
        '''
    def python_type(self):
        """
        Returns what type(v) would have returned for the variable
        at compile time.
        """
    def as_python_constant(self):
        """
        Returns the Python value this variable would have, but only if it is
        completely known at compile-time (e.g., it is constant).

        WARNING: Do NOT mutate the returned constant.  The returned constant
        may or may not correspond to the actual value this variable may take
        on at runtime; for example, if the variable in question is a constant
        list, we may return a copy of that list.
        """
    def is_python_constant(self):
        """
        Returns True if as_python_constant would succeed.
        """

class ComptimeContext:
    """
    This context class provides access to a public API for Dynamo's internals.
    If there is something here you would find useful that is missing, please
    file a feature request at https://github.com/pytorch/pytorch/
    """
    def __init__(self, tx) -> None: ...
    def get_local(self, name: str, *, stacklevel: int = 0) -> ComptimeVar:
        """
        Retrieve the compile-time known information about a local.
        """
    def graph_break(self, msg: str = 'ComptimeContext.graph_break') -> None:
        """
        Manually trigger a graph break
        """
    def graph(self):
        """
        Retrieve the partially constructed FX graph that would be
        passed to the user compiler after compilation.
        """
    def print_graph(self, *, verbose: bool = True, file: Incomplete | None = None) -> None:
        """
        Print the partially constructed FX graph that would be passed
        to the user compiler after compilation.
        """
    def print_disas(self, *, file: Incomplete | None = None, stacklevel: int = 0) -> None:
        """
        Print the current series of opcodes being executed (not including
        parent frames), including where you are in the particular opcode
        stream.
        """
    def print_value_stack(self, *, file: Incomplete | None = None, stacklevel: int = 0) -> None:
        """
        Print the current Python value stack.  Note that this is NOT the same
        as the traceback; use print_bt() to print that.  Note that at
        stacklevel=0, this will typically be empty, as comptime cannot
        currently be used in an expression context where there would be
        intermediates on the stack.  If you would find this useful, please
        file a bug at https://github.com/pytorch/pytorch/

        NB: Stack grows downwards in our print
        """
    def print_locals(self, *, file: Incomplete | None = None, stacklevel: int = 0) -> None:
        """
        Print all of the locals available in the current context.
        By default this view is very limited; you can get more information
        about any individual local using get_local().
        """
    def print_bt(self, *, file: Incomplete | None = None, stacklevel: int = 0) -> None:
        """
        Print the user code backtrace, starting at the beginning of the
        frame Dynamo started evaluating.  Note that this MAY NOT go all
        the way to the torch.compile invocation, as we may have done
        a graph break and are compiling an intermediate frame as the
        starting point.  If you think the other behavior would be better,
        file a bug at https://github.com/pytorch/pytorch/
        """
    def print_guards(self, *, file: Incomplete | None = None) -> None:
        """
        Print the currently installed guards for the Dynamo context.
        This does NOT include guards associated with variables that
        may or may not be installed in the future if those variables
        are used.
        """

def graph_break(): ...
def print_graph(): ...
def print_disas(*, stacklevel: int = 0): ...
def print_value_stack(*, stacklevel: int = 0): ...
def print_value_stack_and_return(e, *, stacklevel: int = 0): ...
def print_locals(*, stacklevel: int = 0): ...
def print_bt(*, stacklevel: int = 0): ...
def print_guards(): ...
def comptime(fn) -> None:
    """fn gets called at compile time in TorchDynamo, does nothing otherwise"""
