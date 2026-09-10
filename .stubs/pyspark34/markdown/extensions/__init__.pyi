from _typeshed import Incomplete

class Extension:
    """ Base class for extensions to subclass. """
    config: Incomplete
    def __init__(self, **kwargs) -> None:
        """ Initiate Extension and set up configs. """
    def getConfig(self, key, default: str = ''):
        """ Return a setting for the given key or an empty string. """
    def getConfigs(self):
        """ Return all configs settings as a dict. """
    def getConfigInfo(self):
        """ Return all `config` descriptions as a list of tuples. """
    def setConfig(self, key, value) -> None:
        """ Set a `config` setting for `key` with the given `value`. """
    def setConfigs(self, items) -> None:
        """ Set multiple `config` settings given a dict or list of tuples. """
    def extendMarkdown(self, md) -> None:
        """
        Add the various processors and patterns to the Markdown Instance.

        This method must be overridden by every extension.

        Keyword arguments:

        * md: The Markdown instance.

        """
