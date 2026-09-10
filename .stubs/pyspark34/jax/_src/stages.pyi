import jax
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from jax._src import core as core, source_info_util as source_info_util, traceback_util as traceback_util, tree_util as tree_util, util as util
from jax._src.interpreters import mlir as mlir
from jax._src.lib import xla_client as xc
from jax._src.lib.mlir import ir as ir
from typing import Any, NamedTuple, Protocol

xla_extension: Incomplete
map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
CompilerOptions = dict[str, str | bool]

class Executable(Protocol):
    """Protocol for executables, which a user-facing ``Compiled`` encapsulates."""
    def call(self, *args_flat) -> Sequence[Any]:
        """Execute on the flat list of arguments, returning flat outputs."""
    def input_shardings(self) -> Sequence[jax.sharding.XLACompatibleSharding]:
        """Flat sequence of input shardings.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend,
    compiler, or runtime.
    """
    def output_shardings(self) -> Sequence[jax.sharding.XLACompatibleSharding]:
        """Flat sequence of output shardings.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend,
    compiler, or runtime.
    """
    def as_text(self) -> str:
        """A human-readable text representation of this executable.

    Intended for visualization and debugging purposes. This need not be a valid
    nor reliable serialization. It is relayed directly to external callers.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend,
    compiler, or runtime.
    """
    def cost_analysis(self) -> Any:
        """A summary of execution cost estimates.

    Intended for visualization and debugging purposes. The object output by
    this is some simple data structure that can easily be printed or serialized
    (e.g. nested dicts, lists, and tuples with numeric leaves). However, its
    structure can be arbitrary: it need not be consistent across versions of JAX
    and jaxlib, or even across invocations. It is relayed directly to external
    callers.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend,
    compiler, or runtime.
    """
    def memory_analysis(self) -> Any:
        """A summary of estimated memory requirements.

    Intended for visualization and debugging purposes. The object output by
    this is some simple data structure that can easily be printed or serialized
    (e.g. nested dicts, lists, and tuples with numeric leaves). However, its
    structure can be arbitrary: it need not be consistent across versions of JAX
    and jaxlib, or even across invocations. It is relayed directly to external
    callers.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend,
    compiler, or runtime.
    """
    def runtime_executable(self) -> Any:
        """An arbitrary object representation of this executable.

    Intended for debugging purposes. This need not be a valid nor reliable
    serialization. It is relayed directly to external callers, with no
    guarantee on type, structure, or consistency across invocations.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend or
    compiler.
    """
    def create_cpp_call(self, no_kwargs, in_tree, out_tree) -> Any:
        """Optionally constructs a fast c++ dispatcher."""

class Lowering(Protocol):
    """Protocol for lowerings, which a user-facing ``Lowered`` encapsulates."""
    def compile(self, compiler_options: CompilerOptions | None = None) -> Executable:
        """Compile and return a corresponding ``Executable``."""
    def as_text(self, dialect: str | None = None) -> str:
        """A human-readable text representation of this lowering.

    Intended for visualization and debugging purposes. This need not be a valid
    nor reliable serialization. It is relayed directly to external callers.
    """
    def compiler_ir(self, dialect: str | None = None) -> Any:
        '''An arbitrary object representation of this lowering.

    Intended for debugging purposes. This need not be a valid nor reliable
    serialization. It is relayed directly to external callers, with no
    guarantee on type, structure, or consistency across invocations.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend or
    compiler.

    Args:
      dialect: Optional string specifying a representation dialect
      (e.g. "stablehlo")
    '''
    def cost_analysis(self) -> Any:
        """A summary of execution cost estimates.

    Intended for visualization and debugging purposes. The object output by
    this is some simple data structure that can easily be printed or serialized
    (e.g. nested dicts, lists, and tuples with numeric leaves). However, its
    structure can be arbitrary: it need not be consistent across versions of JAX
    and jaxlib, or even across invocations. It is relayed directly to external
    callers.

    This function estimates execution cost in the absence of compiler
    optimizations, which may drastically affect the cost. For execution cost
    estimates after optimizations, compile this lowering and see
    ``Compiled.cost_analysis``.

    May raise ``NotImplementedError`` if unavailable, e.g. based on backend,
    compiler, or runtime.
    """

class XlaExecutable(Executable):
    def xla_extension_executable(self) -> xc.LoadedExecutable: ...
    def call(self, *args_flat) -> Sequence[Any]: ...
    def input_shardings(self) -> Sequence[jax.sharding.XLACompatibleSharding]: ...
    def output_shardings(self) -> Sequence[jax.sharding.XLACompatibleSharding]: ...
    def as_text(self) -> str: ...
    def cost_analysis(self) -> list[dict[str, float]]: ...
    def memory_analysis(self) -> Any: ...
    def runtime_executable(self) -> Any: ...

class XlaLowering(Lowering):
    """Adapts our various internal XLA-backed computations into a ``Lowering``."""
    compile_args: dict[str, Any]
    def hlo(self) -> xc.XlaComputation:
        """Return an HLO representation of this computation."""
    def mhlo(self) -> ir.Module:
        """Return an MHLO representation of this computation."""
    def stablehlo(self) -> ir.Module:
        """Return a StableHLO representation of this computation."""
    def compile(self, compiler_options: CompilerOptions | None = None) -> Executable: ...
    def as_text(self, dialect: str | None = None) -> str: ...
    def compiler_ir(self, dialect: str | None = None) -> Any: ...
    def cost_analysis(self) -> dict[str, float]: ...

@dataclass
class ArgInfo:
    aval: core.AbstractValue
    donated: bool
    def __init__(self, aval, donated) -> None: ...

class Stage:
    args_info: Any
    @property
    def in_tree(self) -> tree_util.PyTreeDef:
        """Tree structure of the pair (positional arguments, keyword arguments)."""
    @property
    def in_avals(self):
        """Tree of input avals."""
    @property
    def donate_argnums(self):
        """Flat tuple of donated argument indices."""

def make_args_info(in_tree, in_avals, donate_argnums): ...

class CompiledCallParams(NamedTuple):
    executable: Executable
    no_kwargs: bool
    in_tree: tree_util.PyTreeDef
    out_tree: tree_util.PyTreeDef

class Compiled(Stage):
    """Compiled representation of a function specialized to types/values.

  A compiled computation is associated with an executable and the
  remaining information needed to execute it. It also provides a
  common API for querying properties of compiled computations across
  JAX's various compilation paths and backends.
  """
    args_info: Any
    out_tree: tree_util.PyTreeDef
    def __init__(self, executable, args_info, out_tree, no_kwargs: bool = False) -> None: ...
    def as_text(self) -> str | None:
        """A human-readable text representation of this executable.

    Intended for visualization and debugging purposes. This is not a valid nor
    reliable serialization.

    Returns ``None`` if unavailable, e.g. based on backend, compiler, or
    runtime.
    """
    def cost_analysis(self) -> Any | None:
        """A summary of execution cost estimates.

    Intended for visualization and debugging purposes. The object output by
    this is some simple data structure that can easily be printed or serialized
    (e.g. nested dicts, lists, and tuples with numeric leaves). However, its
    structure can be arbitrary: it may be inconsistent across versions of JAX
    and jaxlib, or even across invocations.

    Returns ``None`` if unavailable, e.g. based on backend, compiler, or
    runtime.
    """
    def memory_analysis(self) -> Any | None:
        """A summary of estimated memory requirements.

    Intended for visualization and debugging purposes. The object output by
    this is some simple data structure that can easily be printed or serialized
    (e.g. nested dicts, lists, and tuples with numeric leaves). However, its
    structure can be arbitrary: it may be inconsistent across versions of JAX
    and jaxlib, or even across invocations.

    Returns ``None`` if unavailable, e.g. based on backend, compiler, or
    runtime.
    """
    def runtime_executable(self) -> Any | None:
        """An arbitrary object representation of this executable.

    Intended for debugging purposes. This is not valid nor reliable
    serialization. The output has no guarantee of consistency across
    invocations.

    Returns ``None`` if unavailable, e.g. based on backend, compiler, or
    runtime.
    """
    @property
    def input_shardings(self): ...
    @property
    def output_shardings(self): ...
    @staticmethod
    def call(*args, **kwargs): ...
    def __call__(self, *args, **kwargs): ...

class Lowered(Stage):
    """Lowering of a function specialized to argument types and values.

  A lowering is a computation ready for compilation. This class
  carries a lowering together with the remaining information needed to
  later compile and execute it. It also provides a common API for
  querying properties of lowered computations across JAX's various
  lowering paths (:func:`~jax.jit`, :func:`~jax.pmap`, etc.).
  """
    args_info: Any
    out_tree: tree_util.PyTreeDef
    def __init__(self, lowering: XlaLowering, args_info, out_tree: tree_util.PyTreeDef, no_kwargs: bool = False) -> None: ...
    @classmethod
    def from_flat_info(cls, lowering: XlaLowering, in_tree: tree_util.PyTreeDef, in_avals, donate_argnums: tuple[int, ...], out_tree: tree_util.PyTreeDef, no_kwargs: bool = False):
        """Initialize from flat info (``in_avals`` etc.) and an input PyTreeDef.

    Args:
      in_tree: The ``PyTreeDef`` of (args, kwargs).
      out_tree: The ``PyTreeDef`` of the outputs.
      no_kwargs: If ``True`` the transformation, and the
        ``Compiled`` returned from this object will not support keyword
        arguments (an error will be raised if some are provided).
    """
    def compile(self, compiler_options: CompilerOptions | None = None) -> Compiled:
        """Compile, returning a corresponding ``Compiled`` instance."""
    def as_text(self, dialect: str | None = None) -> str:
        '''A human-readable text representation of this lowering.

    Intended for visualization and debugging purposes. This need not be a valid
    nor reliable serialization. It is relayed directly to external callers.

    Args:
      dialect: Optional string specifying a lowering dialect (e.g. "stablehlo")
    '''
    def compiler_ir(self, dialect: str | None = None) -> Any | None:
        '''An arbitrary object representation of this lowering.

    Intended for debugging purposes. This is not a valid nor reliable
    serialization. The output has no guarantee of consistency across
    invocations.

    Returns ``None`` if unavailable, e.g. based on backend, compiler, or
    runtime.

    Args:
      dialect: Optional string specifying a lowering dialect (e.g. "stablehlo")
    '''
    def cost_analysis(self) -> Any | None:
        """A summary of execution cost estimates.

    Intended for visualization and debugging purposes. The object output by
    this is some simple data structure that can easily be printed or serialized
    (e.g. nested dicts, lists, and tuples with numeric leaves). However, its
    structure can be arbitrary: it may be inconsistent across versions of JAX
    and jaxlib, or even across invocations.

    Returns ``None`` if unavailable, e.g. based on backend, compiler, or
    runtime.
    """

class Wrapped(Protocol):
    """A function ready to be specialized, lowered, and compiled.

  This protocol reflects the output of functions such as
  ``jax.jit``. Calling it results in JIT (just-in-time) lowering,
  compilation, and execution. It can also be explicitly lowered prior
  to compilation, and the result compiled prior to execution.
  """
    def __call__(self, *args, **kwargs):
        """Executes the wrapped function, lowering and compiling as needed."""
    def lower(self, *args, **kwargs) -> Lowered:
        """Lower this function explicitly for the given arguments.

    A lowered function is staged out of Python and translated to a
    compiler's input language, possibly in a backend-dependent
    manner. It is ready for compilation but not yet compiled.

    Returns:
      A ``Lowered`` instance representing the lowering.
    """
