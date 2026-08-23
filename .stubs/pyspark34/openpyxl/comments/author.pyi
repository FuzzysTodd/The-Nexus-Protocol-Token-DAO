from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Sequence as Sequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class AuthorList(Serialisable):
    tagname: str
    author: Incomplete
    authors: Incomplete
    def __init__(self, author=()) -> None: ...
