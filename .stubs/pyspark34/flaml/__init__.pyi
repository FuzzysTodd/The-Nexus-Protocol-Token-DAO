from _typeshed import Incomplete
from flaml.automl import AutoML as AutoML, logger_formatter as logger_formatter
from flaml.internal._telemetry import log_telemetry as log_telemetry
from flaml.onlineml.autovw import AutoVW as AutoVW
from flaml.tune.searcher import BlendSearch as BlendSearch, BlendSearchTuner as BlendSearchTuner, CFO as CFO, FLOW2 as FLOW2, RandomSearch as RandomSearch
from flaml.version import __version__ as __version__

is_log_telemetry: bool
logger: Incomplete
