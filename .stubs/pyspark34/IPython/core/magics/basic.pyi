from IPython.core import magic_arguments as magic_arguments, page as page
from IPython.core.error import UsageError as UsageError
from IPython.core.magic import Magics as Magics, line_magic as line_magic, magic_escapes as magic_escapes, magics_class as magics_class
from IPython.testing.skipdoctest import skip_doctest as skip_doctest
from IPython.utils.ipstruct import Struct as Struct
from IPython.utils.text import dedent as dedent, format_screen as format_screen, indent as indent
from _typeshed import Incomplete

class MagicsDisplay:
    ignore: Incomplete
    magics_manager: Incomplete
    def __init__(self, magics_manager, ignore: Incomplete | None = None) -> None: ...

class BasicMagics(Magics):
    """Magics that provide central IPython functionality.

    These are various magics that don't fit into specific categories but that
    are all part of the base 'IPython experience'."""
    def alias_magic(self, line: str = '') -> None:
        '''Create an alias for an existing line or cell magic.

        Examples
        --------
        ::

          In [1]: %alias_magic t timeit
          Created `%t` as an alias for `%timeit`.
          Created `%%t` as an alias for `%%timeit`.

          In [2]: %t -n1 pass
          1 loops, best of 3: 954 ns per loop

          In [3]: %%t -n1
             ...: pass
             ...:
          1 loops, best of 3: 954 ns per loop

          In [4]: %alias_magic --cell whereami pwd
          UsageError: Cell magic function `%%pwd` not found.
          In [5]: %alias_magic --line whereami pwd
          Created `%whereami` as an alias for `%pwd`.

          In [6]: %whereami
          Out[6]: u\'/home/testuser\'

          In [7]: %alias_magic h history "-p -l 30" --line
          Created `%h` as an alias for `%history -l 30`.
        '''
    def lsmagic(self, parameter_s: str = ''):
        """List currently available magic functions."""
    def magic(self, parameter_s: str = '') -> None:
        """Print information about the magic function system.

        Supported formats: -latex, -brief, -rest
        """
    def page(self, parameter_s: str = '') -> None:
        """Pretty print the object and display it through a pager.

        %page [options] OBJECT

        If no object is given, use _ (last output).

        Options:

          -r: page str(object), don't pretty-print it."""
    def pprint(self, parameter_s: str = '') -> None:
        """Toggle pretty printing on/off."""
    def colors(self, parameter_s: str = '') -> None:
        """Switch color scheme for prompts, info system and exception handlers.

        Currently implemented schemes: NoColor, Linux, LightBG.

        Color scheme names are not case-sensitive.

        Examples
        --------
        To get a plain black and white terminal::

          %colors nocolor
        """
    def xmode(self, parameter_s: str = '') -> None:
        """Switch modes for the exception handlers.

        Valid modes: Plain, Context, Verbose, and Minimal.

        If called without arguments, acts as a toggle.

        When in verbose mode the value `--show` (and `--hide`)
        will respectively show (or hide) frames with ``__tracebackhide__ =
        True`` value set.
        """
    def quickref(self, arg) -> None:
        """ Show a quick reference sheet """
    def doctest_mode(self, parameter_s: str = '') -> None:
        """Toggle doctest mode on and off.

        This mode is intended to make IPython behave as much as possible like a
        plain Python shell, from the perspective of how its prompts, exceptions
        and output look.  This makes it easy to copy and paste parts of a
        session into doctests.  It does so by:

        - Changing the prompts to the classic ``>>>`` ones.
        - Changing the exception reporting mode to 'Plain'.
        - Disabling pretty-printing of output.

        Note that IPython also supports the pasting of code snippets that have
        leading '>>>' and '...' prompts in them.  This means that you can paste
        doctests from files or docstrings (even if they have leading
        whitespace), and the code will execute correctly.  You can then use
        '%history -t' to see the translated history; this will give you the
        input after removal of all the leading prompts and whitespace, which
        can be pasted back into an editor.

        With these features, you can switch into this mode easily whenever you
        need to do testing and changes to doctests, without having to leave
        your existing IPython session.
        """
    def gui(self, parameter_s: str = ''):
        """Enable or disable IPython GUI event loop integration.

        %gui [GUINAME]

        This magic replaces IPython's threaded shells that were activated
        using the (pylab/wthread/etc.) command line flags.  GUI toolkits
        can now be enabled at runtime and keyboard
        interrupts should work without any problems.  The following toolkits
        are supported:  wxPython, PyQt4, PyGTK, Tk and Cocoa (OSX)::

            %gui wx      # enable wxPython event loop integration
            %gui qt      # enable PyQt/PySide event loop integration
                         # with the latest version available.
            %gui qt6     # enable PyQt6/PySide6 event loop integration
            %gui qt5     # enable PyQt5/PySide2 event loop integration
            %gui gtk     # enable PyGTK event loop integration
            %gui gtk3    # enable Gtk3 event loop integration
            %gui gtk4    # enable Gtk4 event loop integration
            %gui tk      # enable Tk event loop integration
            %gui osx     # enable Cocoa event loop integration
                         # (requires %matplotlib 1.1)
            %gui         # disable all event loop integration

        WARNING:  after any of these has been called you can simply create
        an application object, but DO NOT start the event loop yourself, as
        we have already handled that.
        """
    def precision(self, s: str = ''):
        """Set floating point precision for pretty printing.

        Can set either integer precision or a format string.

        If numpy has been imported and precision is an int,
        numpy display precision will also be set, via ``numpy.set_printoptions``.

        If no argument is given, defaults will be restored.

        Examples
        --------
        ::

            In [1]: from math import pi

            In [2]: %precision 3
            Out[2]: u'%.3f'

            In [3]: pi
            Out[3]: 3.142

            In [4]: %precision %i
            Out[4]: u'%i'

            In [5]: pi
            Out[5]: 3

            In [6]: %precision %e
            Out[6]: u'%e'

            In [7]: pi**10
            Out[7]: 9.364805e+04

            In [8]: %precision
            Out[8]: u'%r'

            In [9]: pi**10
            Out[9]: 93648.047476082982
        """
    def notebook(self, s) -> None:
        '''Export and convert IPython notebooks.

        This function can export the current IPython history to a notebook file.
        For example, to export the history to "foo.ipynb" do "%notebook foo.ipynb".
        '''

class AsyncMagics(BasicMagics):
    def autoawait(self, parameter_s) -> None:
        """
        Allow to change the status of the autoawait option.

        This allow you to set a specific asynchronous code runner.

        If no value is passed, print the currently used asynchronous integration
        and whether it is activated.

        It can take a number of value evaluated in the following order:

        - False/false/off deactivate autoawait integration
        - True/true/on activate autoawait integration using configured default
          loop
        - asyncio/curio/trio activate autoawait integration and use integration
          with said library.

        - `sync` turn on the pseudo-sync integration (mostly used for
          `IPython.embed()` which does not run IPython with a real eventloop and
          deactivate running asynchronous code. Turning on Asynchronous code with
          the pseudo sync loop is undefined behavior and may lead IPython to crash.

        If the passed parameter does not match any of the above and is a python
        identifier, get said object from user namespace and set it as the
        runner, and activate autoawait.

        If the object is a fully qualified object name, attempt to import it and
        set it as the runner, and activate autoawait.

        The exact behavior of autoawait is experimental and subject to change
        across version of IPython and Python.
        """
