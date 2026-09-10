from .html import HTMLExporter as HTMLExporter
from _typeshed import Incomplete
from nbconvert.preprocessors.base import Preprocessor as Preprocessor

class _RevealMetadataPreprocessor(Preprocessor):
    def preprocess(self, nb, resources: Incomplete | None = None): ...

class SlidesExporter(HTMLExporter):
    """Exports HTML slides with reveal.js"""
    export_from_notebook: str
    reveal_url_prefix: Incomplete
    reveal_theme: Incomplete
    reveal_transition: Incomplete
    reveal_scroll: Incomplete
    reveal_number: Incomplete
    font_awesome_url: Incomplete
