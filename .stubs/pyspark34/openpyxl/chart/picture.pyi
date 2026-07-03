from _typeshed import Incomplete
from openpyxl.descriptors.nested import NestedBool as NestedBool, NestedFloat as NestedFloat, NestedMinMax as NestedMinMax, NestedNoneSet as NestedNoneSet
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class PictureOptions(Serialisable):
    tagname: str
    applyToFront: Incomplete
    applyToSides: Incomplete
    applyToEnd: Incomplete
    pictureFormat: Incomplete
    pictureStackUnit: Incomplete
    __elements__: Incomplete
    def __init__(self, applyToFront: Incomplete | None = None, applyToSides: Incomplete | None = None, applyToEnd: Incomplete | None = None, pictureFormat: Incomplete | None = None, pictureStackUnit: Incomplete | None = None) -> None: ...
