import socket
from _typeshed import Incomplete
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.input import PipeInput
from prompt_toolkit.styles import BaseStyle
from typing import Awaitable, Callable

__all__ = ['TelnetServer']

class _ConnectionStdout:
    """
    Wrapper around socket which provides `write` and `flush` methods for the
    Vt100_Output output.
    """
    def __init__(self, connection: socket.socket, encoding: str) -> None: ...
    def write(self, data: str) -> None: ...
    def isatty(self) -> bool: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    @property
    def encoding(self) -> str: ...
    @property
    def errors(self) -> str: ...

class TelnetConnection:
    """
    Class that represents one Telnet connection.
    """
    conn: Incomplete
    addr: Incomplete
    interact: Incomplete
    server: Incomplete
    encoding: Incomplete
    style: Incomplete
    vt100_input: Incomplete
    enable_cpr: Incomplete
    vt100_output: Incomplete
    size: Incomplete
    stdout: Incomplete
    parser: Incomplete
    context: Incomplete
    def __init__(self, conn: socket.socket, addr: tuple[str, int], interact: Callable[[TelnetConnection], Awaitable[None]], server: TelnetServer, encoding: str, style: BaseStyle | None, vt100_input: PipeInput, enable_cpr: bool = True) -> None: ...
    async def run_application(self) -> None:
        """
        Run application.
        """
    def feed(self, data: bytes) -> None:
        """
        Handler for incoming data. (Called by TelnetServer.)
        """
    def close(self) -> None:
        """
        Closed by client.
        """
    def send(self, formatted_text: AnyFormattedText) -> None:
        """
        Send text to the client.
        """
    def send_above_prompt(self, formatted_text: AnyFormattedText) -> None:
        """
        Send text to the client.
        This is asynchronous, returns a `Future`.
        """
    def erase_screen(self) -> None:
        """
        Erase the screen and move the cursor to the top.
        """

class TelnetServer:
    '''
    Telnet server implementation.

    Example::

        async def interact(connection):
            connection.send("Welcome")
            session = PromptSession()
            result = await session.prompt_async(message="Say something: ")
            connection.send(f"You said: {result}
")

        async def main():
            server = TelnetServer(interact=interact, port=2323)
            await server.run()
    '''
    host: Incomplete
    port: Incomplete
    interact: Incomplete
    encoding: Incomplete
    style: Incomplete
    enable_cpr: Incomplete
    connections: Incomplete
    def __init__(self, host: str = '127.0.0.1', port: int = 23, interact: Callable[[TelnetConnection], Awaitable[None]] = ..., encoding: str = 'utf-8', style: BaseStyle | None = None, enable_cpr: bool = True) -> None: ...
    async def run(self, ready_cb: Callable[[], None] | None = None) -> None:
        """
        Run the telnet server, until this gets cancelled.

        :param ready_cb: Callback that will be called at the point that we're
            actually listening.
        """
    def start(self) -> None:
        """
        Deprecated: Use `.run()` instead.

        Start the telnet server (stop by calling and awaiting `stop()`).
        """
    async def stop(self) -> None:
        """
        Deprecated: Use `.run()` instead.

        Stop a telnet server that was started using `.start()` and wait for the
        cancellation to complete.
        """
