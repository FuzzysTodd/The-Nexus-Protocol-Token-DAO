from .. import parameters

__all__ = ['Render', 'Pipe', 'Unflatten', 'View']

class Render(parameters.Parameters):
    """Parameters for calling and calling ``graphviz.render()``."""
class Pipe(parameters.Parameters):
    """Parameters for calling and calling ``graphviz.pipe()``."""
class Unflatten: ...
class View:
    """Open filepath with its default viewing application
        (platform-specific)."""
