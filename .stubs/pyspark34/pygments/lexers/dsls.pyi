from _typeshed import Incomplete
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['ProtoBufLexer', 'ZeekLexer', 'PuppetLexer', 'RslLexer', 'MscgenLexer', 'VGLLexer', 'AlloyLexer', 'PanLexer', 'CrmshLexer', 'ThriftLexer', 'FlatlineLexer', 'SnowballLexer']

class ProtoBufLexer(RegexLexer):
    """
    Lexer for Protocol Buffer definition files.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class ThriftLexer(RegexLexer):
    """
    For Thrift interface definitions.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ZeekLexer(RegexLexer):
    """
    For Zeek scripts.

    .. versionadded:: 2.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
BroLexer = ZeekLexer

class PuppetLexer(RegexLexer):
    """
    For Puppet configuration DSL.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class RslLexer(RegexLexer):
    """
    RSL is the formal specification
    language used in RAISE (Rigorous Approach to Industrial Software Engineering)
    method.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """
        Check for the most common text in the beginning of a RSL file.
        """

class MscgenLexer(RegexLexer):
    """
    For Mscgen files.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class VGLLexer(RegexLexer):
    """
    For SampleManager VGL source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete

class AlloyLexer(RegexLexer):
    """
    For Alloy source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    iden_rex: str
    string_rex: str
    text_tuple: Incomplete
    tokens: Incomplete

class PanLexer(RegexLexer):
    """
    Lexer for pan source files.

    Based on tcsh lexer.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class CrmshLexer(RegexLexer):
    """
    Lexer for crmsh configuration files for Pacemaker clusters.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    elem: Incomplete
    sub: Incomplete
    acl: Incomplete
    bin_rel: Incomplete
    un_ops: Incomplete
    date_exp: Incomplete
    acl_mod: str
    bin_ops: str
    val_qual: str
    rsc_role_action: str
    tokens: Incomplete

class FlatlineLexer(RegexLexer):
    """
    Lexer for Flatline expressions.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    special_forms: Incomplete
    builtins: Incomplete
    valid_name: str
    tokens: Incomplete

class SnowballLexer(ExtendedRegexLexer):
    """
    Lexer for Snowball source code.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    tokens: Incomplete
    def get_tokens_unprocessed(self, text: Incomplete | None = None, context: Incomplete | None = None): ...
