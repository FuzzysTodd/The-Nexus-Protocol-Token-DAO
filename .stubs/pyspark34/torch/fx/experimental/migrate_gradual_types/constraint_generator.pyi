from _typeshed import Incomplete
from torch.fx.experimental.migrate_gradual_types.constraint import ApplyBroadcasting as ApplyBroadcasting, BinConstraintD as BinConstraintD, BinConstraintT as BinConstraintT, CalcConv as CalcConv, CalcMaxPool as CalcMaxPool, CalcProduct as CalcProduct, CanReshape as CanReshape, Conj as Conj, DGreatestUpperBound as DGreatestUpperBound, DVar as DVar, Disj as Disj, F as F, GetItem as GetItem, GetItemTensor as GetItemTensor, IndexSelect as IndexSelect, T as T, TGreatestUpperBound as TGreatestUpperBound, TVar as TVar, Transpose as Transpose
from torch.fx.experimental.migrate_gradual_types.operation import op_add as op_add, op_consistency as op_consistency, op_div as op_div, op_eq as op_eq, op_gt as op_gt, op_leq as op_leq, op_lt as op_lt, op_matching as op_matching, op_mul as op_mul, op_neq as op_neq, op_precision as op_precision, op_sub as op_sub
from torch.fx.experimental.migrate_gradual_types.util import gen_bvar as gen_bvar, gen_dvar as gen_dvar, gen_nat_constraints as gen_nat_constraints, gen_tensor_dims as gen_tensor_dims, gen_tvar as gen_tvar
from torch.fx.node import Node as Node, Target as Target
from torch.fx.tensor_type import Dyn as Dyn, TensorType as TensorType
from torch.nn.modules.batchnorm import BatchNorm2d as BatchNorm2d
from torch.nn.modules.conv import Conv2d as Conv2d

MAX_TENSOR_RANK: int

def register_inference_rule(call_target): ...
def generate_flatten_constraints(start_dim, end_dim, input, flattened, n, counter): ...
def get_attr_inference_rule(n: Node, symbols, constraints, counter):
    '''
    If the attribute is "device" then the tensor shape is preserved
    '''
def bmm_inference_rule(n: Node, symbols, constraints, counter):
    """
    Constraints that match the input to a size 3 tensor
    and switch the dimensions according to the rules
    of batch multiplication
    """
def index_select_inference_rule(n: Node, symbols, constraints, counter):
    """
    We constrain the second argument to a vector or Dyn.
    The output replaces the input with the shape of the vector
    at the position given by the index (first argument)
    """
def expand_inference_rule(n: Node, symbols, constraints, counter):
    """
    We generate the exact constraints as we do for tensor additions but we constraint
    the rank of this expression to be equal to len(n.args[1:]) so that only
    those cases get considered for the output
    """
def equality_inference_rule(n: Node, symbols, constraints, counter):
    """
    We generate the constraint: input = output
    """
def transpose_inference_rule(n: Node, symbols, constraints, counter):
    """
    Can be considered as a sequence of two index selects, so we generate constraints accordingly
    """
def type_inference_rule(n: Node, symbols, constraints, counter):
    """
    We generate the constraint: input = output
    """
def masked_fill_inference_rule(n: Node, symbols, constraints, counter):
    """
    Similar to addition. For now we implemenent the constraints when
    the argument is a boolean tensor. There is also a case for when
    it is a condition. We will leave this out for now.
    """
def embedding_inference_rule_functional(n: Node, symbols, constraints, counter): ...
def embedding_inference_rule(n: Node, module_instance, symbols, constraints, counter):
    """
    The output shape differs from the input shape in the last dimension
    """
def gen_embedding_rules(n: Node, symbols, embedding_dim, counter): ...
def tensor_inference_rule(n: Node, symbols, constraints, counter):
    """
    If the tensor is a scalar, we will skip it since we
    do not support scalars yet. We will add support in the future
    if it's needed. For our examples so far, scalars are not needed.
    """
def view_inference_rule(n: Node, symbols, constraints, counter):
    """
    Similar to reshape but with an extra condition on the strides
    """
def size_inference_rule(n: Node, symbols, constraints, counter):
    """
    The constraint is just lhs = rhs.
    Ex: size = input_ids.size()
    """
def range_check(i, n):
    """
    Checks if an index i is within range of a size n list
    Args:
        i: index
        n: list size

    Returns: Boolean
    """
def cumsum_inference_rule(n: Node, symbols, constraints, counter):
    """
    Input and output shapes should be equal
    We should verify that the index is valid
    """
def assert_inference_rule(n: Node, symbols, constraints, counter): ...
def getitem_inference_rule(n: Node, symbols, constraints, counter): ...
def gt_inference_rule(n: Node, symbols, constraints, counter): ...
def eq_inference_rule(n: Node, symbols, constraints, counter): ...
def neq_inference_rule(n: Node, symbols, constraints, counter):
    """
    Translates to inconsistent in gradual types.
    To prove inequality, we should prove that
    tensors are either different sizes or
    disagree on at least one dimension

    This is a WIP (works when the condition
    is false. We are working on making this operation work
    when the condition is true as well)
    """
def lt_inference_rule(n: Node, symbols, constraints, counter): ...
def full_inference_rule(n: Node, symbols, constraints, counter): ...
def arange_inference_rule(n: Node, symbols, constraints, counter): ...
def gen_broadcasting_constraints(e1, e2, symbols, counter, output_var): ...
def broadcasting_inference_rule(n: Node, symbols, constraints, counter): ...
def flatten_inference_rule(n: Node, symbols, constraints, counter): ...
def layer_norm_functional(n: Node, symbols, constraints, counter):
    """
    We generate the constraint: input = output
    """
def layer_norm_inference_rule(n: Node, module_instance, symbols, constraints, counter):
    """
    Input and output shapes should be equal.
    Input should be consistent with the normalized_shape
    """
def gen_layer_norm_constraints(n: Node, normalized_shape, symbols, counter): ...
def relu_inference_rule(n: Node, module_instance, symbols, constraints, counter):
    """
    Input and output shapes should be equal.
    """
def linear_inference_rule(n: Node, module_instance, symbols, constraints, counter):
    """
    Input and output sizes should be the same except for the last dimension
    If the input is Dyn, then so should the output
    """
def torch_dim_inference_rule(n: Node, symbols, constraints, counter): ...
def torch_linear_inference_rule(n: Node, symbols, constraints, counter): ...
def linear_constraints(n: Node, in_features, out_features, symbols, counter): ...
def add_layer_norm_constraints(input_dim, normalized_dim):
    """
    The constraints say that the type has te form: [*, 1024, 1024]
     while the normalized_dim have the form [1024, 1024]
    Args:
        input_dim: Input shape of layer norm
        normalized_dim: normalized_dim parameter of the module instance

    """
def add_linear_constraints(dims1, dims2, in_features, out_features): ...
def reshape_inference_rule(n: Node, symbols, constraints, counter): ...
def batchnorm_inference_rule(n: Node, module_instance, symbols, constraints, counter): ...
def adaptive_inference_rule(n: Node, module_instance, symbols, constraints, counter): ...
def conv2d_inference_rule(n: Node, module_instance, symbols, constraints, counter): ...
def maxpool_inference_rule(n: Node, module_instance, symbols, constraints, counter): ...

class ConstraintGenerator:
    traced: Incomplete
    traced_params: Incomplete
    constraints: Incomplete
    symbol_dict: Incomplete
    graph: Incomplete
    def __init__(self, traced, graph: Incomplete | None = None) -> None: ...
    def generate_constraints(self, counter: int = 0):
        """
        Iterate through every node and generate constraints
        Effect: self.constraints will be populated with the final constraints
        """
    def generate_constraints_node(self, n: Node, counter):
        """
        Generate constraints the given node:
        Currently supported operations:
        - Reshape
        - Add
        - conv2d
        """
