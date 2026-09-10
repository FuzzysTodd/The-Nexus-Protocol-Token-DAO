from _typeshed import Incomplete
from enum import Enum
from torch.fx.node import Node as Node, map_arg as map_arg
from typing import Dict, List, NamedTuple, Set

class Partition:
    """Partition class contains all the information about an individual partition.
    It also provides necessary methods for manipulation the partition.
    """
    nodes: Incomplete
    partition_id: Incomplete
    parents: Incomplete
    children: Incomplete
    bfs_level: int
    used_mem_bytes: int
    logical_device_ids: Incomplete
    def __init__(self, partition_id: int) -> None: ...
    def recalculate_mem_size(self) -> None: ...
    def add_node(self, node): ...
    def remove_node(self, node): ...

class Device(NamedTuple):
    name: str
    available_mem_bytes: int
    logical_id: int

class NodeLatency(NamedTuple):
    mem_latency_sec: float
    computer_latency_sec: float

class PartitionLatency(NamedTuple):
    mem_latency_sec: float
    computer_latency_sec: float
    overall_latency_sec: float

class PartitionMode(Enum):
    size_based: int
    sparse_nn: int
    cost_aware: int
    kl_based: int
    aot_based: int

class PartitionerConfig(NamedTuple):
    devices: List[Device]
    mode: PartitionMode = ...
    transfer_rate_bytes_per_sec: float = ...
    node_to_latency_mapping: Dict[Node, NodeLatency] = ...
    node_to_partition_mapping: Dict[Node, int] = ...
    partition_to_logical_device_mapping: Dict[int, List[int]] = ...
    saturate_host: bool = ...

def get_extra_size_of(node: Node, nodes: Set[Node]) -> int:
    """Given a node and a set of nodes,
    this function return the extra size that needed
    if this node is included in this set.
    """
def get_latency_of_one_partition(partition: Partition, node_to_latency_mapping: Dict[Node, NodeLatency]) -> PartitionLatency:
    """Given a partiton and its nodes' latency, return a PartitionLatency for this partition"""
def get_partition_to_latency_mapping(partitions: List[Partition], node_to_latency_mapping: Dict[Node, NodeLatency]) -> Dict[Partition, PartitionLatency]:
    """Given all the partitions and node_to_latency_mapping dictionary,
    return a mapping dictionary of each partition to its overall latency
    """
def get_comm_latency_between(parent_partition: Partition, child_partition: Partition, transfer_rate_bytes_per_sec: float):
    """Given two partitions (parent and child),
    calculate the communication latency between the two.
    """
def get_latency_of_partitioned_graph(partitions: List[Partition], partition_to_latency_mapping: Dict[Partition, PartitionLatency], transfer_rate_bytes_per_sec: float):
    """Given all paritions in a graph, find the critical path among all partitions
    and return its latency as the latency of the whole graph
    """
