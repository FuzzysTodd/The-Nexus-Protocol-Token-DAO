from tensorboard.compat import tf as tf

def PluginDirectory(logdir, plugin_name):
    """Returns the plugin directory for plugin_name."""
def ListPlugins(logdir):
    """List all the plugins that have registered assets in logdir.

    If the plugins_dir does not exist, it returns an empty list. This maintains
    compatibility with old directories that have no plugins written.

    Args:
      logdir: A directory that was created by a TensorFlow events writer.

    Returns:
      a list of plugin names, as strings
    """
def ListAssets(logdir, plugin_name):
    """List all the assets that are available for given plugin in a logdir.

    Args:
      logdir: A directory that was created by a TensorFlow summary.FileWriter.
      plugin_name: A string name of a plugin to list assets for.

    Returns:
      A string list of available plugin assets. If the plugin subdirectory does
      not exist (either because the logdir doesn't exist, or because the plugin
      didn't register) an empty list is returned.
    """
def RetrieveAsset(logdir, plugin_name, asset_name):
    """Retrieve a particular plugin asset from a logdir.

    Args:
      logdir: A directory that was created by a TensorFlow summary.FileWriter.
      plugin_name: The plugin we want an asset from.
      asset_name: The name of the requested asset.

    Returns:
      string contents of the plugin asset.

    Raises:
      KeyError: if the asset does not exist.
    """
