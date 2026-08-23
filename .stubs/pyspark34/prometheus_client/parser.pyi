from .metrics_core import Metric as Metric
from .samples import Sample as Sample
from _typeshed import Incomplete
from typing import Iterable, Match, TextIO

def text_string_to_metric_families(text: str) -> Iterable[Metric]:
    """Parse Prometheus text format from a unicode string.

    See text_fd_to_metric_families.
    """

ESCAPE_SEQUENCES: Incomplete

def replace_escape_sequence(match: Match[str]) -> str: ...

HELP_ESCAPING_RE: Incomplete
ESCAPING_RE: Incomplete

def text_fd_to_metric_families(fd: TextIO) -> Iterable[Metric]:
    """Parse Prometheus text format from a file descriptor.

    This is a laxer parser than the main Go parser,
    so successful parsing does not imply that the parsed
    text meets the specification.

    Yields Metric's.
    """
