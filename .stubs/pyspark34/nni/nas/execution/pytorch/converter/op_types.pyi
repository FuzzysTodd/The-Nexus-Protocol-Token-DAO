from _typeshed import Incomplete
from enum import Enum

MODULE_EXCEPT_LIST: Incomplete

class OpTypeName(str, Enum):
    """
    op type to its type name str
    """
    Attr: str
    Constant: str
    LayerChoice: str
    InputChoice: str
    ValueChoice: str
    Placeholder: str
    MergedSlice: str
    Repeat: str
    Cell: str
