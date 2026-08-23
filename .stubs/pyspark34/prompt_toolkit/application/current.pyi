from .application import Application
from _typeshed import Incomplete
from prompt_toolkit.input.base import Input
from prompt_toolkit.output.base import Output
from typing import Any, Generator

__all__ = ['AppSession', 'get_app_session', 'get_app', 'get_app_or_none', 'set_app', 'create_app_session', 'create_app_session_from_tty']

class AppSession:
    """
    An AppSession is an interactive session, usually connected to one terminal.
    Within one such session, interaction with many applications can happen, one
    after the other.

    The input/output device is not supposed to change during one session.

    Warning: Always use the `create_app_session` function to create an
    instance, so that it gets activated correctly.

    :param input: Use this as a default input for all applications
        running in this session, unless an input is passed to the `Application`
        explicitly.
    :param output: Use this as a default output.
    """
    app: Incomplete
    def __init__(self, input: Input | None = None, output: Output | None = None) -> None: ...
    @property
    def input(self) -> Input: ...
    @property
    def output(self) -> Output: ...

def get_app_session() -> AppSession: ...
def get_app() -> Application[Any]:
    """
    Get the current active (running) Application.
    An :class:`.Application` is active during the
    :meth:`.Application.run_async` call.

    We assume that there can only be one :class:`.Application` active at the
    same time. There is only one terminal window, with only one stdin and
    stdout. This makes the code significantly easier than passing around the
    :class:`.Application` everywhere.

    If no :class:`.Application` is running, then return by default a
    :class:`.DummyApplication`. For practical reasons, we prefer to not raise
    an exception. This way, we don't have to check all over the place whether
    an actual `Application` was returned.

    (For applications like pymux where we can have more than one `Application`,
    we'll use a work-around to handle that.)
    """
def get_app_or_none() -> Application[Any] | None:
    """
    Get the current active (running) Application, or return `None` if no
    application is running.
    """
def set_app(app: Application[Any]) -> Generator[None, None, None]:
    """
    Context manager that sets the given :class:`.Application` active in an
    `AppSession`.

    This should only be called by the `Application` itself.
    The application will automatically be active while its running. If you want
    the application to be active in other threads/coroutines, where that's not
    the case, use `contextvars.copy_context()`, or use `Application.context` to
    run it in the appropriate context.
    """
def create_app_session(input: Input | None = None, output: Output | None = None) -> Generator[AppSession, None, None]:
    """
    Create a separate AppSession.

    This is useful if there can be multiple individual `AppSession`s going on.
    Like in the case of an Telnet/SSH server. This functionality uses
    contextvars and requires at least Python 3.7.
    """
def create_app_session_from_tty() -> Generator[AppSession, None, None]:
    """
    Create `AppSession` that always prefers the TTY input/output.

    Even if `sys.stdin` and `sys.stdout` are connected to input/output pipes,
    this will still use the terminal for interaction (because `sys.stderr` is
    still connected to the terminal).

    Usage::

        from prompt_toolkit.shortcuts import prompt

        with create_app_session_from_tty():
            prompt('>')
    """
