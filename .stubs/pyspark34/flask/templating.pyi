import typing as t
from .app import Flask as Flask
from .globals import current_app as current_app, request as request
from .helpers import stream_with_context as stream_with_context
from .sansio.app import App as App
from .sansio.scaffold import Scaffold as Scaffold
from .signals import before_render_template as before_render_template, template_rendered as template_rendered
from _typeshed import Incomplete
from jinja2 import BaseLoader, Environment as BaseEnvironment, Template as Template

class Environment(BaseEnvironment):
    """Works like a regular Jinja2 environment but has some additional
    knowledge of how Flask's blueprint works so that it can prepend the
    name of the blueprint to referenced templates if necessary.
    """
    app: Incomplete
    def __init__(self, app: App, **options: t.Any) -> None: ...

class DispatchingJinjaLoader(BaseLoader):
    """A loader that looks for templates in the application and all
    the blueprint folders.
    """
    app: Incomplete
    def __init__(self, app: App) -> None: ...
    def get_source(self, environment: Environment, template: str) -> tuple[str, str | None, t.Callable | None]: ...
    def list_templates(self) -> list[str]: ...

def render_template(template_name_or_list: str | Template | list[str | Template], **context: t.Any) -> str:
    """Render a template by name with the given context.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.
    """
def render_template_string(source: str, **context: t.Any) -> str:
    """Render a template from the given source string with the given
    context.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.
    """
def stream_template(template_name_or_list: str | Template | list[str | Template], **context: t.Any) -> t.Iterator[str]:
    """Render a template by name with the given context as a stream.
    This returns an iterator of strings, which can be used as a
    streaming response from a view.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.

    .. versionadded:: 2.2
    """
def stream_template_string(source: str, **context: t.Any) -> t.Iterator[str]:
    """Render a template from the given source string with the given
    context as a stream. This returns an iterator of strings, which can
    be used as a streaming response from a view.

    :param source: The source code of the template to render.
    :param context: The variables to make available in the template.

    .. versionadded:: 2.2
    """
