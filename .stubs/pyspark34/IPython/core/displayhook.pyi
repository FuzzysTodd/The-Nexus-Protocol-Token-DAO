from _typeshed import Incomplete
from traitlets.config.configurable import Configurable

class DisplayHook(Configurable):
    """The custom IPython displayhook to replace sys.displayhook.

    This class does many things, but the basic idea is that it is a callable
    that gets called anytime user code returns a value.
    """
    shell: Incomplete
    exec_result: Incomplete
    cull_fraction: Incomplete
    do_full_cache: int
    cache_size: Incomplete
    def __init__(self, shell: Incomplete | None = None, cache_size: int = 1000, **kwargs) -> None: ...
    @property
    def prompt_count(self): ...
    def check_for_underscore(self) -> None:
        """Check if the user has set the '_' variable by hand."""
    def quiet(self):
        """Should we silence the display hook because of ';'?"""
    @staticmethod
    def semicolon_at_end_of_expression(expression):
        """Parse Python expression and detects whether last token is ';'"""
    def start_displayhook(self) -> None:
        """Start the displayhook, initializing resources."""
    def write_output_prompt(self) -> None:
        """Write the output prompt.

        The default implementation simply writes the prompt to
        ``sys.stdout``.
        """
    def compute_format_data(self, result):
        '''Compute format data of the object to be displayed.

        The format data is a generalization of the :func:`repr` of an object.
        In the default implementation the format data is a :class:`dict` of
        key value pair where the keys are valid MIME types and the values
        are JSON\'able data structure containing the raw data for that MIME
        type. It is up to frontends to determine pick a MIME to to use and
        display that data in an appropriate manner.

        This method only computes the format data for the object and should
        NOT actually print or write that to a stream.

        Parameters
        ----------
        result : object
            The Python object passed to the display hook, whose format will be
            computed.

        Returns
        -------
        (format_dict, md_dict) : dict
            format_dict is a :class:`dict` whose keys are valid MIME types and values are
            JSON\'able raw data for that MIME type. It is recommended that
            all return values of this should always include the "text/plain"
            MIME type representation of the object.
            md_dict is a :class:`dict` with the same MIME type keys
            of metadata associated with each output.

        '''
    prompt_end_newline: bool
    def write_format_data(self, format_dict, md_dict: Incomplete | None = None) -> None:
        """Write the format data dict to the frontend.

        This default version of this method simply writes the plain text
        representation of the object to ``sys.stdout``. Subclasses should
        override this method to send the entire `format_dict` to the
        frontends.

        Parameters
        ----------
        format_dict : dict
            The format dict for the object passed to `sys.displayhook`.
        md_dict : dict (optional)
            The metadata dict to be associated with the display data.
        """
    ___: Incomplete
    __: Incomplete
    _: Incomplete
    def update_user_ns(self, result) -> None:
        """Update user_ns with various things like _, __, _1, etc."""
    def fill_exec_result(self, result) -> None: ...
    def log_output(self, format_dict) -> None:
        """Log the output."""
    def finish_displayhook(self) -> None:
        """Finish up all displayhook activities."""
    def __call__(self, result: Incomplete | None = None) -> None:
        """Printing with history cache management.

        This is invoked every time the interpreter needs to print, and is
        activated by setting the variable sys.displayhook to it.
        """
    def cull_cache(self) -> None:
        """Output cache is full, cull the oldest entries"""
    def flush(self) -> None: ...

class CapturingDisplayHook:
    shell: Incomplete
    outputs: Incomplete
    def __init__(self, shell, outputs: Incomplete | None = None) -> None: ...
    def __call__(self, result: Incomplete | None = None) -> None: ...
