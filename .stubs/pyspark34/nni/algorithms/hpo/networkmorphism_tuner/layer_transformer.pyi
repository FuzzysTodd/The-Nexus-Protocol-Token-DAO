from .layers import StubDense as StubDense, StubReLU as StubReLU, get_batch_norm_class as get_batch_norm_class, get_conv_class as get_conv_class, get_n_dim as get_n_dim

NOISE_RATIO: float

def deeper_conv_block(conv_layer, kernel_size, weighted: bool = True):
    """deeper conv layer.
    """
def dense_to_deeper_block(dense_layer, weighted: bool = True):
    """deeper dense layer.
    """
def wider_pre_dense(layer, n_add, weighted: bool = True):
    """wider previous dense layer.
    """
def wider_pre_conv(layer, n_add_filters, weighted: bool = True):
    """wider previous conv layer.
    """
def wider_next_conv(layer, start_dim, total_dim, n_add, weighted: bool = True):
    """wider next conv layer.
    """
def wider_bn(layer, start_dim, total_dim, n_add, weighted: bool = True):
    """wider batch norm layer.
    """
def wider_next_dense(layer, start_dim, total_dim, n_add, weighted: bool = True):
    """wider next dense layer.
    """
def add_noise(weights, other_weights):
    """add noise to the layer.
    """
def init_dense_weight(layer) -> None:
    """initilize dense layer weight.
    """
def init_conv_weight(layer):
    """initilize conv layer weight.
    """
def init_bn_weight(layer) -> None:
    """initilize batch norm layer weight.
    """
