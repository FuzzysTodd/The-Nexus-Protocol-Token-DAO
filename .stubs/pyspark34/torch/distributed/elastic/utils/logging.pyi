from torch.distributed.elastic.utils.log_level import get_log_level as get_log_level

def get_logger(name: str | None = None):
    """
    Util function to set up a simple logger that writes
    into stderr. The loglevel is fetched from the LOGLEVEL
    env. variable or WARNING as default. The function will use the
    module name of the caller if no name is provided.

    Args:
        name: Name of the logger. If no name provided, the name will
              be derived from the call stack.
    """
