from _typeshed import Incomplete
from coloredlogs.converter import capture as capture, convert as convert
from coloredlogs.demo import demonstrate_colored_logging as demonstrate_colored_logging

logger: Incomplete

def main() -> None:
    """Command line interface for the ``coloredlogs`` program."""
def convert_command_output(*command) -> None:
    """
    Command line interface for ``coloredlogs --to-html``.

    Takes a command (and its arguments) and runs the program under ``script``
    (emulating an interactive terminal), intercepts the output of the command
    and converts ANSI escape sequences in the output to HTML.
    """
