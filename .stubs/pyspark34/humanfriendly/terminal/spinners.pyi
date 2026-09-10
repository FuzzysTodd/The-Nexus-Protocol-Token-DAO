from _typeshed import Incomplete

__all__ = ['AutomaticSpinner', 'GLYPHS', 'MINIMUM_INTERVAL', 'Spinner']

GLYPHS: Incomplete
MINIMUM_INTERVAL: float

class Spinner:
    """Show a spinner on the terminal as a simple means of feedback to the user."""
    interactive: Incomplete
    interval: Incomplete
    label: Incomplete
    states: Incomplete
    stream: Incomplete
    timer: Incomplete
    total: Incomplete
    counter: int
    last_update: int
    def __init__(self, **options) -> None:
        """
        Initialize a :class:`Spinner` object.

        :param label:

          The label for the spinner (a string or :data:`None`, defaults to
          :data:`None`).

        :param total:

          The expected number of steps (an integer or :data:`None`). If this is
          provided the spinner will show a progress percentage.

        :param stream:

          The output stream to show the spinner on (a file-like object,
          defaults to :data:`sys.stderr`).

        :param interactive:

          :data:`True` to enable rendering of the spinner, :data:`False` to
          disable (defaults to the result of ``stream.isatty()``).

        :param timer:

          A :class:`.Timer` object (optional). If this is given the spinner
          will show the elapsed time according to the timer.

        :param interval:

          The spinner will be updated at most once every this many seconds
          (a floating point number, defaults to :data:`MINIMUM_INTERVAL`).

        :param glyphs:

          A list of strings with single characters that are drawn in the same
          place in succession to implement a simple animated effect (defaults
          to :data:`GLYPHS`).
        """
    def step(self, progress: int = 0, label: Incomplete | None = None) -> None:
        """
        Advance the spinner by one step and redraw it.

        :param progress: The number of the current step, relative to the total
                         given to the :class:`Spinner` constructor (an integer,
                         optional). If not provided the spinner will not show
                         progress.
        :param label: The label to use while redrawing (a string, optional). If
                      not provided the label given to the :class:`Spinner`
                      constructor is used instead.

        This method advances the spinner by one step without starting a new
        line, causing an animated effect which is very simple but much nicer
        than waiting for a prompt which is completely silent for a long time.

        .. note:: This method uses time based rate limiting to avoid redrawing
                  the spinner too frequently. If you know you're dealing with
                  code that will call :func:`step()` at a high frequency,
                  consider using :func:`sleep()` to avoid creating the
                  equivalent of a busy loop that's rate limiting the spinner
                  99% of the time.
        """
    def sleep(self) -> None:
        """
        Sleep for a short period before redrawing the spinner.

        This method is useful when you know you're dealing with code that will
        call :func:`step()` at a high frequency. It will sleep for the interval
        with which the spinner is redrawn (less than a second). This avoids
        creating the equivalent of a busy loop that's rate limiting the
        spinner 99% of the time.

        This method doesn't redraw the spinner, you still have to call
        :func:`step()` in order to do that.
        """
    def clear(self) -> None:
        """
        Clear the spinner.

        The next line which is shown on the standard output or error stream
        after calling this method will overwrite the line that used to show the
        spinner.
        """
    def __enter__(self):
        """
        Enable the use of spinners as context managers.

        :returns: The :class:`Spinner` object.
        """
    def __exit__(self, exc_type: Incomplete | None = None, exc_value: Incomplete | None = None, traceback: Incomplete | None = None) -> None:
        """Clear the spinner when leaving the context."""

class AutomaticSpinner:
    """
    Show a spinner on the terminal that automatically starts animating.

    This class shows a spinner on the terminal (just like :class:`Spinner`
    does) that automatically starts animating. This class should be used as a
    context manager using the :keyword:`with` statement. The animation
    continues for as long as the context is active.

    :class:`AutomaticSpinner` provides an alternative to :class:`Spinner`
    for situations where it is not practical for the caller to periodically
    call :func:`~Spinner.step()` to advance the animation, e.g. because
    you're performing a blocking call and don't fancy implementing threading or
    subprocess handling just to provide some user feedback.

    This works using the :mod:`multiprocessing` module by spawning a
    subprocess to render the spinner while the main process is busy doing
    something more useful. By using the :keyword:`with` statement you're
    guaranteed that the subprocess is properly terminated at the appropriate
    time.
    """
    label: Incomplete
    show_time: Incomplete
    shutdown_event: Incomplete
    subprocess: Incomplete
    def __init__(self, label, show_time: bool = True) -> None:
        """
        Initialize an automatic spinner.

        :param label: The label for the spinner (a string).
        :param show_time: If this is :data:`True` (the default) then the spinner
                          shows elapsed time.
        """
    def __enter__(self) -> None:
        """Enable the use of automatic spinners as context managers."""
    def __exit__(self, exc_type: Incomplete | None = None, exc_value: Incomplete | None = None, traceback: Incomplete | None = None) -> None:
        """Enable the use of automatic spinners as context managers."""
