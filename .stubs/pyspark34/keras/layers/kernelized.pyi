from _typeshed import Incomplete
from keras import initializers as initializers
from keras.engine import base_layer as base_layer, input_spec as input_spec

class RandomFourierFeatures(base_layer.Layer):
    '''Layer that projects its inputs into a random feature space.

    This layer implements a mapping from input space to a space with
    `output_dim` dimensions, which approximates shift-invariant kernels. A
    kernel function `K(x, y)` is shift-invariant if `K(x, y) == k(x - y)` for
    some function `k`.  Many popular Radial Basis Functions (RBF), including
    Gaussian and Laplacian kernels, are shift-invariant.

    The implementation of this layer is based on the following paper:
    ["Random Features for Large-Scale Kernel Machines"](
      https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf)
    by Ali Rahimi and Ben Recht.

    The distribution from which the parameters of the random features map
    (layer) are sampled determines which shift-invariant kernel the layer
    approximates (see paper for more details). You can use the distribution of
    your choice. The layer supports out-of-the-box approximations of the
    following two RBF kernels:

    - Gaussian: `K(x, y) == exp(- square(x - y) / (2 * square(scale)))`
    - Laplacian: `K(x, y) = exp(-abs(x - y) / scale))`

    **Note:** Unlike what is described in the paper and unlike what is used in
    the Scikit-Learn implementation, the output of this layer does not apply
    the `sqrt(2 / D)` normalization factor.

    **Usage:** Typically, this layer is used to "kernelize" linear models by
    applying a non-linear transformation (this layer) to the input features and
    then training a linear model on top of the transformed features. Depending
    on the loss function of the linear model, the composition of this layer and
    the linear model results to models that are equivalent (up to approximation)
    to kernel SVMs (for hinge loss), kernel logistic regression (for logistic
    loss), kernel linear regression (for squared loss), etc.

    Examples:

    A kernel multinomial logistic regression model with Gaussian kernel for
    MNIST:

    ```python
    model = keras.Sequential([
      keras.Input(shape=(784,)),
      RandomFourierFeatures(
          output_dim=4096,
          scale=10.,
          kernel_initializer=\'gaussian\'),
      layers.Dense(units=10, activation=\'softmax\'),
    ])
    model.compile(
        optimizer=\'adam\',
        loss=\'categorical_crossentropy\',
        metrics=[\'categorical_accuracy\']
    )
    ```

    A quasi-SVM classifier for MNIST:

    ```python
    model = keras.Sequential([
      keras.Input(shape=(784,)),
      RandomFourierFeatures(
          output_dim=4096,
          scale=10.,
          kernel_initializer=\'gaussian\'),
      layers.Dense(units=10),
    ])
    model.compile(
        optimizer=\'adam\',
        loss=\'hinge\',
        metrics=[\'categorical_accuracy\']
    )
    ```

    To use another kernel, just replace the layer creation line with:

    ```python
    random_features_layer = RandomFourierFeatures(
        output_dim=500,
        kernel_initializer=<my_initializer>,
        scale=...,
        ...)
    ```

    Args:
      output_dim: Positive integer, the dimension of the layer\'s output, i.e.,
        the number of random features used to approximate the kernel.
      kernel_initializer: Determines the distribution of the parameters of the
        random features map (and therefore the kernel approximated by the
        layer).  It can be either a string identifier or a Keras `Initializer`
        instance.  Currently only \'gaussian\' and \'laplacian\' are supported
        string identifiers (case insensitive). Note that the kernel matrix is
        not trainable.
      scale: For Gaussian and Laplacian kernels, this corresponds to a scaling
        factor of the corresponding kernel approximated by the layer (see
        concrete definitions above). When provided, it should be a positive
        float. If None, a default value is used: if the kernel initializer is
        set to "gaussian", `scale` defaults to `sqrt(input_dim / 2)`, otherwise,
        it defaults to 1.0.  Both the approximation error of the kernel and the
        classification quality are sensitive to this parameter. If `trainable`
        is set to `True`, this parameter is learned end-to-end during training
        and the provided value serves as the initial value.
        **Note:** When features from this layer are fed to a linear model,
          by making `scale` trainable, the resulting optimization problem is
          no longer convex (even if the loss function used by the linear model
          is convex).
      trainable: Whether the scaling parameter of the layer should be trainable.
        Defaults to `False`.
      name: String, name to use for this layer.
    '''
    output_dim: Incomplete
    kernel_initializer: Incomplete
    scale: Incomplete
    def __init__(self, output_dim, kernel_initializer: str = 'gaussian', scale: Incomplete | None = None, trainable: bool = False, name: Incomplete | None = None, **kwargs) -> None: ...
    input_spec: Incomplete
    unscaled_kernel: Incomplete
    bias: Incomplete
    kernel_scale: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
