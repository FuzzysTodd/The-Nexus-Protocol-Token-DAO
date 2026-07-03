import tempfile
import torch
import torch._dynamo.test_case
import torch.nn as nn
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum
from torch.testing._internal.common_utils import FILE_SCHEMA as FILE_SCHEMA, IS_SANDCASTLE as IS_SANDCASTLE, TEST_WITH_ROCM as TEST_WITH_ROCM, TEST_WITH_TSAN as TEST_WITH_TSAN, TestCase as TestCase, find_free_port as find_free_port, retry_on_connect_failures as retry_on_connect_failures, sandcastle_skip as sandcastle_skip, sandcastle_skip_if as sandcastle_skip_if
from torch.testing._internal.distributed.multi_threaded_pg import ProcessLocalGroup as ProcessLocalGroup
from typing import Dict, NamedTuple

logger: Incomplete

class TestSkip(NamedTuple):
    exit_code: int
    message: str

TEST_SKIPS: Incomplete

@dataclass
class DistTestCases:
    skip_collective = ...
    backend_feature = ...

def skip_if_no_gpu(func):
    """Skips if the world size exceeds the number of GPUs, ensuring that if the
    test is run, each rank has its own GPU via ``torch.cuda.device(rank)``."""
def skip_if_small_worldsize(func): ...
def skip_if_odd_worldsize(func): ...
def require_n_gpus_for_nccl_backend(n, backend): ...
def import_transformers_or_skip(): ...
def skip_if_lt_x_gpu(x): ...
def nccl_skip_if_lt_x_gpu(backend, x): ...
def verify_ddp_error_logged(model_DDP, err_substr) -> None: ...
def with_nccl_blocking_wait(func):
    """
    Convenience decorator to set/unset NCCL_BLOCKING_WAIT flag. Note that use of
    this decorator will override the setting of NCCL_ASYNC_ERROR_HANDLING for
    the particular test. After the test, both NCCL_BLOCKING_WAIT and
    NCCL_ASYNC_ERROR_HANDLING will be restored to their original values.
    """
def with_dist_debug_levels(levels):
    """
    Runs a test for each distributed debug level specified in levels.
    """
def requires_gloo(): ...
def requires_nccl_version(version, msg): ...
def requires_nccl(): ...
def requires_ucc(): ...
def requires_mpi(): ...
def skip_if_rocm(func):
    """Skips a test for ROCm"""
def skip_if_win32(): ...
def create_tcp_store(addr: str = 'localhost', world_size: int = 1, is_master: bool = True, timeout=..., wait_for_workers: bool = True, jit_class: bool = False):
    """
    Creates a TCP store. Retries if the chosen port is already in use.
    """

TIMEOUT_DEFAULT: int
TIMEOUT_OVERRIDE: Incomplete

def create_device(interface: Incomplete | None = None): ...
def get_timeout(test_id) -> int: ...
def captured_output() -> Generator[Incomplete, None, None]: ...
def simple_sparse_reduce_tests(rank: int, world_size: int, num_inputs: int = 1):
    """
    Generate a number of basic test cases for sparse reduction.
    These cover tensors with a varying number of sparse dimensions and a varying
    number of dense dimensions. The only reduction operation we support is sum.
    """
def init_multigpu_helper(world_size: int, backend: str):
    """Multigpu tests are designed to simulate the multi nodes with multi
    GPUs on each node. Nccl backend requires equal #GPUs in each process.
    On a single node, all visible GPUs are evenly
    divided to subsets, each process only uses a subset.
    """

tmp_dir: tempfile.TemporaryDirectory | None

def initialize_temp_directories(init_method: str | None = None) -> None: ...
def cleanup_temp_dir() -> None: ...

DEFAULT_WORLD_SIZE: int

class MultiProcessTestCase(TestCase):
    MAIN_PROCESS_RANK: int
    TEST_ERROR_EXIT_CODE: int
    @property
    def world_size(self) -> int: ...
    def join_or_run(self, fn): ...
    def __init__(self, method_name: str = 'runTest') -> None: ...
    skip_return_code_checks: Incomplete
    processes: Incomplete
    rank: Incomplete
    file_name: Incomplete
    pid_to_pipe: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    class Event(Enum):
        GET_TRACEBACK: int
    def run_test(self, test_name: str, parent_pipe) -> None: ...
    @property
    def is_master(self) -> bool: ...

EFA_PROBE_RESULT: Incomplete

def has_efa() -> bool:
    """
    If shell command `fi_info -p efa -t FI_EP_RDM` returns exit code 0 then we assume that the machine has
    Libfabric EFA interfaces and EFA software components installed,
    see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html.
    """
def tp_transports():
    '''
    If the machine has Libfabric EFA interfaces and EFA software components installed it may cause
    \'RuntimeError: In operator() at tensorpipe/common/ibv.h:172 "": Operation not supported\' if tensorpipe
    uses InfiniBand transport, so we exclude it from tensorpipe transports,
    see https://github.com/pytorch/pytorch/issues/73885 and https://github.com/pytorch/pytorch/issues/65022
    '''
def spawn_threads_and_init_comms(func: Incomplete | None = None, timeout=..., world_size=...):
    """
    Wrapper to use with a test method
    """

class MultiThreadedTestCase(TestCase):
    """
    Test runner that runs all tests with the in-proc process group using
    multiple threads with the threaded process group.

    Each test spawns world_size threads and run the test method in each thread.

    Difference from regular MultiProcess test runner:
    Must explicitly defines SetUp and call self._spawn_threads() to run the tests.
    Cannot use setUp / tearDown (must use perThreadSetup / perThreadShutdown)
        to set up / tear down each thread when running each test.
    No global state possible
        How bad of a limitation is this?
    """
    exception_queue: Incomplete
    MAIN_THREAD_RANK: int
    def join_or_run(self, fn): ...
    def __init__(self, method_name: str = 'runTest') -> None: ...
    def perThreadSetUp(self) -> None: ...
    def perThreadTearDown(self) -> None: ...
    rank: Incomplete
    threads: Incomplete
    def setUp(self) -> None:
        """
        setUp only set up things in the main thread, if you want to configure things
        in the spawned threads, use perThreadSetUp
        """
    def tearDown(self) -> None:
        """
        tearDown only set up things in the main thread, if you want to configure things
        in the spawned threads, use perThreadTearDown
        """
    def run_test_with_threaded_pg(self, test_name, rank, world_size) -> None:
        """
        Run the current test associated with `test_name` using the threaded process group.
        """
    @property
    def world_size(self) -> int: ...
    def assertEqualOnRank(self, x, y, msg: Incomplete | None = None, *, rank: int = 0) -> None:
        """
        The reason why we have this util function instead of
        self.assertEqual is all threads are sharing one CPU RNG
        so the assertion result is only reliable on rank 0
        """
    def assertNotEqualOnRank(self, x, y, msg: Incomplete | None = None, *, rank: int = 0) -> None: ...

class SaveForwardInputsModule(nn.Module):
    l: Incomplete
    forward_inputs: Incomplete
    cast_forward_inputs: Incomplete
    def __init__(self, forward_inputs: Dict[nn.Module, torch.Tensor], cast_forward_inputs: bool) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class SaveForwardInputsModel(nn.Module):
    c1: Incomplete
    c2: Incomplete
    forward_inputs: Incomplete
    def __init__(self, forward_inputs: Dict[nn.Module, torch.Tensor], cast_forward_inputs: bool) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class DynamoDistributedSingleProcTestCase(torch._dynamo.test_case.TestCase):
    """
    Test harness for single-process dynamo distributed tests,
    initializes dist process group.

    Prefer this for simple tests, as it's easier to debug.
    """
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...

class DynamoDistributedMultiProcTestCase(MultiProcessTestCase):
    """
    Use this for tests that actually run on multiple GPUs.

    Decorate tests with @skip_if_lt_x_gpu(ngpu)

    Note: MultiProcTestCase spawns processes per test and is slow.
    Prefer MultiThreadedTestCase for most tests. Perhaps use this one
    sparingly for integration tests.
    """
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    @property
    def world_size(self) -> int: ...
