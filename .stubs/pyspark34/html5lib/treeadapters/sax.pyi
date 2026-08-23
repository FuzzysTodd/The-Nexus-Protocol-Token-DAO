from ..constants import adjustForeignAttributes as adjustForeignAttributes, unadjustForeignAttributes as unadjustForeignAttributes
from _typeshed import Incomplete

prefix_mapping: Incomplete

def to_sax(walker, handler) -> None:
    """Call SAX-like content handler based on treewalker walker

    :arg walker: the treewalker to use to walk the tree to convert it

    :arg handler: SAX handler to use

    """
