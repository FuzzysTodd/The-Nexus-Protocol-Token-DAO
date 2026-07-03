from .lib import config_util as config_util
from _typeshed import Incomplete
from wandb.errors import UsageError as UsageError

def parse_config(params, exclude: Incomplete | None = None, include: Incomplete | None = None): ...
