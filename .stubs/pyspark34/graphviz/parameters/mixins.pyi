from . import engines, formats, formatters, renderers

__all__ = ['Parameters']

class Parameters(engines.Engine, formats.Format, renderers.Renderer, formatters.Formatter):
    """Parameters for calling ``graphviz.render()`` and ``graphviz.pipe()``."""
