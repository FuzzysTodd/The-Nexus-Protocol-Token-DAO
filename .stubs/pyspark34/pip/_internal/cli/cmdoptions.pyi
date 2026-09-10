from _typeshed import Incomplete
from optparse import Option, OptionGroup, OptionParser, Values
from pip._internal.cli.parser import ConfigOptionParser as ConfigOptionParser
from pip._internal.exceptions import CommandError as CommandError
from pip._internal.locations import USER_CACHE_DIR as USER_CACHE_DIR, get_src_prefix as get_src_prefix
from pip._internal.models.format_control import FormatControl as FormatControl
from pip._internal.models.index import PyPI as PyPI
from pip._internal.models.target_python import TargetPython as TargetPython
from pip._internal.utils.hashes import STRONG_HASHES as STRONG_HASHES
from pip._internal.utils.misc import strtobool as strtobool
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import Any, Callable, Dict

logger: Incomplete

def raise_option_error(parser: OptionParser, option: Option, msg: str) -> None:
    """
    Raise an option parsing error using parser.error().

    Args:
      parser: an OptionParser instance.
      option: an Option instance.
      msg: the error text.
    """
def make_option_group(group: Dict[str, Any], parser: ConfigOptionParser) -> OptionGroup:
    """
    Return an OptionGroup object
    group  -- assumed to be dict with 'name' and 'options' keys
    parser -- an optparse Parser
    """
def check_dist_restriction(options: Values, check_target: bool = False) -> None:
    """Function for determining if custom platform options are allowed.

    :param options: The OptionParser options.
    :param check_target: Whether or not to check if --target is being used.
    """

class PipOption(Option):
    TYPES: Incomplete
    TYPE_CHECKER: Incomplete

help_: Callable[..., Option]
debug_mode: Callable[..., Option]
isolated_mode: Callable[..., Option]
require_virtualenv: Callable[..., Option]
override_externally_managed: Callable[..., Option]
python: Callable[..., Option]
verbose: Callable[..., Option]
no_color: Callable[..., Option]
version: Callable[..., Option]
quiet: Callable[..., Option]
progress_bar: Callable[..., Option]
log: Callable[..., Option]
no_input: Callable[..., Option]
keyring_provider: Callable[..., Option]
proxy: Callable[..., Option]
retries: Callable[..., Option]
timeout: Callable[..., Option]

def exists_action() -> Option: ...

cert: Callable[..., Option]
client_cert: Callable[..., Option]
index_url: Callable[..., Option]

def extra_index_url() -> Option: ...

no_index: Callable[..., Option]

def find_links() -> Option: ...
def trusted_host() -> Option: ...
def constraints() -> Option: ...
def requirements() -> Option: ...
def editable() -> Option: ...

src: Callable[..., Option]

def no_binary() -> Option: ...
def only_binary() -> Option: ...

platforms: Callable[..., Option]
python_version: Callable[..., Option]
implementation: Callable[..., Option]
abis: Callable[..., Option]

def add_target_python_options(cmd_opts: OptionGroup) -> None: ...
def make_target_python(options: Values) -> TargetPython: ...
def prefer_binary() -> Option: ...

cache_dir: Callable[..., Option]
no_cache: Callable[..., Option]
no_deps: Callable[..., Option]
ignore_requires_python: Callable[..., Option]
no_build_isolation: Callable[..., Option]
check_build_deps: Callable[..., Option]
use_pep517: Any
no_use_pep517: Any
config_settings: Callable[..., Option]
build_options: Callable[..., Option]
global_options: Callable[..., Option]
no_clean: Callable[..., Option]
pre: Callable[..., Option]
disable_pip_version_check: Callable[..., Option]
root_user_action: Callable[..., Option]
hash: Callable[..., Option]
require_hashes: Callable[..., Option]
list_path: Callable[..., Option]

def check_list_path_option(options: Values) -> None: ...

list_exclude: Callable[..., Option]
no_python_version_warning: Callable[..., Option]
ALWAYS_ENABLED_FEATURES: Incomplete
use_new_feature: Callable[..., Option]
use_deprecated_feature: Callable[..., Option]
general_group: Dict[str, Any]
index_group: Dict[str, Any]
