import argparse
from _typeshed import Incomplete
from collections.abc import Iterable, Sequence
from markdown_it import __version__ as __version__
from markdown_it.main import MarkdownIt as MarkdownIt

version_str: Incomplete

def main(args: Sequence[str] | None = None) -> int: ...
def convert(filenames: Iterable[str]) -> None: ...
def convert_file(filename: str) -> None:
    """
    Parse a Markdown file and dump the output to stdout.
    """
def interactive() -> None:
    """
    Parse user input, dump to stdout, rinse and repeat.
    Python REPL style.
    """
def parse_args(args: Sequence[str] | None) -> argparse.Namespace:
    """Parse input CLI arguments."""
def print_heading() -> None: ...
