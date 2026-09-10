from _typeshed import Incomplete
from fusion_base import Fusion
from onnx import NodeProto as NodeProto
from onnx_model import OnnxModel as OnnxModel
from typing import Dict, List, Tuple

logger: Incomplete

class FusionEmbedLayerNoMask(Fusion):
    """
    Fuse embedding layer into one node (EmbedLayerNormalization).
    It supports the following model types: BERT, DistilBert, ALBert.
    """
    utils: Incomplete
    shape_infer_helper: Incomplete
    attention: Incomplete
    embed_node: Incomplete
    def __init__(self, model: OnnxModel, description: str = 'no mask') -> None: ...
    def match_two_gather(self, add: NodeProto) -> None | Tuple[NodeProto, NodeProto]: ...
    cross_attention: Incomplete
    def check_attention_subgraph(self, layernorm: NodeProto, input_name_to_nodes: Dict[str, List[NodeProto]], is_distil_bert: bool) -> bool:
        """Check that LayerNormalization has a child of Attention node or subgraph like Attention.

        Args:
            layernorm (NodeProto): LayerNormalization node
            input_name_to_nodes (Dict[str, List[NodeProto]]): map from input name to nodes
            is_distil_bert (bool): whether it is DistilBert or not

        Returns:
            bool: whether there is Attention node or subgraph like Attention
        """
    def match_position_embedding_distilbert(self, position_embedding_gather, input_ids, output_name_to_node):
        """  Match position embedding path from input_ids to Gather for DistilBert.

        Pattern is like the following:
                 (input_ids)
                      |
                     Shape
                       |                          |    Gather (indices=1)
                       |       |
                       |      Cast (optional)
                       |       |
                       |      Range (start=0, end=*, delta=1)
                       |       |
                       |    Unsqueeze
                       |    /
                      Expand
                        |
                      Gather
        """
    def match_position_embedding_roberta(self, position_embedding_gather, input_ids, output_name_to_node):
        '''Match position embedding path from input_ids to Gather for Roberta.

        Roberta Embedding Layer Pattern (* is optional since it might be removed by ORT, ? is the padding word id):
          (input_ids) --> Equal(B=?) -- Not -- Cast(to=6) -- CumSum(axis=1) -- Mul -- Cast(to=7) -- Add(B=1) -- Cast(to=7)* --> Gather
                                                |                              ^
                                                V                              |
                                                +------------------------------+

        Roberta new pattern from transformers v4.9:
           (input_ids) --> Equal(B=?) -- Not -- Cast(to=6) -- CumSum(axis=1) -- Add(B=0) -- Mul -- Cast(to=7) -- Add(B=1) --> Gather
                                                |                                           ^
                                                V                                           |
                                                +-------------------------------------------+

        start_node = position_embedding_gather
        start_index = 1

        # match optional Cast node.
        parent = self.model.get_parent(start_node, start_index, output_name_to_node)
        if parent is None:
            return
        if parent.op_type == "Cast":
            if OnnxModel.get_node_attribute(parent, "to") != 7:
                return
            start_node = parent
            start_index = 0

        i, path, return_indices = self.model.match_parent_paths(
            start_node,
            [ ([\'Add\', \'Cast\', \'Mul\', \'CumSum\', \'Cast\', \'Not\', \'Equal\'], [start_index, 0, 0, 0, 0, 0, 0]),
              ([\'Add\', \'Cast\', \'Mul\', \'Add\', \'CumSum\', \'Cast\', \'Not\', \'Equal\'], [start_index, 0, 0, 0, 0, 0, 0, 0])],
            output_name_to_node)

        if path is not None:
            # constant input of Add shall be 1.
            i, value = self.model.get_constant_input(path[0])
            if value != 1:
                return False

            _, self.padding_word_id = self.model.get_constant_input(path[-1])

            return input_ids == path[-1].input[0]
        '''
    def match_position_embedding_bert(self, position_embedding_gather, input_ids, output_name_to_node):
        """  Match position embedding path from input_ids to Gather for BERT.

        BERT Embedding Layer Pattern:
                                    (input_ids)
                                   /                                          /          Shape
                                /              |
                              /              Gather (indices=1)
                             /                  |
                            /                  Add (optional, B=0)
                           /                    |
                        Gather (segment_ids) Unsqueeze (axes=0)
                           \\        |           |
                            \\     Gather      Slice (data[1,512], starts=0, ends=*, axes=1, steps=1)
                              \\    /            |
                                Add          Gather
                                   \\       /
                                      Add
                                       |
                                LayerNormalization
        """
    def match_position_embedding(self, position_embedding_gather, input_ids, output_name_to_node): ...
    def check_embedding(self, word_embedding_gather, segment_embedding_gather, position_embedding_gather):
        """Sanity check of embedding weights, and match hidden_size of weights and shape of inputs."""
    def cast_to_int32(self, input_name: str) -> Tuple[str, None | NodeProto]:
        """Cast a graph input or node input to int32.

        Args:
            input_name (str): name of graph input or node input

        Returns:
            A tuple of casted input name and the cast node.
            int32_output (str): If input is int32, it is the input name, Otherwise it is output name of Cast node.
            input_cast_node (Union[None, NodeProto]): Cast node. It could be None if input is int32.
        """
    def create_fused_node(self, input_ids: str, layernorm: NodeProto, word_embedding_gather: NodeProto, position_embedding_gather: NodeProto, segment_embedding_gather: None | NodeProto, position_ids: str | None = None, embedding_sum_output: bool = False):
        """Create an EmbedLayerNormalization node. Note that segment embedding is optional.

        Args:
            input_ids (str): input_ids for word embeddings
            layernorm (NodeProto): LayerNormalization or SkipLayerNormalization node.
            word_embedding_gather (NodeProto): the Gather node for word embedding
            position_embedding_gather (NodeProto): the Gather node for position embedding
            segment_embedding_gather (Union[None, NodeProto]): the Gather node for segment embedding, or None.

        Returns:
            NodeProto: the EmbedLayerNormalization node created.
        """
    prune_graph: bool
    def finish_fusion(self, layernorm, embed_node) -> None: ...
    def is_embedding_sum_needed(self, add_before_layer_norm):
        """Check that Add before layer norm has an output to add before next layernorm

        Args:
            add_before_layer_norm (NodeProto): Add before any LayerNormalization node in topological order of graph

        Returns:
            bool: whether there is an extra output needed out of embed layer norm node
        """
    def fuse_gpt2(self, layernorm, add_before_layernorm, input_name_to_nodes, output_name_to_node, optional_segment_gather: Incomplete | None = None): ...
    def fuse_distilbert(self, layernorm, add_before_layernorm, input_name_to_nodes, output_name_to_node):
        """Fuse embedding layer for DistilBert
        Args:
            layernorm (NodeProto): node of LayerNormalization or SkipLayerNormalization
            add_before_layernorm (NodeProto): the Add node before LayerNormalization, or the SkipLayerNormalization itself
            input_name_to_nodes (Dict[str, List[NodeProto]]): map from input name to nodes
            output_name_to_node (Dict[str, List[NodeProto]]): map from output name to nodes
        """
    def fuse_bert(self, layernorm, add_before_layernorm, input_name_to_nodes, output_name_to_node):
        """Fuse embedding layer for Bert
        Args:
            layernorm (NodeProto): node of LayerNormalization or SkipLayerNormalization
            add_before_layernorm (NodeProto): the Add node before LayerNormalization, or the SkipLayerNormalization itself
            input_name_to_nodes (Dict[str, List[NodeProto]]): map from input name to nodes
            output_name_to_node (Dict[str, List[NodeProto]]): map from output name to nodes
        """
    def fuse(self, node, input_name_to_nodes, output_name_to_node) -> None: ...

class FusionEmbedLayerNormalization(FusionEmbedLayerNoMask):
    use_mask_index: Incomplete
    def __init__(self, model: OnnxModel, use_mask_index: bool = False) -> None: ...
    def replace_mask(self, mask_int32, attention_nodes) -> None: ...
    attention: Incomplete
    cross_attention: Incomplete
    embed_node: Incomplete
    def fuse(self, node, input_name_to_nodes, output_name_to_node) -> None: ...
