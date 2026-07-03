from _typeshed import Incomplete
from tensorflow.python.framework import random_seed as random_seed
from tensorflow.python.ops import array_ops as array_ops, gen_candidate_sampling_ops as gen_candidate_sampling_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: Incomplete | None = None, name: Incomplete | None = None):
    '''Samples a set of classes using a uniform base distribution.

  This operation randomly samples a tensor of sampled classes
  (`sampled_candidates`) from the range of integers `[0, range_max)`.

  See the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf)
  for a quick course on Candidate Sampling.

  The elements of `sampled_candidates` are drawn without replacement
  (if `unique=True`) or with replacement (if `unique=False`) from
  the base distribution.

  The base distribution for this operation is the uniform distribution
  over the range of integers `[0, range_max)`.

  In addition, this operation returns tensors `true_expected_count`
  and `sampled_expected_count` representing the number of times each
  of the target classes (`true_classes`) and the sampled
  classes (`sampled_candidates`) is expected to occur in an average
  tensor of sampled classes. These values correspond to `Q(y|x)`
  defined in the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).
  If `unique=True`, then these are post-rejection probabilities and we
  compute them approximately.

  Note that this function (and also other `*_candidate_sampler`
  functions) only gives you the ingredients to implement the various
  Candidate Sampling algorithms listed in the big table in the
  [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf). You
  still need to implement the algorithms yourself.

  For example, according to that table, the phrase "negative samples"
  may mean different things in different algorithms. For instance, in
  NCE, "negative samples" means `S_i` (which is just the sampled
  classes) which may overlap with true classes, while in Sampled
  Logistic, "negative samples" means `S_i - T_i` which excludes the
  true classes. The return value `sampled_candidates` corresponds to
  `S_i`, not to any specific definition of "negative samples" in any
  specific algorithm. It\'s your responsibility to pick an algorithm
  and calculate the "negative samples" defined by that algorithm
  (e.g. `S_i - T_i`).

  As another example, the `true_classes` argument is for calculating
  the `true_expected_count` output (as a by-product of this function\'s
  main calculation), which may be needed by some algorithms (according
  to that table). It\'s not for excluding true classes in the return
  value `sampled_candidates`. Again that step is algorithm-specific
  and should be carried out by you.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    num_true: An `int`.  The number of target classes per training example.
    num_sampled: An `int`.  The number of classes to randomly sample. The
      `sampled_candidates` return value will have shape `[num_sampled]`. If
      `unique=True`, `num_sampled` must be less than or equal to `range_max`.
    unique: A `bool`. Determines whether all sampled classes in a batch are
      unique.
    range_max: An `int`. The number of possible classes.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    sampled_candidates: A tensor of type `int64` and shape
      `[num_sampled]`. The sampled classes, either with possible
      duplicates (`unique=False`) or all unique (`unique=True`). As
      noted above, `sampled_candidates` may overlap with true classes.
    true_expected_count: A tensor of type `float`.  Same shape as
      `true_classes`. The expected counts under the sampling distribution
      of each of `true_classes`.
    sampled_expected_count: A tensor of type `float`. Same shape as
      `sampled_candidates`. The expected counts under the sampling distribution
      of each of `sampled_candidates`.
  '''
def log_uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: Incomplete | None = None, name: Incomplete | None = None):
    '''Samples a set of classes using a log-uniform (Zipfian) base distribution.

  This operation randomly samples a tensor of sampled classes
  (`sampled_candidates`) from the range of integers `[0, range_max)`.

  See the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf)
  for a quick course on Candidate Sampling.

  The elements of `sampled_candidates` are drawn without replacement
  (if `unique=True`) or with replacement (if `unique=False`) from
  the base distribution.

  The base distribution for this operation is an approximately log-uniform
  or Zipfian distribution:

  `P(class) = (log(class + 2) - log(class + 1)) / log(range_max + 1)`

  This sampler is useful when the target classes approximately follow such
  a distribution - for example, if the classes represent words in a lexicon
  sorted in decreasing order of frequency. If your classes are not ordered by
  decreasing frequency, do not use this op.

  In addition, this operation returns tensors `true_expected_count`
  and `sampled_expected_count` representing the number of times each
  of the target classes (`true_classes`) and the sampled
  classes (`sampled_candidates`) is expected to occur in an average
  tensor of sampled classes.  These values correspond to `Q(y|x)`
  defined in the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).
  If `unique=True`, then these are post-rejection probabilities and we
  compute them approximately.

  Note that this function (and also other `*_candidate_sampler`
  functions) only gives you the ingredients to implement the various
  Candidate Sampling algorithms listed in the big table in the
  [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf). You
  still need to implement the algorithms yourself.

  For example, according to that table, the phrase "negative samples"
  may mean different things in different algorithms. For instance, in
  NCE, "negative samples" means `S_i` (which is just the sampled
  classes) which may overlap with true classes, while in Sampled
  Logistic, "negative samples" means `S_i - T_i` which excludes the
  true classes. The return value `sampled_candidates` corresponds to
  `S_i`, not to any specific definition of "negative samples" in any
  specific algorithm. It\'s your responsibility to pick an algorithm
  and calculate the "negative samples" defined by that algorithm
  (e.g. `S_i - T_i`).

  As another example, the `true_classes` argument is for calculating
  the `true_expected_count` output (as a by-product of this function\'s
  main calculation), which may be needed by some algorithms (according
  to that table). It\'s not for excluding true classes in the return
  value `sampled_candidates`. Again that step is algorithm-specific
  and should be carried out by you.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    num_true: An `int`.  The number of target classes per training example.
    num_sampled: An `int`.  The number of classes to randomly sample.
    unique: A `bool`. Determines whether all sampled classes in a batch are
      unique.
    range_max: An `int`. The number of possible classes.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    sampled_candidates: A tensor of type `int64` and shape
      `[num_sampled]`. The sampled classes. As noted above,
      `sampled_candidates` may overlap with true classes.
    true_expected_count: A tensor of type `float`.  Same shape as
      `true_classes`. The expected counts under the sampling distribution
      of each of `true_classes`.
    sampled_expected_count: A tensor of type `float`. Same shape as
      `sampled_candidates`. The expected counts under the sampling distribution
      of each of `sampled_candidates`.
  '''
def learned_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed: Incomplete | None = None, name: Incomplete | None = None):
    '''Samples a set of classes from a distribution learned during training.

  This operation randomly samples a tensor of sampled classes
  (`sampled_candidates`) from the range of integers `[0, range_max)`.

  See the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf)
  for a quick course on Candidate Sampling.

  The elements of `sampled_candidates` are drawn without replacement
  (if `unique=True`) or with replacement (if `unique=False`) from
  the base distribution.

  The base distribution for this operation is constructed on the fly
  during training.  It is a unigram distribution over the target
  classes seen so far during training.  Every integer in `[0, range_max)`
  begins with a weight of 1, and is incremented by 1 each time it is
  seen as a target class.  The base distribution is not saved to checkpoints,
  so it is reset when the model is reloaded.

  In addition, this operation returns tensors `true_expected_count`
  and `sampled_expected_count` representing the number of times each
  of the target classes (`true_classes`) and the sampled
  classes (`sampled_candidates`) is expected to occur in an average
  tensor of sampled classes.  These values correspond to `Q(y|x)`
  defined in the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).
  If `unique=True`, then these are post-rejection probabilities and we
  compute them approximately.

  Note that this function (and also other `*_candidate_sampler`
  functions) only gives you the ingredients to implement the various
  Candidate Sampling algorithms listed in the big table in the
  [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf). You
  still need to implement the algorithms yourself.

  For example, according to that table, the phrase "negative samples"
  may mean different things in different algorithms. For instance, in
  NCE, "negative samples" means `S_i` (which is just the sampled
  classes) which may overlap with true classes, while in Sampled
  Logistic, "negative samples" means `S_i - T_i` which excludes the
  true classes. The return value `sampled_candidates` corresponds to
  `S_i`, not to any specific definition of "negative samples" in any
  specific algorithm. It\'s your responsibility to pick an algorithm
  and calculate the "negative samples" defined by that algorithm
  (e.g. `S_i - T_i`).

  As another example, the `true_classes` argument is for calculating
  the `true_expected_count` output (as a by-product of this function\'s
  main calculation), which may be needed by some algorithms (according
  to that table). It\'s not for excluding true classes in the return
  value `sampled_candidates`. Again that step is algorithm-specific
  and should be carried out by you.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    num_true: An `int`.  The number of target classes per training example.
    num_sampled: An `int`.  The number of classes to randomly sample.
    unique: A `bool`. Determines whether all sampled classes in a batch are
      unique.
    range_max: An `int`. The number of possible classes.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    sampled_candidates: A tensor of type `int64` and shape
      `[num_sampled]`. The sampled classes. As noted above,
      `sampled_candidates` may overlap with true classes.
    true_expected_count: A tensor of type `float`.  Same shape as
      `true_classes`. The expected counts under the sampling distribution
      of each of `true_classes`.
    sampled_expected_count: A tensor of type `float`. Same shape as
      `sampled_candidates`. The expected counts under the sampling distribution
      of each of `sampled_candidates`.

  '''
def fixed_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, vocab_file: str = '', distortion: float = 1.0, num_reserved_ids: int = 0, num_shards: int = 1, shard: int = 0, unigrams=(), seed: Incomplete | None = None, name: Incomplete | None = None):
    '''Samples a set of classes using the provided (fixed) base distribution.

  This operation randomly samples a tensor of sampled classes
  (`sampled_candidates`) from the range of integers `[0, range_max)`.

  See the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf)
  for a quick course on Candidate Sampling.

  The elements of `sampled_candidates` are drawn without replacement
  (if `unique=True`) or with replacement (if `unique=False`) from
  the base distribution.

  The base distribution is read from a file or passed in as an
  in-memory array. There is also an option to skew the distribution by
  applying a distortion power to the weights.

  In addition, this operation returns tensors `true_expected_count`
  and `sampled_expected_count` representing the number of times each
  of the target classes (`true_classes`) and the sampled
  classes (`sampled_candidates`) is expected to occur in an average
  tensor of sampled classes.  These values correspond to `Q(y|x)`
  defined in the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).
  If `unique=True`, then these are post-rejection probabilities and we
  compute them approximately.

  Note that this function (and also other `*_candidate_sampler`
  functions) only gives you the ingredients to implement the various
  Candidate Sampling algorithms listed in the big table in the
  [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf). You
  still need to implement the algorithms yourself.

  For example, according to that table, the phrase "negative samples"
  may mean different things in different algorithms. For instance, in
  NCE, "negative samples" means `S_i` (which is just the sampled
  classes) which may overlap with true classes, while in Sampled
  Logistic, "negative samples" means `S_i - T_i` which excludes the
  true classes. The return value `sampled_candidates` corresponds to
  `S_i`, not to any specific definition of "negative samples" in any
  specific algorithm. It\'s your responsibility to pick an algorithm
  and calculate the "negative samples" defined by that algorithm
  (e.g. `S_i - T_i`).

  As another example, the `true_classes` argument is for calculating
  the `true_expected_count` output (as a by-product of this function\'s
  main calculation), which may be needed by some algorithms (according
  to that table). It\'s not for excluding true classes in the return
  value `sampled_candidates`. Again that step is algorithm-specific
  and should be carried out by you.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    num_true: An `int`.  The number of target classes per training example.
    num_sampled: An `int`.  The number of classes to randomly sample.
    unique: A `bool`. Determines whether all sampled classes in a batch are
      unique.
    range_max: An `int`. The number of possible classes.
    vocab_file: Each valid line in this file (which should have a CSV-like
      format) corresponds to a valid word ID. IDs are in sequential order,
      starting from num_reserved_ids. The last entry in each line is expected
      to be a value corresponding to the count or relative probability. Exactly
      one of `vocab_file` and `unigrams` needs to be passed to this operation.
    distortion: The distortion is used to skew the unigram probability
      distribution.  Each weight is first raised to the distortion\'s power
      before adding to the internal unigram distribution. As a result,
      `distortion = 1.0` gives regular unigram sampling (as defined by the vocab
      file), and `distortion = 0.0` gives a uniform distribution.
    num_reserved_ids: Optionally some reserved IDs can be added in the range
      `[0, num_reserved_ids)` by the users. One use case is that a special
      unknown word token is used as ID 0. These IDs will have a sampling
      probability of 0.
    num_shards: A sampler can be used to sample from a subset of the original
      range in order to speed up the whole computation through parallelism. This
      parameter (together with `shard`) indicates the number of partitions that
      are being used in the overall computation.
    shard: A sampler can be used to sample from a subset of the original range
      in order to speed up the whole computation through parallelism. This
      parameter (together with `num_shards`) indicates the particular partition
      number of the operation, when partitioning is being used.
    unigrams: A list of unigram counts or probabilities, one per ID in
      sequential order. Exactly one of `vocab_file` and `unigrams` should be
      passed to this operation.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    sampled_candidates: A tensor of type `int64` and shape
      `[num_sampled]`. The sampled classes. As noted above,
      `sampled_candidates` may overlap with true classes.
    true_expected_count: A tensor of type `float`.  Same shape as
      `true_classes`. The expected counts under the sampling distribution
      of each of `true_classes`.
    sampled_expected_count: A tensor of type `float`. Same shape as
      `sampled_candidates`. The expected counts under the sampling distribution
      of each of `sampled_candidates`.

  '''
def all_candidate_sampler(true_classes, num_true, num_sampled, unique, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Generate the set of all classes.

  Deterministically generates and returns the set of all possible classes.
  For testing purposes.  There is no need to use this, since you might as
  well use full softmax or full logistic regression.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    num_true: An `int`.  The number of target classes per training example.
    num_sampled: An `int`.  The number of possible classes.
    unique: A `bool`. Ignored.
      unique.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    sampled_candidates: A tensor of type `int64` and shape `[num_sampled]`.
      This operation deterministically returns the entire range
      `[0, num_sampled]`.
    true_expected_count: A tensor of type `float`.  Same shape as
      `true_classes`. The expected counts under the sampling distribution
      of each of `true_classes`. All returned values are 1.0.
    sampled_expected_count: A tensor of type `float`. Same shape as
      `sampled_candidates`. The expected counts under the sampling distribution
      of each of `sampled_candidates`. All returned values are 1.0.
  """
def compute_accidental_hits(true_classes, sampled_candidates, num_true, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Compute the position ids in `sampled_candidates` matching `true_classes`.

  In Candidate Sampling, this operation facilitates virtually removing
  sampled classes which happen to match target classes.  This is done
  in Sampled Softmax and Sampled Logistic.

  See our [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).

  We presuppose that the `sampled_candidates` are unique.

  We call it an 'accidental hit' when one of the target classes
  matches one of the sampled classes.  This operation reports
  accidental hits as triples `(index, id, weight)`, where `index`
  represents the row number in `true_classes`, `id` represents the
  position in `sampled_candidates`, and weight is `-FLOAT_MAX`.

  The result of this op should be passed through a `sparse_to_dense`
  operation, then added to the logits of the sampled classes. This
  removes the contradictory effect of accidentally sampling the true
  target classes as noise classes for the same example.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    sampled_candidates: A tensor of type `int64` and shape `[num_sampled]`.
      The sampled_candidates output of CandidateSampler.
    num_true: An `int`.  The number of target classes per training example.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    indices: A `Tensor` of type `int32` and shape `[num_accidental_hits]`.
      Values indicate rows in `true_classes`.
    ids: A `Tensor` of type `int64` and shape `[num_accidental_hits]`.
      Values indicate positions in `sampled_candidates`.
    weights: A `Tensor` of type `float` and shape `[num_accidental_hits]`.
      Each value is `-FLOAT_MAX`.

  """
