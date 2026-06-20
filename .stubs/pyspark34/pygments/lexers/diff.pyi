from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['DiffLexer', 'DarcsPatchLexer', 'WDiffLexer']

class DiffLexer(RegexLexer):
    """
    Lexer for unified or context-style diffs or patches.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class DarcsPatchLexer(RegexLexer):
    """
    DarcsPatchLexer is a lexer for the various versions of the darcs patch
    format.  Examples of this format are derived by commands such as
    ``darcs annotate --patch`` and ``darcs send``.

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    DPATCH_KEYWORDS: Incomplete
    tokens: Incomplete

class WDiffLexer(RegexLexer):
    '''
    A wdiff lexer.

    Note that:

    * It only works with normal output (without options like ``-l``).
    * If the target files contain "[-", "-]", "{+", or "+}",
      especially they are unbalanced, the lexer will get confused.

    .. versionadded:: 2.2
    '''
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    ins_op: str
    ins_cl: str
    del_op: str
    del_cl: str
    normal: str
    tokens: Incomplete
