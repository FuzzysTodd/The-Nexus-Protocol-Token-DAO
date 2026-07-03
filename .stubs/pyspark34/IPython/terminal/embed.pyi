from IPython.core import compilerop as compilerop, magic_arguments as magic_arguments, ultratb as ultratb
from IPython.core.interactiveshell import DummyMod as DummyMod, InteractiveShell as InteractiveShell
from IPython.core.magic import Magics as Magics, line_magic as line_magic, magics_class as magics_class
from IPython.terminal.interactiveshell import TerminalInteractiveShell as TerminalInteractiveShell
from IPython.terminal.ipapp import load_default_config as load_default_config
from IPython.utils.io import ask_yes_no as ask_yes_no
from _typeshed import Incomplete

class KillEmbedded(Exception): ...
KillEmbeded = KillEmbedded

class EmbeddedMagics(Magics):
    def kill_embedded(self, parameter_s: str = '') -> None:
        '''%kill_embedded : deactivate for good the current embedded IPython

        This function (after asking for confirmation) sets an internal flag so
        that an embedded IPython will never activate again for the given call
        location. This is useful to permanently disable a shell that is being
        called inside a loop: once you\'ve figured out what you needed from it,
        you may then kill it and the program will then continue to run without
        the interactive shell interfering again.

        Kill Instance Option:

            If for some reasons you need to kill the location where the instance
            is created and not called, for example if you create a single
            instance in one place and debug in many locations, you can use the
            ``--instance`` option to kill this specific instance. Like for the
            ``call location`` killing an "instance" should work even if it is
            recreated within a loop.

        .. note::

            This was the default behavior before IPython 5.2

        '''
    def exit_raise(self, parameter_s: str = '') -> None:
        """%exit_raise Make the current embedded kernel exit and raise and exception.

        This function sets an internal flag so that an embedded IPython will
        raise a `IPython.terminal.embed.KillEmbedded` Exception on exit, and then exit the current I. This is
        useful to permanently exit a loop that create IPython embed instance.
        """

class _Sentinel:
    repr: Incomplete
    def __init__(self, repr) -> None: ...

class InteractiveShellEmbed(TerminalInteractiveShell):
    dummy_mode: Incomplete
    exit_msg: Incomplete
    embedded: Incomplete
    should_raise: Incomplete
    display_banner: Incomplete
    term_title: Incomplete
    @property
    def embedded_active(self): ...
    @embedded_active.setter
    def embedded_active(self, value) -> None: ...
    def __init__(self, **kw) -> None: ...
    def init_sys_modules(self) -> None:
        """
        Explicitly overwrite :mod:`IPython.core.interactiveshell` to do nothing.
        """
    def init_magics(self) -> None: ...
    keep_running: bool
    exit_now: bool
    old_banner2: Incomplete
    banner2: Incomplete
    def __call__(self, header: str = '', local_ns: Incomplete | None = None, module: Incomplete | None = None, dummy: Incomplete | None = None, stack_depth: int = 1, compile_flags: Incomplete | None = None, **kw) -> None:
        """Activate the interactive interpreter.

        __call__(self,header='',local_ns=None,module=None,dummy=None) -> Start
        the interpreter shell with the given local and global namespaces, and
        optionally print a header string at startup.

        The shell can be globally activated/deactivated using the
        dummy_mode attribute. This allows you to turn off a shell used
        for debugging globally.

        However, *each* time you call the shell you can override the current
        state of dummy_mode with the optional keyword parameter 'dummy'. For
        example, if you set dummy mode on with IPShell.dummy_mode = True, you
        can still have a specific call work by making it as IPShell(dummy=False).
        """
    user_module: Incomplete
    user_ns: Incomplete
    def mainloop(self, local_ns: Incomplete | None = None, module: Incomplete | None = None, stack_depth: int = 0, compile_flags: Incomplete | None = None) -> None:
        """Embeds IPython into a running python program.

        Parameters
        ----------
        local_ns, module
            Working local namespace (a dict) and module (a module or similar
            object). If given as None, they are automatically taken from the scope
            where the shell was called, so that program variables become visible.
        stack_depth : int
            How many levels in the stack to go to looking for namespaces (when
            local_ns or module is None). This allows an intermediate caller to
            make sure that this function gets the namespace from the intended
            level in the stack. By default (0) it will get its locals and globals
            from the immediate caller.
        compile_flags
            A bit field identifying the __future__ features
            that are enabled, as passed to the builtin :func:`compile` function.
            If given as None, they are automatically taken from the scope where
            the shell was called.

        """

def embed(*, header: str = '', compile_flags: Incomplete | None = None, **kwargs) -> None:
    """Call this to embed IPython at the current point in your program.

    The first invocation of this will create a :class:`terminal.embed.InteractiveShellEmbed`
    instance and then call it.  Consecutive calls just call the already
    created instance.

    If you don't want the kernel to initialize the namespace
    from the scope of the surrounding function,
    and/or you want to load full IPython configuration,
    you probably want `IPython.start_ipython()` instead.

    Here is a simple example::

        from IPython import embed
        a = 10
        b = 20
        embed(header='First time')
        c = 30
        d = 40
        embed()

    Parameters
    ----------

    header : str
        Optional header string to print at startup.
    compile_flags
        Passed to the `compile_flags` parameter of :py:meth:`terminal.embed.InteractiveShellEmbed.mainloop()`,
        which is called when the :class:`terminal.embed.InteractiveShellEmbed` instance is called.
    **kwargs : various, optional
        Any other kwargs will be passed to the :class:`terminal.embed.InteractiveShellEmbed` constructor.
        Full customization can be done by passing a traitlets :class:`Config` in as the
        `config` argument (see :ref:`configure_start_ipython` and :ref:`terminal_options`).
    """
