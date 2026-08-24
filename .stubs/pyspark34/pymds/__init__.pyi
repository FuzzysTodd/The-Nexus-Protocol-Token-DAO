from ..internal_utils.version import VERSION
from .decorator import mds_log as mds_log
from .synapse_logger import get_mds_json_logger as get_mds_json_logger, get_mds_logger as get_mds_logger

__all__ = ['get_mds_logger', 'get_mds_json_logger', 'mds_log', 'add_mds_table_handler']

__version__ = VERSION

# Names in __all__ with no definition:
#   add_mds_table_handler
