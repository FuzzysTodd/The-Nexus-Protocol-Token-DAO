from keras.saving import object_registration as object_registration
from keras.saving.legacy.saved_model import constants as constants, layer_serialization as layer_serialization

class MetricSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    """Metric serialization."""
    @property
    def object_identifier(self): ...
