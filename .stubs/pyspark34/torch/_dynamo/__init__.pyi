from .backends.registry import list_backends as list_backends, register_backend as register_backend
from .convert_frame import replay as replay
from .eval_frame import OptimizedModule as OptimizedModule, assume_constant_result as assume_constant_result, disable as disable, explain as explain, export as export, optimize as optimize, optimize_assert as optimize_assert, run as run, skip as skip
from .external_utils import is_compiling as is_compiling

__all__ = ['allow_in_graph', 'assume_constant_result', 'disallow_in_graph', 'graph_break', 'optimize', 'optimize_assert', 'export', 'explain', 'run', 'replay', 'disable', 'reset', 'skip', 'OptimizedModule', 'is_compiling', 'register_backend', 'list_backends']

def reset() -> None:
    """Clear all compile caches and restore initial state"""
def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.
    ::

        torch._dynamo.allow_in_graph(my_custom_function)

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Will capture a single graph containing `my_custom_function()`.
    """
def disallow_in_graph(fn):
    """
    Customize which functions TorchDynamo will exclude in the generated
    graph and force a graph break on.
    ::

        torch._dynamo.disallow_in_graph(torch.sub)

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = torch.sub(x, 1)
            x = torch.add(x, 1)
            return x

        fn(...)

    Will break the graph on `torch.sub`, and give two graphs each with a
    single `torch.add()` op.
    """
def graph_break() -> None:
    """Force a graph break"""
