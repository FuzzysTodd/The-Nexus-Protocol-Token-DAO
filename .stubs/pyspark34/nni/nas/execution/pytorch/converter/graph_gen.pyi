from .op_types import MODULE_EXCEPT_LIST as MODULE_EXCEPT_LIST, OpTypeName as OpTypeName
from .utils import build_cand_name as build_cand_name, build_full_name as build_full_name, build_python_name as build_python_name, get_full_name_by_scope_name as get_full_name_by_scope_name, is_layerchoice_node as is_layerchoice_node, match_node as match_node
from _typeshed import Incomplete
from nni.nas.execution.common import Cell as Cell, Graph as Graph, Model as Model, Node as Node, Operation as Operation
from nni.nas.nn.pytorch import InputChoice as InputChoice, LayerChoice as LayerChoice, Placeholder as Placeholder
from nni.nas.utils import get_importable_name as get_importable_name, get_init_parameters_or_fail as get_init_parameters_or_fail

class GraphConverter:
    global_seq: int
    global_graph_id: int
    def __init__(self) -> None: ...
    def create_prim_constant_node(self, ir_graph, node, module_name): ...
    def handle_prim_attr_node(self, node, module): ...
    def remove_unconnected_nodes(self, ir_graph, targeted_type: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        ir_graph : Graph
            our ir graph representation
        targeted_type : str
            nodes with ```targeted_type``` will be removed from graph if their fanout is 0.
            ```None``` means removing all the nodes whose fanout is 0.
        """
    def handle_graph_nodes(self, script_module, sm_graph, module, module_name, module_python_name, ir_model, ir_graph, shared_module_index: Incomplete | None = None):
        """
        Convert torch script node to our node ir, and build our graph ir

        Parameters
        ----------
        script_module : torch.jit.RecursiveScriptModule
            the torch script of ```module```
        sm_graph : torch._C.Graph
            the graph in torch script
        module : nn.Module
            the targeted pytorch module
        module_name : str
            ```module```'s name
        ir_model : Model
            the whole graph ir
        ir_graph : Graph
            the graph ir of ```module```
        shared_module_index : dict
            it is used for knowing which module has been created an ir node,
            if created and invoked again, then the new ir node can simply reference that ir node.
            this way we can identify shared modules (i.e., one module invoked multiple times in `forward` function)

        Returns
        -------
        dict
            the mapping from graph node to our graph ir node
        """
    def merge_aten_slices(self, ir_graph) -> None:
        """
        if there is aten::slice node, merge the consecutive ones together.
        ```x[:, :, 1:, 1:]``` in python code will be converted into 4 node in torch script,
        each node has 5 inputs: tensor, dim, x, y, z (i.e., x:y:z)
        """
    def refine_graph(self, ir_graph) -> None:
        """
        Do the following process to simplify graph:
        1. remove unconnected constant node
        2. remove unconnected getattr node
        """
    def convert_module(self, script_module, module, module_name, ir_model):
        """
        Convert a module to its graph ir (i.e., Graph) along with its input arguments

        Parameters
        ----------
        script_module : torch.jit.RecursiveScriptModule
            the script module of ```module``` obtained with torch.jit.script
        module : nn.Module
            the targeted module instance
        module_name : str
            the constructed name space of ```module```
        ir_model : Model
            the whole graph ir

        Returns
        -------
        Graph
            the built graph ir from module, ```None``` means do not further parse the module
        dict
            the input arguments of this module
        """

class GraphConverterWithShape(GraphConverter):
    """
    Convert a pytorch model to nni ir along with input/output shape info.
    Based ir acquired through ``torch.jit.script``
    and shape info acquired through ``torch.jit.trace``.

    .. warning::

        Known issues:

        1. ``InputChoice`` and ``ValueChoice`` not supported yet.
        2. Currently random inputs are fed while tracing layerchoice.
           If forward path of candidates depends on input data, then wrong path will be traced.
           This will result in incomplete shape info.
    """
    def convert_module(self, script_module, module, module_name, ir_model, dummy_input): ...
    def propagate_shape(self, ir_model: Model): ...
    def remove_dummy_nodes(self, ir_model: Model): ...

def convert_to_graph(script_module, module, converter: Incomplete | None = None, **kwargs):
    """
    Convert module to our graph ir, i.e., build a :class:`Model` type

    Parameters
    ----------
    script_module : torch.jit.RecursiveScriptModule
        the script module obtained with torch.jit.script
    module : nn.Module
        the targeted module instance
    converter : `TorchConverter`
        default `GraphConverter` is used
    kwargs:
        will be passed to `converter.convert_module()`

    Returns
    -------
    Model
        the constructed IR model
    """
