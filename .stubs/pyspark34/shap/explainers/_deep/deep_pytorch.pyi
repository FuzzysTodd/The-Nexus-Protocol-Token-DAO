from .._explainer import Explainer as Explainer
from _typeshed import Incomplete

torch: Incomplete

class PyTorchDeep(Explainer):
    multi_input: bool
    data: Incomplete
    layer: Incomplete
    input_handle: Incomplete
    interim: bool
    interim_inputs_shape: Incomplete
    expected_value: Incomplete
    model: Incomplete
    multi_output: bool
    num_outputs: int
    device: Incomplete
    def __init__(self, model, data) -> None: ...
    target_handle: Incomplete
    def add_target_handle(self, layer) -> None: ...
    def add_handles(self, model, forward_handle, backward_handle):
        """
        Add handles to all non-container layers in the model.
        Recursively for non-container layers
        """
    def remove_attributes(self, model) -> None:
        """
        Removes the x and y attributes which were added by the forward handles
        Recursively searches for non-container layers
        """
    def gradient(self, idx, inputs): ...
    def shap_values(self, X, ranked_outputs: Incomplete | None = None, output_rank_order: str = 'max', check_additivity: bool = False): ...

def deeplift_grad(module, grad_input, grad_output):
    """The backward hook which computes the deeplift
    gradient for an nn.Module
    """
def add_interim_values(module, input, output) -> None:
    """The forward hook used to save interim tensors, detached
    from the graph. Used to calculate the multipliers
    """
def get_target_input(module, input, output) -> None:
    """A forward hook which saves the tensor - attached to its graph.
    Used if we want to explain the interim outputs of a model
    """

failure_case_modules: Incomplete

def deeplift_tensor_grad(grad): ...

complex_module_gradients: Incomplete

def passthrough(module, grad_input, grad_output) -> None:
    """No change made to gradients"""
def maxpool(module, grad_input, grad_output): ...
def linear_1d(module, grad_input, grad_output) -> None:
    """No change made to gradients."""
def nonlinear_1d(module, grad_input, grad_output): ...

op_handler: Incomplete
