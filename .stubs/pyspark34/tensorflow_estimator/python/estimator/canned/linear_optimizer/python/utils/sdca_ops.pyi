from _typeshed import Incomplete

class _SparseFeatureColumn:
    """Represents a sparse feature column.

  This is meant to be a more efficient representation than tf.SparseFeature for
  the purpose of SDCA optimization.
  Contains three tensors representing a sparse feature column, they are
  example indices (`int64`), feature indices (`int64`), and feature
  values (`float`).
  Feature weights are optional, and are treated as `1.0f` if missing.

  For example, consider a batch of 4 examples, which contains the following
  features in a particular `_SparseFeatureColumn`:

  * Example 0: feature 5, value 1
  * Example 1: feature 6, value 1 and feature 10, value 0.5
  * Example 2: no features
  * Example 3: two copies of feature 2, value 1

  This _SparseFeatureColumn will be represented as follows:

  ```
   <0, 5,  1>
   <1, 6,  1>
   <1, 10, 0.5>
   <3, 2,  1>
   <3, 2,  1>
  ```

  For a batch of 2 examples below:

  * Example 0: feature 5
  * Example 1: feature 6

  is represented by `_SparseFeatureColumn` as:

  ```
   <0, 5,  1>
   <1, 6,  1>

  ```

  @@__init__
  @@example_indices
  @@feature_indices
  @@feature_values
  """
    def __init__(self, example_indices, feature_indices, feature_values) -> None:
        """Creates a `_SparseFeatureColumn` representation.

    Args:
      example_indices: A 1-D int64 tensor of shape `[N]`. Also, accepts python
        lists, or numpy arrays.
      feature_indices: A 1-D int64 tensor of shape `[N]`. Also, accepts python
        lists, or numpy arrays.
      feature_values: An optional 1-D tensor float tensor of shape `[N]`. Also,
        accepts python lists, or numpy arrays.

    Returns:
      A `_SparseFeatureColumn`
    """
    @property
    def example_indices(self):
        """The example indices represented as a dense tensor.

    Returns:
      A 1-D Tensor of int64 with shape `[N]`.
    """
    @property
    def feature_indices(self):
        """The feature indices represented as a dense tensor.

    Returns:
      A 1-D Tensor of int64 with shape `[N]`.
    """
    @property
    def feature_values(self):
        """The feature values represented as a dense tensor.

    Returns:
      May return None, or a 1-D Tensor of float32 with shape `[N]`.
    """

class _SDCAModel:
    '''Stochastic dual coordinate ascent solver for linear models.

    Loss functions supported:

     * Binary logistic loss
     * Squared loss
     * Hinge loss
     * Smooth hinge loss
     * Poisson log loss

    ### Usage

    ```python
    # Create a solver with the desired parameters.
    lr = _SDCAModel(examples, variables, options)
    min_op = lr.minimize()
    opt_op = lr.update_weights(min_op)

    predictions = lr.predictions(examples)
    # Primal loss + L1 loss + L2 loss.
    regularized_loss = lr.regularized_loss(examples)
    # Primal loss only
    unregularized_loss = lr.unregularized_loss(examples)

    examples: {
      sparse_features: list of SparseFeatureColumn.
      dense_features: list of dense tensors of type float32.
      example_labels: a tensor of type float32 and shape [Num examples]
      example_weights: a tensor of type float32 and shape [Num examples]
      example_ids: a tensor of type string and shape [Num examples]
    }
    variables: {
      sparse_features_weights: list of tensors of shape [vocab size]
      dense_features_weights: list of tensors of shape [dense_feature_dimension]
    }
    options: {
      symmetric_l1_regularization: 0.0
      symmetric_l2_regularization: 1.0
      loss_type: "logistic_loss"
      num_loss_partitions: 1 (Optional, with default value of 1. Number of
      partitions of the global loss function, 1 means single machine solver,
      and >1 when we have more than one optimizer working concurrently.)
      num_table_shards: 1 (Optional, with default value of 1. Number of shards
      of the internal state table, typically set to match the number of
      parameter servers for large data sets.
    }
    ```

    In the training program you will just have to run the returned Op from
    minimize().

    ```python
    # Execute opt_op and train for num_steps.
    for _ in range(num_steps):
      opt_op.run()

    # You can also check for convergence by calling
    lr.approximate_duality_gap()
    ```
  '''
    def __init__(self, examples, variables, options) -> None:
        """Create a new sdca optimizer."""
    def predictions(self, examples):
        """Add operations to compute predictions by the model.

    If logistic_loss is being used, predicted probabilities are returned.
    If poisson_loss is being used, predictions are exponentiated.
    Otherwise, (raw) linear predictions (w*x) are returned.

    Args:
      examples: Examples to compute predictions on.

    Returns:
      An Operation that computes the predictions for examples.

    Raises:
      ValueError: if examples are not well defined.
    """
    def minimize(self, global_step: Incomplete | None = None, name: Incomplete | None = None):
        """Add operations to train a linear model by minimizing the loss function.

    Args:
      global_step: Optional `Variable` to increment by one after the variables
        have been updated.
      name: Optional name for the returned operation.

    Returns:
      An Operation that updates the variables passed in the constructor.
    """
    def update_weights(self, train_op):
        """Updates the model weights.

    This function must be called on at least one worker after `minimize`.
    In distributed training this call can be omitted on non-chief workers to
    speed up training.

    Args:
      train_op: The operation returned by the `minimize` call.

    Returns:
      An Operation that updates the model weights.
    """
    def approximate_duality_gap(self):
        """Add operations to compute the approximate duality gap.

    Returns:
      An Operation that computes the approximate duality gap over all
      examples.
    """
    def unregularized_loss(self, examples):
        """Add operations to compute the loss (without the regularization loss).

    Args:
      examples: Examples to compute unregularized loss on.

    Returns:
      An Operation that computes mean (unregularized) loss for given set of
      examples.

    Raises:
      ValueError: if examples are not well defined.
    """
    def regularized_loss(self, examples):
        """Add operations to compute the loss with regularization loss included.

    Args:
      examples: Examples to compute loss on.

    Returns:
      An Operation that computes mean (regularized) loss for given set of
      examples.
    Raises:
      ValueError: if examples are not well defined.
    """
