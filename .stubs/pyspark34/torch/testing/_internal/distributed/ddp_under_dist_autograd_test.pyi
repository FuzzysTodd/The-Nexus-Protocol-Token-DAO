import abc
import enum
import torch
import torch.distributed as dist
import torch.nn as nn
from _typeshed import Incomplete
from torch.distributed import rpc as rpc
from torch.distributed.nn import RemoteModule as RemoteModule
from torch.nn.parallel import DistributedDataParallel as DistributedDataParallel
from torch.testing._internal.common_distributed import requires_gloo as requires_gloo, requires_nccl as requires_nccl, skip_if_lt_x_gpu as skip_if_lt_x_gpu, skip_if_rocm as skip_if_rocm
from torch.testing._internal.dist_utils import INIT_METHOD_TEMPLATE as INIT_METHOD_TEMPLATE, dist_init as dist_init
from torch.testing._internal.distributed.rpc.rpc_agent_test_fixture import RpcAgentTestFixture as RpcAgentTestFixture
from typing import NamedTuple

NUM_EM_ROW: int
D_SPARSE: int
D_DENSE: int
D_HID: int
D_OUT: int
NUM_TRAINERS: int
WORLD_SIZE: Incomplete
TRAINER_RANKS: Incomplete
REMOTE_WORKER_RANK: Incomplete
MASTER_RANK: Incomplete

class DdpMode(enum.Enum):
    NONE: Incomplete
    OUTSIDE: Incomplete
    INSIDE: Incomplete

def init_logger(): ...

gLogger: Incomplete

class FeatureSet(NamedTuple):
    """ A feature set has 2 types of features"""
    dense_features: torch.Tensor
    sparse_features: torch.LongTensor
    values: torch.Tensor

class RemoteEM(nn.Module):
    em: Incomplete
    def __init__(self, num_embeddings: int, embedding_dim: int) -> None: ...
    def forward(self, input: torch.Tensor): ...

def getLinear(d_in, d_out): ...

class RemoteNet(nn.Module):
    fc: Incomplete
    relu: Incomplete
    def __init__(self, d_in: int, d_out: int) -> None: ...
    def forward(self, input: torch.Tensor): ...

class HybridModel(nn.Module):
    remote_em_rref: Incomplete
    remote_net_rref: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    non_ddp_params: Incomplete
    ddp_params: Incomplete
    def __init__(self, remote_em_rref: rpc.RRef, remote_net_rref: rpc.RRef, process_group_for_ddp: dist.ProcessGroup = None) -> None: ...
    def forward(self, input: FeatureSet): ...

class Trainer:
    rank: Incomplete
    trainer_group: Incomplete
    remote_em_rref: Incomplete
    remote_net_rref: Incomplete
    hybrid_module: Incomplete
    non_ddp_params: Incomplete
    def __init__(self, remote_em_rref: rpc.RRef, remote_net_rref: rpc.RRef, ddp_mode: DdpMode, rank: int) -> None: ...
    def destroy_pg(self) -> None: ...
    def train_batch(self, mini_batch: FeatureSet, trainer_has_less_inputs: bool, simulate_uneven_inputs: bool): ...

def get_training_examples(): ...

shutdown_signal: Incomplete

def set_shutdown_signal() -> None: ...

class DdpUnderDistAutogradTest(RpcAgentTestFixture, metaclass=abc.ABCMeta):
    @property
    def world_size(self) -> int: ...
    def remote_worker_name(self) -> str: ...
    def trainer_name(self, rank): ...
    def do_test_on_master(self, ddp_mode: DdpMode, simulate_uneven_inputs: bool, remote_em_rref: rpc.RRef, remote_net_rref: rpc.RRef): ...
    def test_backward_no_ddp(self) -> None: ...
    def test_backward_ddp_outside(self) -> None: ...
    def test_backward_ddp_outside_uneven_inputs(self) -> None: ...
    def test_backward_ddp_inside(self) -> None: ...

class CommonDdpComparisonTest(RpcAgentTestFixture, metaclass=abc.ABCMeta):
    @property
    def world_size(self) -> int: ...
    def trainer_name(self, rank): ...
    @staticmethod
    def get_remote_grads(rref, context_id): ...

class DdpComparisonTest(CommonDdpComparisonTest, metaclass=abc.ABCMeta):
    def test_ddp_comparison(self) -> None: ...
    def test_ddp_comparison_uneven_inputs(self) -> None: ...
    def test_ddp_dist_autograd_sparse_grads(self) -> None: ...
    def test_ddp_dist_autograd_local_vs_remote(self) -> None: ...

class CudaDdpComparisonTest(CommonDdpComparisonTest, metaclass=abc.ABCMeta):
    def test_ddp_dist_autograd_local_vs_remote_gpu(self) -> None: ...
