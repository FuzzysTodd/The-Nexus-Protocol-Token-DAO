from pip._internal.cli.parser import ConfigOptionParser
from typing import List, Tuple

__all__ = ['create_main_parser', 'parse_command']

def create_main_parser() -> ConfigOptionParser:
    """Creates and returns the main parser for pip's CLI"""
def parse_command(args: List[str]) -> Tuple[str, List[str]]: ...
