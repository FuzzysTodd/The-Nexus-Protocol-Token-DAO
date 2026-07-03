from . import exceptions as exceptions
from ._utils import AttributeDict as AttributeDict
from _typeshed import Incomplete

def load_dash_env_vars(): ...

DASH_ENV_VARS: Incomplete

def get_combined_config(name, val, default: Incomplete | None = None):
    """Consolidate the config with priority from high to low provided init
    value > OS environ > default."""
def pathname_configs(url_base_pathname: Incomplete | None = None, routes_pathname_prefix: Incomplete | None = None, requests_pathname_prefix: Incomplete | None = None): ...
def pages_folder_config(name, pages_folder, use_pages): ...
