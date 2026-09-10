from IPython.core import pylabtools as pylabtools
from IPython.core.application import ENV_CONFIG_DIRS as ENV_CONFIG_DIRS, SYSTEM_CONFIG_DIRS as SYSTEM_CONFIG_DIRS
from IPython.terminal import pt_inputhooks as pt_inputhooks
from IPython.utils.contexts import preserve_keys as preserve_keys
from IPython.utils.path import filefind as filefind
from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

gui_keys: Incomplete
backend_keys: Incomplete
shell_flags: Incomplete
addflag: Incomplete
nosep_config: Incomplete
shell_aliases: Incomplete

class InteractiveShellApp(Configurable):
    """A Mixin for applications that start InteractiveShell instances.

    Provides configurables for loading extensions and executing files
    as part of configuring a Shell environment.

    The following methods should be called by the :meth:`initialize` method
    of the subclass:

      - :meth:`init_path`
      - :meth:`init_shell` (to be implemented by the subclass)
      - :meth:`init_gui_pylab`
      - :meth:`init_extensions`
      - :meth:`init_code`
    """
    extensions: Incomplete
    extra_extensions: Incomplete
    reraise_ipython_extension_failures: Incomplete
    default_extensions: Incomplete
    hide_initial_ns: Incomplete
    exec_files: Incomplete
    exec_PYTHONSTARTUP: Incomplete
    file_to_run: Incomplete
    exec_lines: Incomplete
    code_to_run: Incomplete
    module_to_run: Incomplete
    gui: Incomplete
    matplotlib: Incomplete
    pylab: Incomplete
    pylab_import_all: Incomplete
    ignore_cwd: Incomplete
    shell: Incomplete
    interact: Incomplete
    user_ns: Incomplete
    def init_path(self) -> None:
        """Add current working directory, '', to sys.path

        Unlike Python's default, we insert before the first `site-packages`
        or `dist-packages` directory,
        so that it is after the standard library.

        .. versionchanged:: 7.2
            Try to insert after the standard library, instead of first.
        .. versionchanged:: 8.0
            Allow optionally not including the current directory in sys.path
        """
    def init_shell(self) -> None: ...
    def init_gui_pylab(self):
        """Enable GUI event loop integration, taking pylab into account."""
    def init_extensions(self) -> None:
        """Load all IPython extensions in IPythonApp.extensions.

        This uses the :meth:`ExtensionManager.load_extensions` to load all
        the extensions listed in ``self.extensions``.
        """
    def init_code(self) -> None:
        """run the pre-flight code, specified via exec_lines"""
