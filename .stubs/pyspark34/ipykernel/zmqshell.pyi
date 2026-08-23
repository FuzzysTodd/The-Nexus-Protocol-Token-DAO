from IPython.core.displaypub import DisplayPublisher
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.magic import Magics
from _typeshed import Incomplete
from ipykernel import connect_qtconsole as connect_qtconsole, get_connection_file as get_connection_file, get_connection_info as get_connection_info
from ipykernel.displayhook import ZMQShellDisplayHook as ZMQShellDisplayHook
from ipykernel.jsonutil import encode_images as encode_images, json_clean as json_clean

class ZMQDisplayPublisher(DisplayPublisher):
    """A display publisher that publishes data using a ZeroMQ PUB socket."""
    session: Incomplete
    pub_socket: Incomplete
    parent_header: Incomplete
    topic: Incomplete
    def set_parent(self, parent) -> None:
        """Set the parent for outbound messages."""
    def publish(self, data, metadata: Incomplete | None = None, transient: Incomplete | None = None, update: bool = False) -> None:
        """Publish a display-data message

        Parameters
        ----------
        data : dict
            A mime-bundle dict, keyed by mime-type.
        metadata : dict, optional
            Metadata associated with the data.
        transient : dict, optional, keyword-only
            Transient data that may only be relevant during a live display,
            such as display_id.
            Transient data should not be persisted to documents.
        update : bool, optional, keyword-only
            If True, send an update_display_data message instead of display_data.
        """
    def clear_output(self, wait: bool = False) -> None:
        """Clear output associated with the current execution (cell).

        Parameters
        ----------
        wait : bool (default: False)
            If True, the output will not be cleared immediately,
            instead waiting for the next display before clearing.
            This reduces bounce during repeated clear & display loops.

        """
    def register_hook(self, hook) -> None:
        """
        Registers a hook with the thread-local storage.

        Parameters
        ----------
        hook : Any callable object

        Returns
        -------
        Either a publishable message, or `None`.
        The DisplayHook objects must return a message from
        the __call__ method if they still require the
        `session.send` method to be called after transformation.
        Returning `None` will halt that execution path, and
        session.send will not be called.
        """
    def unregister_hook(self, hook):
        """
        Un-registers a hook with the thread-local storage.

        Parameters
        ----------
        hook : Any callable object which has previously been
            registered as a hook.

        Returns
        -------
        bool - `True` if the hook was removed, `False` if it wasn't
            found.
        """

class KernelMagics(Magics):
    """Kernel magics."""
    def edit(self, parameter_s: str = '', last_call: Incomplete | None = None) -> None:
        """Bring up an editor and execute the resulting code.

        Usage:
          %edit [options] [args]

        %edit runs an external text editor. You will need to set the command for
        this editor via the ``TerminalInteractiveShell.editor`` option in your
        configuration file before it will work.

        This command allows you to conveniently edit multi-line code right in
        your IPython session.

        If called without arguments, %edit opens up an empty editor with a
        temporary file and will execute the contents of this file when you
        close it (don't forget to save it!).

        Options:

        -n <number>
          Open the editor at a specified line number. By default, the IPython
          editor hook uses the unix syntax 'editor +N filename', but you can
          configure this by providing your own modified hook if your favorite
          editor supports line-number specifications with a different syntax.

        -p
          Call the editor with the same data as the previous time it was used,
          regardless of how long ago (in your current session) it was.

        -r
          Use 'raw' input. This option only applies to input taken from the
          user's history.  By default, the 'processed' history is used, so that
          magics are loaded in their transformed version to valid Python.  If
          this option is given, the raw input as typed as the command line is
          used instead.  When you exit the editor, it will be executed by
          IPython's own processor.

        Arguments:

        If arguments are given, the following possibilities exist:

        - The arguments are numbers or pairs of colon-separated numbers (like
          1 4:8 9). These are interpreted as lines of previous input to be
          loaded into the editor. The syntax is the same of the %macro command.

        - If the argument doesn't start with a number, it is evaluated as a
          variable and its contents loaded into the editor. You can thus edit
          any string which contains python code (including the result of
          previous edits).

        - If the argument is the name of an object (other than a string),
          IPython will try to locate the file where it was defined and open the
          editor at the point where it is defined. You can use ``%edit function``
          to load an editor exactly at the point where 'function' is defined,
          edit it and have the file be executed automatically.

          If the object is a macro (see %macro for details), this opens up your
          specified editor with a temporary file containing the macro's data.
          Upon exit, the macro is reloaded with the contents of the file.

          Note: opening at an exact line is only supported under Unix, and some
          editors (like kedit and gedit up to Gnome 2.8) do not understand the
          '+NUMBER' parameter necessary for this feature. Good editors like
          (X)Emacs, vi, jed, pico and joe all do.

        - If the argument is not found as a variable, IPython will look for a
          file with that name (adding .py if necessary) and load it into the
          editor. It will execute its contents with execfile() when you exit,
          loading any code in the file into your interactive namespace.

        Unlike in the terminal, this is designed to use a GUI editor, and we do
        not know when it has closed. So the file you edit will not be
        automatically executed or printed.

        Note that %edit is also available through the alias %ed.
        """
    def clear(self, arg_s) -> None:
        """Clear the terminal."""
    cls: Incomplete
    def less(self, arg_s) -> None:
        """Show a file through the pager.

        Files ending in .py are syntax-highlighted."""
    more: Incomplete
    def man(self, arg_s) -> None:
        """Find the man page for the given command and display in pager."""
    def connect_info(self, arg_s) -> None:
        """Print information for connecting other clients to this kernel

        It will print the contents of this session's connection file, as well as
        shortcuts for local clients.

        In the simplest case, when called from the most recently launched kernel,
        secondary clients can be connected, simply with:

        $> jupyter <app> --existing

        """
    def qtconsole(self, arg_s) -> None:
        """Open a qtconsole connected to this kernel.

        Useful for connecting a qtconsole to running notebooks, for better
        debugging.
        """
    def autosave(self, arg_s) -> None:
        """Set the autosave interval in the notebook (in seconds).

        The default value is 120, or two minutes.
        ``%autosave 0`` will disable autosave.

        This magic only has an effect when called from the notebook interface.
        It has no effect when called in a startup file.
        """

class ZMQInteractiveShell(InteractiveShell):
    """A subclass of InteractiveShell for ZMQ."""
    displayhook_class: Incomplete
    display_pub_class: Incomplete
    data_pub_class: Incomplete
    kernel: Incomplete
    parent_header: Incomplete
    readline_use: Incomplete
    autoindent: Incomplete
    exiter: Incomplete
    keepkernel_on_exit: Incomplete
    active_eventloop: Incomplete
    def enable_gui(self, gui) -> None:
        """Enable a given guil."""
    def init_environment(self) -> None:
        """Configure the user's environment."""
    def init_hooks(self) -> None:
        """Initialize hooks."""
    def init_data_pub(self) -> None:
        """Delay datapub init until request, for deprecation warnings"""
    @property
    def data_pub(self): ...
    @data_pub.setter
    def data_pub(self, pub) -> None: ...
    exit_now: Incomplete
    def ask_exit(self) -> None:
        """Engage the exit actions."""
    def run_cell(self, *args, **kwargs):
        """Run a cell."""
    def set_next_input(self, text, replace: bool = False) -> None:
        """Send the specified text to the frontend to be presented at the next
        input cell."""
    def set_parent(self, parent) -> None:
        """Set the parent header for associating output with its triggering input"""
    def get_parent(self):
        """Get the parent header."""
    def init_magics(self) -> None:
        """Initialize magics."""
    def init_virtualenv(self) -> None:
        """Initialize virtual environment."""
    def system_piped(self, cmd) -> None:
        """Call the given cmd in a subprocess, piping stdout/err

        Parameters
        ----------
        cmd : str
            Command to execute (can not end in '&', as background processes are
            not supported.  Should not be a command that expects input
            other than simple text.
        """
    system = system_piped
