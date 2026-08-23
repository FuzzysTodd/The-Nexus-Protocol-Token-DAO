from _typeshed import Incomplete
from collections.abc import Generator
from lingua.extractors import Extractor
from mako.ext.extract import MessageExtractor as MessageExtractor

class LinguaMakoExtractor(Extractor, MessageExtractor):
    """Mako templates"""
    use_bytes: bool
    extensions: Incomplete
    default_config: Incomplete
    options: Incomplete
    filename: Incomplete
    python_extractor: Incomplete
    def __call__(self, filename, options, fileobj: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
    def process_python(self, code, code_lineno, translator_strings) -> Generator[Incomplete, None, None]: ...
