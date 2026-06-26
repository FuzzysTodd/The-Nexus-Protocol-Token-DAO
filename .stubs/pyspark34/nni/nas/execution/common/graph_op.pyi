from _typeshed import Incomplete
from typing import Any, Dict, List

__all__ = ['Operation', 'Cell', 'PyTorchOperation', 'TensorFlowOperation']

class Operation:
    '''
    Calculation logic of a graph node.

    The constructor is private. Use `Operation.new()` to create operation object.

    `Operation` is a naive record.
    Do not "mutate" its attributes or store information relate to specific node.
    All complex logic should be implemented in `Node` class.

    Attributes
    ----------
    type
        Operation type name (e.g. Conv2D).
        If it starts with underscore, the "operation" is a special one (e.g. subgraph, input/output).
    parameters
        Arbitrary key-value parameters (e.g. kernel_size).
    '''
    io_names: List[str]
    type: Incomplete
    parameters: Incomplete
    attributes: Incomplete
    def __init__(self, type_name: str, parameters: Dict[str, Any] = {}, _internal: bool = False, attributes: Dict[str, Any] = {}) -> None: ...
    def to_init_code(self, field: str) -> str: ...
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...
    def __bool__(self) -> bool: ...
    @staticmethod
    def new(type_name: str, parameters: Dict[str, Any] = ..., cell_name: str = ..., attributes: Dict[str, Any] = ...) -> Operation: ...
    def __eq__(self, other): ...

class PyTorchOperation(Operation):
    @classmethod
    def to_class_name(cls, type_name) -> str | None: ...
    @classmethod
    def is_functional(cls, type_name) -> bool: ...
    def get_import_pkg(self) -> str | None: ...
    def to_init_code(self, field: str) -> str | None: ...
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str:
        """
        Parameters
        ----------
        field : str
            the name of member submodule
        output : str
            the output name (lvalue) of this line of code
        inputs : List[str]
            variables used in this line of code
        inputs_value : List[Any]
            some variables are actually constant, their real values are recorded in ```inputs_value```.
            if not constant, we simply put None at the corresponding index

        Returns
        -------
        str
            generated code line
        """

class TensorFlowOperation(Operation): ...

class Cell(PyTorchOperation):
    '''
    TODO: this is pytorch cell

    An operation reference to a subgraph.

    Example code:
    ```
        def __init__(...):
            ...
            self.cell = CustomCell(...)
            self.relu = K.layers.ReLU()
            ...

        def forward(...):
            ...
            x = self.cell(x)
            ...
    ```

    In above example, node `self.cell`\'s operation is `Cell(cell_name=\'CustomCell\')`.
    For comparison, `self.relu`\'s operation is `Operation(type=\'ReLU\')`.

    TODO: parameters of subgraph (see `Node` class)

    Attributes
    ----------
    type
        Always "_cell".
    parameters
        A dict with only one item; the key is "cell" and the value is cell\'s name.
    framework
        No real usage. Exists for compatibility with base class.
    '''
    type: str
    cell_name: Incomplete
    parameters: Incomplete
    attributes: Incomplete
    def __init__(self, cell_name: str, parameters: Dict[str, Any] = ..., attributes: Dict[str, Any] = ...) -> None: ...
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class _IOPseudoOperation(Operation):
    """
    This is the pseudo operation used by I/O nodes.
    The benefit is that users no longer need to verify `Node.operation is not None`,
    especially in static type checking.
    """
    io_names: Incomplete
    def __init__(self, type_name: str, io_names: List[str] = ...) -> None: ...
    def to_init_code(self, field: str) -> str: ...
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...
    def __bool__(self) -> bool: ...
