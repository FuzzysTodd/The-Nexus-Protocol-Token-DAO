from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.req_command import SessionCommandMixin as SessionCommandMixin, warn_if_run_as_root as warn_if_run_as_root
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.exceptions import InstallationError as InstallationError
from pip._internal.req import parse_requirements as parse_requirements
from pip._internal.req.constructors import install_req_from_line as install_req_from_line, install_req_from_parsed_requirement as install_req_from_parsed_requirement
from pip._internal.utils.misc import check_externally_managed as check_externally_managed, protect_pip_from_modification_on_windows as protect_pip_from_modification_on_windows
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import List

logger: Incomplete

class UninstallCommand(Command, SessionCommandMixin):
    """
    Uninstall packages.

    pip is able to uninstall most installed packages. Known exceptions are:

    - Pure distutils packages installed with ``python setup.py install``, which
      leave behind no metadata to determine what files were installed.
    - Script wrappers installed by ``python setup.py develop``.
    """
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
