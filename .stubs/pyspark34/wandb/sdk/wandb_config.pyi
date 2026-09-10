from . import wandb_helper as wandb_helper
from .lib import config_util as config_util
from _typeshed import Incomplete
from wandb.util import check_dict_contains_nested_artifact as check_dict_contains_nested_artifact, json_friendly_val as json_friendly_val

logger: Incomplete

class Config:
    '''Config object.

    Config objects are intended to hold all of the hyperparameters associated with
    a wandb run and are saved with the run object when `wandb.init` is called.

    We recommend setting `wandb.config` once at the top of your training experiment or
    setting the config as a parameter to init, ie. `wandb.init(config=my_config_dict)`

    You can create a file called `config-defaults.yaml`, and it will automatically be
    loaded into `wandb.config`. See https://docs.wandb.com/guides/track/config#file-based-configs.

    You can also load a config YAML file with your custom name and pass the filename
    into `wandb.init(config="special_config.yaml")`.
    See https://docs.wandb.com/guides/track/config#file-based-configs.

    Examples:
        Basic usage
        ```
        wandb.config.epochs = 4
        wandb.init()
        for x in range(wandb.config.epochs):
            # train
        ```

        Using wandb.init to set config
        ```
        wandb.init(config={"epochs": 4, "batch_size": 32})
        for x in range(wandb.config.epochs):
            # train
        ```

        Nested configs
        ```
        wandb.config[\'train\'][\'epochs\'] = 4
        wandb.init()
        for x in range(wandb.config[\'train\'][\'epochs\']):
            # train
        ```

        Using absl flags
        ```
        flags.DEFINE_string(‘model’, None, ‘model to run’) # name, default, help
        wandb.config.update(flags.FLAGS) # adds all absl flags to config
        ```

        Argparse flags
        ```python
        wandb.init()
        wandb.config.epochs = 4

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-b",
            "--batch-size",
            type=int,
            default=8,
            metavar="N",
            help="input batch size for training (default: 8)",
        )
        args = parser.parse_args()
        wandb.config.update(args)
        ```

        Using TensorFlow flags (deprecated in tensorflow v2)
        ```python
        flags = tf.app.flags
        flags.DEFINE_string("data_dir", "/tmp/data")
        flags.DEFINE_integer("batch_size", 128, "Batch size.")
        wandb.config.update(flags.FLAGS)  # adds all of the tensorflow flags to config
        ```
    '''
    def __init__(self) -> None: ...
    def keys(self): ...
    def as_dict(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def items(self): ...
    __setattr__ = __setitem__
    def __getattr__(self, key): ...
    def __contains__(self, key) -> bool: ...
    def update(self, d, allow_val_change: Incomplete | None = None) -> None: ...
    def get(self, *args): ...
    def persist(self) -> None:
        """Call the callback if it's set."""
    def setdefaults(self, d) -> None: ...
    def update_locked(self, d, user: Incomplete | None = None, _allow_val_change: Incomplete | None = None) -> None: ...

class ConfigStatic:
    def __init__(self, config) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def keys(self): ...
    def __getitem__(self, key): ...
