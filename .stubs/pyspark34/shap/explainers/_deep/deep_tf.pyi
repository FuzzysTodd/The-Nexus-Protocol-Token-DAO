from ...utils._exceptions import DimensionError as DimensionError
from .._explainer import Explainer as Explainer
from _typeshed import Incomplete

keras: Incomplete
tf: Incomplete
tf_ops: Incomplete
tf_backprop: Incomplete
tf_execute: Incomplete
tf_gradients_impl: Incomplete

def custom_record_gradient(op_name, inputs, attrs, results):
    ''' This overrides tensorflow.python.eager.backprop._record_gradient.

    We need to override _record_gradient in order to get gradient backprop to
    get called for ResourceGather operations. In order to make this work we
    temporarily "lie" about the input type to prevent the node from getting
    pruned from the gradient backprop process. We then reset the type directly
    afterwards back to what it was (an integer type).
    '''

class TFDeep(Explainer):
    """
    Using tf.gradients to implement the backpropagation was
    inspired by the gradient-based implementation approach proposed by Ancona et al, ICLR 2018. Note
    that this package does not currently use the reveal-cancel rule for ReLu units proposed in DeepLIFT.
    """
    model_inputs: Incomplete
    model_output: Incomplete
    multi_output: bool
    model: Incomplete
    multi_input: bool
    data: Incomplete
    orig_grads: Incomplete
    session: Incomplete
    graph: Incomplete
    learning_phase_ops: Incomplete
    learning_phase_flags: Incomplete
    expected_value: Incomplete
    phi_symbolics: Incomplete
    def __init__(self, model, data, session: Incomplete | None = None, learning_phase_flags: Incomplete | None = None) -> None:
        """ An explainer object for a deep model using a given background dataset.

        Note that the complexity of the method scales linearly with the number of background data
        samples. Passing the entire training dataset as `data` will give very accurate expected
        values, but will be computationally expensive. The variance of the expectation estimates scales by
        roughly 1/sqrt(N) for N background data samples. So 100 samples will give a good estimate,
        and 1000 samples a very good estimate of the expected values.

        Parameters
        ----------
        model : tf.keras.Model or (input : [tf.Operation], output : tf.Operation)
            A keras model object or a pair of TensorFlow operations (or a list and an op) that
            specifies the input and output of the model to be explained. Note that SHAP values
            are specific to a single output value, so you get an explanation for each element of
            the output tensor (which must be a flat rank one vector).

        data : [numpy.array] or [pandas.DataFrame] or function
            The background dataset to use for integrating out features. DeepExplainer integrates
            over all these samples for each explanation. The data passed here must match the input
            operations given to the model. If a function is supplied, it must be a function that
            takes a particular input example and generates the background dataset for that example
        session : None or tensorflow.Session
            The TensorFlow session that has the model we are explaining. If None is passed then
            we do our best to find the right session, first looking for a keras session, then
            falling back to the default TensorFlow session.

        learning_phase_flags : None or list of tensors
            If you have your own custom learning phase flags pass them here. When explaining a prediction
            we need to ensure we are not in training mode, since this changes the behavior of ops like
            batch norm or dropout. If None is passed then we look for tensors in the graph that look like
            learning phase flags (this works for Keras models). Note that we assume all the flags should
            have a value of False during predictions (and hence explanations).

        """
    def phi_symbolic(self, i):
        """ Get the SHAP value computation graph for a given model output.
        """
    def shap_values(self, X, ranked_outputs: Incomplete | None = None, output_rank_order: str = 'max', check_additivity: bool = True): ...
    def run(self, out, model_inputs, X):
        """ Runs the model while also setting the learning phase flags to False.
        """
    def custom_grad(self, op, *grads):
        """ Passes a gradient op creation request to the correct handler.
        """
    def execute_with_overridden_gradients(self, f): ...

def tensors_blocked_by_false(ops):
    """ Follows a set of ops assuming their value is False and find blocked Switch paths.

    This is used to prune away parts of the model graph that are only used during the training
    phase (like dropout, batch norm, etc.).
    """
def backward_walk_ops(start_ops, tensor_blacklist, op_type_blacklist): ...
def forward_walk_ops(start_ops, tensor_blacklist, op_type_blacklist, within_ops): ...
def softmax(explainer, op, *grads):
    """ Just decompose softmax into its components and recurse, we can handle all of them :)

    We assume the 'axis' is the last dimension because the TF codebase swaps the 'axis' to
    the last dimension before the softmax op if 'axis' is not already the last dimension.
    We also don't subtract the max before tf.exp for numerical stability since that might
    mess up the attributions and it seems like TensorFlow doesn't define softmax that way
    (according to the docs)
    """
def maxpool(explainer, op, *grads): ...
def gather(explainer, op, *grads): ...
def linearity_1d_nonlinearity_2d(input_ind0, input_ind1, op_func): ...
def nonlinearity_1d_nonlinearity_2d(input_ind0, input_ind1, op_func): ...
def nonlinearity_1d(input_ind): ...
def nonlinearity_1d_handler(input_ind, explainer, op, *grads): ...
def nonlinearity_2d_handler(input_ind0, input_ind1, op_func, explainer, op, *grads): ...
def linearity_1d(input_ind): ...
def linearity_1d_handler(input_ind, explainer, op, *grads): ...
def linearity_with_excluded(input_inds): ...
def linearity_with_excluded_handler(input_inds, explainer, op, *grads): ...
def passthrough(explainer, op, *grads): ...
def break_dependence(explainer, op, *grads):
    """ This function name is used to break attribution dependence in the graph traversal.

    These operation types may be connected above input data values in the graph but their outputs
    don't depend on the input values (for example they just depend on the shape).
    """

op_handlers: Incomplete
