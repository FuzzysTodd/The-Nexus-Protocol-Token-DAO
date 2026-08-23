from .common_utils import print_normal as print_normal
from .config_schema import NNIConfigSchema as NNIConfigSchema

def expand_path(experiment_config, key) -> None:
    """Change '~' to user home directory"""
def parse_relative_path(root_path, experiment_config, key) -> None:
    """Change relative path to absolute path"""
def parse_time(time):
    """Change the time to seconds"""
def parse_path(experiment_config, config_path) -> None:
    """Parse path in config file"""
def set_default_values(experiment_config) -> None: ...
def validate_all_content(experiment_config, config_path) -> None:
    """Validate whether experiment_config is valid"""
