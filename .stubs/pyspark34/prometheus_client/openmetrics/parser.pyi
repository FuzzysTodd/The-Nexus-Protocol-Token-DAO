from ..metrics_core import METRIC_LABEL_NAME_RE as METRIC_LABEL_NAME_RE, Metric as Metric
from ..samples import Exemplar as Exemplar, Sample as Sample, Timestamp as Timestamp
from ..utils import floatToGoString as floatToGoString
from _typeshed import Incomplete
from collections.abc import Generator

def text_string_to_metric_families(text) -> Generator[Incomplete, Incomplete, None]:
    """Parse Openmetrics text format from a unicode string.

    See text_fd_to_metric_families.
    """

ESCAPE_SEQUENCES: Incomplete
ESCAPING_RE: Incomplete

def text_fd_to_metric_families(fd) -> Generator[Incomplete, None, Incomplete]:
    """Parse Prometheus text format from a file descriptor.

    This is a laxer parser than the main Go parser,
    so successful parsing does not imply that the parsed
    text meets the specification.

    Yields Metric's.
    """
