from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.cmdoptions import make_target_python as make_target_python
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.configuration import Configuration as Configuration
from pip._internal.metadata import get_environment as get_environment
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.misc import get_pip_version as get_pip_version
from pip._vendor.certifi import where as where
from types import ModuleType
from typing import Any, Dict, List

logger: Incomplete

def show_value(name: str, value: Any) -> None: ...
def show_sys_implementation() -> None: ...
def create_vendor_txt_map() -> Dict[str, str]: ...
def get_module_from_module_name(module_name: str) -> ModuleType | None: ...
def get_vendor_version_from_module(module_name: str) -> str | None: ...
def show_actual_vendor_versions(vendor_txt_versions: Dict[str, str]) -> None:
    """Log the actual version and print extra info if there is
    a conflict or if the actual version could not be imported.
    """
def show_vendor_versions() -> None: ...
def show_tags(options: Values) -> None: ...
def ca_bundle_info(config: Configuration) -> str: ...

class DebugCommand(Command):
    """
    Display debug information.
    """
    usage: str
    ignore_require_venv: bool
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
