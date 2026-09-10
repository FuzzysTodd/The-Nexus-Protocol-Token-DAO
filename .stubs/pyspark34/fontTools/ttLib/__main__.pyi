from fontTools.ttLib.ttFont import *
from _typeshed import Incomplete
from fontTools.ttLib import TTLibError as TTLibError, TTLibFileIsCollectionError as TTLibFileIsCollectionError
from fontTools.ttLib.ttCollection import TTCollection as TTCollection

def main(args: Incomplete | None = None) -> None:
    """Open/save fonts with TTFont() or TTCollection()

      ./fonttools ttLib [-oFILE] [-yNUMBER] files...

    If multiple files are given on the command-line,
    they are each opened (as a font or collection),
    and added to the font list.

    If -o (output-file) argument is given, the font
    list is then saved to the output file, either as
    a single font, if there is only one font, or as
    a collection otherwise.

    If -y (font-number) argument is given, only the
    specified font from collections is opened.

    The above allow extracting a single font from a
    collection, or combining multiple fonts into a
    collection.

    If --lazy or --no-lazy are give, those are passed
    to the TTFont() or TTCollection() constructors.
    """
