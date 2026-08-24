from typing import Any, TypeVar

__all__ = ['get_init_parameters_or_fail', 'serialize', 'serialize_cls', 'basic_unit', 'model_wrapper', 'is_basic_unit', 'is_model_wrapped']

T = TypeVar('T')

def get_init_parameters_or_fail(obj: Any): ...
def serialize(cls, *args, **kwargs):
    """
    To create an serializable instance inline without decorator. For example,

    .. code-block:: python

        self.op = serialize(MyCustomOp, hidden_units=128)
    """
def serialize_cls(cls):
    """
    To create an serializable class.
    """
def basic_unit(cls, basic_unit_tag: bool = True) -> T:
    """
    To wrap a module as a basic unit, is to make it a primitive and stop the engine from digging deeper into it.

    ``basic_unit_tag`` is true by default. If set to false, it will not be explicitly mark as a basic unit, and
    graph parser will continue to parse. Currently, this is to handle a special case in ``nn.Sequential``.

    Although ``basic_unit`` calls ``trace`` in its implementation, it is not for serialization. Rather, it is meant
    to capture the initialization arguments for mutation. Also, graph execution engine will stop digging into the inner
    modules when it reaches a module that is decorated with ``basic_unit``.

    .. code-block:: python

        @basic_unit
        class PrimitiveOp(nn.Module):
            ...
    """
def model_wrapper(cls) -> T:
    """
    Wrap the base model (search space). For example,

    .. code-block:: python

        @model_wrapper
        class MyModel(nn.Module):
            ...

    The wrapper serves two purposes:

    1. Capture the init parameters of python class so that it can be re-instantiated in another process.
    2. Reset uid in namespace so that the auto label counting in each model stably starts from zero.

    Currently, NNI might not complain in simple cases where ``@model_wrapper`` is actually not needed.
    But in future, we might enforce ``@model_wrapper`` to be required for base model.
    """
def is_basic_unit(cls_or_instance) -> bool: ...
def is_model_wrapped(cls_or_instance) -> bool: ...
