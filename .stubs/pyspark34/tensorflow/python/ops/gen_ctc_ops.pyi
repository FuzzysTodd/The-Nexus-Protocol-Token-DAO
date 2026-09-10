from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _CTCBeamSearchDecoderOutput(NamedTuple):
    decoded_indices: Incomplete
    decoded_values: Incomplete
    decoded_shape: Incomplete
    log_probability: Incomplete

def ctc_beam_search_decoder(inputs, sequence_length, beam_width, top_paths, merge_repeated: bool = True, name: Incomplete | None = None):
    '''Performs beam search decoding on the logits given in input.

  A note about the attribute merge_repeated: For the beam search decoder,
  this means that if consecutive entries in a beam are the same, only
  the first of these is emitted.  That is, when the top path is "A B B B B",
  "A B" is returned if merge_repeated = True but "A B B B B" is
  returned if merge_repeated = False.

  Args:
    inputs: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths, size `(batch)`.
    beam_width: An `int` that is `>= 1`.
      A scalar >= 0 (beam search beam width).
    top_paths: An `int` that is `>= 1`.
      A scalar >= 0, <= beam_width (controls output size).
    merge_repeated: An optional `bool`. Defaults to `True`.
      If true, merge repeated classes in output.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (decoded_indices, decoded_values, decoded_shape, log_probability).

    decoded_indices: A list of `top_paths` `Tensor` objects with type `int64`.
    decoded_values: A list of `top_paths` `Tensor` objects with type `int64`.
    decoded_shape: A list of `top_paths` `Tensor` objects with type `int64`.
    log_probability: A `Tensor`. Has the same type as `inputs`.
  '''

CTCBeamSearchDecoder: Incomplete

def ctc_beam_search_decoder_eager_fallback(inputs, sequence_length, beam_width, top_paths, merge_repeated, name, ctx): ...

class _CTCGreedyDecoderOutput(NamedTuple):
    decoded_indices: Incomplete
    decoded_values: Incomplete
    decoded_shape: Incomplete
    log_probability: Incomplete

def ctc_greedy_decoder(inputs, sequence_length, merge_repeated: bool = False, blank_index: int = -1, name: Incomplete | None = None):
    '''Performs greedy decoding on the logits given in inputs.

  A note about the attribute merge_repeated: if enabled, when
  consecutive logits\' maximum indices are the same, only the first of
  these is emitted.  Labeling the blank \'*\', the sequence "A B B * B B"
  becomes "A B B" if merge_repeated = True and "A B B B B" if
  merge_repeated = False.

  Regardless of the value of merge_repeated, if the maximum index of a given
  time and batch corresponds to the blank, index `(num_classes - 1)`, no new
  element is emitted.

  Args:
    inputs: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths, size `(batch_size)`.
    merge_repeated: An optional `bool`. Defaults to `False`.
      If True, merge repeated classes in output.
    blank_index: An optional `int`. Defaults to `-1`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (decoded_indices, decoded_values, decoded_shape, log_probability).

    decoded_indices: A `Tensor` of type `int64`.
    decoded_values: A `Tensor` of type `int64`.
    decoded_shape: A `Tensor` of type `int64`.
    log_probability: A `Tensor`. Has the same type as `inputs`.
  '''

CTCGreedyDecoder: Incomplete

def ctc_greedy_decoder_eager_fallback(inputs, sequence_length, merge_repeated, blank_index, name, ctx): ...

class _CTCLossOutput(NamedTuple):
    loss: Incomplete
    gradient: Incomplete

def ctc_loss(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated: bool = False, ctc_merge_repeated: bool = True, ignore_longer_outputs_than_inputs: bool = False, name: Incomplete | None = None):
    """Calculates the CTC Loss (log probability) for each batch entry.  Also calculates

  the gradient.  This class performs the softmax operation for you, so inputs
  should be e.g. linear projections of outputs by an LSTM.

  Args:
    inputs: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
    labels_indices: A `Tensor` of type `int64`.
      The indices of a `SparseTensor<int32, 2>`.
      `labels_indices(i, :) == [b, t]` means `labels_values(i)` stores the id for
      `(batch b, time t)`.
    labels_values: A `Tensor` of type `int32`.
      The values (labels) associated with the given batch and time.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths (batch).
    preprocess_collapse_repeated: An optional `bool`. Defaults to `False`.
      Scalar, if true then repeated labels are
      collapsed prior to the CTC calculation.
    ctc_merge_repeated: An optional `bool`. Defaults to `True`.
      Scalar.  If set to false, *during* CTC calculation
      repeated non-blank labels will not be merged and are interpreted as
      individual labels.  This is a simplified version of CTC.
    ignore_longer_outputs_than_inputs: An optional `bool`. Defaults to `False`.
      Scalar. If set to true, during CTC
      calculation, items that have longer output sequences than input sequences
      are skipped: they don't contribute to the loss term and have zero-gradient.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (loss, gradient).

    loss: A `Tensor`. Has the same type as `inputs`.
    gradient: A `Tensor`. Has the same type as `inputs`.
  """

CTCLoss: Incomplete

def ctc_loss_eager_fallback(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated, ctc_merge_repeated, ignore_longer_outputs_than_inputs, name, ctx): ...

class _CTCLossV2Output(NamedTuple):
    loss: Incomplete
    gradient: Incomplete

def ctc_loss_v2(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated: bool = False, ctc_merge_repeated: bool = True, ignore_longer_outputs_than_inputs: bool = False, name: Incomplete | None = None):
    """Calculates the CTC Loss (log probability) for each batch entry.  Also calculates

  the gradient.  This class performs the softmax operation for you, so inputs
  should be e.g. linear projections of outputs by an LSTM.

  Args:
    inputs: A `Tensor` of type `float32`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits. Default blank
      label is 0 rather num_classes - 1.
    labels_indices: A `Tensor` of type `int64`.
      The indices of a `SparseTensor<int32, 2>`.
      `labels_indices(i, :) == [b, t]` means `labels_values(i)` stores the id for
      `(batch b, time t)`.
    labels_values: A `Tensor` of type `int32`.
      The values (labels) associated with the given batch and time.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths (batch).
    preprocess_collapse_repeated: An optional `bool`. Defaults to `False`.
      Scalar, if true then repeated labels are
      collapsed prior to the CTC calculation.
    ctc_merge_repeated: An optional `bool`. Defaults to `True`.
      Scalar.  If set to false, *during* CTC calculation
      repeated non-blank labels will not be merged and are interpreted as
      individual labels.  This is a simplified version of CTC.
    ignore_longer_outputs_than_inputs: An optional `bool`. Defaults to `False`.
      Scalar. If set to true, during CTC
      calculation, items that have longer output sequences than input sequences
      are skipped: they don't contribute to the loss term and have zero-gradient.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (loss, gradient).

    loss: A `Tensor` of type `float32`.
    gradient: A `Tensor` of type `float32`.
  """

CTCLossV2: Incomplete

def ctc_loss_v2_eager_fallback(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated, ctc_merge_repeated, ignore_longer_outputs_than_inputs, name, ctx): ...
