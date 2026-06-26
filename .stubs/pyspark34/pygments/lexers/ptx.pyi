from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PtxLexer']

class PtxLexer(RegexLexer):
    """
    For NVIDIA `PTX <https://docs.nvidia.com/cuda/parallel-thread-execution/>`_
    source.

    .. versionadded:: 2.16
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    string: str
    followsym: str
    identifier: Incomplete
    block_label: Incomplete
    tokens: Incomplete
