from _typeshed import Incomplete

__all__ = ['app']

class Zone:
    image: Incomplete
    imageDimmed: Incomplete
    img: Incomplete
    fld: Incomplete
    txt: Incomplete
    def __init__(self, image, initialField, initialText) -> None: ...
    def initScrollText(self, frm, txt, contents) -> None: ...
    colorCycle: Incomplete
    def refresh(self) -> None: ...

class FindZone(Zone):
    def addTags(self, m) -> None: ...
    rex: Incomplete
    rexSel: Incomplete
    def substitute(self, *args) -> None: ...

class ReplaceZone(Zone):
    def addTags(self, m) -> None: ...
    diff: int
    repl: Incomplete
    def substitute(self) -> None: ...

def app() -> None: ...
