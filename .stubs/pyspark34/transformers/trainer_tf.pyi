import tensorflow as tf
from .integrations import is_comet_available as is_comet_available, is_wandb_available as is_wandb_available
from .modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel
from .optimization_tf import GradientAccumulator as GradientAccumulator, create_optimizer as create_optimizer
from .trainer_utils import EvalPrediction as EvalPrediction, IntervalStrategy as IntervalStrategy, PREFIX_CHECKPOINT_DIR as PREFIX_CHECKPOINT_DIR, PredictionOutput as PredictionOutput, enable_full_determinism as enable_full_determinism, set_seed as set_seed
from .training_args_tf import TFTrainingArguments as TFTrainingArguments
from .utils import ENV_VARS_TRUE_VALUES as ENV_VARS_TRUE_VALUES, logging as logging
from _typeshed import Incomplete
from typing import Callable, Dict, Optional, Tuple

logger: Incomplete

class TFTrainer:
    """
    TFTrainer is a simple but feature-complete training and eval loop for TensorFlow, optimized for 🤗 Transformers.

    Args:
        model ([`TFPreTrainedModel`]):
            The model to train, evaluate or use for predictions.
        args ([`TFTrainingArguments`]):
            The arguments to tweak training.
        train_dataset ([`~tf.data.Dataset`], *optional*):
            The dataset to use for training. The dataset should yield tuples of `(features, labels)` where `features`
            is a dict of input features and `labels` is the labels. If `labels` is a tensor, the loss is calculated by
            the model by calling `model(features, labels=labels)`. If `labels` is a dict, such as when using a
            QuestionAnswering head model with multiple targets, the loss is instead calculated by calling
            `model(features, **labels)`.
        eval_dataset ([`~tf.data.Dataset`], *optional*):
            The dataset to use for evaluation. The dataset should yield tuples of `(features, labels)` where `features`
            is a dict of input features and `labels` is the labels. If `labels` is a tensor, the loss is calculated by
            the model by calling `model(features, labels=labels)`. If `labels` is a dict, such as when using a
            QuestionAnswering head model with multiple targets, the loss is instead calculated by calling
            `model(features, **labels)`.
        compute_metrics (`Callable[[EvalPrediction], Dict]`, *optional*):
            The function that will be used to compute metrics at evaluation. Must take a [`EvalPrediction`] and return
            a dictionary string to metric values.
        tb_writer (`tf.summary.SummaryWriter`, *optional*):
            Object to write to TensorBoard.
        optimizers (`Tuple[tf.keras.optimizers.Optimizer, tf.keras.optimizers.schedules.LearningRateSchedule]`, *optional*):
            A tuple containing the optimizer and the scheduler to use. The optimizer default to an instance of
            [`tf.keras.optimizers.Adam`] if `args.weight_decay_rate` is 0 else an instance of [`AdamWeightDecay`]. The
            scheduler will default to an instance of [`tf.keras.optimizers.schedules.PolynomialDecay`] if
            `args.num_warmup_steps` is 0 else an instance of [`WarmUp`].
    """
    model: Incomplete
    args: Incomplete
    train_dataset: Incomplete
    eval_dataset: Incomplete
    compute_metrics: Incomplete
    gradient_accumulator: Incomplete
    global_step: int
    epoch_logging: int
    eval_loss: Incomplete
    tb_writer: Incomplete
    def __init__(self, model: TFPreTrainedModel, args: TFTrainingArguments, train_dataset: Optional[tf.data.Dataset] = None, eval_dataset: Optional[tf.data.Dataset] = None, compute_metrics: Optional[Callable[[EvalPrediction], Dict]] = None, tb_writer: Optional[tf.summary.SummaryWriter] = None, optimizers: Tuple[tf.keras.optimizers.Optimizer, tf.keras.optimizers.schedules.LearningRateSchedule] = (None, None)) -> None: ...
    total_train_batch_size: Incomplete
    num_train_examples: Incomplete
    def get_train_tfdataset(self) -> tf.data.Dataset:
        """
        Returns the training [`~tf.data.Dataset`].

        Subclass and override this method if you want to inject some custom behavior.
        """
    def get_eval_tfdataset(self, eval_dataset: Optional[tf.data.Dataset] = None) -> tf.data.Dataset:
        """
        Returns the evaluation [`~tf.data.Dataset`].

        Args:
            eval_dataset ([`~tf.data.Dataset`], *optional*):
                If provided, will override *self.eval_dataset*. The dataset should yield tuples of `(features, labels)`
                where `features` is a dict of input features and `labels` is the labels. If `labels` is a tensor, the
                loss is calculated by the model by calling `model(features, labels=labels)`. If `labels` is a dict,
                such as when using a QuestionAnswering head model with multiple targets, the loss is instead calculated
                by calling `model(features, **labels)`.

        Subclass and override this method if you want to inject some custom behavior.
        """
    def get_test_tfdataset(self, test_dataset: tf.data.Dataset) -> tf.data.Dataset:
        """
        Returns a test [`~tf.data.Dataset`].

        Args:
            test_dataset ([`~tf.data.Dataset`]):
                The dataset to use. The dataset should yield tuples of `(features, labels)` where `features` is a dict
                of input features and `labels` is the labels. If `labels` is a tensor, the loss is calculated by the
                model by calling `model(features, labels=labels)`. If `labels` is a dict, such as when using a
                QuestionAnswering head model with multiple targets, the loss is instead calculated by calling
                `model(features, **labels)`.

        Subclass and override this method if you want to inject some custom behavior.
        """
    def create_optimizer_and_scheduler(self, num_training_steps: int):
        """
        Setup the optimizer and the learning rate scheduler.

        We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the
        TFTrainer's init through `optimizers`, or subclass and override this method.
        """
    def setup_wandb(self) -> None:
        '''
        Setup the optional Weights & Biases (`wandb`) integration.

        One can subclass and override this method to customize the setup if needed. Find more information `here
        <https://docs.wandb.com/huggingface>`__. You can also override the following environment variables:

        Environment:
            WANDB_PROJECT:
                (Optional): str - "huggingface" by default, set this to a custom string to store results in a different
                project.
            WANDB_DISABLED:
                (Optional): boolean - defaults to false, set to "true" to disable wandb entirely.
        '''
    def setup_comet(self) -> None:
        '''
        Setup the optional Comet.ml integration.

        Environment:
            COMET_MODE:
                (Optional): str - "OFFLINE", "ONLINE", or "DISABLED"
            COMET_PROJECT_NAME:
                (Optional): str - Comet.ml project name for experiments
            COMET_OFFLINE_DIRECTORY:
                (Optional): str - folder to use for saving offline experiments when `COMET_MODE` is "OFFLINE"

        For a number of configurable items in the environment, see `here
        <https://www.comet.ml/docs/python-sdk/advanced/#comet-configuration-variables>`__
        '''
    def prediction_loop(self, dataset: tf.data.Dataset, steps: int, num_examples: int, description: str, prediction_loss_only: Optional[bool] = None) -> PredictionOutput:
        """
        Prediction/evaluation loop, shared by [`~TFTrainer.evaluate`] and [`~TFTrainer.predict`].

        Works both with or without labels.
        """
    def log(self, logs: Dict[str, float]) -> None:
        """
        Log `logs` on the various objects watching training.

        Subclass and override this method to inject custom behavior.

        Args:
            logs (`Dict[str, float]`):
                The values to log.
        """
    def evaluate(self, eval_dataset: Optional[tf.data.Dataset] = None) -> Dict[str, float]:
        """
        Run evaluation and returns metrics.

        The calling script will be responsible for providing a method to compute metrics, as they are task-dependent
        (pass it to the init `compute_metrics` argument).

        Args:
            eval_dataset ([`~tf.data.Dataset`], *optional*):
                Pass a dataset if you wish to override `self.eval_dataset`. The dataset should yield tuples of
                `(features, labels)` where `features` is a dict of input features and `labels` is the labels. If
                `labels` is a tensor, the loss is calculated by the model by calling `model(features, labels=labels)`.
                If `labels` is a dict, such as when using a QuestionAnswering head model with multiple targets, the
                loss is instead calculated by calling `model(features, **labels)`.

        Returns:
            A dictionary containing the evaluation loss and the potential metrics computed from the predictions.
        """
    def prediction_step(self, features: tf.Tensor, labels: tf.Tensor, nb_instances_in_global_batch: tf.Tensor) -> tf.Tensor:
        """
        Compute the prediction on features and update the loss with labels.

        Subclass and override to inject some custom behavior.
        """
    def distributed_prediction_steps(self, batch): ...
    steps_per_epoch: Incomplete
    train_loss: Incomplete
    def train(self) -> None:
        """
        Train method to train the model.
        """
    def training_step(self, features, labels, nb_instances_in_global_batch):
        """
        Perform a training step on features and labels.

        Subclass and override to inject some custom behavior.
        """
    def apply_gradients(self, features, labels, nb_instances_in_global_batch) -> None: ...
    def distributed_training_steps(self, batch) -> None: ...
    def run_model(self, features, labels, training):
        """
        Computes the loss of the given features and labels pair.

        Subclass and override this method if you want to inject some custom behavior.

        Args:
            features (`tf.Tensor`): A batch of input features.
            labels (`tf.Tensor`): A batch of labels.
            training (`bool`): Whether or not to run the model in training mode.

        Returns:
            A tuple of two `tf.Tensor`: The loss and logits.
        """
    def predict(self, test_dataset: tf.data.Dataset) -> PredictionOutput:
        """
        Run prediction and returns predictions and potential metrics.

        Depending on the dataset and your use case, your test dataset may contain labels. In that case, this method
        will also return metrics, like in `evaluate()`.

        Args:
            test_dataset ([`~tf.data.Dataset`]):
                Dataset to run the predictions on. The dataset should yield tuples of `(features, labels)` where
                `features` is a dict of input features and `labels` is the labels. If `labels` is a tensor, the loss is
                calculated by the model by calling `model(features, labels=labels)`. If `labels` is a dict, such as
                when using a QuestionAnswering head model with multiple targets, the loss is instead calculated by
                calling `model(features, **labels)`

        Returns: *NamedTuple* A namedtuple with the following keys:

            - predictions (`np.ndarray`): The predictions on `test_dataset`.
            - label_ids (`np.ndarray`, *optional*): The labels (if the dataset contained some).
            - metrics (`Dict[str, float]`, *optional*): The potential dictionary of metrics (if the dataset contained
              labels).
        """
    def save_model(self, output_dir: Optional[str] = None):
        """
        Will save the model, so you can reload it using `from_pretrained()`.
        """
