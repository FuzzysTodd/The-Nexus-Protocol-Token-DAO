from _typeshed import Incomplete
from tensorflow.core.profiler import tfprof_options_pb2 as tfprof_options_pb2, tfprof_output_pb2 as tfprof_output_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.profiler import option_builder as option_builder, tfprof_logger as tfprof_logger
from tensorflow.python.util.tf_export import tf_export as tf_export

ALL_ADVICE: Incomplete

class Profiler:
    """TensorFlow multi-step profiler.


  ```python
  Typical use case:
    # Currently we are only allowed to create 1 profiler per process.
    profiler = Profiler(sess.graph)

    for i in range(total_steps):
      if i % 10000 == 0:
        run_meta = tf.compat.v1.RunMetadata()
        _ = sess.run(...,
                     options=tf.compat.v1.RunOptions(
                         trace_level=tf.RunOptions.FULL_TRACE),
                     run_metadata=run_meta)
        profiler.add_step(i, run_meta)

        # Profile the parameters of your model.
        profiler.profile_name_scope(options=(option_builder.ProfileOptionBuilder
            .trainable_variables_parameter()))

        # Or profile the timing of your model operations.
        opts = option_builder.ProfileOptionBuilder.time_and_memory()
        profiler.profile_operations(options=opts)

        # Or you can generate a timeline:
        opts = (option_builder.ProfileOptionBuilder(
                option_builder.ProfileOptionBuilder.time_and_memory())
                .with_step(i)
                .with_timeline_output(filename).build())
        profiler.profile_graph(options=opts)
      else:
        _ = sess.run(...)
    # Auto detect problems and generate advice.
    profiler.advise()
  ```
  """
    def __init__(self, graph: Incomplete | None = None, op_log: Incomplete | None = None) -> None:
        """Constructor.

    Args:
      graph: tf.Graph. If None and eager execution is not enabled, use default
        graph.
      op_log: optional. tensorflow::tfprof::OpLogProto proto. Used to define
        extra op types.
    """
    def __del__(self) -> None: ...
    def add_step(self, step, run_meta) -> None:
        """Add statistics of a step.

    Args:
      step: int, An id used to group one or more different `run_meta` together.
        When profiling with the profile_xxx APIs, user can use the `step` id in
        the `options` to profile these `run_meta` together.
      run_meta: RunMetadata proto that contains statistics of a session run.
    """
    def profile_python(self, options):
        """Profile the statistics of the Python codes.

      By default, it shows the call stack from root. To avoid
      redundant output, you may use options to filter as below
        options['show_name_regexes'] = ['.*my_code.py.*']

    Args:
      options: A dict of options. See core/profiler/g3doc/options.md.

    Returns:
      a MultiGraphNodeProto that records the results.
    """
    def profile_operations(self, options):
        """Profile the statistics of the Operation types (e.g.

    MatMul, Conv2D).

    Args:
      options: A dict of options. See core/profiler/g3doc/options.md.

    Returns:
      a MultiGraphNodeProto that records the results.
    """
    def profile_name_scope(self, options):
        """Profile the statistics of graph nodes, organized by name scope.

    Args:
      options: A dict of options. See core/profiler/g3doc/options.md.

    Returns:
      a GraphNodeProto that records the results.
    """
    def profile_graph(self, options):
        """Profile the statistics of graph nodes, organized by dataflow graph.

    Args:
      options: A dict of options. See core/profiler/g3doc/options.md.

    Returns:
      a GraphNodeProto that records the results.
    """
    def advise(self, options):
        """Automatically detect problems and generate reports.

    Args:
      options: A dict of options. See ALL_ADVICE example above.

    Returns:
      An Advise proto that contains the reports from all checkers.
    """
    def serialize_to_string(self):
        """Serialize the ProfileProto to a binary string.

      Users can write it to file for offline analysis by tfprof commandline
      or graphical interface.

    Returns:
      ProfileProto binary string.
    """

def profile(graph: Incomplete | None = None, run_meta: Incomplete | None = None, op_log: Incomplete | None = None, cmd: str = 'scope', options=...):
    '''Profile model.

    Tutorials and examples can be found in:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/profiler/g3doc/python_api.md

  Args:
    graph: tf.Graph. If None and eager execution is not enabled, use default
      graph.
    run_meta: optional tensorflow.RunMetadata proto. It is necessary to
      support run time information profiling, such as time and memory.
    op_log: tensorflow.tfprof.OpLogProto proto. User can assign "types" to graph
      nodes with op_log. "types" allow user to flexibly group and account
      profiles using options[\'accounted_type_regexes\'].
    cmd: string. Either \'op\', \'scope\', \'graph\' or \'code\'. \'op\' view organizes
      profile using operation type. (e.g. MatMul) \'scope\' view organizes profile
      using graph node name scope. \'graph\' view organizes profile using graph
      node inputs/outputs. \'code\' view organizes profile using Python call
      stack.
    options: A dict of options. See core/profiler/g3doc/options.md.

  Returns:
    If cmd is \'scope\' or \'graph\', returns GraphNodeProto proto.
    If cmd is \'op\' or \'code\', returns MultiGraphNodeProto proto.
    Side effect: stdout/file/timeline.json depending on options[\'output\']
  '''
def advise(graph: Incomplete | None = None, run_meta: Incomplete | None = None, options=...):
    """Auto profile and advise.

    Builds profiles and automatically check anomalies of various
    aspects. For more details:
    https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md

  Args:
    graph: tf.Graph. If None and eager execution is not enabled, use default
      graph.
    run_meta: optional tensorflow.RunMetadata proto. It is necessary to
      support run time information profiling, such as time and memory.
    options: see ALL_ADVICE example above. Default checks everything.

  Returns:
    Returns AdviceProto proto
  """
