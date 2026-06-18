import tensorflow as tf
from . import default_layers as default_layers
from _typeshed import Incomplete

class Compressor:
    """
    Common base class for all compressors.

    This class is designed for other base classes.
    Algorithms should inherit ``Pruner`` or ``Quantizer`` instead.

    Attributes
    ----------
    compressed_model : tf.keras.Model
        Compressed user model.
    wrappers : list of tf.keras.Model
        A wrapper is an instrumented TF ``Layer``, in ``Model`` format.

    Parameters
    ----------
    model : tf.keras.Model
        The user model to be compressed.
    config_list : list of JSON object
        User configuration. The format is detailed in tutorial.
    LayerWrapperClass : a class derive from Model
        The class used to instrument layers.
    """
    compressed_model: Incomplete
    wrappers: Incomplete
    def __init__(self, model, config_list, LayerWrapperClass) -> None: ...
    def set_wrappers_attribute(self, name, value) -> None:
        """
        Call ``setattr`` on all wrappers.
        """
    def validate_config(self, model, config_list) -> None:
        """
        Compression algorithm should overload this function to validate configuration.
        """

class LayerWrapper(tf.keras.Model):
    """
    Abstract base class of layer wrappers.

    Concrete layer wrapper classes must inherit this to support ``isinstance`` check.
    """
    def __init__(self) -> None: ...

class Pruner(Compressor):
    """
    Base class for pruning algorithms.

    End users should use ``compress`` and callback APIs (WIP) to prune their models.

    The underlying model is instrumented upon initialization of pruner object.
    So if you want to pre-train the model, train it before creating pruner object.

    The compressed model can only execute in eager mode.

    Algorithm developers should override ``calc_masks`` method to specify pruning strategy.

    Parameters
    ----------
    model : tf.keras.Model
        The user model to prune.
    config_list : list of JSON object
        User configuration. The format is detailed in tutorial.
    """
    def __init__(self, model, config_list) -> None: ...
    def compress(self):
        """
        Apply compression on a pre-trained model.

        If you want to prune the model during training, use callback API (WIP) instead.

        Returns
        -------
        tf.keras.Model
            The compressed model.
        """
    def export_model(self, model_path, mask_path: Incomplete | None = None) -> None:
        '''
        Export pruned model and optionally mask tensors.

        Parameters
        ----------
        model_path : path-like
            The path passed to ``Model.save()``.
            You can use ".h5" extension name to export HDF5 format.
        mask_path : path-like or None
            Export masks to the path when set.
            Because Keras cannot save tensors without a ``Model``,
            this will create a model, set all masks as its weights, and then save that model.
            Masks in saved model will be named by corresponding layer name in compressed model.

        Returns
        -------
        None
        '''
    def calc_masks(self, wrapper, **kwargs) -> None:
        """
        Abstract method to be overridden by algorithm. End users should ignore it.

        If the callback is set up, this method will be invoked at end of each training minibatch.
        If not, it will only be called when end user invokes ``compress``.

        Parameters
        ----------
        wrapper : PrunerLayerWrapper
            The instrumented layer.
        **kwargs
            Reserved for forward compatibility.

        Returns
        -------
        dict of (str, tf.Tensor), or None
            The key is weight ``Variable``'s name. The value is a mask ``Tensor`` of weight's shape and dtype.
            If a weight's key does not appear in the return value, that weight will not be pruned.
            Returning ``None`` means the mask is not changed since last time.
            Weight names are globally unique, e.g. `model/conv_1/kernel:0`.
        """

class PrunerLayerWrapper(LayerWrapper):
    """
    Instrumented TF layer.

    Wrappers will be passed to pruner's ``calc_masks`` API,
    and the pruning algorithm should use wrapper's attributes to calculate masks.

    Once instrumented, underlying layer's weights will get **modified** by masks before forward pass.

    Attributes
    ----------
    layer : tf.keras.layers.Layer
        The original layer.
    config : JSON object
        Selected configuration. The format is detailed in tutorial.
    pruner : Pruner
        Bound pruner object.
    masks : dict of (str, tf.Tensor)
        Current masks. The key is weight's name and the value is mask tensor.
        On initialization, `masks` is an empty dict, which means no weight is pruned.
        Afterwards, `masks` is the last return value of ``Pruner.calc_masks``.
        See ``Pruner.calc_masks`` for details.
    """
    layer: Incomplete
    config: Incomplete
    pruner: Incomplete
    masks: Incomplete
    def __init__(self, layer, config, pruner) -> None: ...
    def call(self, *inputs): ...
