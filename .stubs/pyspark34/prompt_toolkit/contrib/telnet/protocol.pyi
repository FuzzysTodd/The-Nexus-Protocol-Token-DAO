from _typeshed import Incomplete
from typing import Callable

__all__ = ['TelnetProtocolParser']

class TelnetProtocolParser:
    """
    Parser for the Telnet protocol.
    Usage::

        def data_received(data):
            print(data)

        def size_received(rows, columns):
            print(rows, columns)

        p = TelnetProtocolParser(data_received, size_received)
        p.feed(binary_data)
    """
    data_received_callback: Incomplete
    size_received_callback: Incomplete
    ttype_received_callback: Incomplete
    def __init__(self, data_received_callback: Callable[[bytes], None], size_received_callback: Callable[[int, int], None], ttype_received_callback: Callable[[str], None]) -> None: ...
    def received_data(self, data: bytes) -> None: ...
    def do_received(self, data: bytes) -> None:
        """Received telnet DO command."""
    def dont_received(self, data: bytes) -> None:
        """Received telnet DONT command."""
    def will_received(self, data: bytes) -> None:
        """Received telnet WILL command."""
    def wont_received(self, data: bytes) -> None:
        """Received telnet WONT command."""
    def command_received(self, command: bytes, data: bytes) -> None: ...
    def naws(self, data: bytes) -> None:
        """
        Received NAWS. (Window dimensions.)
        """
    def ttype(self, data: bytes) -> None:
        """
        Received terminal type.
        """
    def negotiate(self, data: bytes) -> None:
        """
        Got negotiate data.
        """
    def feed(self, data: bytes) -> None:
        """
        Feed data to the parser.
        """
