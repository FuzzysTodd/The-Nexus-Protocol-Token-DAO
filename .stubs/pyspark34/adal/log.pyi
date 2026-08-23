from _typeshed import Incomplete

ADAL_LOGGER_NAME: str

def create_log_context(correlation_id: Incomplete | None = None, enable_pii: bool = False): ...
def set_logging_options(options: Incomplete | None = None) -> None:
    """Configure adal logger, including level and handler spec'd by python
    logging module.

    Basic Usages::
        >>>adal.set_logging_options({
        >>>  'level': 'DEBUG',
        >>>  'handler': logging.FileHandler('adal.log')
        >>>})
    """
def get_logging_options():
    """Get logging options

    :returns: a dict, with a key of 'level' for logging level.
    """

class Logger:
    """wrapper around python built-in logging to log correlation_id, and stack
    trace through keyword argument of 'log_stack_trace'
    """
    log_context: Incomplete
    def __init__(self, component_name, log_context) -> None: ...
    def warn(self, msg, *args, **kwargs) -> None:
        '''
        The recommended way to call this function with variable content,
        is to use the `warn("hello %(name)s", {"name": "John Doe"}` form,
        so that this method will scrub pii value when needed.
        '''
    def info(self, msg, *args, **kwargs) -> None: ...
    def debug(self, msg, *args, **kwargs) -> None: ...
    def exception(self, msg, *args, **kwargs) -> None: ...

def scrub_pii(arg_dict, padding: str = '...'):
    """
    The input is a dict with semantic keys,
    and the output will be a dict with PII values replaced by padding.
    """
