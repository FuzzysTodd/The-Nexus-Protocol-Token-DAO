from keras import backend as backend

class DropoutRNNCellMixin:
    """Object that hold dropout related fields for RNN Cell.

    This class is not a standalone RNN cell. It suppose to be used with a RNN
    cell by multiple inheritance. Any cell that mix with class should have
    following fields:
      dropout: a float number within range [0, 1). The ratio that the input
        tensor need to dropout.
      recurrent_dropout: a float number within range [0, 1). The ratio that the
        recurrent state weights need to dropout.
      _random_generator: A backend.RandomGenerator instance, which will be used
        to produce outputs based on the inputs and dropout rate.
    This object will create and cache created dropout masks, and reuse them for
    the incoming data, so that the same mask is used for every batch input.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def reset_dropout_mask(self) -> None:
        """Reset the cached dropout masks if any.

        This is important for the RNN layer to invoke this in it `call()` method
        so that the cached mask is cleared before calling the `cell.call()`. The
        mask should be cached across the timestep within the same batch, but
        shouldn't be cached between batches. Otherwise it will introduce
        unreasonable bias against certain index of data within the batch.
        """
    def reset_recurrent_dropout_mask(self) -> None:
        """Reset the cached recurrent dropout masks if any.

        This is important for the RNN layer to invoke this in it call() method
        so that the cached mask is cleared before calling the cell.call(). The
        mask should be cached across the timestep within the same batch, but
        shouldn't be cached between batches. Otherwise it will introduce
        unreasonable bias against certain index of data within the batch.
        """
    def get_dropout_mask_for_cell(self, inputs, training, count: int = 1):
        """Get the dropout mask for RNN cell's input.

        It will create mask based on context if there isn't any existing cached
        mask. If a new mask is generated, it will update the cache in the cell.

        Args:
          inputs: The input tensor whose shape will be used to generate dropout
            mask.
          training: Boolean tensor, whether its in training mode, dropout will
            be ignored in non-training mode.
          count: Int, how many dropout mask will be generated. It is useful for
            cell that has internal weights fused together.
        Returns:
          List of mask tensor, generated or cached mask based on context.
        """
    def get_recurrent_dropout_mask_for_cell(self, inputs, training, count: int = 1):
        """Get the recurrent dropout mask for RNN cell.

        It will create mask based on context if there isn't any existing cached
        mask. If a new mask is generated, it will update the cache in the cell.

        Args:
          inputs: The input tensor whose shape will be used to generate dropout
            mask.
          training: Boolean tensor, whether its in training mode, dropout will
            be ignored in non-training mode.
          count: Int, how many dropout mask will be generated. It is useful for
            cell that has internal weights fused together.
        Returns:
          List of mask tensor, generated or cached mask based on context.
        """
