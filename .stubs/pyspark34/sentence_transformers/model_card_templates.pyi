from .util import fullname as fullname
from _typeshed import Incomplete

class ModelCardTemplate:
    __TAGS__: Incomplete
    __DEFAULT_VARS__: Incomplete
    __MODEL_CARD__: str
    __TRAINING_SECTION__: str
    __USAGE_TRANSFORMERS__: str
    @staticmethod
    def model_card_get_pooling_function(pooling_mode): ...
    @staticmethod
    def get_train_objective_info(dataloader, loss): ...
