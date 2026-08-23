from typing import List

class ANSI:
    """
    Helper for en.wikipedia.org/wiki/ANSI_escape_code
    """
    @classmethod
    def bold(cls, s: str) -> str: ...
    @classmethod
    def gray(cls, s: str) -> str: ...
    @classmethod
    def red(cls, s: str) -> str: ...

def tabulate(rows: List[List[str | int]], headers: List[str]) -> str:
    """
    Inspired by:

    - stackoverflow.com/a/8356620/593036
    - stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
    """
