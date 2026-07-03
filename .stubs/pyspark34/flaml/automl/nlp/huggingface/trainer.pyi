from _typeshed import Incomplete
from transformers import Seq2SeqTrainer

Seq2SeqTrainer = object

class TrainerForAuto(Seq2SeqTrainer):
    def predict(self, test_dataset, ignore_keys: Incomplete | None = None, metric_key_prefix: Incomplete | None = None, max_length: Incomplete | None = None, num_beams: Incomplete | None = None): ...
    def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys): ...
    intermediate_results: Incomplete
    def log(self, logs) -> None: ...
    ckpt_to_global_step: Incomplete
    ckpt_to_metric: Incomplete
    def evaluate(self, eval_dataset: Incomplete | None = None, ignore_keys: Incomplete | None = None, metric_key_prefix: str = 'eval'):
        """Overriding transformers.Trainer.evaluate by saving metrics and checkpoint path."""
