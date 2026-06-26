from .command_type import CommandType as CommandType

__all__ = ['CommandType', 'LegacyCommandChannel', 'send', 'receive', '_set_in_file', '_set_out_file', '_get_out_file']

def _set_in_file(in_file) -> None: ...
def _set_out_file(out_file) -> None: ...
def _get_out_file(): ...

class LegacyCommandChannel:
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...

def send(command, data) -> None:
    """Send command to Training Service.
    command: CommandType object.
    data: string payload.
    """
def receive():
    """Receive a command from Training Service.
    Returns a tuple of command (CommandType) and payload (str)
    """
