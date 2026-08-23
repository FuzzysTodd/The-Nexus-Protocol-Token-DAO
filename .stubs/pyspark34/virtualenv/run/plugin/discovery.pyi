from .base import PluginLoader

__all__ = ['get_discover', 'Discovery']

class Discovery(PluginLoader):
    """Discovery plugins."""

def get_discover(parser, args): ...
