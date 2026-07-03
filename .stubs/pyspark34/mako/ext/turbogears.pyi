from _typeshed import Incomplete
from mako import compat as compat
from mako.lookup import TemplateLookup as TemplateLookup
from mako.template import Template as Template

class TGPlugin:
    """TurboGears compatible Template Plugin."""
    extra_vars_func: Incomplete
    extension: Incomplete
    lookup: Incomplete
    tmpl_options: Incomplete
    def __init__(self, extra_vars_func: Incomplete | None = None, options: Incomplete | None = None, extension: str = 'mak') -> None: ...
    def load_template(self, templatename, template_string: Incomplete | None = None):
        """Loads a template from a file or a string"""
    def render(self, info, format: str = 'html', fragment: bool = False, template: Incomplete | None = None): ...
