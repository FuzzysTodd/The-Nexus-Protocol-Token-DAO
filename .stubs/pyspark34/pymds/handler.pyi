from .internal_logger import log_debug as log_debug
from .scrubbers.scrubber import AppAttemptIdScrubber as AppAttemptIdScrubber, CreditCardScrubber as CreditCardScrubber, HiveRowExceptionScrubber as HiveRowExceptionScrubber, IScrub as IScrub, InvalidLicenseScrubber as InvalidLicenseScrubber, JWTTokenScrubber as JWTTokenScrubber, SASSignatureScrubber as SASSignatureScrubber, SmtpScrubber as SmtpScrubber
from _typeshed import Incomplete
from logging import Handler, LogRecord as LogRecord
from typing import Any, Dict, List

MDS_AGENT_PORT: int
MDS_ROUTE_PREFIX: str
LOGGER_ROOT_PREFIX: str
BUFMAX: Incomplete
on_spark_driver: Incomplete
fluent_logger: Incomplete
cluster_info: Incomplete
hostname: Incomplete
default_scrubbers: List[IScrub]

class SynapseHandler(Handler):
    tableName: Incomplete
    scrubbers: Incomplete
    def __init__(self, tableName: str, scrubbers: List[IScrub] | None = None) -> None: ...
    def scrub(self, msg: str) -> str: ...
    def emit(self, record: LogRecord): ...
    def get_mds_event_fields(self, record: LogRecord) -> Dict[str, Any]: ...
