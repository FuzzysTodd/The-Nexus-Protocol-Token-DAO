from _typeshed import Incomplete
from tensorboard import default as default, main_lib as main_lib, program as program
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.uploader import uploader_subcommand as uploader_subcommand
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

def run_main() -> None:
    """Initializes flags and calls main()."""
