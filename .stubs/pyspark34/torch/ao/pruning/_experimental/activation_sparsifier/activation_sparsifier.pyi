from _typeshed import Incomplete
from torch import nn
from typing import Any, Dict

__all__ = ['ActivationSparsifier']

class ActivationSparsifier:
    """
    The Activation sparsifier class aims to sparsify/prune activations in a neural
    network. The idea is to attach the sparsifier to a layer (or layers) and it
    zeroes out the activations based on the mask_fn (or sparsification function)
    input by the user.
    The mask_fn is applied once all the inputs are aggregated and reduced i.e.
    mask = mask_fn(reduce_fn(aggregate_fn(activations)))

    Note::
        The sparsification mask is computed on the input **before it goes through the attached layer**.

    Args:
        model (nn.Module):
            The model whose layers will be sparsified. The layers that needs to be
            sparsified should be added separately using the register_layer() function
        aggregate_fn (Optional, Callable):
            default aggregate_fn that is used if not specified while registering the layer.
            specifies how inputs should be aggregated over time.
            The aggregate_fn should usually take 2 torch tensors and return the aggregated tensor.
            Example
                def add_agg_fn(tensor1, tensor2):  return tensor1 + tensor2
                reduce_fn (Optional, Callable):
                    default reduce_fn that is used if not specified while registering the layer.
                    reduce_fn will be called on the aggregated tensor i.e. the tensor obtained after
                    calling agg_fn() on all inputs.
                    Example
                def mean_reduce_fn(agg_tensor):    return agg_tensor.mean(dim=0)
                mask_fn (Optional, Callable):
                    default mask_fn that is used to create the sparsification mask using the tensor obtained after
                    calling the reduce_fn(). This is used by default if a custom one is passed in the
                    register_layer().
                    Note that the mask_fn() definition should contain the sparse arguments that is passed in sparse_config
                    arguments.
                features (Optional, list):
                    default selected features to sparsify.
                    If this is non-empty, then the mask_fn will be applied for each feature of the input.
                    For example,
                mask = [mask_fn(reduce_fn(aggregated_fn(input[feature])) for feature in features]
                feature_dim (Optional, int):
                    default dimension of input features. Again, features along this dim will be chosen
                    for sparsification.
                sparse_config (Dict):
                    Default configuration for the mask_fn. This config will be passed
                    with the mask_fn()

    Example:
        >>> # xdoctest: +SKIP
        >>> model = SomeModel()
        >>> act_sparsifier = ActivationSparsifier(...)  # init activation sparsifier
        >>> # Initialize aggregate_fn
        >>> def agg_fn(x, y):
        >>>     return x + y
        >>>
        >>> # Initialize reduce_fn
        >>> def reduce_fn(x):
        >>>     return torch.mean(x, dim=0)
        >>>
        >>> # Initialize mask_fn
        >>> def mask_fn(data):
        >>>     return torch.eye(data.shape).to(data.device)
        >>>
        >>>
        >>> act_sparsifier.register_layer(model.some_layer, aggregate_fn=agg_fn, reduce_fn=reduce_fn, mask_fn=mask_fn)
        >>>
        >>> # start training process
        >>> for _ in [...]:
        >>>     # epoch starts
        >>>         # model.forward(), compute_loss() and model.backwards()
        >>>     # epoch ends
        >>>     act_sparsifier.step()
        >>> # end training process
        >>> sparsifier.squash_mask()
    """
    model: Incomplete
    defaults: Incomplete
    data_groups: Incomplete
    state: Incomplete
    def __init__(self, model: nn.Module, aggregate_fn: Incomplete | None = None, reduce_fn: Incomplete | None = None, mask_fn: Incomplete | None = None, features: Incomplete | None = None, feature_dim: Incomplete | None = None, **sparse_config) -> None: ...
    def register_layer(self, layer: nn.Module, aggregate_fn: Incomplete | None = None, reduce_fn: Incomplete | None = None, mask_fn: Incomplete | None = None, features: Incomplete | None = None, feature_dim: Incomplete | None = None, **sparse_config):
        """
        Registers a layer for sparsification. The layer should be part of self.model.
        Specifically, registers a pre-forward hook to the layer. The hook will apply the aggregate_fn
        and store the aggregated activations that is input over each step.

        Note::
            - There is no need to pass in the name of the layer as it is automatically computed as per
              the fqn convention.

            - All the functions (fn) passed as argument will be called at a dim, feature level.
        """
    def get_mask(self, name: str = None, layer: nn.Module = None):
        """
        Returns mask associated to the layer.

        The mask is
            - a torch tensor is features for that layer is None.
            - a list of torch tensors for each feature, otherwise

        Note::
            The shape of the mask is unknown until model.forward() is applied.
            Hence, if get_mask() is called before model.forward(), an
            error will be raised.
        """
    def unregister_layer(self, name) -> None:
        """Detaches the sparsifier from the layer
        """
    def step(self) -> None:
        """Internally calls the update_mask() function for each layer
        """
    def update_mask(self, name, data, configs) -> None:
        """
        Called for each registered layer and does the following-
            1. apply reduce_fn on the aggregated activations
            2. use mask_fn to compute the sparsification mask

        Note:
            the reduce_fn and mask_fn is called for each feature, dim over the data
        """
    def squash_mask(self, attach_sparsify_hook: bool = True, **kwargs) -> None:
        """
        Unregisters aggreagate hook that was applied earlier and registers sparsification hooks if
        attach_sparsify_hook = True.
        """
    def state_dict(self) -> Dict[str, Any]:
        """Returns the state of the sparsifier as a :class:`dict`.

        It contains:
        * state - contains name -> mask mapping.
        * data_groups - a dictionary containing all config information for each
            layer
        * defaults - the default config while creating the constructor
        """
    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        """The load_state_dict() restores the state of the sparsifier based on the state_dict

        Args:
        * state_dict - the dictionary that to which the current sparsifier needs to be restored to
        """
    def __get_state__(self) -> Dict[str, Any]: ...
    def __set_state__(self, state: Dict[str, Any]) -> None: ...
