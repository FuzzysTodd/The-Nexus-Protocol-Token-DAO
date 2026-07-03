from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils
from keras.saving.legacy.saved_model import json_utils as json_utils
from keras.utils import tf_utils as tf_utils
from typing import NamedTuple

class Node:
    """A `Node` describes a layer `__call__()` event.

    A Functional model is a DAG with `Node` instances as nodes, and
    `KerasTensor` instances as edges. Nodes aren't `Layer` instances, because a
    single layer could be called multiple times, which would result in graph
    cycles.

    A `__call__()` event involves input tensors (and other input arguments),
    the layer that was called, and the resulting output tensors.
    A `Node` will include all this information.

    Since a single `Layer` could be called multiple times, the `Node` instances
    are stored on layers as a list. Each time a layer is called a node is added
    to `layer._inbound_nodes`. Each time the output of a layer is used by
    another layer, a node is added to `layer._outbound_nodes`.

    Every `KerasTensor` instance has a `KerasHistory` object attached,
    which tracks the `Node` that records the `__call__()` event that created
    the tensor. By recursively walking through `Node` instances
    via the `KerasHistory` metadata of `KerasTensor` instances, once can
    retrieve the entire DAG of a Functional model.

    Args:
        layer: The layer that was called in the `Layer.__call__()`
          event that this node represents.
        call_args: The positional arguments the layer was called with.
        call_kwargs: The keyword arguments the layer was called with.
        outputs: The output tensors of the `Layer.__call__()`
    """
    layer: Incomplete
    is_input: Incomplete
    outputs: Incomplete
    call_args: Incomplete
    call_kwargs: Incomplete
    flat_input_ids: Incomplete
    flat_output_ids: Incomplete
    def __init__(self, layer, call_args: Incomplete | None = None, call_kwargs: Incomplete | None = None, outputs: Incomplete | None = None) -> None: ...
    @property
    def keras_inputs(self):
        """Tensors input to this node that can be traced back to a
        `keras.Input`."""
    @property
    def parent_nodes(self):
        """Returns all the `Node`s whose output this node immediately depends
        on."""
    def iterate_inbound(self) -> Generator[Incomplete, None, None]:
        """Yields tuples representing the data inbound from other nodes.

        Yields:
          tuples like: (inbound_layer, node_index, tensor_index, tensor).
        """
    def map_arguments(self, tensor_dict):
        """Maps Keras Tensors to computed Tensors using `tensor_dict`."""
    def serialize(self, make_node_key, node_conversion_map):
        """Serializes `Node` for Functional API's `get_config`."""
    @property
    def input_tensors(self): ...
    @property
    def output_tensors(self): ...
    @property
    def input_shapes(self): ...
    @property
    def output_shapes(self): ...
    @property
    def outbound_layer(self): ...
    @property
    def inbound_layers(self):
        """Return all layers that feed into the current node."""

class KerasHistory(NamedTuple('KerasHistory', [('layer', Incomplete), ('node_index', Incomplete), ('tensor_index', Incomplete)])):
    """Tracks the Layer call that created a Tensor, for Keras Graph Networks.

    During construction of Keras Graph Networks, this metadata is added to
    each Tensor produced as the output of a Layer, starting with an
    `InputLayer`. This allows Keras to track how each Tensor was produced, and
    this information is later retraced by the `keras.engine.Network` class to
    reconstruct the Keras Graph Network.

    Attributes:
      layer: The Layer that produced the Tensor.
      node_index: The specific call to the Layer that produced this Tensor.
        Layers can be called multiple times in order to share weights. A new
        node is created every time a Layer is called. The corresponding node
        that represents the call event that produced the Tensor can be found at
        `layer._inbound_nodes[node_index]`.
      tensor_index: The output index for this Tensor. Always zero if the Layer
        that produced this Tensor only has one output. Nested structures of
        Tensors are deterministically assigned an index via `nest.flatten`.
    """

def is_keras_tensor(obj): ...
