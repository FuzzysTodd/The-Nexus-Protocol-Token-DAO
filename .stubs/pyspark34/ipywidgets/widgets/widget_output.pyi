from .._version import __jupyter_widgets_output_version__ as __jupyter_widgets_output_version__
from .domwidget import DOMWidget as DOMWidget
from .trait_types import TypedTuple as TypedTuple
from .widget import register as register
from _typeshed import Incomplete

class Output(DOMWidget):
    """Widget used as a context manager to display output.

    This widget can capture and display stdout, stderr, and rich output.  To use
    it, create an instance of it and display it.

    You can then use the widget as a context manager: any output produced while in the
    context will be captured and displayed in the widget instead of the standard output
    area.

    You can also use the .capture() method to decorate a function or a method. Any output
    produced by the function will then go to the output widget. This is useful for
    debugging widget callbacks, for example.

    Example::
        import ipywidgets as widgets
        from IPython.display import display
        out = widgets.Output()
        display(out)

        print('prints to output area')

        with out:
            print('prints to output widget')

        @out.capture()
        def func():
            print('prints to output widget')
    """
    msg_id: Incomplete
    outputs: Incomplete
    def clear_output(self, *pargs, **kwargs) -> None:
        """
        Clear the content of the output widget.

        Parameters
        ----------

        wait: bool
            If True, wait to clear the output until new output is
            available to replace it. Default: False
        """
    def capture(self, clear_output: bool = False, *clear_args, **clear_kwargs):
        """
        Decorator to capture the stdout and stderr of a function.

        Parameters
        ----------

        clear_output: bool
            If True, clear the content of the output widget at every
            new function call. Default: False

        wait: bool
            If True, wait to clear the output until new output is
            available to replace it. This is only used if clear_output
            is also True.
            Default: False
        """
    def __enter__(self) -> None:
        """Called upon entering output widget context manager."""
    def __exit__(self, etype: type[BaseException] | None, evalue: BaseException | None, tb: types.TracebackType | None):
        """Called upon exiting output widget context manager."""
    def append_stdout(self, text) -> None:
        """Append text to the stdout stream."""
    def append_stderr(self, text) -> None:
        """Append text to the stderr stream."""
    def append_display_data(self, display_object) -> None:
        """Append a display object as an output.

        Parameters
        ----------
        display_object : IPython.core.display.DisplayObject
            The object to display (e.g., an instance of
            `IPython.display.Markdown` or `IPython.display.Image`).
        """
