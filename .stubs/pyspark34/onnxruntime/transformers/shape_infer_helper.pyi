from _typeshed import Incomplete
from symbolic_shape_infer import SymbolicShapeInference
from typing import Dict

file_path: Incomplete
logger: Incomplete

class SymbolicShapeInferenceHelper(SymbolicShapeInference):
    model_: Incomplete
    all_shapes_inferred_: bool
    is_inferred_: bool
    dynamic_axis_mapping_: Incomplete
    def __init__(self, model, verbose: int = 0, int_max=..., auto_merge: bool = True, guess_output_rank: bool = False) -> None: ...
    def infer(self, dynamic_axis_mapping: Dict[str, int], max_runs: int = 128):
        '''Run shape inference, and try replace dynamic axis from string to integer when mapping is provided.

        Args:
            dynamic_axis_mapping (_type_): a dictionary with name of dynamic axis as key, like {"batch_size" : 4}
            max_runs (int, optional): limit maximum number of runs to avoid infinite loop. Defaults to 32.

        Returns:
            bool: whether all shapes has been inferred or not.
        '''
    def get_edge_shape(self, edge):
        """Get shape of an edge.

        Args:
            edge (str): name of edge

        Returns:
            Optional[List[int]]: the shape, or None if shape is unknown
        """
    def compare_shape(self, edge, edge_other):
        """Compare shape of two edges.

        Args:
            edge (str): name of edge
            edge_other (str): name of another edge

        Raises:
            Exception: At least one shape is missed for edges to compare

        Returns:
            bool: whether the shape is same or not
        """
