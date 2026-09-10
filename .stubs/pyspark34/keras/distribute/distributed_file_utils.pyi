from _typeshed import Incomplete

GCP_METADATA_HEADER: Incomplete

def write_dirpath(dirpath, strategy):
    """Returns the writing dir that should be used to save file distributedly.

    `dirpath` would be created if it doesn't exist.

    Args:
      dirpath: Original dirpath that would be used without distribution.
      strategy: The tf.distribute strategy object currently used.

    Returns:
      The writing dir path that should be used to save with distribution.
    """
def remove_temp_dirpath(dirpath, strategy) -> None:
    """Removes the temp path after writing is finished.

    Args:
      dirpath: Original dirpath that would be used without distribution.
      strategy: The tf.distribute strategy object currently used.
    """
def write_filepath(filepath, strategy):
    """Returns the writing file path to be used to save file distributedly.

    Directory to contain `filepath` would be created if it doesn't exist.

    Args:
      filepath: Original filepath that would be used without distribution.
      strategy: The tf.distribute strategy object currently used.

    Returns:
      The writing filepath that should be used to save file with distribution.
    """
def remove_temp_dir_with_filepath(filepath, strategy) -> None:
    """Removes the temp path for file after writing is finished.

    Args:
      filepath: Original filepath that would be used without distribution.
      strategy: The tf.distribute strategy object currently used.
    """
def support_on_demand_checkpoint_callback(strategy): ...
