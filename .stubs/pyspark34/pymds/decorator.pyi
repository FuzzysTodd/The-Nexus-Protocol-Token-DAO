from .synapse_logger import get_mds_json_logger as get_mds_json_logger
from _typeshed import Incomplete

def mds_log(extract_message_fn: Incomplete | None = None, extract_mds_fn: Incomplete | None = None, logger: Incomplete | None = None):
    '''
    Decorator helper to ease wrapping of function invocations.

    Parameters
    ----------
    extract_message_fn
       Receive invocation args/kwargs and returns a dict to be added to the log message dictionary.
    extract_mds_fn
       Receive invocation args/kwargs and returns a dict to be added to the extra parameter.
       Keys prefixed w/ "mds_" will be added to the MDS event and result in Kusto/MDS columns.
    logger
       Implementation of logging.Logger.
    '''
