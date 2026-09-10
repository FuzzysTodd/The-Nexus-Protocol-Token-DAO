from _typeshed import Incomplete
from torch._jit_internal import Final as Final, Future as Future, export as export, ignore as ignore, is_scripting as is_scripting, unused as unused
from torch.jit._async import fork as fork, wait as wait
from torch.jit._freeze import freeze as freeze, optimize_for_inference as optimize_for_inference, run_frozen_optimizations as run_frozen_optimizations
from torch.jit._fuser import fuser as fuser, last_executed_optimized_graph as last_executed_optimized_graph, optimized_execution as optimized_execution, set_fusion_strategy as set_fusion_strategy
from torch.jit._script import Attribute as Attribute, CompilationUnit as CompilationUnit, RecursiveScriptClass as RecursiveScriptClass, RecursiveScriptModule as RecursiveScriptModule, ScriptFunction as ScriptFunction, ScriptModule as ScriptModule, ScriptWarning as ScriptWarning, interface as interface, script as script, script_method as script_method
from torch.jit._serialization import jit_module_from_flatbuffer as jit_module_from_flatbuffer, load as load, save as save, save_jit_module_to_flatbuffer as save_jit_module_to_flatbuffer
from torch.jit._trace import ONNXTracedModule as ONNXTracedModule, TopLevelTracedModule as TopLevelTracedModule, TracedModule as TracedModule, TracerWarning as TracerWarning, TracingCheckError as TracingCheckError, is_tracing as is_tracing, trace as trace, trace_module as trace_module
from torch.utils import set_module as set_module
from typing import Any

def export_opnames(m):
    """
        Generates new bytecode for a Script module and returns what the op list
        would be for a Script Module based off the current code base. If you
        have a LiteScriptModule and want to get the currently present
        list of ops call _export_operator_list instead.
    """

Error: Incomplete

def annotate(the_type, the_value):
    '''
    This method is a pass-through function that returns `the_value`, used to hint TorchScript
    compiler the type of `the_value`. It is a no-op when running outside of TorchScript.

    Though TorchScript can infer correct type for most Python expressions, there are some cases where
    type inference can be wrong, including:

    - Empty containers like `[]` and `{}`, which TorchScript assumes to be container of `Tensor`
    - Optional types like `Optional[T]` but assigned a valid value of type `T`, TorchScript would assume
      it is type `T` rather than `Optional[T]`

    Note that `annotate()` does not help in `__init__` method of `torch.nn.Module` subclasses because it
    is executed in eager mode. To annotate types of `torch.nn.Module` attributes,
    use :meth:`~torch.jit.Annotate` instead.

    Example:

    .. testcode::

        import torch
        from typing import Dict

        @torch.jit.script
        def fn():
            # Telling TorchScript that this empty dictionary is a (str -> int) dictionary
            # instead of default dictionary type of (str -> Tensor).
            d = torch.jit.annotate(Dict[str, int], {})

            # Without `torch.jit.annotate` above, following statement would fail because of
            # type mismatch.
            d["name"] = 20

    .. testcleanup::

        del fn

    Args:
        the_type: Python type that should be passed to TorchScript compiler as type hint for `the_value`
        the_value: Value or expression to hint type for.

    Returns:
        `the_value` is passed back as return value.
    '''
def script_if_tracing(fn):
    """
    Compiles ``fn`` when it is first called during tracing. ``torch.jit.script``
    has a non-negligible start up time when it is first called due to
    lazy-initializations of many compiler builtins. Therefore you should not use
    it in library code. However, you may want to have parts of your library work
    in tracing even if they use control flow. In these cases, you should use
    ``@torch.jit.script_if_tracing`` to substitute for
    ``torch.jit.script``.

    Args:
        fn: A function to compile.

    Returns:
        If called during tracing, a :class:`ScriptFunction` created by `torch.jit.script` is returned.
        Otherwise, the original function `fn` is returned.
    """
def isinstance(obj, target_type):
    '''
    This function provides for container type refinement in TorchScript. It can refine
    parameterized containers of the List, Dict, Tuple, and Optional types. E.g. ``List[str]``,
    ``Dict[str, List[torch.Tensor]]``, ``Optional[Tuple[int,str,int]]``. It can also
    refine basic types such as bools and ints that are available in TorchScript.

    Args:
        obj: object to refine the type of
        target_type: type to try to refine obj to
    Returns:
        ``bool``: True if obj was successfully refined to the type of target_type,
            False otherwise with no new type refinement


    Example (using ``torch.jit.isinstance`` for type refinement):
    .. testcode::

        import torch
        from typing import Any, Dict, List

        class MyModule(torch.nn.Module):
            def __init__(self):
                super().__init__()

            def forward(self, input: Any): # note the Any type
                if torch.jit.isinstance(input, List[torch.Tensor]):
                    for t in input:
                        y = t.clamp(0, 0.5)
                elif torch.jit.isinstance(input, Dict[str, str]):
                    for val in input.values():
                        print(val)

        m = torch.jit.script(MyModule())
        x = [torch.rand(3,3), torch.rand(4,3)]
        m(x)
        y = {"key1":"val1","key2":"val2"}
        m(y)
    '''

class strict_fusion:
    """
    This class errors if not all nodes have been fused in
    inference, or symbolically differentiated in training.

    Example:

    Forcing fusion of additions.

    .. code-block:: python

        @torch.jit.script
        def foo(x):
            with torch.jit.strict_fusion():
                return x + x + x

    """
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: Any, value: Any, tb: Any) -> None: ...

def enable_onednn_fusion(enabled: bool):
    """
    Enables or disables onednn JIT fusion based on the parameter `enabled`.
    """
def onednn_fusion_enabled():
    """
    Returns whether onednn JIT fusion is enabled
    """
