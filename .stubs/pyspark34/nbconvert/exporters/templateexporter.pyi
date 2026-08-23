import typing as t
from .exporter import Exporter as Exporter
from _typeshed import Incomplete
from jinja2 import BaseLoader
from nbconvert import filters as filters
from nbformat import NotebookNode as NotebookNode

JINJA_EXTENSIONS: Incomplete
ROOT: Incomplete
DEV_MODE: Incomplete
default_filters: Incomplete

def recursive_update(target, new):
    """Recursively update one dictionary using another.
    None values will delete their keys.
    """
def deprecated(msg) -> None:
    """Emit a deprecation warning."""

class ExtensionTolerantLoader(BaseLoader):
    """A template loader which optionally adds a given extension when searching.

    Constructor takes two arguments: *loader* is another Jinja loader instance
    to wrap. *extension* is the extension, which will be added to the template
    name if finding the template without it fails. This should include the dot,
    e.g. '.tpl'.
    """
    loader: Incomplete
    extension: Incomplete
    def __init__(self, loader, extension) -> None:
        """Initialize the loader."""
    def get_source(self, environment, template):
        """Get the source for a template."""
    def list_templates(self):
        """List available templates."""

class TemplateExporter(Exporter):
    """
    Exports notebooks into other file formats.  Uses Jinja 2 templating engine
    to output new formats.  Inherit from this class if you are creating a new
    template type along with new filters/preprocessors.  If the filters/
    preprocessors provided by default suffice, there is no need to inherit from
    this class.  Instead, override the template_file and file_extension
    traits via a config file.

    Filters available by default for templates:

    {filters}
    """
    __doc__: Incomplete
    @property
    def template(self): ...
    @property
    def environment(self): ...
    @property
    def default_config(self): ...
    template_name: Incomplete
    template_file: Incomplete
    raw_template: Incomplete
    enable_async: Incomplete
    template_paths: Incomplete
    extra_template_basedirs: Incomplete
    extra_template_paths: Incomplete
    template_extension: Incomplete
    template_data_paths: Incomplete
    exclude_input: Incomplete
    exclude_input_prompt: Incomplete
    exclude_output: Incomplete
    exclude_output_prompt: Incomplete
    exclude_output_stdin: Incomplete
    exclude_code_cell: Incomplete
    exclude_markdown: Incomplete
    exclude_raw: Incomplete
    exclude_unknown: Incomplete
    extra_loaders: Incomplete
    filters: Incomplete
    raw_mimetypes: Incomplete
    def __init__(self, config: Incomplete | None = None, **kw) -> None:
        """
        Public constructor

        Parameters
        ----------
        config : config
            User configuration instance.
        extra_loaders : list[of Jinja Loaders]
            ordered list of Jinja loader to find templates. Will be tried in order
            before the default FileSystem ones.
        template_file : str (optional, kw arg)
            Template to use when exporting.
        """
    def from_filename(self, filename: str, resources: dict[str, t.Any] | None = None, **kw: t.Any) -> tuple[str, dict[str, t.Any]]:
        """Convert a notebook from a filename."""
    def from_file(self, file_stream: t.Any, resources: dict[str, t.Any] | None = None, **kw: t.Any) -> tuple[str, dict[str, t.Any]]:
        """Convert a notebook from a file."""
    def from_notebook_node(self, nb: NotebookNode, resources: dict[str, t.Any] | None = None, **kw: t.Any) -> tuple[str, dict[str, t.Any]]:
        """
        Convert a notebook from a notebook node instance.

        Parameters
        ----------
        nb : :class:`~nbformat.NotebookNode`
            Notebook node
        resources : dict
            Additional resources that can be accessed read/write by
            preprocessors and filters.
        """
    def register_filter(self, name, jinja_filter):
        """
        Register a filter.
        A filter is a function that accepts and acts on one string.
        The filters are accessible within the Jinja templating engine.

        Parameters
        ----------
        name : str
            name to give the filter in the Jinja engine
        filter : filter
        """
    def default_filters(self):
        """Override in subclasses to provide extra filters.

        This should return an iterable of 2-tuples: (name, class-or-function).
        You should call the method on the parent class and include the filters
        it provides.

        If a name is repeated, the last filter provided wins. Filters from
        user-supplied config win over filters provided by classes.
        """
    @classmethod
    def get_compatibility_base_template_conf(cls, name):
        """Get the base template config."""
    def get_template_names(self):
        """Finds a list of template names where each successive template name is the base template"""
    def get_prefix_root_dirs(self):
        """Get the prefix root dirs."""
