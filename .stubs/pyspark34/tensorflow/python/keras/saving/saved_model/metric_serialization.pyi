from tensorflow.python.keras.saving.saved_model import constants as constants, layer_serialization as layer_serialization
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.trackable import data_structures as data_structures

class MetricSavedModelSaver(layer_serialization.LayerSavedModelSaver):
    """Metric serialization."""
    @property
    def object_identifier(self): ...
