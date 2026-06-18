import abc
from _typeshed import Incomplete
from tensorflow.python.client import session as session
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, ops as ops
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from tensorflow.python.util.tf_export import tf_export as tf_export

def format_master_url(master, rpc_layer: Incomplete | None = None): ...
def get_accelerator_devices(master, config_proto):
    """Returns accelerator devices given a master and a configuration."""

class ClusterResolver(metaclass=abc.ABCMeta):
    """Abstract class for all implementations of ClusterResolvers.

  This defines the skeleton for all implementations of ClusterResolvers.
  ClusterResolvers are a way for TensorFlow to communicate with various cluster
  management systems (e.g. GCE, AWS, etc...) and gives TensorFlow necessary
  information to set up distributed training.

  By letting TensorFlow communicate with these systems, we will be able to
  automatically discover and resolve IP addresses for various TensorFlow
  workers. This will eventually allow us to automatically recover from
  underlying machine failures and scale TensorFlow worker clusters up and down.

  Note to Implementors of `tf.distribute.cluster_resolver.ClusterResolver`
  subclass: In addition to these abstract methods, when task_type, task_id, and
  rpc_layer attributes are applicable, you should also implement them either as
  properties with getters or setters, or directly set the attributes
  `self._task_type`, `self._task_id`, or `self._rpc_layer` so the base class'
  getters and setters are used. See
  `tf.distribute.cluster_resolver.SimpleClusterResolver.__init__` for an
  example.

  In general, multi-client tf.distribute strategies such as
  `tf.distribute.experimental.MultiWorkerMirroredStrategy` require task_type and
  task_id properties to be available in the `ClusterResolver` they are using. On
  the other hand, these concepts are not applicable in single-client strategies,
  such as `tf.distribute.experimental.TPUStrategy`, because the program is only
  expected to be run on one task, so there should not be a need to have code
  branches according to task type and task id.

  - task_type is the name of the server's current named job (e.g. 'worker',
     'ps' in a distributed parameterized training job).
  - task_id is the ordinal index of the server within the task type.
  - rpc_layer is the protocol used by TensorFlow to communicate with other
      TensorFlow servers in a distributed environment.
  """
    @abc.abstractmethod
    def cluster_spec(self):
        """Retrieve the current state of the cluster and return a `tf.train.ClusterSpec`.

    Returns:
      A `tf.train.ClusterSpec` representing the state of the cluster at the
      moment this function is called.

    Implementors of this function must take care in ensuring that the
    ClusterSpec returned is up-to-date at the time of calling this function.
    This usually means retrieving the information from the underlying cluster
    management system every time this function is invoked and reconstructing
    a cluster_spec, rather than attempting to cache anything.
    """
    @abc.abstractmethod
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Retrieves the name or URL of the session master.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the master.
      task_id: (Optional) The index of the TensorFlow task of the master.
      rpc_layer: (Optional) The RPC protocol for the given cluster.

    Returns:
      The name or URL of the session master.

    Implementors of this function must take care in ensuring that the master
    returned is up-to-date at the time to calling this function. This usually
    means retrieving the master every time this function is invoked.
    """
    def num_accelerators(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, config_proto: Incomplete | None = None):
        """Returns the number of accelerator cores per worker.

    This returns the number of accelerator cores (such as GPUs and TPUs)
    available per worker.

    Optionally, we allow callers to specify the task_type, and task_id, for
    if they want to target a specific TensorFlow task to query
    the number of accelerators. This is to support heterogenous environments,
    where the number of accelerators cores per host is different.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the machine we
        want to query.
      task_id: (Optional) The index of the TensorFlow task of the machine we
        want to query.
      config_proto: (Optional) Configuration for starting a new session to
        query how many accelerator cores it has.

    Returns:
      A map of accelerator types to number of cores.
    """
    @property
    def environment(self):
        '''Returns the current environment which TensorFlow is running in.

    There are two possible return values, "google" (when TensorFlow is running
    in a Google-internal environment) or an empty string (when TensorFlow is
    running elsewhere).

    If you are implementing a ClusterResolver that works in both the Google
    environment and the open-source world (for instance, a TPU ClusterResolver
    or similar), you will have to return the appropriate string depending on the
    environment, which you will have to detect.

    Otherwise, if you are implementing a ClusterResolver that will only work
    in open-source TensorFlow, you do not need to implement this property.
    '''
    @property
    def task_type(self):
        '''Returns the task type this `ClusterResolver` indicates.

    In TensorFlow distributed environment, each job may have an applicable
    task type. Valid task types in TensorFlow include
    \'chief\': a worker that is designated with more responsibility,
    \'worker\': a regular worker for training/evaluation,
    \'ps\': a parameter server, or
    \'evaluator\': an evaluator that evaluates the checkpoints for metrics.

    See [Multi-worker configuration](
    https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)
    for more information about \'chief\' and \'worker\' task type, which are most
    commonly used.

    Having access to such information is useful when user needs to run specific
    code according to task types. For example,

    ```python
    cluster_spec = tf.train.ClusterSpec({
        "ps": ["localhost:2222", "localhost:2223"],
        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]
    })

    # SimpleClusterResolver is used here for illustration; other cluster
    # resolvers may be used for other source of task type/id.
    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",
                                            task_id=1)

    ...

    if cluster_resolver.task_type == \'worker\':
      # Perform something that\'s only applicable on workers. This block
      # will run on this particular instance since we\'ve specified this task to
      # be a worker in above cluster resolver.
    elif cluster_resolver.task_type == \'ps\':
      # Perform something that\'s only applicable on parameter servers. This
      # block will not run on this particular instance.
    ```

    Returns `None` if such information is not available or is not applicable
    in the current distributed environment, such as training with
    `tf.distribute.experimental.TPUStrategy`.

    For more information, please see
    `tf.distribute.cluster_resolver.ClusterResolver`\'s class doc.
    '''
    @property
    def task_id(self):
        '''Returns the task id this `ClusterResolver` indicates.

    In TensorFlow distributed environment, each job may have an applicable
    task id, which is the index of the instance within its task type. This is
    useful when user needs to run specific code according to task index. For
    example,

    ```python
    cluster_spec = tf.train.ClusterSpec({
        "ps": ["localhost:2222", "localhost:2223"],
        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]
    })

    # SimpleClusterResolver is used here for illustration; other cluster
    # resolvers may be used for other source of task type/id.
    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",
                                            task_id=0)

    ...

    if cluster_resolver.task_type == \'worker\' and cluster_resolver.task_id == 0:
      # Perform something that\'s only applicable on \'worker\' type, id 0. This
      # block will run on this particular instance since we\'ve specified this
      # task to be a \'worker\', id 0 in above cluster resolver.
    else:
      # Perform something that\'s only applicable on other ids. This block will
      # not run on this particular instance.
    ```

    Returns `None` if such information is not available or is not applicable
    in the current distributed environment, such as training with
    `tf.distribute.cluster_resolver.TPUClusterResolver`.

    For more information, please see
    `tf.distribute.cluster_resolver.ClusterResolver`\'s class docstring.
    '''
    @task_type.setter
    def task_type(self, task_type) -> None:
        """Setter of `task_type` property. See `task_type` property doc."""
    @task_id.setter
    def task_id(self, task_id) -> None:
        """Setter of `task_id` property. See `task_type` property doc."""

class SimpleClusterResolver(ClusterResolver):
    '''Simple implementation of ClusterResolver that accepts all attributes.

  Please see the base class for documentation of arguments of its constructor.

  It is useful if you want to specify some or all attributes.

  Usage example with `tf.distribute.Strategy`:

    ```Python
    cluster = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",
                                               "worker1.example.com:2222"]})

    # On worker 0
    cluster_resolver = SimpleClusterResolver(cluster, task_type="worker",
                                             task_id=0,
                                             num_accelerators={"GPU": 8},
                                             rpc_layer="grpc")
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
        cluster_resolver=cluster_resolver)

    # On worker 1
    cluster_resolver = SimpleClusterResolver(cluster, task_type="worker",
                                             task_id=1,
                                             num_accelerators={"GPU": 8},
                                             rpc_layer="grpc")
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
        cluster_resolver=cluster_resolver)
    ```
  '''
    def __init__(self, cluster_spec, master: str = '', task_type: Incomplete | None = None, task_id: Incomplete | None = None, environment: str = '', num_accelerators: Incomplete | None = None, rpc_layer: Incomplete | None = None) -> None:
        """Creates a SimpleClusterResolver from a ClusterSpec."""
    def cluster_spec(self):
        """Returns the ClusterSpec passed into the constructor."""
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Returns the master address to use when creating a session.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the master.
      task_id: (Optional) The index of the TensorFlow task of the master.
      rpc_layer: (Optional) The RPC used by distributed TensorFlow.

    Returns:
      The name or URL of the session master.

    If a task_type and task_id is given, this will override the `master`
    string passed into the initialization function.
    """
    @property
    def task_type(self): ...
    @property
    def task_id(self): ...
    @task_type.setter
    def task_type(self, task_type) -> None: ...
    @task_id.setter
    def task_id(self, task_id) -> None: ...
    @property
    def environment(self): ...
    def num_accelerators(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, config_proto: Incomplete | None = None):
        """Returns the number of accelerator cores per worker.

    The SimpleClusterResolver does not do automatic detection of accelerators,
    and thus all arguments are unused and we simply return the value provided
    in the constructor.

    Args:
      task_type: Unused.
      task_id: Unused.
      config_proto: Unused.
    """
    @property
    def rpc_layer(self): ...
    @rpc_layer.setter
    def rpc_layer(self, rpc_layer) -> None: ...

class UnionClusterResolver(ClusterResolver):
    '''Performs a union on underlying ClusterResolvers.

  This class performs a union given two or more existing ClusterResolvers. It
  merges the underlying ClusterResolvers, and returns one unified ClusterSpec
  when cluster_spec is called. The details of the merge function is
  documented in the cluster_spec function.

  For additional ClusterResolver properties such as task type, task index,
  rpc layer, environment, etc..., we will return the value from the first
  ClusterResolver in the union.

  An example to combine two cluster resolvers:

    ```Python
    cluster_0 = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",
                                                 "worker1.example.com:2222"]})
    cluster_resolver_0 = SimpleClusterResolver(cluster, task_type="worker",
                                               task_id=0,
                                               rpc_layer="grpc")

    cluster_1 = tf.train.ClusterSpec({"ps": ["ps0.example.com:2222",
                                             "ps1.example.com:2222"]})
    cluster_resolver_1 = SimpleClusterResolver(cluster, task_type="ps",
                                               task_id=0,
                                               rpc_layer="grpc")

    # Its task type would be "worker".
    cluster_resolver = UnionClusterResolver(cluster_resolver_0,
                                            cluster_resolver_1)
    ```

  An example to override the number of GPUs in a TFConfigClusterResolver
  instance:

    ```Python
    tf_config = TFConfigClusterResolver()
    gpu_override = SimpleClusterResolver(tf_config.cluster_spec(),
                                         num_accelerators={"GPU": 1})
    cluster_resolver = UnionResolver(gpu_override, tf_config)
    ```
  '''
    def __init__(self, *args, **kwargs) -> None:
        """Initializes a UnionClusterResolver with other ClusterResolvers.

    Args:
      *args: `ClusterResolver` objects to be unionized.
      **kwargs:
        rpc_layer - (Optional) Override value for the RPC layer used by
          TensorFlow.
        task_type - (Optional) Override value for the current task type.
        task_id - (Optional) Override value for the current task index.

    Raises:
      TypeError: If any argument is not a subclass of `ClusterResolvers`.
      ValueError: If there are no arguments passed.
    """
    def cluster_spec(self):
        """Returns a union of all the ClusterSpecs from the ClusterResolvers.

    Returns:
      A ClusterSpec containing host information merged from all the underlying
      ClusterResolvers.

    Raises:
      KeyError: If there are conflicting keys detected when merging two or
      more dictionaries, this exception is raised.

    Note: If there are multiple ClusterResolvers exposing ClusterSpecs with the
    same job name, we will merge the list/dict of workers.

    If *all* underlying ClusterSpecs expose the set of workers as lists, we will
    concatenate the lists of workers, starting with the list of workers from
    the first ClusterResolver passed into the constructor.

    If *any* of the ClusterSpecs expose the set of workers as a dict, we will
    treat all the sets of workers as dicts (even if they are returned as lists)
    and will only merge them into a dict if there is no conflicting keys. If
    there is a conflicting key, we will raise a `KeyError`.
    """
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Returns the master address to use when creating a session.

    This usually returns the master from the first ClusterResolver passed in,
    but you can override this by specifying the task_type and task_id.

    Note: this is only useful for TensorFlow 1.x.

    Args:
      task_type: (Optional) The type of the TensorFlow task of the master.
      task_id: (Optional) The index of the TensorFlow task of the master.
      rpc_layer: (Optional) The RPC protocol for the given cluster.

    Returns:
      The name or URL of the session master.
    """
    @property
    def task_type(self): ...
    @property
    def task_id(self): ...
    @task_type.setter
    def task_type(self, task_type) -> None: ...
    @task_id.setter
    def task_id(self, task_id) -> None: ...
    @property
    def environment(self): ...
    def num_accelerators(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, config_proto: Incomplete | None = None): ...
    @property
    def rpc_layer(self): ...
    @rpc_layer.setter
    def rpc_layer(self, rpc_layer) -> None: ...
