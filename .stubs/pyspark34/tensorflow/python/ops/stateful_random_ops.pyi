from _typeshed import Incomplete
from tensorflow.python.distribute import sharded_variable as sharded_variable, values_util as values_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_stateful_random_ops as gen_stateful_random_ops, gen_stateless_random_ops_v2 as gen_stateless_random_ops_v2, math_ops as math_ops, resource_variable_ops as resource_variable_ops, stateless_random_ops as stateless_random_ops, variables as variables
from tensorflow.python.ops.stateless_random_ops import Algorithm as Algorithm
from tensorflow.python.trackable import autotrackable as autotrackable
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

UINT64_HALF_SPAN: Incomplete
MAX_INT64: Incomplete
MIN_INT64: Incomplete
UINT64_SPAN: Incomplete
SEED_TYPE: str
SEED_MIN = MIN_INT64
SEED_MAX = MAX_INT64
SEED_UINT_SPAN = UINT64_SPAN
SEED_TYPE_BITS: int
SEED_BIT_MASK: int
SEED_SIZE: int
STATE_TYPE = SEED_TYPE
ALGORITHM_TYPE = STATE_TYPE
PHILOX_KEY_SIZE: int
THREEFRY_KEY_SIZE: int
PHILOX_COUNTER_SIZE: int
THREEFRY_COUNTER_SIZE: int
PHILOX_STATE_SIZE: Incomplete
THREEFRY_STATE_SIZE: Incomplete
RNG_ALG_PHILOX: Incomplete
RNG_ALG_THREEFRY: Incomplete
DEFAULT_ALGORITHM = RNG_ALG_PHILOX

def non_deterministic_ints(shape, dtype=...):
    """Non-deterministically generates some integers.

  This op may use some OS-provided source of non-determinism (e.g. an RNG), so
  each execution will give different results.

  Args:
    shape: the shape of the result.
    dtype: (optional) the dtype of the result.

  Returns:
    a tensor whose element values are non-deterministically chosen.
  """
def create_rng_state(seed, alg):
    '''Creates a RNG state from an integer or a vector.

  Example:

  >>> tf.random.create_rng_state(
  ...     1234, "philox")
  <tf.Tensor: shape=(3,), dtype=int64, numpy=array([1234,    0,    0])>
  >>> tf.random.create_rng_state(
  ...     [12, 34], "threefry")
  <tf.Tensor: shape=(2,), dtype=int64, numpy=array([12, 34])>

  Args:
    seed: an integer or 1-D numpy array.
    alg: the RNG algorithm. Can be a string, an `Algorithm` or an integer.

  Returns:
    a 1-D numpy array whose size depends on the algorithm.
  '''
def get_replica_id(): ...

class Generator(autotrackable.AutoTrackable):
    '''Random-number generator.

  Example:

  Creating a generator from a seed:

  >>> g = tf.random.Generator.from_seed(1234)
  >>> g.normal(shape=(2, 3))
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
  array([[ 0.9356609 ,  1.0854305 , -0.93788373],
         [-0.5061547 ,  1.3169702 ,  0.7137579 ]], dtype=float32)>

  Creating a generator from a non-deterministic state:

  >>> g = tf.random.Generator.from_non_deterministic_state()
  >>> g.normal(shape=(2, 3))
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=...>

  All the constructors allow explicitly choosing an Random-Number-Generation
  (RNG) algorithm. Supported algorithms are `"philox"` and `"threefry"`. For
  example:

  >>> g = tf.random.Generator.from_seed(123, alg="philox")
  >>> g.normal(shape=(2, 3))
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
  array([[ 0.8673864 , -0.29899067, -0.9310337 ],
         [-1.5828488 ,  1.2481191 , -0.6770643 ]], dtype=float32)>

  CPU, GPU and TPU with the same algorithm and seed will generate the same
  integer random numbers. Float-point results (such as the output of `normal`)
  may have small numerical discrepancies between different devices.

  This class uses a `tf.Variable` to manage its internal state. Every time
  random numbers are generated, the state of the generator will change. For
  example:

  >>> g = tf.random.Generator.from_seed(1234)
  >>> g.state
  <tf.Variable ... numpy=array([1234,    0,    0])>
  >>> g.normal(shape=(2, 3))
  <...>
  >>> g.state
  <tf.Variable ... numpy=array([2770,    0,    0])>

  The shape of the state is algorithm-specific.

  There is also a global generator:

  >>> g = tf.random.get_global_generator()
  >>> g.normal(shape=(2, 3))
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=...>

  When creating a generator inside a `tf.distribute.Strategy` scope, each
  replica will get a different stream of random numbers.

  For example, in this code:

  ```
  strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
  with strat.scope():
    g = tf.random.Generator.from_seed(1)
    def f():
      return g.normal([])
    results = strat.run(f).values
  ```

  `results[0]` and `results[1]` will have different values.

  If the generator is seeded (e.g. created via `Generator.from_seed`), the
  random numbers will be determined by the seed, even though different replicas
  get different numbers.  One can think of a random number generated on a
  replica as a hash of the replica ID and a "master" random number that may be
  common to all replicas. Hence, the whole system is still deterministic.

  (Note that the random numbers on different replicas are not correlated, even
  if they are deterministically determined by the same seed. They are not
  correlated in the sense that no matter what statistics one calculates on them,
  there won\'t be any discernable correlation.)

  Generators can be freely saved and restored using `tf.train.Checkpoint`. The
  checkpoint can be restored in a distribution strategy with a different number
  of replicas than the original strategy. If a replica ID is present in both the
  original and the new distribution strategy, its state will be properly
  restored (i.e. the random-number stream from the restored point will be the
  same as that from the saving point) unless the replicas have already diverged
  in their RNG call traces before saving (e.g. one replica has made one RNG call
  while another has made two RNG calls). We don\'t have such guarantee if the
  generator is saved in a strategy scope and restored outside of any strategy
  scope, or vice versa.

  When a generator is created within the scope of
  `tf.distribute.experimental.ParameterServerStrategy`, the workers
  will share the generator\'s state (placed on one of the parameter
  servers). In this way the workers will still get different
  random-number streams, as stated above. (This is similar to replicas
  in a `tf.distribute.MirroredStrategy` sequentially accessing a
  generator created outside the strategy.) Each RNG call on a worker
  will incur a round-trip to a parameter server, which may have
  performance impacts. When creating a
  `tf.distribute.experimental.ParameterServerStrategy`, please make
  sure that the `variable_partitioner` argument won\'t shard small
  variables of shape `[2]` or `[3]` (because generator states must not
  be sharded). Ways to avoid sharding small variables include setting
  `variable_partitioner` to `None` or to
  `tf.distribute.experimental.partitioners.MinSizePartitioner` with a
  large enough `min_shard_bytes` (see
  `tf.distribute.experimental.ParameterServerStrategy`\'s documentation
  for more details).
  '''
    @classmethod
    def from_state(cls, state, alg):
        """Creates a generator from a state.

    See `__init__` for description of `state` and `alg`.

    Args:
      state: the new state.
      alg: the RNG algorithm.

    Returns:
      The new generator.
    """
    @classmethod
    def from_seed(cls, seed, alg: Incomplete | None = None):
        """Creates a generator from a seed.

    A seed is a 1024-bit unsigned integer represented either as a Python
    integer or a vector of integers. Seeds shorter than 1024-bit will be
    padded. The padding, the internal structure of a seed and the way a seed
    is converted to a state are all opaque (unspecified). The only semantics
    specification of seeds is that two different seeds are likely to produce
    two independent generators (but no guarantee).

    Args:
      seed: the seed for the RNG.
      alg: (optional) the RNG algorithm. If None, it will be auto-selected. See
        `__init__` for its possible values.

    Returns:
      The new generator.
    """
    @classmethod
    def from_non_deterministic_state(cls, alg: Incomplete | None = None):
        """Creates a generator by non-deterministically initializing its state.

    The source of the non-determinism will be platform- and time-dependent.

    Args:
      alg: (optional) the RNG algorithm. If None, it will be auto-selected. See
        `__init__` for its possible values.

    Returns:
      The new generator.
    """
    @classmethod
    def from_key_counter(cls, key, counter, alg):
        '''Creates a generator from a key and a counter.

    This constructor only applies if the algorithm is a counter-based algorithm.
    See method `key` for the meaning of "key" and "counter".

    Args:
      key: the key for the RNG, a scalar of type STATE_TYPE.
      counter: a vector of dtype STATE_TYPE representing the initial counter for
        the RNG, whose length is algorithm-specific.,
      alg: the RNG algorithm. If None, it will be auto-selected. See
        `__init__` for its possible values.

    Returns:
      The new generator.
    '''
    def __init__(self, copy_from: Incomplete | None = None, state: Incomplete | None = None, alg: Incomplete | None = None) -> None:
        '''Creates a generator.

    The new generator will be initialized by one of the following ways, with
    decreasing precedence:
    (1) If `copy_from` is not None, the new generator is initialized by copying
        information from another generator.
    (2) If `state` and `alg` are not None (they must be set together), the new
        generator is initialized by a state.

    Args:
      copy_from: a generator to be copied from.
      state: a vector of dtype STATE_TYPE representing the initial state of the
        RNG, whose length and semantics are algorithm-specific. If it\'s a
        variable, the generator will reuse it instead of creating a new
        variable.
      alg: the RNG algorithm. Possible values are
        `tf.random.Algorithm.PHILOX` for the Philox algorithm and
        `tf.random.Algorithm.THREEFRY` for the ThreeFry algorithm
        (see paper \'Parallel Random Numbers: As Easy as 1, 2, 3\'
        [https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]).
        The string names `"philox"` and `"threefry"` can also be used.
        Note `PHILOX` guarantees the same numbers are produced (given
        the same random state) across all architectures (CPU, GPU, XLA etc).
    '''
    def reset(self, state) -> None:
        '''Resets the generator by a new state.

    See `__init__` for the meaning of "state".

    Args:
      state: the new state.
    '''
    def reset_from_seed(self, seed) -> None:
        '''Resets the generator by a new seed.

    See `from_seed` for the meaning of "seed".

    Args:
      seed: the new seed.
    '''
    def reset_from_key_counter(self, key, counter) -> None:
        '''Resets the generator by a new key-counter pair.

    See `from_key_counter` for the meaning of "key" and "counter".

    Args:
      key: the new key.
      counter: the new counter.
    '''
    @property
    def state(self):
        """The internal state of the RNG."""
    @property
    def algorithm(self):
        """The RNG algorithm id (a Python integer or scalar integer Tensor)."""
    @property
    def key(self):
        """The 'key' part of the state of a counter-based RNG.

    For a counter-base RNG algorithm such as Philox and ThreeFry (as
    described in paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
    [https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]),
    the RNG state consists of two parts: counter and key. The output is
    generated via the formula: output=hash(key, counter), i.e. a hashing of
    the counter parametrized by the key. Two RNGs with two different keys can
    be thought as generating two independent random-number streams (a stream
    is formed by increasing the counter).

    Returns:
      A scalar which is the 'key' part of the state, if the RNG algorithm is
        counter-based; otherwise it raises a ValueError.
    """
    def skip(self, delta):
        """Advance the counter of a counter-based RNG.

    Args:
      delta: the amount of advancement. The state of the RNG after
        `skip(n)` will be the same as that after `normal([n])`
        (or any other distribution). The actual increment added to the
        counter is an unspecified implementation detail.

    Returns:
      A `Tensor` of type `int64`.
    """
    def normal(self, shape, mean: float = 0.0, stddev: float = 1.0, dtype=..., name: Incomplete | None = None):
        """Outputs random values from a normal distribution.

    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output
        tensor.
      mean: A 0-D Tensor or Python value of type `dtype`. The mean of the normal
        distribution.
      stddev: A 0-D Tensor or Python value of type `dtype`. The standard
        deviation of the normal distribution.
      dtype: The type of the output.
      name: A name for the operation (optional).

    Returns:
      A tensor of the specified shape filled with random normal values.
    """
    def truncated_normal(self, shape, mean: float = 0.0, stddev: float = 1.0, dtype=..., name: Incomplete | None = None):
        """Outputs random values from a truncated normal distribution.

    The generated values follow a normal distribution with specified mean and
    standard deviation, except that values whose magnitude is more than
    2 standard deviations from the mean are dropped and re-picked.

    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output
        tensor.
      mean: A 0-D Tensor or Python value of type `dtype`. The mean of the
        truncated normal distribution.
      stddev: A 0-D Tensor or Python value of type `dtype`. The standard
        deviation of the normal distribution, before truncation.
      dtype: The type of the output.
      name: A name for the operation (optional).

    Returns:
      A tensor of the specified shape filled with random truncated normal
        values.
    """
    def uniform(self, shape, minval: int = 0, maxval: Incomplete | None = None, dtype=..., name: Incomplete | None = None):
        """Outputs random values from a uniform distribution.

    The generated values follow a uniform distribution in the range
    `[minval, maxval)`. The lower bound `minval` is included in the range, while
    the upper bound `maxval` is excluded. (For float numbers especially
    low-precision types like bfloat16, because of
    rounding, the result may sometimes include `maxval`.)

    For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
    be specified explicitly.

    In the integer case, the random integers are slightly biased unless
    `maxval - minval` is an exact power of two.  The bias is small for values of
    `maxval - minval` significantly smaller than the range of the output (either
    `2**32` or `2**64`).

    For full-range random integers, pass `minval=None` and `maxval=None` with an
    integer `dtype` (for integer dtypes, `minval` and `maxval` must be both
    `None` or both not `None`).

    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output
        tensor.
      minval: A Tensor or Python value of type `dtype`, broadcastable with
        `shape` (for integer types, broadcasting is not supported, so it needs
        to be a scalar). The lower bound (included) on the range of random
        values to generate. Pass `None` for full-range integers. Defaults to 0.
      maxval: A Tensor or Python value of type `dtype`, broadcastable with
        `shape` (for integer types, broadcasting is not supported, so it needs
        to be a scalar). The upper bound (excluded) on the range of random
        values to generate. Pass `None` for full-range integers. Defaults to 1
        if `dtype` is floating point.
      dtype: The type of the output.
      name: A name for the operation (optional).

    Returns:
      A tensor of the specified shape filled with random uniform values.

    Raises:
      ValueError: If `dtype` is integral and `maxval` is not specified.
    """
    def uniform_full_int(self, shape, dtype=..., name: Incomplete | None = None):
        """Uniform distribution on an integer type's entire range.

    This method is the same as setting `minval` and `maxval` to `None` in the
    `uniform` method.

    Args:
      shape: the shape of the output.
      dtype: (optional) the integer type, default to uint64.
      name: (optional) the name of the node.

    Returns:
      A tensor of random numbers of the required shape.
    """
    def binomial(self, shape, counts, probs, dtype=..., name: Incomplete | None = None):
        """Outputs random values from a binomial distribution.

    The generated values follow a binomial distribution with specified count and
    probability of success parameters.

    Example:

    ```python
    counts = [10., 20.]
    # Probability of success.
    probs = [0.8]

    rng = tf.random.Generator.from_seed(seed=234)
    binomial_samples = rng.binomial(shape=[2], counts=counts, probs=probs)


    counts = ... # Shape [3, 1, 2]
    probs = ...  # Shape [1, 4, 2]
    shape = [3, 4, 3, 4, 2]
    rng = tf.random.Generator.from_seed(seed=1717)
    # Sample shape will be [3, 4, 3, 4, 2]
    binomial_samples = rng.binomial(shape=shape, counts=counts, probs=probs)
    ```


    Args:
      shape: A 1-D integer Tensor or Python array. The shape of the output
        tensor.
      counts: Tensor. The counts of the binomial distribution. Must be
        broadcastable with `probs`, and broadcastable with the rightmost
        dimensions of `shape`.
      probs: Tensor. The probability of success for the
        binomial distribution. Must be broadcastable with `counts` and
        broadcastable with the rightmost dimensions of `shape`.
      dtype: The type of the output. Default: tf.int32
      name: A name for the operation (optional).

    Returns:
      samples: A Tensor of the specified shape filled with random binomial
        values.  For each i, each samples[i, ...] is an independent draw from
        the binomial distribution on counts[i] trials with probability of
        success probs[i].
    """
    def make_seeds(self, count: int = 1):
        """Generates seeds for stateless random ops.

    For example:

    ```python
    seeds = get_global_generator().make_seeds(count=10)
    for i in range(10):
      seed = seeds[:, i]
      numbers = stateless_random_normal(shape=[2, 3], seed=seed)
      ...
    ```

    Args:
      count: the number of seed pairs (note that stateless random ops need a
        pair of seeds to invoke).

    Returns:
      A tensor of shape [2, count] and dtype int64.
    """
    def split(self, count: int = 1):
        '''Returns a list of independent `Generator` objects.

    Two generators are independent of each other in the sense that the
    random-number streams they generate don\'t have statistically detectable
    correlations. The new generators are also independent of the old one.
    The old generator\'s state will be changed (like other random-number
    generating methods), so two calls of `split` will return different
    new generators.

    For example:

    ```python
    gens = get_global_generator().split(count=10)
    for gen in gens:
      numbers = gen.normal(shape=[2, 3])
      # ...
    gens2 = get_global_generator().split(count=10)
    # gens2 will be different from gens
    ```

    The new generators will be put on the current device (possible different
    from the old generator\'s), for example:

    ```python
    with tf.device("/device:CPU:0"):
      gen = Generator(seed=1234)  # gen is on CPU
    with tf.device("/device:GPU:0"):
      gens = gen.split(count=10)  # gens are on GPU
    ```

    Args:
      count: the number of generators to return.

    Returns:
      A list (length `count`) of `Generator` objects independent of each other.
      The new generators have the same RNG algorithm as the old one.
    '''

global_generator: Incomplete

def get_global_generator():
    """Retrieves the global generator.

  This function will create the global generator the first time it is called,
  and the generator will be placed at the default device at that time, so one
  needs to be careful when this function is first called. Using a generator
  placed on a less-ideal device will incur performance regression.

  Returns:
    The global `tf.random.Generator` object.
  """
def set_global_generator(generator) -> None:
    """Replaces the global generator with another `Generator` object.

  This function replaces the global generator with the provided `generator`
  object.
  A random number generator utilizes a `tf.Variable` object to store its state.
  The user shall be aware of caveats how `set_global_generator` interacts with
  `tf.function`:

  - tf.function puts restrictions on Variable creation thus one cannot freely
    create a new random generator instance inside `tf.function`.
    To call `set_global_generator` inside `tf.function`, the generator instance
    must have already been created eagerly.
  - tf.function captures the Variable during trace-compilation, thus a compiled
    f.function will not be affected `set_global_generator` as demonstrated by
    random_test.py/RandomTest.testResetGlobalGeneratorBadWithDefun .

  For most use cases, avoid calling `set_global_generator` after program
  initialization, and prefer to reset the state of the existing global generator
  instead, such as,

  >>> rng = tf.random.get_global_generator()
  >>> rng.reset_from_seed(30)


  Args:
    generator: the new `Generator` object.
  """
