from _typeshed import Incomplete
from traitlets.config.configurable import LoggingConfigurable

class NbConvertBase(LoggingConfigurable):
    """Global configurable class for shared config

    Useful for display data priority that might be used by many transformers
    """
    display_data_priority: Incomplete
    default_language: Incomplete
