import typing as t
from .runtime import Undefined as Undefined
from _typeshed import Incomplete

class TemplateError(Exception):
    """Baseclass for all template errors."""
    def __init__(self, message: str | None = None) -> None: ...
    @property
    def message(self) -> str | None: ...

class TemplateNotFound(IOError, LookupError, TemplateError):
    """Raised if a template does not exist.

    .. versionchanged:: 2.11
        If the given name is :class:`Undefined` and no message was
        provided, an :exc:`UndefinedError` is raised.
    """
    message: str | None
    name: Incomplete
    templates: Incomplete
    def __init__(self, name: str | Undefined | None, message: str | None = None) -> None: ...

class TemplatesNotFound(TemplateNotFound):
    """Like :class:`TemplateNotFound` but raised if multiple templates
    are selected.  This is a subclass of :class:`TemplateNotFound`
    exception, so just catching the base exception will catch both.

    .. versionchanged:: 2.11
        If a name in the list of names is :class:`Undefined`, a message
        about it being undefined is shown rather than the empty string.

    .. versionadded:: 2.2
    """
    templates: Incomplete
    def __init__(self, names: t.Sequence[str | Undefined] = (), message: str | None = None) -> None: ...

class TemplateSyntaxError(TemplateError):
    """Raised to tell the user that there is a problem with the template."""
    lineno: Incomplete
    name: Incomplete
    filename: Incomplete
    source: Incomplete
    translated: bool
    def __init__(self, message: str, lineno: int, name: str | None = None, filename: str | None = None) -> None: ...
    def __reduce__(self): ...

class TemplateAssertionError(TemplateSyntaxError):
    """Like a template syntax error, but covers cases where something in the
    template caused an error at compile time that wasn't necessarily caused
    by a syntax error.  However it's a direct subclass of
    :exc:`TemplateSyntaxError` and has the same attributes.
    """
class TemplateRuntimeError(TemplateError):
    """A generic runtime error in the template engine.  Under some situations
    Jinja may raise this exception.
    """
class UndefinedError(TemplateRuntimeError):
    """Raised if a template tries to operate on :class:`Undefined`."""
class SecurityError(TemplateRuntimeError):
    """Raised if a template tries to do something insecure if the
    sandbox is enabled.
    """
class FilterArgumentError(TemplateRuntimeError):
    """This error is raised if a filter was called with inappropriate
    arguments
    """
