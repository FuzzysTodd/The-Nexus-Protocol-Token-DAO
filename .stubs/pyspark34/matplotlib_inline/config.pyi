from _typeshed import Incomplete
from traitlets.config.configurable import SingletonConfigurable

def pil_available():
    """Test if PIL/Pillow is available"""

class InlineBackendConfig(SingletonConfigurable): ...

class InlineBackend(InlineBackendConfig):
    """An object to store configuration of the inline backend."""
    rc: Incomplete
    figure_formats: Incomplete
    figure_format: Incomplete
    print_figure_kwargs: Incomplete
    close_figures: Incomplete
    shell: Incomplete
