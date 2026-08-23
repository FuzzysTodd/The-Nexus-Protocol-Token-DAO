from _typeshed import Incomplete

__all__ = ['greek_unicode', 'sub', 'sup', 'xsym', 'vobj', 'hobj', 'pretty_symbol', 'annotated']

greek_unicode: Incomplete
sub: Incomplete
sup: Incomplete

def vobj(symb, height):
    """Construct vertical object of a given height

       see: xobj
    """
def hobj(symb, width):
    """Construct horizontal object of a given width

       see: xobj
    """
def xsym(sym):
    """get symbology for a 'character'"""
def pretty_symbol(symb_name, bold_name: bool = False):
    """return pretty representation of a symbol"""
def annotated(letter):
    """
    Return a stylised drawing of the letter ``letter``, together with
    information on how to put annotations (super- and subscripts to the
    left and to the right) on it.

    See pretty.py functions _print_meijerg, _print_hyper on how to use this
    information.
    """
