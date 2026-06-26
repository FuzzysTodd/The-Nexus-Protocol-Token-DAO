from ..trainer import Trainer as Trainer
from ..utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete

class SageMakerTrainer(Trainer):
    def __init__(self, args: Incomplete | None = None, **kwargs) -> None: ...
