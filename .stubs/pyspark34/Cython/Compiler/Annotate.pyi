from . import Version as Version
from .. import Utils as Utils
from .Code import CCodeWriter as CCodeWriter
from _typeshed import Incomplete

class AnnotationCCodeWriter(CCodeWriter):
    COMPLETE_CODE_TITLE: str
    show_entire_c_code: Incomplete
    annotation_buffer: Incomplete
    last_annotated_pos: Incomplete
    annotations: Incomplete
    code: Incomplete
    scopes: Incomplete
    def __init__(self, create_from: Incomplete | None = None, buffer: Incomplete | None = None, copy_formatting: bool = True, show_entire_c_code: bool = False, source_desc: Incomplete | None = None) -> None: ...
    def create_new(self, create_from, buffer, copy_formatting): ...
    def mark_pos(self, pos, trace: bool = True) -> None: ...
    def annotate(self, pos, item) -> None: ...
    def save_annotation(self, source_filename, target_filename, coverage_xml: Incomplete | None = None) -> None: ...

class AnnotationItem:
    style: Incomplete
    text: Incomplete
    tag: Incomplete
    size: Incomplete
    def __init__(self, style, text, tag: str = '', size: int = 0) -> None: ...
    def start(self): ...
    def end(self): ...
