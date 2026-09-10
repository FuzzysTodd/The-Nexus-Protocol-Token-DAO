from .._explanation import Explanation as Explanation
from ..explainers._explainer import Explainer as Explainer
from _typeshed import Incomplete

keras: Incomplete
tf: Incomplete
torch: Incomplete

class Gradient(Explainer):
    """ Explains a model using expected gradients (an extension of integrated gradients).

    Expected gradients an extension of the integrated gradients method (Sundararajan et al. 2017), a
    feature attribution method designed for differentiable models based on an extension of Shapley
    values to infinite player games (Aumann-Shapley values). Integrated gradients values are a bit
    different from SHAP values, and require a single reference value to integrate from. As an adaptation
    to make them approximate SHAP values, expected gradients reformulates the integral as an expectation
    and combines that expectation with sampling reference values from the background dataset. This leads
    to a single combined expectation of gradients that converges to attributions that sum to the
    difference between the expected model output and the current output.

    Examples
    --------
    See :ref:`Gradient Explainer Examples <gradient_explainer_examples>`
    """
    features: Incomplete
    explainer: Incomplete
    def __init__(self, model, data, session: Incomplete | None = None, batch_size: int = 50, local_smoothing: int = 0) -> None:
        """ An explainer object for a differentiable model using a given background dataset.

        Parameters
        ----------
        model : tf.keras.Model, (input : [tf.Tensor], output : tf.Tensor), torch.nn.Module, or a tuple
                (model, layer), where both are torch.nn.Module objects

            For TensorFlow this can be a model object, or a pair of TensorFlow tensors (or a list and
            a tensor) that specifies the input and output of the model to be explained. Note that for
            TensowFlow 2 you must pass a tensorflow function, not a tuple of input/output tensors).

            For PyTorch this can be a nn.Module object (model), or a tuple (model, layer), where both
            are nn.Module objects. The model is an nn.Module object which takes as input a tensor
            (or list of tensors) of shape data, and returns a single dimensional output. If the input
            is a tuple, the returned shap values will be for the input of the layer argument. layer must
            be a layer in the model, i.e. model.conv2.

        data : [numpy.array] or [pandas.DataFrame] or [torch.tensor]
            The background dataset to use for integrating out features. Gradient explainer integrates
            over these samples. The data passed here must match the input tensors given in the
            first argument. Single element lists can be passed unwrapped.
        """
    def __call__(self, X, nsamples: int = 200):
        """ Return an explanation object for the model applied to X.

        Parameters
        ----------
        X : list,
            if framework == 'tensorflow': numpy.array, or pandas.DataFrame
            if framework == 'pytorch': torch.tensor
            A tensor (or list of tensors) of samples (where X.shape[0] == # samples) on which to
            explain the model's output.
        nsamples : int
            number of background samples
        Returns
        -------
        shap.Explanation:
        """
    def shap_values(self, X, nsamples: int = 200, ranked_outputs: Incomplete | None = None, output_rank_order: str = 'max', rseed: Incomplete | None = None, return_variances: bool = False):
        ''' Return the values for the model applied to X.

        Parameters
        ----------
        X : list,
            if framework == \'tensorflow\': numpy.array, or pandas.DataFrame
            if framework == \'pytorch\': torch.tensor
            A tensor (or list of tensors) of samples (where X.shape[0] == # samples) on which to
            explain the model\'s output.

        ranked_outputs : None or int
            If ranked_outputs is None then we explain all the outputs in a multi-output model. If
            ranked_outputs is a positive integer then we only explain that many of the top model
            outputs (where "top" is determined by output_rank_order). Note that this causes a pair
            of values to be returned (shap_values, indexes), where shap_values is a list of numpy arrays
            for each of the output ranks, and indexes is a matrix that tells for each sample which output
            indexes were chosen as "top".

        output_rank_order : "max", "min", "max_abs", or "custom"
            How to order the model outputs when using ranked_outputs, either by maximum, minimum, or
            maximum absolute value. If "custom" Then "ranked_outputs" contains a list of output nodes.

        rseed : None or int
            Seeding the randomness in shap value computation  (background example choice,
            interpolation between current and background example, smoothing).

        Returns
        -------
        array or list
            For a models with a single output this returns a tensor of SHAP values with the same shape
            as X. For a model with multiple outputs this returns a list of SHAP value tensors, each of
            which are the same shape as X. If ranked_outputs is None then this list of tensors matches
            the number of model outputs. If ranked_outputs is a positive integer a pair is returned
            (shap_values, indexes), where shap_values is a list of tensors with a length of
            ranked_outputs, and indexes is a matrix that tells for each sample which output indexes
            were chosen as "top".
        '''

class _TFGradient(Explainer):
    model: Incomplete
    model_inputs: Incomplete
    model_output: Incomplete
    multi_output: bool
    multi_input: bool
    data: Incomplete
    batch_size: Incomplete
    local_smoothing: Incomplete
    session: Incomplete
    graph: Incomplete
    keras_phase_placeholder: Incomplete
    gradients: Incomplete
    def __init__(self, model, data, session: Incomplete | None = None, batch_size: int = 50, local_smoothing: int = 0) -> None: ...
    def gradient(self, i): ...
    def shap_values(self, X, nsamples: int = 200, ranked_outputs: Incomplete | None = None, output_rank_order: str = 'max', rseed: Incomplete | None = None, return_variances: bool = False): ...
    def run(self, out, model_inputs, X): ...

class _PyTorchGradient(Explainer):
    multi_input: bool
    model_inputs: Incomplete
    batch_size: Incomplete
    local_smoothing: Incomplete
    layer: Incomplete
    input_handle: Incomplete
    interim: bool
    data: Incomplete
    model: Incomplete
    multi_output: Incomplete
    gradients: Incomplete
    def __init__(self, model, data, batch_size: int = 50, local_smoothing: int = 0) -> None: ...
    def gradient(self, idx, inputs): ...
    @staticmethod
    def get_interim_input(self, input, output) -> None: ...
    def add_handles(self, layer) -> None: ...
    def shap_values(self, X, nsamples: int = 200, ranked_outputs: Incomplete | None = None, output_rank_order: str = 'max', rseed: Incomplete | None = None, return_variances: bool = False): ...
