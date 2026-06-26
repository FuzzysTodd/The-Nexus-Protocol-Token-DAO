from pathlib import Path

def get_config_directory() -> Path:
    """
    Get NNI config directory.
    Create it if not exist.
    """
def get_config_file(name: str) -> Path:
    """
    Get an NNI config file.
    Copy from `nni/runtime/default_config` if not exist.
    """
def get_builtin_config_file(name: str) -> Path:
    """
    Get a readonly builtin config file.
    """
