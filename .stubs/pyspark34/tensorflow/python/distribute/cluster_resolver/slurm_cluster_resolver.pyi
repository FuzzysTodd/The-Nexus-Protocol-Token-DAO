from _typeshed import Incomplete
from tensorflow.python.distribute.cluster_resolver.cluster_resolver import ClusterResolver as ClusterResolver, format_master_url as format_master_url
from tensorflow.python.training.server_lib import ClusterSpec as ClusterSpec
from tensorflow.python.util.tf_export import tf_export as tf_export

def expand_hostlist(hostlist):
    """Create a list of hosts out of a SLURM hostlist.

  The order of nodes is preserved and no deduplication is done
  Input: 'n[1-2],m5,o[3-4,6,7-9]')
  Output: ['n1', 'n2', 'm5', 'o3', 'o4', 'o6', 'o7', 'o8', 'o9']
  """
def expand_tasks_per_node(tasks_per_node):
    """Expands the tasks per node expression from SLURM.

  The order is preserved so it can be matched to the hostlist
  Input: '3(x2),2,1'
  Output: [3, 3, 2, 1]
  """
def get_num_gpus():
    """Returns the number of GPUs visible on the current node.

  Currently only implemented for NVIDIA GPUs.
  """

class SlurmClusterResolver(ClusterResolver):
    """ClusterResolver for system with Slurm workload manager.

  This is an implementation of ClusterResolver for Slurm clusters. This allows
  the specification of jobs and task counts, number of tasks per node, number
  of GPUs on each node and number of GPUs for each task. It retrieves system
  attributes by Slurm environment variables, resolves allocated computing node
  names, constructs a cluster and returns a ClusterResolver object which can be
  used for distributed TensorFlow.
  """
    task_type: Incomplete
    task_id: Incomplete
    rpc_layer: Incomplete
    def __init__(self, jobs: Incomplete | None = None, port_base: int = 8888, gpus_per_node: Incomplete | None = None, gpus_per_task: Incomplete | None = None, tasks_per_node: Incomplete | None = None, auto_set_gpu: bool = True, rpc_layer: str = 'grpc') -> None:
        """Creates a new SlurmClusterResolver object.

    For any parameter not set it will query the environment for the value.
    It uses those parameters to check which nodes have processes reside on and
    resolves their hostnames.
    With the number tasks per node it offsets the port number for each process.
    With the number of GPUs per node and per task it allocates GPUs to tasks by
    setting environment variables.
    Using the resolver works best (and is easier) with homogeneous tasks but
    heterogeneous tasks (number of tasks varying per node) are also possible as
    long as the number of GPUs per task stays constant.

    Used environment variables:
      - SLURM_PROCID
      - (opt) SLURM_STEP_NUM_TASKS
      - (opt) SLURM_STEP_NODELIST
      - (opt) SLURM_STEP_TASKS_PER_NODE

    Args:
      jobs: Dictionary with job names as key and number of tasks in the job as
        value. Defaults to as many 'worker's as there are (Slurm) tasks.
      port_base: The first port number to start with for processes on a node.
      gpus_per_node: Number of GPUs available on each node. Defaults to the
        number of GPUs reported by nvidia-smi
      gpus_per_task: Number of GPUs to be used for each task. Default is to
        evenly distribute the gpus_per_node to tasks_per_node.
      tasks_per_node: Number of tasks running on each node. Can be an integer if
        the number of tasks per node is constant or a dictionary mapping
        hostnames to number of tasks on that node. If not set the Slurm
        environment is queried for the correct mapping.
      auto_set_gpu: Set the visible CUDA devices automatically while resolving
        the cluster by setting CUDA_VISIBLE_DEVICES environment variable.
        Defaults to True.
      rpc_layer: The protocol TensorFlow used to communicate between nodes.
        Defaults to 'grpc'.

    Returns:
      A ClusterResolver object which can be used with distributed TensorFlow.

    Raises:
      RuntimeError: If requested more GPUs per node than available or
        requested more tasks than assigned tasks or
        resolving missing values from the environment failed.
    """
    def cluster_spec(self):
        """Returns a ClusterSpec object based on the latest instance group info.

    This returns a ClusterSpec object for use based on information from the
    specified initialization parameters and Slurm environment variables. The
    cluster specification is resolved each time this function is called. The
    resolver extract hostnames of nodes by scontrol and pack tasks in that
    order until a node a has number of tasks that is equal to specification.
    GPUs on nodes are allocated to tasks by specification through setting
    CUDA_VISIBLE_DEVICES environment variable.

    Returns:
      A ClusterSpec containing host information retrieved from Slurm's
        environment variables.
    """
    def get_task_info(self):
        """Returns job name and task_id for the process which calls this.

    This returns the job name and task index for the process which calls this
    function according to its rank and cluster specification. The job name and
    task index are set after a cluster is constructed by cluster_spec otherwise
    defaults to None.

    Returns:
      A string specifying job name the process belongs to and an integer
        specifying the task index the process belongs to in that job.
    """
    def master(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, rpc_layer: Incomplete | None = None):
        """Returns the master string for connecting to a TensorFlow master.

    Args:
      task_type: (Optional) Overrides the default auto-selected task type.
      task_id: (Optional) Overrides the default auto-selected task index.
      rpc_layer: (Optional) Overrides the default RPC protocol TensorFlow uses
        to communicate across nodes.

    Returns:
      A connection string for connecting to a TensorFlow master.
    """
    def num_accelerators(self, task_type: Incomplete | None = None, task_id: Incomplete | None = None, config_proto: Incomplete | None = None): ...
