from _typeshed import Incomplete
from torch.onnx import errors as errors
from typing import Callable, Collection, Generic, Sequence, Set

OpsetVersion = int

class OverrideDict(Collection[_K], Generic[_K, _V]):
    """A dictionary that merges built-in and custom symbolic functions.

    It supports overriding and un-overriding built-in symbolic functions with custom
    ones.
    """
    def __init__(self) -> None: ...
    def set_base(self, key: _K, value: _V) -> None: ...
    def in_base(self, key: _K) -> bool:
        """Checks if a key is in the base dictionary."""
    def override(self, key: _K, value: _V) -> None:
        """Overrides a base key-value with a new pair."""
    def remove_override(self, key: _K) -> None:
        """Un-overrides a key-value pair."""
    def overridden(self, key: _K) -> bool:
        """Checks if a key-value pair is overridden."""
    def __getitem__(self, key: _K) -> _V: ...
    def get(self, key: _K, default: _V | None = None): ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...

class _SymbolicFunctionGroup:
    """Different versions of symbolic functions registered to the same name.

    O(number of registered versions of an op) search is performed to find the most
    recent version of the op.

    The registration is delayed until op is used to improve startup time.

    Function overloads with different arguments are not allowed.
    Custom op overrides are supported.
    """
    def __init__(self, name: str) -> None: ...
    def __getitem__(self, key: OpsetVersion) -> Callable: ...
    def get(self, opset: OpsetVersion) -> Callable | None:
        """Find the most recent version of the function."""
    def add(self, func: Callable, opset: OpsetVersion) -> None:
        """Adds a symbolic function.

        Args:
            func: The function to add.
            opset: The opset version of the function to add.
        """
    def add_custom(self, func: Callable, opset: OpsetVersion) -> None:
        """Adds a custom symbolic function.

        Args:
            func: The symbolic function to register.
            opset: The corresponding opset version.
        """
    def remove_custom(self, opset: OpsetVersion) -> None:
        """Removes a custom symbolic function.

        Args:
            opset: The opset version of the custom function to remove.
        """
    def get_min_supported(self) -> OpsetVersion:
        """Returns the lowest built-in opset version supported by the function."""

class SymbolicRegistry:
    """Registry for symbolic functions.

    The registry maintains a mapping from qualified names to symbolic functions.
    It is used to register new symbolic functions and to dispatch calls to
    the appropriate function.
    """
    def __init__(self) -> None: ...
    def register(self, name: str, opset: OpsetVersion, func: Callable, custom: bool = False) -> None:
        """Registers a symbolic function.

        Args:
            name: The qualified name of the function to register. In the form of 'domain::op'.
                E.g. 'aten::add'.
            opset: The opset version of the function to register.
            func: The symbolic function to register.
            custom: Whether the function is a custom function that overrides existing ones.

        Raises:
            ValueError: If the separator '::' is not in the name.
        """
    def unregister(self, name: str, opset: OpsetVersion) -> None:
        """Unregisters a symbolic function.

        Args:
            name: The qualified name of the function to unregister.
            opset: The opset version of the function to unregister.
        """
    def get_function_group(self, name: str) -> _SymbolicFunctionGroup | None:
        """Returns the function group for the given name."""
    def is_registered_op(self, name: str, version: int) -> bool:
        """Returns whether the given op is registered for the given opset version."""
    def all_functions(self) -> Set[str]:
        """Returns the set of all registered function names."""

def onnx_symbolic(name: str, opset: OpsetVersion | Sequence[OpsetVersion], decorate: Sequence[Callable] | None = None, custom: bool = False) -> Callable:
    '''Registers a symbolic function.

    Usage::

    ```
    @onnx_symbolic("aten::symbolic_b", opset=10, decorate=[quantized_aten_handler(scale=1/128, zero_point=0)])
    @symbolic_helper.parse_args("v", "v", "b")
    def symbolic_b(g: _C.Graph, x: _C.Value, y: _C.Value, arg1: bool) -> _C.Value:
        ...
    ```

    Args:
        name: The qualified name of the function in the form of \'domain::op\'.
            E.g. \'aten::add\'.
        opset: The opset versions of the function to register at.
        decorate: A sequence of decorators to apply to the function.
        custom: Whether the function is a custom symbolic function.

    Raises:
        ValueError: If the separator \'::\' is not in the name.
    '''
def custom_onnx_symbolic(name: str, opset: OpsetVersion | Sequence[OpsetVersion], decorate: Sequence[Callable] | None = None) -> Callable:
    """Registers a custom symbolic function.

    Args:
        name: the qualified name of the function.
        opset: the opset version of the function.
        decorate: a sequence of decorators to apply to the function.

    Returns:
        The decorator.

    Raises:
        ValueError: If the separator '::' is not in the name.
    """

registry: Incomplete
