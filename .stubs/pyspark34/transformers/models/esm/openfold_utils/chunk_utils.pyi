from .tensor_utils import tensor_tree_map as tensor_tree_map, tree_map as tree_map
from _typeshed import Incomplete
from typing import Any, Callable, Dict

def chunk_layer(layer: Callable, inputs: Dict[str, Any], chunk_size: int, no_batch_dims: int, low_mem: bool = False, _out: Any = None, _add_into_out: bool = False) -> Any:
    '''
    Implements the "chunking" procedure described in section 1.11.8.

    Layer outputs and inputs are assumed to be simple "pytrees," consisting only of (arbitrarily nested) lists, tuples,
    and dicts with torch.Tensor leaves.

    Args:
        layer:
            The layer to be applied chunk-wise
        inputs:
            A (non-nested) dictionary of keyworded inputs. All leaves must be tensors and must share the same batch
            dimensions.
        chunk_size:
            The number of sub-batches per chunk. If multiple batch dimensions are specified, a "sub-batch" is defined
            as a single indexing of all batch dimensions simultaneously (s.t. the number of sub-batches is the product
            of the batch dimensions).
        no_batch_dims:
            How many of the initial dimensions of each input tensor can be considered batch dimensions.
        low_mem:
            Avoids flattening potentially large input tensors. Unnecessary in most cases, and is ever so slightly
            slower than the default setting.
    Returns:
        The reassembled output of the layer on the inputs.
    '''

class ChunkSizeTuner:
    max_chunk_size: Incomplete
    cached_chunk_size: Incomplete
    cached_arg_data: Incomplete
    def __init__(self, max_chunk_size: int = 512) -> None: ...
    def tune_chunk_size(self, representative_fn: Callable, args: tuple, min_chunk_size: int) -> int: ...
