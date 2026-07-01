from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.compat import v2_compat as v2_compat
from tensorflow.python.distribute import multi_process_lib as multi_process_lib, multi_worker_util as multi_worker_util
from tensorflow.python.eager import context as context
from tensorflow.python.framework import test_util as test_util
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

multiprocessing = multi_process_lib.multiprocessing

class _ProcessStatusInfo(NamedTuple):
    task_type: Incomplete
    task_id: Incomplete
    is_successful: Incomplete
    exc_info: Incomplete
    return_value: Incomplete

class MultiProcessRunnerResult(NamedTuple):
    return_value: Incomplete
    stdout: Incomplete

class TestEnvironment(NamedTuple):
    task_type: Incomplete
    task_id: Incomplete
    cluster_spec: Incomplete
    rpc_layer: Incomplete
    grpc_fail_fast: Incomplete
    v2_enabled: Incomplete
    executing_eagerly: Incomplete
    visible_gpus: Incomplete

class Resources(NamedTuple):
    process_status_queue: Incomplete
    parent_to_sub_queue: Incomplete
    streaming_pipe_w: Incomplete
    barrier: Incomplete

class MultiProcessRunner:
    """A utility class to start multiple processes to simulate a cluster.

  We need to use multiple processes to simulate a cluster in TF 2.0 tests
  because TF 2.0 has some process-global data structures that have to be
  separated by processes. We also need child processes to test out our fault
  tolerance because shutting down a standard TensorFlow server within its
  process is not supported.

  Note: the main test program that uses this runner class must run main program
  via `test_main` defined in this file. Using this runner in non-test binaries
  is not supported yet.

  This class is not thread-safe. Child processes will inherit TF2 behavior flag.
  """
    def __init__(self, fn, cluster_spec, rpc_layer: Incomplete | None = None, max_run_time: Incomplete | None = None, grpc_fail_fast: Incomplete | None = None, stream_output: bool = True, return_output: bool = False, use_dill_for_args: bool = True, daemon: bool = False, dependence_on_chief: bool = True, auto_restart: bool = False, share_gpu: bool = True, args: Incomplete | None = None, kwargs: Incomplete | None = None) -> None:
        '''Instantiation of a `MultiProcessRunner`.

    Args:
      fn: Function to be run on child processes. This will be run on processes
        for all task types.
      cluster_spec: Dict for cluster spec. The utility function
        `tf.__internal__.distribute.multi_process_runner.create_cluster_spec`
        can be conveniently used to create such dict. The following is an
        example of cluster with three workers and two ps\'s.
        {"worker": ["worker0.example.com:2222",
                    "worker1.example.com:2222",
                    "worker2.example.com:2222"],
         "ps": ["ps0.example.com:2222",
                "ps1.example.com:2222"]}
      rpc_layer: RPC layer to use. Default value is \'grpc\'.
      max_run_time: `None` or integer. If not `None`, child processes are forced
        to exit at approximately this many seconds after this utility is called.
        We achieve this through `signal.alarm()` api. Note that this is best
        effort at Python level since Python signal handler does not get executed
        when it runs lower level C/C++ code. So it can be delayed for
        arbitrarily long time. If any of the child process is still running when
        `max_run_time` is up, they will be force-terminated and an
        `UnexpectedSubprocessExitError` may be raised. If `None`, child
        processes are not forced to exit.
      grpc_fail_fast: Whether GRPC connection between processes should fail
        without retrying. Defaults to None, in which case the environment
        variable is not explicitly set.
      stream_output: True if the output/error from the subprocesses should be
        streamed to be printed in parent process\' log. Defaults to True.
      return_output: If True, the output/error from the subprocesses should be
        collected to be attached to the resulting namedtuple returned from
        `join()`. The list of output can be retrieved via `stdout` attribute.
        Defaults to False.
      use_dill_for_args: Whether to use dill to pickle `args` and `kwargs`. dill
        can pickle more objects, but doesn\'t work with types in
        `multiprocessing` library like `Mutex`.
      daemon: Whether to start processes as daemons.
      dependence_on_chief: Whether to terminates the cluster if the chief exits.
        If auto_restart is True, it only terminates the cluster if the chief
        exits with a zero exit code.
      auto_restart: Whether to automatically restart processes that exit with
        non-zero exit code.
      share_gpu: Whether to share GPUs among workers. If False, each worker is
        assigned different GPUs in a roundrobin fashion. This should be True
        whenever possible for better test execution coverage; some situations
        that need it to be False are tests that runs NCCL.
      args: Positional arguments to be sent to `fn` run on subprocesses.
      kwargs: Keyword arguments to be sent to `fn` run on subprocesses.

    Raises:
      RuntimeError: if `multi_process_runner.test_main()` is not called.
      ValueError: if there are more than one chief in the `cluster_spec`.
      SkipTest: if thread sanitizer is enabled (which is incompatible with MPR).
    '''
    def set_args(self, args: Incomplete | None = None, kwargs: Incomplete | None = None) -> None: ...
    def start(self) -> None:
        """Starts processes, one for each task in `cluster_spec`.

    Note that this is best effort by the applicable multiprocessing library,
    and it may take up to seconds for a subprocess to be successfully started.
    """
    def start_in_process_as(self, as_task_type, as_task_id) -> None:
        """Start the processes, with the specified task run in main process.

    This is similar to `start()` except that the task with task_type
    `as_task_type` and task_id `as_task_id` is run in the main process.
    This method is particularly useful when debugging tool such as `pdb` is
    needed in some specific task. Note that since this method is blocking until
    that specific task exits, additional actions would need a thread to be
    called:

    ```python
    def fn():
      # user code to be run
      import pdb; pdb.set_trace()

    def follow_ups():
      time.sleep(5)
      mpr.start_single_process(
          task_type='evaluator',
          task_id=0)

    mpr = multi_process_runner.MultiProcessRunner(
        fn,
        multi_worker_test_base.create_cluster_spec(
            has_chief=True, num_workers=1))
    threading.Thread(target=follow_ups).start()
    mpr.start_in_process_as(as_task_type='chief', as_task_id=0)
    mpr.join()
    ```

    Note that if `return_output=True`, the logs/stdout by task
    run by the main process is not available in result.stdout.

    Args:
      as_task_type: The task type to be run in the main process.
      as_task_id: The task id to be run in the main process.
    """
    def start_single_process(self, task_type, task_id, cluster_spec: Incomplete | None = None, fn: Incomplete | None = None, args: Incomplete | None = None, kwargs: Incomplete | None = None) -> None:
        """Starts a single process.

    This starts a process in the cluster with the task type, task id, and the
    process function (`fn`). If process function is `None`, the function
    provided at `__init__` will be used. If `cluster_spec` is `None`, the
    cluster spec provided at `__init__` will be used.

    TODO(rchao): It is meant that all subprocesses will be updated with the new
    cluster spec, but this has yet to be implemented. At this time only the
    newly started subprocess picks up this updated cluster spec.

    Args:
      task_type: The task type.
      task_id: The task id.
      cluster_spec: The cluster spec to be used on the newly started
        process. If `None`, the cluster spec provided at `__init__` will be
        used.
      fn: The process function to be run on the newly started
        process. If specified, specify `args` and `kwargs` as well. If `None`,
        the function provided at `__init__` will be used.
      args: Optional positional arguments to be supplied in `fn`.
      kwargs: Optional keyword arguments to be supplied in `fn`.
    """
    def get_process_id(self, task_type, task_id):
        """Returns the subprocess id given the task type and task id."""
    def get_process_exit_code(self, task_type, task_id):
        """Returns the subprocess exit code given the task type and task id.

    Args:
      task_type: The task type.
      task_id: The task id.

    Returns:
      The subprocess exit code; `None` if the subprocess has not exited yet.

    Raises:
      KeyError: If the corresponding subprocess is not found with `task_type`
        and `task_id`.
    """
    def process_exists(self, task_type, task_id):
        """Returns whether the subprocess still exists given the task type and id.

    Args:
      task_type: The task type.
      task_id: The task id.

    Returns:
      Boolean; whether the subprocess still exists. If the subprocess has
      exited, this returns False.
    """
    def join(self, timeout=...):
        """Joins all the processes with timeout.

    If any of the subprocesses does not exit approximately after `timeout`
    seconds has passed after `join` call, this raises a
    `SubprocessTimeoutError`.

    Note: At timeout, it uses SIGTERM to terminate the subprocesses, in order to
    log the stack traces of the subprocesses when they exit. However, this
    results in timeout when the test runs with tsan (thread sanitizer); if tsan
    is being run on the test targets that rely on timeout to assert information,
    `MultiProcessRunner.terminate_all()` must be called after `join()`, before
    the test exits, so the subprocesses are terminated with SIGKILL, and data
    race is removed.

    Args:
      timeout: optional integer or `None`. If provided as an integer, and not
      all processes report status within roughly `timeout` seconds, a
      `SubprocessTimeoutError` exception will be raised. If `None`, `join` never
      times out.

    Returns:
      A `MultiProcessRunnerResult` object, which has two attributes,
      `return_value` and `stdout`. `return_value` always contains a list of
      return values from the subprocesses, although the order is not meaningful.
      If `return_output` argument is True at `__init__`, `stdout` is available
      that contains a list of all messages from subprocesses' stdout and stderr.

    Raises:
      SubprocessTimeoutError: if not all processes report status approximately
        within `timeout` seconds. When this is raised, a
        `MultiProcessRunnerResult` object can be retrieved by
        `SubprocessTimeoutError`'s mpr_result attribute, which has the same
        structure as above 'Returns' section describes.
      UnexpectedSubprocessExitError: If any of the subprocesses did not exit
        properly (for example, they exit on SIGTERM or SIGKILL signal). When
        this is raised, a `MultiProcessRunnerResult` object can be retrieved by
        `UnexpectedSubprocessExitError`'s mpr_result attribute, which has the
        same structure as above 'Returns' section describes. If `max_run_time`
        is not `None`, it is expected that some subprocesses may be
        force-killed when `max_run_time` is up, and this is raised in those
        cases.
      Exception: if there is an Exception propagated from any subprocess. When
        this is raised, a `MultiProcessRunnerResult` object can be retrieved by
        `UnexpectedSubprocessExitError`'s mpr_result attribute, which has the
        same structure as above 'Returns' section describes.
    """
    def terminate(self, task_type, task_id) -> None:
        """Terminates the process with `task_type` and `task_id`.

    If auto_retart=True, the terminated task will be restarted unless the chief
    has already exited with zero exit code.

    Args:
      task_type: the task type.
      task_id: the task id.

    """
    def terminate_all(self, sig: Incomplete | None = None) -> None:
        """Terminates all subprocesses."""

class _Process(multi_process_lib.Process):
    """A modified `multiprocessing.Process` that can set up environment variables."""
    run: Incomplete
    def __init__(self, test_env, **kwargs) -> None: ...

class _ProcFunc:
    """Represents a callable to run in a subprocess."""
    def __call__(self, resources, test_env, fn, args, kwargs, use_dill_for_args) -> None:
        """The wrapper function that actually gets run in child process(es)."""

def is_oss():
    """Returns whether the test is run under OSS."""

class MultiProcessPoolRunner:
    """A utility class to start a process pool to simulate a cluster.

  It's similar to MultiProcessRunner, but uses a pool of processes to avoid the
  expensive initialization cost of Tensorflow.
  """
    def __init__(self, cluster_spec, initializer: Incomplete | None = None, share_gpu: bool = True) -> None:
        '''Creates a multi-process pool runner.

    Args:
      cluster_spec: Dict for cluster spec. The following is an example of
        cluster with three workers.
        {"worker": ["worker0.example.com:2222",
                    "worker1.example.com:2222",
                    "worker2.example.com:2222"]}
      initializer: a callable to called at the startup of worker processes.
      share_gpu: Whether to share GPUs among workers. If False, each worker is
        assigned different GPUs in a roundrobin fashion.

    Raises:
      RuntimeError: if `multi_process_runner.test_main()` is not called.
      ValueError: if there are more than one chief in the `cluster_spec`.
    '''
    def __del__(self) -> None: ...
    def shutdown(self) -> None:
        """Shuts down the worker pool."""
    def run(self, fn, args: Incomplete | None = None, kwargs: Incomplete | None = None):
        """Runs `fn` with `args` and `kwargs` on all jobs.

    Args:
      fn: The function to be run.
      args: Optional positional arguments to be supplied in `fn`.
      kwargs: Optional keyword arguments to be supplied in `fn`.

    Returns:
      A list of return values.
    """

class SubprocessTimeoutError(RuntimeError):
    """An error that indicates there is at least one subprocess timing out.

  When this is raised, a namedtuple object representing the multi-process run
  result can be retrieved by
  `tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError`'s
  `mpr_result` attribute. See
  `tf.__internal__.distribute.multi_process_runner.run` for more information.
  """
    mpr_result: Incomplete
    def __init__(self, msg, mpr_result) -> None: ...

class UnexpectedSubprocessExitError(RuntimeError):
    """An error indicating there is at least one subprocess with unexpected exit.

  When this is raised, a namedtuple object representing the multi-process run
  result can be retrieved by
  `tf.__internal__.distribute.multi_process_runner
  .UnexpectedSubprocessExitError`'s
  `mpr_result` attribute. See
  `tf.__internal__.distribute.multi_process_runner.run` for more information.
  """
    mpr_result: Incomplete
    def __init__(self, msg, mpr_result) -> None: ...

class NotInitializedError(RuntimeError):
    """An error indicating `multi_process_runner.run` is used without init.

  When this is raised, user is supposed to call
  `tf.__internal__.distribute.multi_process_runner.test_main()` within
  `if __name__ == '__main__':` block to properly initialize
  `multi_process_runner.run`.
  """

def run(fn, cluster_spec, rpc_layer: Incomplete | None = None, max_run_time: Incomplete | None = None, return_output: bool = False, timeout=..., args: Incomplete | None = None, kwargs: Incomplete | None = None):
    '''Run `fn` in multiple processes according to `cluster_spec`.

  Given a callable `fn`, `tf.__internal__.distribute.multi_process_runner.run`
  launches multiple processes, each of which runs `fn`. These processes are
  referred to as "subprocesses" or "child processes". Each of those subprocesses
  will have their `TF_CONFIG` environment variable set, according to
  `cluster_spec` and their task types. The stdout of the subprocesses are
  streamed to the main process\' and thus available in logs (if `stream_output`
  is True), with [type-id] prefix.

  `tf.__internal__.distribute.multi_process_runner.run` will block until all
  subprocesses have successfully exited, and return a namedtuple object that
  represents the run result. This object has a `return_value` attribute, which
  is a list that contains subprocesses `fn`\'s return values, for those
  subprocesses that successfully returned from `fn`. The order of `return_value`
  list is not meaningful. If an optional arg `return_output` (default to False)
  is set to True, the namedtuple object will have an additional attribute
  `stdout`, which is a list containing the stdout of the subprocesses. If any
  subprocess\' `fn` ends up raising an error, that error will be reraised from
  `tf.__internal__.distribute.multi_process_runner.run`, and the aforementioned
  namedtuple object will be available through the exception\'s
  `mpr_result` attribute.

  This utility is used for simulating running TensorFlow programs across
  multiple task types, and each of the task type may contain more than one task
  (except for "chief" where more than one task is prohibited). Test coverage of
  multi-worker training is the main application of this utility, where code
  written for multi-worker training can be realistically covered in unit tests.

  Any test module that uses
  `tf.__internal__.distribute.multi_process_runner.run()` must call
  `tf.__internal__.distribute.multi_process_runner.test_main()` instead of
  regular `test.main()` inside `if __name__ == \'__main__\':` block for proper
  initialization.

  Args:
    fn: Function to be run on child processes. This will be run on processes for
      all task types.
    cluster_spec: Dict for cluster spec. The utility function
      `tf.__internal__.distribute.multi_process_runner.create_cluster_spec` can
      be conveniently used to create such dict. The following is an example of
      cluster with three workers and two ps\'s.
      {"worker": ["worker0.example.com:2222",
                  "worker1.example.com:2222",
                  "worker2.example.com:2222"],
       "ps": ["ps0.example.com:2222",
              "ps1.example.com:2222"]}
    rpc_layer: RPC layer to use. Default value is \'grpc\'.
    max_run_time: `None` or integer. If not `None`, child processes are forced
      to exit at approximately this many seconds after this utility is called.
      We achieve this through `signal.alarm()` api. Note that this is best
      effort at Python level since Python signal handler does not get executed
      when it runs lower level C/C++ code. So it can be delayed for arbitrarily
      long time. If any of the child process is still running when
      `max_run_time` is up, they will be force-terminated and an
      `tf.__internal__.distribute.multi_process_runner
      .UnexpectedSubprocessExitError`
      may be raised. If `None`, child processes are not forced to exit.
    return_output: If True, the output/error from the subprocesses should be
      collected to be attached to the resulting namedtuple returned from this
      utility. The list of output can be retrieved via `stdout` attribute.
      Defaults to False.
    timeout: optional integer or `None`. If provided as an integer, and not all
      processes report status within roughly `timeout` seconds, a
      `tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError`
      exception will be raised. If `None`,
      `tf.__internal__.distribute.multi_process_runner.run` never times out.
      Defaults to the constant `_DEFAULT_TIMEOUT_SEC` defined in
      `multi_process_runner` module.
    args: Positional arguments to be sent to `fn` run on subprocesses.
    kwargs: Keyword arguments to be sent to `fn` run on subprocesses.

  Returns:
      A namedtuple object, which has two attributes,
      `return_value` and `stdout`. `return_value` always contains a list of
      returnvalues from the subprocesses, although the order is not meaningful.
      If `return_output` argument is True, `stdout` is available that contains a
      list of all messages from subprocesses\' stdout and stderr, and the order
      is mostly chronological.

  Raises:
    RuntimeError: if
    `tf.__internal__.distribute.multi_process_runner.test_main()` is
      not called in test\'s `if __name__ == \'__main__\':` block.
    ValueError: if there are more than one chief in the `cluster_spec`.
    tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError: if
      not all processes report status approximately
      within `timeout` seconds. When this is raised, a
      namedtuple object can be retrieved by
      `tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError`\'s
      `mpr_result` attribute, which has the same
      structure as above \'Returns\' section describes.
    tf.__internal__.distribute.multi_process_runner
    .UnexpectedSubprocessExitError:
      If any of the subprocesses did not exit
      properly (for example, they exit on SIGTERM or SIGKILL signal). When
      this is raised, a namedtuple object can be retrieved by
      `tf.__internal__.distribute.multi_process_runner
      .UnexpectedSubprocessExitError`\'s
      `mpr_result` attribute, which has the
      same structure as above \'Returns\' section describes. If `max_run_time`
      is not `None`, it is expected that some subprocesses may be
      force-killed when `max_run_time` is up, and this is raised in those
      cases.
    Exception: if there is an Exception propagated from any subprocess. When
      this is raised, a namedtuple object can be retrieved by
      `tf.__internal__.distribute.multi_process_runner
      .UnexpectedSubprocessExitError`
      `mpr_result` attribute, which has the
      same structure as above \'Returns\' section describes.

  Examples:

  ```python
  class SimpleMultiProcessTest(tf.test.TestCase):

    def test_simple_printing_and_return(self):

      def fn():
        resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()

        # This will print "[chief-0]:     Task type: chief , task id: 0"
        # for chief, for example.
        logging.info(\'Task type: %s, task id: %d\',
                     resolver.task_type, resolver.task_id)

        return resolver.task_type

      result = tf.__internal__.distribute.multi_process_runner.run(
          fn=fn,
          cluster_spec=(
              tf.__internal__
              .distribute.multi_process_runner.create_cluster_spec(
                  has_chief=True, num_workers=2)))
      assert sorted(result.return_value) == [\'chief\', \'worker\', \'worker\']

    def test_error_from_fn(self):

      def fn():
        resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()
        raise ValueError(\'Task type {}, task id {} is errors out\'.format(
            resolver.task_type, resolver.task_id))

      with self.assertRaisesRegexp(ValueError,
                                   \'Task type worker, task id 0 is errors out\'):
        cluster_spec = (
            tf.__internal__.distribute.multi_process_runner.create_cluster_spec(
                num_workers=1))
        tf.__internal__.distribute.multi_process_runner.run(
            fn=fn, cluster_spec=cluster_spec)


  if __name__ == \'__main__\':
    tf.__internal__.distribute.multi_process_runner.test_main()
  ```
  '''
def get_barrier():
    """Returns a `multiprocessing.Barrier` for `multi_process_runner.run`.

  `tf.__internal__.distribute.multi_process_runner.get_barrier()` returns
  a `multiprocessing.Barrier` object which can be used within `fn` of
  `tf.__internal__.distribute.multi_process_runner` to wait with
  `barrier.wait()` call until all other tasks have also reached the
  `barrier.wait()` call, before they can proceed individually.

  Note that all tasks (subprocesses) have to reach `barrier.wait()` call to
  proceed. Currently it is not supported to block on only a subset of tasks
  in the cluster.

  Example:
  ```python

  def fn():
    some_work_to_be_done_by_all_tasks()

    tf.__internal__.distribute.multi_process_runner.get_barrier().wait()

    # The barrier guarantees that at this point, all tasks have finished
    # `some_work_to_be_done_by_all_tasks()`
    some_other_work_to_be_done_by_all_tasks()

  result = tf.__internal__.distribute.multi_process_runner.run(
      fn=fn,
      cluster_spec=(
          tf.__internal__
          .distribute.multi_process_runner.create_cluster_spec(
              num_workers=2)))
  ```


  Returns:
    A `multiprocessing.Barrier` for `multi_process_runner.run`.
  """
def manager():
    """Returns the multiprocessing manager object for concurrency tools.

  The manager object is useful as it controls a server process that holds
  the python objects that can be shared across processes. This can be used
  for parent-subprocess communication:

  ```python
  manager = multi_process_runner.manager()
  some_event_happening_in_subprocess = manager.Event()
  mpr = multi_process_runner.MultiProcessRunner(fn, cluster_spec,
      args=(some_event_happening_in_subprocess,))
  mpr.start()
  some_event_happening_in_subprocess.wait()
  # Do something that only should after some event happens in subprocess.
  ```

  Note that the user of multi_process_runner should not create additional
  `multiprocessing.Manager()` objects; doing so can result in segfault in
  some cases.

  This method should only be called after multi_process_runner.test_main() is
  called.
  """
def test_main() -> None:
    """Main function to be called within `__main__` of a test file.

  Any test module that uses
  `tf.__internal__.distribute.multi_process_runner.run()`
  must call this instead of regular `test.main()` inside
  `if __name__ == '__main__':` block, or an error will be raised when
  `tf.__internal__.distribute.multi_process_runner.run()` is used. This method
  takes
  care of needed initialization for launching multiple subprocesses.

  Example:
  ```python
  class MyTestClass(tf.test.TestCase):
    def testSomething(self):
      # Testing code making use of
      # `tf.__internal__.distribute.multi_process_runner.run()`.

  if __name__ == '__main__':
    tf.__internal__.distribute.multi_process_runner.test_main()
  ```
  """
