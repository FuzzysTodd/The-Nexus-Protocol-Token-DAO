from keras.saving.legacy.saved_model import constants as constants, model_serialization as model_serialization

class NetworkSavedModelSaver(model_serialization.ModelSavedModelSaver):
    """Network serialization."""
    @property
    def object_identifier(self): ...
