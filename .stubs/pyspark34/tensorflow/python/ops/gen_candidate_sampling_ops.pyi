from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _AllCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Incomplete
    true_expected_count: Incomplete
    sampled_expected_count: Incomplete

def all_candidate_sampler(true_classes, num_true, num_sampled, unique, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Generates labels for candidate sampling with a learned unigram distribution.

  See explanations of candidate sampling and the data formats at
  go/candidate-sampling.

  For each batch, this op picks a single set of sampled candidate labels.

  The advantages of sampling candidates per-batch are simplicity and the
  possibility of efficient dense matrix multiplication. The disadvantage is that
  the sampled candidates must be chosen independently of the context and of the
  true labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      A batch_size * num_true matrix, in which each row contains the
      IDs of the num_true target_classes in the corresponding original label.
    num_true: An `int` that is `>= 1`. Number of true labels per context.
    num_sampled: An `int` that is `>= 1`. Number of candidates to produce.
    unique: A `bool`.
      If unique is true, we sample with rejection, so that all sampled
      candidates in a batch are unique. This requires some approximation to
      estimate the post-rejection sampling probabilities.
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).

    sampled_candidates: A `Tensor` of type `int64`.
    true_expected_count: A `Tensor` of type `float32`.
    sampled_expected_count: A `Tensor` of type `float32`.
  """

AllCandidateSampler: Incomplete

def all_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, seed, seed2, name, ctx): ...

class _ComputeAccidentalHitsOutput(NamedTuple):
    indices: Incomplete
    ids: Incomplete
    weights: Incomplete

def compute_accidental_hits(true_classes, sampled_candidates, num_true, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Computes the ids of the positions in sampled_candidates that match true_labels.

  When doing log-odds NCE, the result of this op should be passed through a
  SparseToDense op, then added to the logits of the sampled candidates. This has
  the effect of 'removing' the sampled labels that match the true labels by
  making the classifier sure that they are sampled labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      The true_classes output of UnpackSparseLabels.
    sampled_candidates: A `Tensor` of type `int64`.
      The sampled_candidates output of CandidateSampler.
    num_true: An `int`. Number of true labels per context.
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (indices, ids, weights).

    indices: A `Tensor` of type `int32`.
    ids: A `Tensor` of type `int64`.
    weights: A `Tensor` of type `float32`.
  """

ComputeAccidentalHits: Incomplete

def compute_accidental_hits_eager_fallback(true_classes, sampled_candidates, num_true, seed, seed2, name, ctx): ...

class _FixedUnigramCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Incomplete
    true_expected_count: Incomplete
    sampled_expected_count: Incomplete

def fixed_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, vocab_file: str = '', distortion: int = 1, num_reserved_ids: int = 0, num_shards: int = 1, shard: int = 0, unigrams=[], seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Generates labels for candidate sampling with a learned unigram distribution.

  A unigram sampler could use a fixed unigram distribution read from a
  file or passed in as an in-memory array instead of building up the distribution
  from data on the fly. There is also an option to skew the distribution by
  applying a distortion power to the weights.

  The vocabulary file should be in CSV-like format, with the last field
  being the weight associated with the word.

  For each batch, this op picks a single set of sampled candidate labels.

  The advantages of sampling candidates per-batch are simplicity and the
  possibility of efficient dense matrix multiplication. The disadvantage is that
  the sampled candidates must be chosen independently of the context and of the
  true labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      A batch_size * num_true matrix, in which each row contains the
      IDs of the num_true target_classes in the corresponding original label.
    num_true: An `int` that is `>= 1`. Number of true labels per context.
    num_sampled: An `int` that is `>= 1`.
      Number of candidates to randomly sample.
    unique: A `bool`.
      If unique is true, we sample with rejection, so that all sampled
      candidates in a batch are unique. This requires some approximation to
      estimate the post-rejection sampling probabilities.
    range_max: An `int` that is `>= 1`.
      The sampler will sample integers from the interval [0, range_max).
    vocab_file: An optional `string`. Defaults to `""`.
      Each valid line in this file (which should have a CSV-like format)
      corresponds to a valid word ID. IDs are in sequential order, starting from
      num_reserved_ids. The last entry in each line is expected to be a value
      corresponding to the count or relative probability. Exactly one of vocab_file
      and unigrams needs to be passed to this op.
    distortion: An optional `float`. Defaults to `1`.
      The distortion is used to skew the unigram probability distribution.
      Each weight is first raised to the distortion\'s power before adding to the
      internal unigram distribution. As a result, distortion = 1.0 gives regular
      unigram sampling (as defined by the vocab file), and distortion = 0.0 gives
      a uniform distribution.
    num_reserved_ids: An optional `int`. Defaults to `0`.
      Optionally some reserved IDs can be added in the range [0,
      ..., num_reserved_ids) by the users. One use case is that a special unknown
      word token is used as ID 0. These IDs will have a sampling probability of 0.
    num_shards: An optional `int` that is `>= 1`. Defaults to `1`.
      A sampler can be used to sample from a subset of the original range
      in order to speed up the whole computation through parallelism. This parameter
      (together with \'shard\') indicates the number of partitions that are being
      used in the overall computation.
    shard: An optional `int` that is `>= 0`. Defaults to `0`.
      A sampler can be used to sample from a subset of the original range
      in order to speed up the whole computation through parallelism. This parameter
      (together with \'num_shards\') indicates the particular partition number of a
      sampler op, when partitioning is being used.
    unigrams: An optional list of `floats`. Defaults to `[]`.
      A list of unigram counts or probabilities, one per ID in sequential
      order. Exactly one of vocab_file and unigrams should be passed to this op.
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).

    sampled_candidates: A `Tensor` of type `int64`.
    true_expected_count: A `Tensor` of type `float32`.
    sampled_expected_count: A `Tensor` of type `float32`.
  '''

FixedUnigramCandidateSampler: Incomplete

def fixed_unigram_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, vocab_file, distortion, num_reserved_ids, num_shards, shard, unigrams, seed, seed2, name, ctx): ...

class _LearnedUnigramCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Incomplete
    true_expected_count: Incomplete
    sampled_expected_count: Incomplete

def learned_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Generates labels for candidate sampling with a learned unigram distribution.

  See explanations of candidate sampling and the data formats at
  go/candidate-sampling.

  For each batch, this op picks a single set of sampled candidate labels.

  The advantages of sampling candidates per-batch are simplicity and the
  possibility of efficient dense matrix multiplication. The disadvantage is that
  the sampled candidates must be chosen independently of the context and of the
  true labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      A batch_size * num_true matrix, in which each row contains the
      IDs of the num_true target_classes in the corresponding original label.
    num_true: An `int` that is `>= 1`. Number of true labels per context.
    num_sampled: An `int` that is `>= 1`.
      Number of candidates to randomly sample.
    unique: A `bool`.
      If unique is true, we sample with rejection, so that all sampled
      candidates in a batch are unique. This requires some approximation to
      estimate the post-rejection sampling probabilities.
    range_max: An `int` that is `>= 1`.
      The sampler will sample integers from the interval [0, range_max).
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).

    sampled_candidates: A `Tensor` of type `int64`.
    true_expected_count: A `Tensor` of type `float32`.
    sampled_expected_count: A `Tensor` of type `float32`.
  """

LearnedUnigramCandidateSampler: Incomplete

def learned_unigram_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...

class _LogUniformCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Incomplete
    true_expected_count: Incomplete
    sampled_expected_count: Incomplete

def log_uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Generates labels for candidate sampling with a log-uniform distribution.

  See explanations of candidate sampling and the data formats at
  go/candidate-sampling.

  For each batch, this op picks a single set of sampled candidate labels.

  The advantages of sampling candidates per-batch are simplicity and the
  possibility of efficient dense matrix multiplication. The disadvantage is that
  the sampled candidates must be chosen independently of the context and of the
  true labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      A batch_size * num_true matrix, in which each row contains the
      IDs of the num_true target_classes in the corresponding original label.
    num_true: An `int` that is `>= 1`. Number of true labels per context.
    num_sampled: An `int` that is `>= 1`.
      Number of candidates to randomly sample.
    unique: A `bool`.
      If unique is true, we sample with rejection, so that all sampled
      candidates in a batch are unique. This requires some approximation to
      estimate the post-rejection sampling probabilities.
    range_max: An `int` that is `>= 1`.
      The sampler will sample integers from the interval [0, range_max).
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).

    sampled_candidates: A `Tensor` of type `int64`.
    true_expected_count: A `Tensor` of type `float32`.
    sampled_expected_count: A `Tensor` of type `float32`.
  """

LogUniformCandidateSampler: Incomplete

def log_uniform_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...

class _ThreadUnsafeUnigramCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Incomplete
    true_expected_count: Incomplete
    sampled_expected_count: Incomplete

def thread_unsafe_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Generates labels for candidate sampling with a learned unigram distribution.

  See explanations of candidate sampling and the data formats at
  go/candidate-sampling.

  For each batch, this op picks a single set of sampled candidate labels.

  The advantages of sampling candidates per-batch are simplicity and the
  possibility of efficient dense matrix multiplication. The disadvantage is that
  the sampled candidates must be chosen independently of the context and of the
  true labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      A batch_size * num_true matrix, in which each row contains the
      IDs of the num_true target_classes in the corresponding original label.
    num_true: An `int` that is `>= 1`. Number of true labels per context.
    num_sampled: An `int` that is `>= 1`.
      Number of candidates to randomly sample.
    unique: A `bool`.
      If unique is true, we sample with rejection, so that all sampled
      candidates in a batch are unique. This requires some approximation to
      estimate the post-rejection sampling probabilities.
    range_max: An `int` that is `>= 1`.
      The sampler will sample integers from the interval [0, range_max).
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).

    sampled_candidates: A `Tensor` of type `int64`.
    true_expected_count: A `Tensor` of type `float32`.
    sampled_expected_count: A `Tensor` of type `float32`.
  """

ThreadUnsafeUnigramCandidateSampler: Incomplete

def thread_unsafe_unigram_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...

class _UniformCandidateSamplerOutput(NamedTuple):
    sampled_candidates: Incomplete
    true_expected_count: Incomplete
    sampled_expected_count: Incomplete

def uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Generates labels for candidate sampling with a uniform distribution.

  See explanations of candidate sampling and the data formats at
  go/candidate-sampling.

  For each batch, this op picks a single set of sampled candidate labels.

  The advantages of sampling candidates per-batch are simplicity and the
  possibility of efficient dense matrix multiplication. The disadvantage is that
  the sampled candidates must be chosen independently of the context and of the
  true labels.

  Args:
    true_classes: A `Tensor` of type `int64`.
      A batch_size * num_true matrix, in which each row contains the
      IDs of the num_true target_classes in the corresponding original label.
    num_true: An `int` that is `>= 1`. Number of true labels per context.
    num_sampled: An `int` that is `>= 1`.
      Number of candidates to randomly sample.
    unique: A `bool`.
      If unique is true, we sample with rejection, so that all sampled
      candidates in a batch are unique. This requires some approximation to
      estimate the post-rejection sampling probabilities.
    range_max: An `int` that is `>= 1`.
      The sampler will sample integers from the interval [0, range_max).
    seed: An optional `int`. Defaults to `0`.
      If either seed or seed2 are set to be non-zero, the random number
      generator is seeded by the given seed.  Otherwise, it is seeded by a
      random seed.
    seed2: An optional `int`. Defaults to `0`.
      An second seed to avoid seed collision.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).

    sampled_candidates: A `Tensor` of type `int64`.
    true_expected_count: A `Tensor` of type `float32`.
    sampled_expected_count: A `Tensor` of type `float32`.
  """

UniformCandidateSampler: Incomplete

def uniform_candidate_sampler_eager_fallback(true_classes, num_true, num_sampled, unique, range_max, seed, seed2, name, ctx): ...
