from _typeshed import Incomplete
from torch.testing._internal.common_distributed import MultiProcessTestCase as MultiProcessTestCase
from torch.testing._internal.common_utils import IS_SANDCASTLE as IS_SANDCASTLE, TEST_WITH_DEV_DBG_ASAN as TEST_WITH_DEV_DBG_ASAN, find_free_port as find_free_port
from torch.testing._internal.distributed.ddp_under_dist_autograd_test import CudaDdpComparisonTest as CudaDdpComparisonTest, DdpComparisonTest as DdpComparisonTest, DdpUnderDistAutogradTest as DdpUnderDistAutogradTest
from torch.testing._internal.distributed.nn.api.remote_module_test import CudaRemoteModuleTest as CudaRemoteModuleTest, RemoteModuleTest as RemoteModuleTest, ThreeWorkersRemoteModuleTest as ThreeWorkersRemoteModuleTest
from torch.testing._internal.distributed.pipe_with_ddp_test import PipeWithDDPTest as PipeWithDDPTest
from torch.testing._internal.distributed.rpc.dist_autograd_test import CudaDistAutogradTest as CudaDistAutogradTest, DistAutogradTest as DistAutogradTest, FaultyAgentDistAutogradTest as FaultyAgentDistAutogradTest, TensorPipeAgentDistAutogradTest as TensorPipeAgentDistAutogradTest, TensorPipeCudaDistAutogradTest as TensorPipeCudaDistAutogradTest
from torch.testing._internal.distributed.rpc.dist_optimizer_test import DistOptimizerTest as DistOptimizerTest
from torch.testing._internal.distributed.rpc.examples.parameter_server_test import ParameterServerTest as ParameterServerTest
from torch.testing._internal.distributed.rpc.examples.reinforcement_learning_rpc_test import ReinforcementLearningRpcTest as ReinforcementLearningRpcTest
from torch.testing._internal.distributed.rpc.faulty_agent_rpc_test import FaultyAgentRpcTest as FaultyAgentRpcTest
from torch.testing._internal.distributed.rpc.jit.dist_autograd_test import JitDistAutogradTest as JitDistAutogradTest
from torch.testing._internal.distributed.rpc.jit.rpc_test import JitRpcTest as JitRpcTest
from torch.testing._internal.distributed.rpc.jit.rpc_test_faulty import JitFaultyAgentRpcTest as JitFaultyAgentRpcTest
from torch.testing._internal.distributed.rpc.rpc_agent_test_fixture import RpcAgentTestFixture as RpcAgentTestFixture
from torch.testing._internal.distributed.rpc.rpc_test import CudaRpcTest as CudaRpcTest, RpcTest as RpcTest, TensorPipeAgentCudaRpcTest as TensorPipeAgentCudaRpcTest, TensorPipeAgentRpcTest as TensorPipeAgentRpcTest
from typing import Dict, List, Type

class SpawnHelper(MultiProcessTestCase):
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

GENERIC_TESTS: Incomplete
GENERIC_CUDA_TESTS: Incomplete
TENSORPIPE_TESTS: Incomplete
TENSORPIPE_CUDA_TESTS: Incomplete
FAULTY_AGENT_TESTS: Incomplete

def generate_tests(prefix: str, mixin: Type[RpcAgentTestFixture], tests: List[Type[RpcAgentTestFixture]], module_name: str) -> Dict[str, Type[RpcAgentTestFixture]]:
    '''Mix in the classes needed to autogenerate the tests based on the params.

    Takes a series of test suites, each written against a "generic" agent (i.e.,
    derived from the abstract RpcAgentTestFixture class), as the `tests` args.
    Takes a concrete subclass of RpcAgentTestFixture, which specializes it for a
    certain agent, as the `mixin` arg. Produces all combinations of them.
    Returns a dictionary of class names to class type
    objects which can be inserted into the global namespace of the calling
    module. The name of each test will be a concatenation of the `prefix` arg
    and the original name of the test suite.
    The `module_name` should be the name of the calling module so
    that the classes can be fixed to make it look like they belong to it, which
    is necessary for pickling to work on them.
    '''
