from _typeshed import Incomplete
from torch.distributed._tensor.op_schema import OpSchema as OpSchema, OutputSharding as OutputSharding
from torch.distributed._tensor.ops.common_rules import linear_pointwise_rule as linear_pointwise_rule, pointwise_rule as pointwise_rule
from torch.distributed._tensor.ops.utils import register_prop_rule as register_prop_rule
from torch.distributed._tensor.placement_types import DTensorSpec as DTensorSpec, Replicate as Replicate

aten: Incomplete
linear_pointwise_ops: Incomplete
pointwise_ops: Incomplete
