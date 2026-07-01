import pytorch_lightning as pl
from _typeshed import Incomplete

class PostTrainingDataSparsity(pl.callbacks.Callback):
    """Lightning callback that enables post-training sparsity.

    This callback aims to sparsify the model inside lightning module after training.
    **Note that the model is copied and then sparsified, so the existing model is not modified**

    The sparsified model can be used for comparison and can be accessed using
        <callback_obj>.sparsified

    Args:
        data_sparsifier_class (some implemented class of BaseDataSparsifier)
            The data sparsifier object of this class is created when the
            training starts.
            Note: Objects should not be passed in here as they are created
            once the training completes.

        data_sparsifier_args (Dict)
            Dictionary of args to be passed to the data sparsifier.
            Note: data_list arg should be ignored

    Hooks implemented:
        on_fit_end()
            1. copies the model and attaches it to the sparsifier
            2. sparsier step() is called
            3. squashes the mask()
    """
    data_sparsifier_class: Incomplete
    data_sparsifier_args: Incomplete
    data_sparsifier: Incomplete
    sparsified: Incomplete
    def __init__(self, data_sparsifier_class, data_sparsifier_args) -> None: ...
    def on_fit_end(self, trainer, pl_module) -> None: ...

class TrainingAwareDataSparsity(pl.callbacks.Callback):
    """Lightning callback that enables in-training sparsity.

    This callback aims to sparsify the model inside lightning module during training.
    **Note that the model is copied and then sparsified, so the existing model is not modified**

    The sparsified model can be used for comparison and can be accessed using
        <callback_obj>.sparsified

    Args:
        data_sparsifier_class (some implemented class of BaseDataSparsifier)
            The data sparsifier object of this class is created when the
            training starts.
            Note: Objects should not be passed in here as they are created
            when the training starts.

        data_sparsifier_args (Dict)
            Dictionary of args to be passed to the data sparsifier.
            Note: data_list arg should be ignored

        data_scheduler_class (some implemented class of BaseDataScheduler)
            The data scheduler of this class is created when the training starts
            Note: Objects should not be passed in here as they are created
            when the training starts.

        data_scheduler_args(Dict)
            Dictionary of args to be passed to the data scheduler.
            **Note: data_sparsifier arg should be ignored as the recipe
            creates and pass sparsifier object into the class**

    Hooks implemented:
        on_train_start()
            Data sparsifier and scheduler objects are created.
            Pytorch model attached to the sparsifier

        on_train_epoch_start()
            Loads the state_dict of the data sparsifier

        on_train_epoch_end()
            1. Copies the model and attaches it to the sparsifier
            2. sparsifier step() and scheduler step()
            3. Dump state_dict of the current sparsifier

        on_train_end()
            squash mask
    """
    data_sparsifier_class: Incomplete
    data_sparsifier_args: Incomplete
    data_scheduler_class: Incomplete
    data_scheduler_args: Incomplete
    data_sparsifier: Incomplete
    data_scheduler: Incomplete
    sparsified: Incomplete
    data_sparsifier_state_dict: Incomplete
    def __init__(self, data_sparsifier_class, data_sparsifier_args, data_scheduler_class, data_scheduler_args) -> None: ...
    def on_train_start(self, trainer, pl_module) -> None: ...
    def on_train_epoch_start(self, trainer, pl_module) -> None: ...
    def on_train_epoch_end(self, trainer, pl_module) -> None: ...
    def on_train_end(self, trainer, pl_module) -> None: ...
