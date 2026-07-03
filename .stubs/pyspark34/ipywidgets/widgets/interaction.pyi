from . import Button as Button, Checkbox as Checkbox, DOMWidget as DOMWidget, Dropdown as Dropdown, FloatSlider as FloatSlider, IntSlider as IntSlider, Output as Output, Text as Text, VBox as VBox, ValueWidget as ValueWidget, Widget as Widget
from _typeshed import Incomplete
from traitlets import HasTraits, observe as observe
from warnings import warn as warn

empty: Incomplete

def show_inline_matplotlib_plots() -> None:
    """Show matplotlib plots immediately if using the inline backend.

    With ipywidgets 6.0, matplotlib plots don't work well with interact when
    using the inline backend that comes with ipykernel. Basically, the inline
    backend only shows the plot after the entire cell executes, which does not
    play well with drawing plots inside of an interact function. See
    https://github.com/jupyter-widgets/ipywidgets/issues/1181/ and
    https://github.com/ipython/ipython/issues/10376 for more details. This
    function displays any matplotlib plots if the backend is the inline backend.
    """
def interactive_output(f, controls):
    """Connect widget controls to a function.

    This function does not generate a user interface for the widgets (unlike `interact`).
    This enables customisation of the widget user interface layout.
    The user interface layout must be defined and displayed manually.
    """

class interactive(VBox):
    '''
    A VBox container containing a group of interactive widgets tied to a
    function.

    Parameters
    ----------
    __interact_f : function
        The function to which the interactive widgets are tied. The `**kwargs`
        should match the function signature.
    __options : dict
        A dict of options. Currently, the only supported keys are
        ``"manual"`` (defaults to ``False``), ``"manual_name"`` (defaults
        to ``"Run Interact"``) and ``"auto_display"`` (defaults to ``False``).
    **kwargs : various, optional
        An interactive widget is created for each keyword argument that is a
        valid widget abbreviation.

    Note that the first two parameters intentionally start with a double
    underscore to avoid being mixed up with keyword arguments passed by
    ``**kwargs``.
    '''
    result: Incomplete
    args: Incomplete
    kwargs: Incomplete
    f: Incomplete
    clear_output: Incomplete
    manual: Incomplete
    manual_name: Incomplete
    auto_display: Incomplete
    kwargs_widgets: Incomplete
    manual_button: Incomplete
    out: Incomplete
    children: Incomplete
    def __init__(self, __interact_f, __options={}, **kwargs) -> None: ...
    def update(self, *args) -> None:
        """
        Call the interact function and update the output widget with
        the result of the function call.

        Parameters
        ----------
        *args : ignored
            Required for this method to be used as traitlets callback.
        """
    def signature(self): ...
    def find_abbreviations(self, kwargs):
        """Find the abbreviations for the given function and kwargs.
        Return (name, abbrev, default) tuples.
        """
    def widgets_from_abbreviations(self, seq):
        """Given a sequence of (name, abbrev, default) tuples, return a sequence of Widgets."""
    @classmethod
    def widget_from_abbrev(cls, abbrev, default=...):
        """Build a ValueWidget instance given an abbreviation or Widget."""
    @staticmethod
    def widget_from_single_value(o):
        """Make widgets from single values, which can be used as parameter defaults."""
    @staticmethod
    def widget_from_tuple(o):
        """Make widgets from a tuple abbreviation."""
    @staticmethod
    def widget_from_iterable(o):
        """Make widgets from an iterable. This should not be done for
        a string or tuple."""
    @classmethod
    def factory(cls): ...

class _InteractFactory:
    '''
    Factory for instances of :class:`interactive`.

    This class is needed to support options like::

        >>> @interact.options(manual=True)
        ... def greeting(text="World"):
        ...     print("Hello {}".format(text))

    Parameters
    ----------
    cls : class
        The subclass of :class:`interactive` to construct.
    options : dict
        A dict of options used to construct the interactive
        function. By default, this is returned by
        ``cls.default_options()``.
    kwargs : dict
        A dict of **kwargs to use for widgets.
    '''
    cls: Incomplete
    opts: Incomplete
    kwargs: Incomplete
    def __init__(self, cls, options, kwargs={}) -> None: ...
    def widget(self, f):
        """
        Return an interactive function widget for the given function.

        The widget is only constructed, not displayed nor attached to
        the function.

        Returns
        -------
        An instance of ``self.cls`` (typically :class:`interactive`).

        Parameters
        ----------
        f : function
            The function to which the interactive widgets are tied.
        """
    def __call__(self, __interact_f: Incomplete | None = None, **kwargs):
        '''
        Make the given function interactive by adding and displaying
        the corresponding :class:`interactive` widget.

        Expects the first argument to be a function. Parameters to this
        function are widget abbreviations passed in as keyword arguments
        (``**kwargs``). Can be used as a decorator (see examples).

        Returns
        -------
        f : __interact_f with interactive widget attached to it.

        Parameters
        ----------
        __interact_f : function
            The function to which the interactive widgets are tied. The `**kwargs`
            should match the function signature. Passed to :func:`interactive()`
        **kwargs : various, optional
            An interactive widget is created for each keyword argument that is a
            valid widget abbreviation. Passed to :func:`interactive()`

        Examples
        --------
        Render an interactive text field that shows the greeting with the passed in
        text::

            # 1. Using interact as a function
            def greeting(text="World"):
                print("Hello {}".format(text))
            interact(greeting, text="Jupyter Widgets")

            # 2. Using interact as a decorator
            @interact
            def greeting(text="World"):
                print("Hello {}".format(text))

            # 3. Using interact as a decorator with named parameters
            @interact(text="Jupyter Widgets")
            def greeting(text="World"):
                print("Hello {}".format(text))

        Render an interactive slider widget and prints square of number::

            # 1. Using interact as a function
            def square(num=1):
                print("{} squared is {}".format(num, num*num))
            interact(square, num=5)

            # 2. Using interact as a decorator
            @interact
            def square(num=2):
                print("{} squared is {}".format(num, num*num))

            # 3. Using interact as a decorator with named parameters
            @interact(num=5)
            def square(num=2):
                print("{} squared is {}".format(num, num*num))
        '''
    def options(self, **kwds):
        """
        Change options for interactive functions.

        Returns
        -------
        A new :class:`_InteractFactory` which will apply the
        options when called.
        """

interact: Incomplete
interact_manual: Incomplete

class fixed(HasTraits):
    """A pseudo-widget whose value is fixed and never synced to the client."""
    value: Incomplete
    description: Incomplete
    def __init__(self, value, **kwargs) -> None: ...
    def get_interact_value(self):
        """Return the value for this widget which should be passed to
        interactive functions. Custom widgets can change this method
        to process the raw value ``self.value``.
        """
