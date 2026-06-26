from _typeshed import Incomplete
from collections.abc import Generator
from mako.ext.extract import MessageExtractor as MessageExtractor

class BabelMakoExtractor(MessageExtractor):
    keywords: Incomplete
    options: Incomplete
    config: Incomplete
    def __init__(self, keywords, comment_tags, options) -> None: ...
    def __call__(self, fileobj): ...
    def process_python(self, code, code_lineno, translator_strings) -> Generator[Incomplete, None, None]: ...

def extract(fileobj, keywords, comment_tags, options) -> Generator[Incomplete, Incomplete, None]:
    """Extract messages from Mako templates.

    :param fileobj: the file-like object the messages should be extracted from
    :param keywords: a list of keywords (i.e. function names) that should be
                     recognized as translation functions
    :param comment_tags: a list of translator tags to search for and include
                         in the results
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)`` tuples
    :rtype: ``iterator``
    """
