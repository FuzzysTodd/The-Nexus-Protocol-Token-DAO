import torch
from .graph import Graph
from _typeshed import Incomplete
from torch.fx.operator_schemas import ArgsKwargsPair
from typing import Any, Callable, Dict, List, Tuple

__all__ = ['Node', 'map_arg', 'map_aggregate']

Target = Callable[..., Any] | str

class Node:
    '''
    ``Node`` is the data structure that represents individual operations within
    a ``Graph``. For the most part, Nodes represent callsites to various entities,
    such as operators, methods, and Modules (some exceptions include nodes that
    specify function inputs and outputs). Each ``Node`` has a function specified
    by its ``op`` property. The ``Node`` semantics for each value of ``op`` are as follows:

    - ``placeholder`` represents a function input. The ``name`` attribute specifies the name this value will take on.
      ``target`` is similarly the name of the argument. ``args`` holds either: 1) nothing, or 2) a single argument
      denoting the default parameter of the function input. ``kwargs`` is don\'t-care. Placeholders correspond to
      the function parameters (e.g. ``x``) in the graph printout.
    - ``get_attr`` retrieves a parameter from the module hierarchy. ``name`` is similarly the name the result of the
      fetch is assigned to. ``target`` is the fully-qualified name of the parameter\'s position in the module hierarchy.
      ``args`` and ``kwargs`` are don\'t-care
    - ``call_function`` applies a free function to some values. ``name`` is similarly the name of the value to assign
      to. ``target`` is the function to be applied. ``args`` and ``kwargs`` represent the arguments to the function,
      following the Python calling convention
    - ``call_module`` applies a module in the module hierarchy\'s ``forward()`` method to given arguments. ``name`` is
      as previous. ``target`` is the fully-qualified name of the module in the module hierarchy to call.
      ``args`` and ``kwargs`` represent the arguments to invoke the module on, *excluding the self argument*.
    - ``call_method`` calls a method on a value. ``name`` is as similar. ``target`` is the string name of the method
      to apply to the ``self`` argument. ``args`` and ``kwargs`` represent the arguments to invoke the module on,
      *including the self argument*
    - ``output`` contains the output of the traced function in its ``args[0]`` attribute. This corresponds to the "return" statement
      in the Graph printout.
    '''
    graph: Incomplete
    name: Incomplete
    op: Incomplete
    target: Incomplete
    users: Incomplete
    type: Incomplete
    meta: Incomplete
    def __init__(self, graph: Graph, name: str, op: str, target: Target, args: Tuple['Argument', ...], kwargs: Dict[str, 'Argument'], return_type: Any | None = None) -> None:
        """
        Instantiate an instance of ``Node``. Note: most often, you want to use the
        Graph APIs, i.e. ``Graph.call_module``, ``Graph.call_method``, etc. rather
        than instantiating a ``Node`` directly.

        Args:
            graph (Graph): The ``Graph`` to which this ``Node`` should belong.

            name (str): The name to which the output of this ``Node`` should be assigned

            op (str): The opcode for this ``Node``. Can be one of 'placeholder',
                'call_method', 'call_module', 'call_function', 'get_attr',
                'output'

            target ('Target'): The target this op should call. See the broader
                ``Node`` docstring for more details.

            args (Tuple['Argument']): The args to be passed to ``target``

            kwargs (Dict[str, 'Argument']): The kwargs to be passed to ``target``

            return_type (Optional[Any]): The python type expression representing the
                type of the output of this node. This field can be used for
                annotation of values in the generated code or for other types
                of analyses.
        """
    @property
    def next(self) -> Node:
        """
        Returns the next ``Node`` in the linked list of Nodes.

        Returns:

            The next ``Node`` in the linked list of Nodes.
        """
    @property
    def prev(self) -> Node:
        """
        Returns the previous ``Node`` in the linked list of Nodes.

        Returns:

            The previous ``Node`` in the linked list of Nodes.
        """
    def prepend(self, x: Node) -> None:
        """
        Insert x before this node in the list of nodes in the graph. Example::

            Before: p -> self
                    bx -> x -> ax
            After:  p -> x -> self
                    bx -> ax

        Args:
            x (Node): The node to put before this node. Must be a member of the same graph.
        """
    def append(self, x: Node) -> None:
        """
        Insert ``x`` after this node in the list of nodes in the graph.
        Equivalent to ``self.next.prepend(x)``

        Args:
            x (Node): The node to put after this node. Must be a member of the same graph.
        """
    @property
    def args(self) -> Tuple[Argument, ...]:
        """
        The tuple of arguments to this ``Node``. The interpretation of arguments
        depends on the node's opcode. See the :class:`Node` docstring for more
        information.

        Assignment to this property is allowed. All accounting of uses and users
        is updated automatically on assignment.
        """
    @args.setter
    def args(self, a: Tuple[Argument, ...]):
        """
        Set the tuple of arguments to this Node. The interpretation of arguments
        depends on the node's opcode. See the ``fx.Graph`` docstring for more
        information.
        """
    @property
    def kwargs(self) -> Dict[str, Argument]:
        """
        The dict of keyword arguments to this ``Node``. The interpretation of arguments
        depends on the node's opcode. See the :class:`Node` docstring for more
        information.

        Assignment to this property is allowed. All accounting of uses and users
        is updated automatically on assignment.
        """
    @kwargs.setter
    def kwargs(self, k: Dict[str, Argument]):
        """
        Set the dict of kwargs to this Node. The interpretation of arguments
        depends on the node's opcode. See the ``fx.Graph`` docstring for more
        information.
        """
    @property
    def all_input_nodes(self) -> List['Node']:
        """
        Return all Nodes that are inputs to this Node. This is equivalent to
        iterating over ``args`` and ``kwargs`` and only collecting the values that
        are Nodes.

        Returns:

            List of ``Nodes`` that appear in the ``args`` and ``kwargs`` of this
            ``Node``, in that order.
        """
    def update_arg(self, idx: int, arg: Argument) -> None:
        """
        Update an existing positional argument to contain the new value
        ``arg``. After calling, ``self.args[idx] == arg``.

        Args:

            idx (int): The index into ``self.args`` of the element to update
            arg (Argument): The new argument value to write into ``args``
        """
    def update_kwarg(self, key: str, arg: Argument) -> None:
        """
        Update an existing keyword argument to contain the new value
        ``arg``. After calling, ``self.kwargs[key] == arg``.

        Args:

            key (str): The key in ``self.kwargs`` of the element to update
            arg (Argument): The new argument value to write into ``kwargs``
        """
    @property
    def stack_trace(self) -> str | None:
        """
        Return the Python stack trace that was recorded during tracing, if any.
        This property is usually populated by `Tracer.create_proxy`. To record
        stack traces during tracing for debug purposes, set
        `record_stack_traces = True` on the `Tracer` instance.
        """
    @stack_trace.setter
    def stack_trace(self, trace: str | None): ...
    def format_node(self, placeholder_names: List[str] | None = None, maybe_return_typename: List[str] | None = None) -> str | None:
        """
        Return a descriptive string representation of ``self``.

        This method can be used with no arguments as a debugging
        utility.

        This function is also used internally in the ``__str__`` method
        of ``Graph``. Together, the strings in ``placeholder_names``
        and ``maybe_return_typename`` make up the signature of the
        autogenerated ``forward`` function in this Graph's surrounding
        GraphModule. ``placeholder_names`` and ``maybe_return_typename``
        should not be used otherwise.

        Args:
            placeholder_names: A list that will store formatted strings
                representing the placeholders in the generated
                ``forward`` function. Internal use only.
            maybe_return_typename: A single-element list that will store
                a formatted string representing the output of the
                generated ``forward`` function. Internal use only.

        Returns:
            str: If 1) we're using ``format_node`` as an internal helper
                in the ``__str__`` method of ``Graph``, and 2) ``self``
                is a placeholder Node, return ``None``. Otherwise,
                return a  descriptive string representation of the
                current Node.
        """
    def replace_all_uses_with(self, replace_with: Node, delete_user_cb: Callable[[Node], bool] = ..., *, propagate_meta: bool = False) -> List['Node']:
        """
        Replace all uses of ``self`` in the Graph with the Node ``replace_with``.

        Args:

            replace_with (Node): The node to replace all uses of ``self`` with.
            delete_user_cb (Callable): Callback that is called to determine
              whether a given user of the self node should be removed.
            propagate_meta (bool): Whether or not to copy all properties
              on the .meta field of the original node onto the replacement node.
              For safety, this is only valid to do if the replacement node
              doesn't already have an existing .meta field.

        Returns:

            The list of Nodes on which this change was made.
        """
    def is_impure(self):
        """
        Returns whether this op is impure, i.e. if its op is a placeholder or
        output, or if a call_function or call_module which is impure.

        Returns:

            bool: If the op is impure or not.
        """
    def normalized_arguments(self, root: torch.nn.Module, arg_types: Tuple[Any] | None = None, kwarg_types: Dict[str, Any] | None = None, normalize_to_only_use_kwargs: bool = False) -> ArgsKwargsPair | None:
        """
        Returns normalized arguments to Python targets. This means that
        `args/kwargs` will be matched up to the module/functional's
        signature and return exclusively kwargs in positional order
        if `normalize_to_only_use_kwargs` is true.
        Also populates default values. Does not support positional-only
        parameters or varargs parameters.

        Supports module calls.

        May require `arg_types` and `kwarg_types` in order to disambiguate overloads.

        Args:
            root (torch.nn.Module): Module upon which to resolve module targets.
            arg_types (Optional[Tuple[Any]]): Tuple of arg types for the args
            kwarg_types (Optional[Dict[str, Any]]): Dict of arg types for the kwargs
            normalize_to_only_use_kwargs (bool): Whether to normalize to only use kwargs.

        Returns:

            Returns NamedTuple ArgsKwargsPair, or `None` if not successful.
        """
    def replace_input_with(self, old_input: Node, new_input: Node):
        """
        Loop through input nodes of ``self``, and replace all instances of
        ``old_input`` with ``new_input``.

        Args:

            old_input (Node): The old input node to be replaced.
            new_input (Node): The new input node to replace ``old_input``.
        """

def map_arg(a: Argument, fn: Callable[[Node], Argument]) -> Argument:
    """
    Apply fn to each Node appearing arg. arg may be a list, tuple, slice, or dict with string keys.
    """
def map_aggregate(a: Argument, fn: Callable[[Argument], Argument]) -> Argument:
    """
    Apply fn to each Node appearing arg. arg may be a list, tuple, slice, or dict with string keys.
    """
