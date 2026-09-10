from _typeshed import Incomplete

env_plugin_order: Incomplete

def __getattr__(name):
    """Lazy-Import Plugins

    This function dynamically loads plugins into the imageio.plugin
    namespace upon first access. For example, the following snippet will
    delay importing freeimage until the second line:

    >>> import imageio
    >>> imageio.plugins.freeimage.download()

    """
