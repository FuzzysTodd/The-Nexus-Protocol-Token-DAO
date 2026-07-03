from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.req_command import SessionCommandMixin as SessionCommandMixin
from pip._internal.cli.status_codes import NO_MATCHES_FOUND as NO_MATCHES_FOUND, SUCCESS as SUCCESS
from pip._internal.exceptions import CommandError as CommandError
from pip._internal.metadata import get_default_environment as get_default_environment
from pip._internal.models.index import PyPI as PyPI
from pip._internal.network.xmlrpc import PipXmlrpcTransport as PipXmlrpcTransport
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.misc import write_output as write_output
from typing import Dict, List, TypedDict

class TransformedHit(TypedDict):
    name: str
    summary: str
    versions: List[str]

logger: Incomplete

class SearchCommand(Command, SessionCommandMixin):
    """Search for PyPI packages whose name or summary contains <query>."""
    usage: str
    ignore_require_venv: bool
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
    def search(self, query: List[str], options: Values) -> List[Dict[str, str]]: ...

def transform_hits(hits: List[Dict[str, str]]) -> List['TransformedHit']:
    """
    The list from pypi is really a list of versions. We want a list of
    packages with the list of versions stored inline. This converts the
    list from pypi into one we can use.
    """
def print_dist_installation_info(name: str, latest: str) -> None: ...
def print_results(hits: List['TransformedHit'], name_column_width: int | None = None, terminal_width: int | None = None) -> None: ...
def highest_version(versions: List[str]) -> str: ...
