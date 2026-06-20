from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['IniLexer', 'SystemdLexer', 'DesktopLexer', 'RegeditLexer', 'PropertiesLexer', 'KconfigLexer', 'Cfengine3Lexer', 'ApacheConfLexer', 'SquidConfLexer', 'NginxConfLexer', 'LighttpdConfLexer', 'DockerLexer', 'TerraformLexer', 'TermcapLexer', 'TerminfoLexer', 'PkgConfigLexer', 'PacmanConfLexer', 'AugeasLexer', 'TOMLLexer', 'NestedTextLexer', 'SingularityLexer', 'UnixConfigLexer']

class IniLexer(RegexLexer):
    """
    Lexer for configuration files in INI style.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class DesktopLexer(RegexLexer):
    """
    Lexer for .desktop files.

    .. versionadded:: 2.16
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class SystemdLexer(RegexLexer):
    """
    Lexer for systemd unit files.

    .. versionadded:: 2.16
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class RegeditLexer(RegexLexer):
    """
    Lexer for Windows Registry files produced by regedit.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class PropertiesLexer(RegexLexer):
    """
    Lexer for configuration files in Java's properties format.

    Note: trailing whitespace counts as part of the value as per spec

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class KconfigLexer(RegexLexer):
    """
    For Linux-style Kconfig files.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: int
    def call_indent(level): ...
    def do_indent(level): ...
    tokens: Incomplete

class Cfengine3Lexer(RegexLexer):
    """
    Lexer for CFEngine3 policy files.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ApacheConfLexer(RegexLexer):
    """
    Lexer for configuration files following the Apache config file
    format.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class SquidConfLexer(RegexLexer):
    """
    Lexer for squid configuration files.

    .. versionadded:: 0.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    keywords: Incomplete
    opts: Incomplete
    actions: Incomplete
    actions_stats: Incomplete
    actions_log: Incomplete
    acls: Incomplete
    ip_re: str
    tokens: Incomplete

class NginxConfLexer(RegexLexer):
    """
    Lexer for Nginx configuration files.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class LighttpdConfLexer(RegexLexer):
    """
    Lexer for Lighttpd configuration files.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class DockerLexer(RegexLexer):
    """
    Lexer for Docker configuration files.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class TerraformLexer(ExtendedRegexLexer):
    """
    Lexer for terraformi ``.tf`` files.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    classes: Incomplete
    classes_re: Incomplete
    types: Incomplete
    numeric_functions: Incomplete
    string_functions: Incomplete
    collection_functions: Incomplete
    encoding_functions: Incomplete
    filesystem_functions: Incomplete
    date_time_functions: Incomplete
    hash_crypto_functions: Incomplete
    ip_network_functions: Incomplete
    type_conversion_functions: Incomplete
    builtins: Incomplete
    builtins_re: Incomplete
    def heredoc_callback(self, match, ctx) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class TermcapLexer(RegexLexer):
    """
    Lexer for termcap database source.

    This is very simple and minimal.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class TerminfoLexer(RegexLexer):
    """
    Lexer for terminfo database source.

    This is very simple and minimal.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PkgConfigLexer(RegexLexer):
    """
    Lexer for pkg-config
    (see also `manual page <http://linux.die.net/man/1/pkg-config>`_).

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PacmanConfLexer(RegexLexer):
    """
    Lexer for pacman.conf.

    Actually, IniLexer works almost fine for this format,
    but it yield error token. It is because pacman.conf has
    a form without assignment like:

        UseSyslog
        Color
        TotalDownload
        CheckSpace
        VerbosePkgLists

    These are flags to switch on.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class AugeasLexer(RegexLexer):
    """
    Lexer for Augeas.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class TOMLLexer(RegexLexer):
    """
    Lexer for TOML, a simple language
    for config files.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class NestedTextLexer(RegexLexer):
    """
    Lexer for *NextedText*, a human-friendly data format.

    .. versionadded:: 2.9

    .. versionchanged:: 2.16
        Added support for *NextedText* v3.0.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class SingularityLexer(RegexLexer):
    """
    Lexer for Singularity definition files.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """This is a quite simple script file, but there are a few keywords
        which seem unique to this language."""

class UnixConfigLexer(RegexLexer):
    """
    Lexer for Unix/Linux config files using colon-separated values, e.g.

    * ``/etc/group``
    * ``/etc/passwd``
    * ``/etc/shadow``

    .. versionadded:: 2.12
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
