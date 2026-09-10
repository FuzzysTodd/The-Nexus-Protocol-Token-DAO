from _typeshed import Incomplete

__all__ = ['demonstrate_256_colors', 'demonstrate_ansi_formatting', 'main', 'print_formatted_length', 'print_formatted_number', 'print_formatted_size', 'print_formatted_table', 'print_formatted_timespan', 'print_parsed_length', 'print_parsed_size', 'run_command']

def main() -> None:
    """Command line interface for the ``humanfriendly`` program."""
def run_command(command_line) -> None:
    """Run an external command and show a spinner while the command is running."""
def print_formatted_length(value) -> None:
    """Print a human readable length."""
def print_formatted_number(value) -> None:
    """Print large numbers in a human readable format."""
def print_formatted_size(value, binary) -> None:
    """Print a human readable size."""
def print_formatted_table(delimiter) -> None:
    """Read tabular data from standard input and print a table."""
def print_formatted_timespan(value) -> None:
    """Print a human readable timespan."""
def print_parsed_length(value) -> None:
    """Parse a human readable length and print the number of metres."""
def print_parsed_size(value) -> None:
    """Parse a human readable data size and print the number of bytes."""
def demonstrate_ansi_formatting() -> None:
    """Demonstrate the use of ANSI escape sequences."""
def demonstrate_256_colors(i, j, group: Incomplete | None = None) -> None:
    """Demonstrate 256 color mode support."""
