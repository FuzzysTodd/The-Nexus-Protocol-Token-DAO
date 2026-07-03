from IPython.utils.decorators import undoc as undoc
from IPython.utils.path import compress_user as compress_user, ensure_dir_exists as ensure_dir_exists
from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

BUILTINS_EXTS: Incomplete

class ExtensionManager(Configurable):
    """A class to manage IPython extensions.

    An IPython extension is an importable Python module that has
    a function with the signature::

        def load_ipython_extension(ipython):
            # Do things with ipython

    This function is called after your extension is imported and the
    currently active :class:`InteractiveShell` instance is passed as
    the only argument.  You can do anything you want with IPython at
    that point, including defining new magic and aliases, adding new
    components, etc.
    
    You can also optionally define an :func:`unload_ipython_extension(ipython)`
    function, which will be called if the user unloads or reloads the extension.
    The extension manager will only call :func:`load_ipython_extension` again
    if the extension is reloaded.

    You can put your extension modules anywhere you want, as long as
    they can be imported by Python's standard import mechanism.  However,
    to make it easy to write extensions, you can also put your extensions
    in ``os.path.join(self.ipython_dir, 'extensions')``.  This directory
    is added to ``sys.path`` automatically.
    """
    shell: Incomplete
    loaded: Incomplete
    def __init__(self, shell: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def ipython_extension_dir(self): ...
    def load_extension(self, module_str: str):
        '''Load an IPython extension by its module name.

        Returns the string "already loaded" if the extension is already loaded,
        "no load function" if the module doesn\'t have a load_ipython_extension
        function, or None if it succeeded.
        '''
    def unload_extension(self, module_str: str):
        '''Unload an IPython extension by its module name.

        This function looks up the extension\'s name in ``sys.modules`` and
        simply calls ``mod.unload_ipython_extension(self)``.

        Returns the string "no unload function" if the extension doesn\'t define
        a function to unload itself, "not loaded" if the extension isn\'t loaded,
        otherwise None.
        '''
    def reload_extension(self, module_str: str):
        """Reload an IPython extension by calling reload.

        If the module has not been loaded before,
        :meth:`InteractiveShell.load_extension` is called. Otherwise
        :func:`reload` is called and then the :func:`load_ipython_extension`
        function of the module, if it exists is called.
        """
