from _typeshed import Incomplete

__all__ = ['optimizeWidths', 'main']

class missingdict(dict):
    missing_func: Incomplete
    def __init__(self, missing_func) -> None: ...
    def __missing__(self, v): ...

def optimizeWidths(widths):
    """Given a list of glyph widths, or dictionary mapping glyph width to number of
    glyphs having that, returns a tuple of best CFF default and nominal glyph widths.

    This algorithm is linear in UPEM+numGlyphs."""
def main(args: Incomplete | None = None) -> None:
    """Calculate optimum defaultWidthX/nominalWidthX values"""
