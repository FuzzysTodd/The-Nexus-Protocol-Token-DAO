from keras.mixed_precision import policy as policy
from keras.saving.legacy import serialization as serialization
from keras.saving.legacy.saved_model import base_serialization as base_serialization, constants as constants, save_impl as save_impl, serialized_attributes as serialized_attributes

class LayerSavedModelSaver(base_serialization.SavedModelSaver):
    """Implements Layer SavedModel serialization."""
    @property
    def object_identifier(self): ...
    @property
    def python_properties(self): ...
    def objects_to_serialize(self, serialization_cache): ...
    def functions_to_serialize(self, serialization_cache): ...

def get_serialized(obj): ...

class InputLayerSavedModelSaver(base_serialization.SavedModelSaver):
    """InputLayer serialization."""
    @property
    def object_identifier(self): ...
    @property
    def python_properties(self): ...
    def objects_to_serialize(self, serialization_cache): ...
    def functions_to_serialize(self, serialization_cache): ...

class RNNSavedModelSaver(LayerSavedModelSaver):
    """RNN layer serialization."""
    @property
    def object_identifier(self): ...

class VocabularySavedModelSaver(LayerSavedModelSaver):
    """Handles vocabulary layer serialization.

    This class is needed for StringLookup, IntegerLookup, and TextVectorization,
    which all have a vocabulary as part of the config. Currently, we keep this
    vocab as part of the config until saving, when we need to clear it to avoid
    initializing a StaticHashTable twice (once when restoring the config and
    once when restoring restoring module resources). After clearing the vocab,
    we persist a property to the layer indicating it was constructed with a
    vocab.
    """
    @property
    def python_properties(self): ...
