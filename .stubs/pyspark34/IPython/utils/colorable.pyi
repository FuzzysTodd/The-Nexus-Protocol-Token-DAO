from _typeshed import Incomplete
from traitlets.config import Configurable

available_themes: Incomplete

class Colorable(Configurable):
    """
    A subclass of configurable for all the classes that have a `default_scheme`
    """
    default_style: Incomplete
