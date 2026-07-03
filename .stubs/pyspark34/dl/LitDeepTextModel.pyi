import pytorch_lightning as pl
from _typeshed import Incomplete

class LitDeepTextModel(pl.LightningModule):
    checkpoint: Incomplete
    text_col: Incomplete
    label_col: Incomplete
    num_labels: Incomplete
    additional_layers_to_train: Incomplete
    optimizer_name: Incomplete
    loss_name: Incomplete
    learning_rate: Incomplete
    train_from_scratch: Incomplete
    def __init__(self, checkpoint, text_col, label_col, num_labels, additional_layers_to_train, optimizer_name, loss_name, learning_rate: Incomplete | None = None, train_from_scratch: bool = True) -> None:
        """
        :param checkpoint: Checkpoint for pre-trained model. This is expected to
                            be a checkpoint you could find on [HuggingFace](https://huggingface.co/models)
                            and is of type `AutoModelForSequenceClassification`.
        :param text_col: Text column name.
        :param label_col: Label column name.
        :param num_labels: Number of labels for classification.
        :param additional_layers_to_train: Additional number of layers to train on. For Deep text model
                                            we'd better choose a positive number for better performance.
        :param optimizer_name: Name of the optimizer.
        :param loss_name: Name of the loss function.
        :param learning_rate: Learning rate for the optimizer.
        :param train_from_scratch: Whether train the model from scratch or not. If this is set to true then
                                    additional_layers_to_train param will be ignored. Default to True.
        """
    def forward(self, **inputs): ...
    def configure_optimizers(self): ...
    def training_step(self, batch, batch_idx): ...
    def validation_step(self, batch, batch_idx) -> None: ...
    def validation_epoch_end(self, outputs) -> None: ...
    def test_step(self, batch, batch_idx): ...
