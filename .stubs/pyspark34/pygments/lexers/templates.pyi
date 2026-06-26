from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import DelegatingLexer, Lexer, RegexLexer

__all__ = ['HtmlPhpLexer', 'XmlPhpLexer', 'CssPhpLexer', 'JavascriptPhpLexer', 'ErbLexer', 'RhtmlLexer', 'XmlErbLexer', 'CssErbLexer', 'JavascriptErbLexer', 'SmartyLexer', 'HtmlSmartyLexer', 'XmlSmartyLexer', 'CssSmartyLexer', 'JavascriptSmartyLexer', 'DjangoLexer', 'HtmlDjangoLexer', 'CssDjangoLexer', 'XmlDjangoLexer', 'JavascriptDjangoLexer', 'GenshiLexer', 'HtmlGenshiLexer', 'GenshiTextLexer', 'CssGenshiLexer', 'JavascriptGenshiLexer', 'MyghtyLexer', 'MyghtyHtmlLexer', 'MyghtyXmlLexer', 'MyghtyCssLexer', 'MyghtyJavascriptLexer', 'MasonLexer', 'MakoLexer', 'MakoHtmlLexer', 'MakoXmlLexer', 'MakoJavascriptLexer', 'MakoCssLexer', 'JspLexer', 'CheetahLexer', 'CheetahHtmlLexer', 'CheetahXmlLexer', 'CheetahJavascriptLexer', 'EvoqueLexer', 'EvoqueHtmlLexer', 'EvoqueXmlLexer', 'ColdfusionLexer', 'ColdfusionHtmlLexer', 'ColdfusionCFCLexer', 'VelocityLexer', 'VelocityHtmlLexer', 'VelocityXmlLexer', 'SspLexer', 'TeaTemplateLexer', 'LassoHtmlLexer', 'LassoXmlLexer', 'LassoCssLexer', 'LassoJavascriptLexer', 'HandlebarsLexer', 'HandlebarsHtmlLexer', 'YamlJinjaLexer', 'LiquidLexer', 'TwigLexer', 'TwigHtmlLexer', 'Angular2Lexer', 'Angular2HtmlLexer', 'SqlJinjaLexer']

class ErbLexer(Lexer):
    """
    Generic ERB (Ruby Templating) lexer.

    Just highlights ruby code between the preprocessor directives, other data
    is left untouched by the lexer.

    All options are also forwarded to the `RubyLexer`.
    """
    name: str
    url: str
    aliases: Incomplete
    mimetypes: Incomplete
    ruby_lexer: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]:
        '''
        Since ERB doesn\'t allow "<%" and other tags inside of ruby
        blocks we have to use a split approach here that fails for
        that too.
        '''
    def analyse_text(text): ...

class SmartyLexer(RegexLexer):
    """
    Generic Smarty template lexer.

    Just highlights smarty code between the preprocessor directives, other
    data is left untouched by the lexer.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class VelocityLexer(RegexLexer):
    """
    Generic Velocity template lexer.

    Just highlights velocity directives and variable references, other
    data is left untouched by the lexer.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    identifier: str
    tokens: Incomplete
    def analyse_text(text): ...

class VelocityHtmlLexer(DelegatingLexer):
    """
    Subclass of the `VelocityLexer` that highlights unlexed data
    with the `HtmlLexer`.

    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class VelocityXmlLexer(DelegatingLexer):
    """
    Subclass of the `VelocityLexer` that highlights unlexed data
    with the `XmlLexer`.

    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class DjangoLexer(RegexLexer):
    """
    Generic `django <http://www.djangoproject.com/documentation/templates/>`_
    and `jinja <https://jinja.pocoo.org/jinja/>`_ template lexer.

    It just highlights django/jinja code between the preprocessor directives,
    other data is left untouched by the lexer.
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class MyghtyLexer(RegexLexer):
    """
    Generic myghty templates lexer. Code that isn't Myghty
    markup is yielded as `Token.Other`.

    .. versionadded:: 0.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MyghtyHtmlLexer(DelegatingLexer):
    """
    Subclass of the `MyghtyLexer` that highlights unlexed data
    with the `HtmlLexer`.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MyghtyXmlLexer(DelegatingLexer):
    """
    Subclass of the `MyghtyLexer` that highlights unlexed data
    with the `XmlLexer`.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MyghtyJavascriptLexer(DelegatingLexer):
    """
    Subclass of the `MyghtyLexer` that highlights unlexed data
    with the `JavascriptLexer`.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MyghtyCssLexer(DelegatingLexer):
    """
    Subclass of the `MyghtyLexer` that highlights unlexed data
    with the `CssLexer`.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MasonLexer(RegexLexer):
    """
    Generic mason templates lexer. Stolen from Myghty lexer. Code that isn't
    Mason markup is HTML.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class MakoLexer(RegexLexer):
    """
    Generic mako templates lexer. Code that isn't Mako
    markup is yielded as `Token.Other`.

    .. versionadded:: 0.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MakoHtmlLexer(DelegatingLexer):
    """
    Subclass of the `MakoLexer` that highlights unlexed data
    with the `HtmlLexer`.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MakoXmlLexer(DelegatingLexer):
    """
    Subclass of the `MakoLexer` that highlights unlexed data
    with the `XmlLexer`.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MakoJavascriptLexer(DelegatingLexer):
    """
    Subclass of the `MakoLexer` that highlights unlexed data
    with the `JavascriptLexer`.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class MakoCssLexer(DelegatingLexer):
    """
    Subclass of the `MakoLexer` that highlights unlexed data
    with the `CssLexer`.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class CheetahPythonLexer(Lexer):
    """
    Lexer for handling Cheetah's special $ tokens in Python syntax.
    """
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class CheetahLexer(RegexLexer):
    """
    Generic cheetah templates lexer. Code that isn't Cheetah
    markup is yielded as `Token.Other`.  This also works for
    `spitfire templates`_ which use the same syntax.

    .. _spitfire templates: http://code.google.com/p/spitfire/
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CheetahHtmlLexer(DelegatingLexer):
    """
    Subclass of the `CheetahLexer` that highlights unlexed data
    with the `HtmlLexer`.
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class CheetahXmlLexer(DelegatingLexer):
    """
    Subclass of the `CheetahLexer` that highlights unlexed data
    with the `XmlLexer`.
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class CheetahJavascriptLexer(DelegatingLexer):
    """
    Subclass of the `CheetahLexer` that highlights unlexed data
    with the `JavascriptLexer`.
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class GenshiTextLexer(RegexLexer):
    """
    A lexer that highlights genshi text templates.
    """
    name: str
    url: str
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class GenshiMarkupLexer(RegexLexer):
    """
    Base lexer for Genshi markup, used by `HtmlGenshiLexer` and
    `GenshiLexer`.
    """
    flags: Incomplete
    tokens: Incomplete

class HtmlGenshiLexer(DelegatingLexer):
    """
    A lexer that highlights `genshi <http://genshi.edgewall.org/>`_ and
    `kid <http://kid-templating.org/>`_ kid HTML templates.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class GenshiLexer(DelegatingLexer):
    """
    A lexer that highlights `genshi <http://genshi.edgewall.org/>`_ and
    `kid <http://kid-templating.org/>`_ kid XML templates.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class JavascriptGenshiLexer(DelegatingLexer):
    """
    A lexer that highlights javascript code in genshi text templates.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class CssGenshiLexer(DelegatingLexer):
    """
    A lexer that highlights CSS definitions in genshi text templates.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class RhtmlLexer(DelegatingLexer):
    """
    Subclass of the ERB lexer that highlights the unlexed data with the
    html lexer.

    Nested Javascript and CSS is highlighted too.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class XmlErbLexer(DelegatingLexer):
    """
    Subclass of `ErbLexer` which highlights data outside preprocessor
    directives with the `XmlLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class CssErbLexer(DelegatingLexer):
    """
    Subclass of `ErbLexer` which highlights unlexed data with the `CssLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class JavascriptErbLexer(DelegatingLexer):
    """
    Subclass of `ErbLexer` which highlights unlexed data with the
    `JavascriptLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class HtmlPhpLexer(DelegatingLexer):
    """
    Subclass of `PhpLexer` that highlights unhandled data with the `HtmlLexer`.

    Nested Javascript and CSS is highlighted too.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class XmlPhpLexer(DelegatingLexer):
    """
    Subclass of `PhpLexer` that highlights unhandled data with the `XmlLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class CssPhpLexer(DelegatingLexer):
    """
    Subclass of `PhpLexer` which highlights unmatched data with the `CssLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class JavascriptPhpLexer(DelegatingLexer):
    """
    Subclass of `PhpLexer` which highlights unmatched data with the
    `JavascriptLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class HtmlSmartyLexer(DelegatingLexer):
    """
    Subclass of the `SmartyLexer` that highlights unlexed data with the
    `HtmlLexer`.

    Nested Javascript and CSS is highlighted too.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class XmlSmartyLexer(DelegatingLexer):
    """
    Subclass of the `SmartyLexer` that highlights unlexed data with the
    `XmlLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class CssSmartyLexer(DelegatingLexer):
    """
    Subclass of the `SmartyLexer` that highlights unlexed data with the
    `CssLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class JavascriptSmartyLexer(DelegatingLexer):
    """
    Subclass of the `SmartyLexer` that highlights unlexed data with the
    `JavascriptLexer`.
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class HtmlDjangoLexer(DelegatingLexer):
    """
    Subclass of the `DjangoLexer` that highlights unlexed data with the
    `HtmlLexer`.

    Nested Javascript and CSS is highlighted too.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class XmlDjangoLexer(DelegatingLexer):
    """
    Subclass of the `DjangoLexer` that highlights unlexed data with the
    `XmlLexer`.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class CssDjangoLexer(DelegatingLexer):
    """
    Subclass of the `DjangoLexer` that highlights unlexed data with the
    `CssLexer`.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class JavascriptDjangoLexer(DelegatingLexer):
    """
    Subclass of the `DjangoLexer` that highlights unlexed data with the
    `JavascriptLexer`.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class JspRootLexer(RegexLexer):
    """
    Base for the `JspLexer`. Yields `Token.Other` for area outside of
    JSP tags.

    .. versionadded:: 0.7
    """
    tokens: Incomplete

class JspLexer(DelegatingLexer):
    """
    Lexer for Java Server Pages.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class EvoqueLexer(RegexLexer):
    """
    For files using the Evoque templating system.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """Evoque templates use $evoque, which is unique."""

class EvoqueHtmlLexer(DelegatingLexer):
    """
    Subclass of the `EvoqueLexer` that highlights unlexed data with the
    `HtmlLexer`.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class EvoqueXmlLexer(DelegatingLexer):
    """
    Subclass of the `EvoqueLexer` that highlights unlexed data with the
    `XmlLexer`.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class ColdfusionLexer(RegexLexer):
    """
    Coldfusion statements
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class ColdfusionMarkupLexer(RegexLexer):
    """
    Coldfusion markup only
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ColdfusionHtmlLexer(DelegatingLexer):
    """
    Coldfusion markup in html
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class ColdfusionCFCLexer(DelegatingLexer):
    """
    Coldfusion markup/script components

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class SspLexer(DelegatingLexer):
    """
    Lexer for Scalate Server Pages.

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class TeaTemplateRootLexer(RegexLexer):
    """
    Base for the `TeaTemplateLexer`. Yields `Token.Other` for area outside of
    code blocks.

    .. versionadded:: 1.5
    """
    tokens: Incomplete

class TeaTemplateLexer(DelegatingLexer):
    """
    Lexer for `Tea Templates <http://teatrove.org/>`_.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class LassoHtmlLexer(DelegatingLexer):
    """
    Subclass of the `LassoLexer` which highlights unhandled data with the
    `HtmlLexer`.

    Nested JavaScript and CSS is also highlighted.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class LassoXmlLexer(DelegatingLexer):
    """
    Subclass of the `LassoLexer` which highlights unhandled data with the
    `XmlLexer`.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class LassoCssLexer(DelegatingLexer):
    """
    Subclass of the `LassoLexer` which highlights unhandled data with the
    `CssLexer`.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class LassoJavascriptLexer(DelegatingLexer):
    """
    Subclass of the `LassoLexer` which highlights unhandled data with the
    `JavascriptLexer`.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class HandlebarsLexer(RegexLexer):
    """
    Generic handlebars template lexer.

    Highlights only the Handlebars template tags (stuff between `{{` and `}}`).
    Everything else is left for a delegating lexer.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    tokens: Incomplete

class HandlebarsHtmlLexer(DelegatingLexer):
    """
    Subclass of the `HandlebarsLexer` that highlights unlexed data with the
    `HtmlLexer`.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class YamlJinjaLexer(DelegatingLexer):
    """
    Subclass of the `DjangoLexer` that highlights unlexed data with the
    `YamlLexer`.

    Commonly used in Saltstack salt states.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class LiquidLexer(RegexLexer):
    """
    Lexer for Liquid templates.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class TwigLexer(RegexLexer):
    """
    Twig template lexer.

    It just highlights Twig code between the preprocessor directives,
    other data is left untouched by the lexer.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class TwigHtmlLexer(DelegatingLexer):
    """
    Subclass of the `TwigLexer` that highlights unlexed data with the
    `HtmlLexer`.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class Angular2Lexer(RegexLexer):
    """
    Generic angular2 template lexer.

    Highlights only the Angular template tags (stuff between `{{` and `}}` and
    special attributes: '(event)=', '[property]=', '[(twoWayBinding)]=').
    Everything else is left for a delegating lexer.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    tokens: Incomplete

class Angular2HtmlLexer(DelegatingLexer):
    """
    Subclass of the `Angular2Lexer` that highlights unlexed data with the
    `HtmlLexer`.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...

class SqlJinjaLexer(DelegatingLexer):
    """
    Templated SQL lexer.

    .. versionadded:: 2.13
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...
