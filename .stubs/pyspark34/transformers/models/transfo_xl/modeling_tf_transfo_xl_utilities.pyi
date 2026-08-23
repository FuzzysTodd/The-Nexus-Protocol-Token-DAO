import tensorflow as tf
from ...tf_utils import shape_list as shape_list
from _typeshed import Incomplete

class TFAdaptiveSoftmaxMask(tf.keras.layers.Layer):
    vocab_size: Incomplete
    d_embed: Incomplete
    d_proj: Incomplete
    cutoffs: Incomplete
    cutoff_ends: Incomplete
    div_val: Incomplete
    shortlist_size: Incomplete
    n_clusters: Incomplete
    head_size: Incomplete
    keep_order: Incomplete
    out_layers: Incomplete
    out_projs: Incomplete
    def __init__(self, vocab_size, d_embed, d_proj, cutoffs, div_val: int = 1, keep_order: bool = False, **kwargs) -> None: ...
    cluster_weight: Incomplete
    cluster_bias: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, hidden, target, return_mean: bool = True, training: bool = False): ...
