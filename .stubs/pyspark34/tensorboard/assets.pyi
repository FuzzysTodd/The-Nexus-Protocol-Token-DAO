from _typeshed import Incomplete
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

def get_default_assets_zip_provider():
    """Try to get a function to provide frontend assets.

    Returns:
      Either (a) a callable that takes no arguments and returns an open
      file handle to a Zip archive of frontend assets, or (b) `None`, if
      the frontend assets cannot be found.
    """
