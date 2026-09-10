import collections
import typing as t
from _typeshed import Incomplete
from nbformat import NotebookNode as NotebookNode
from traitlets import Unicode
from traitlets.config.configurable import LoggingConfigurable

class ResourcesDict(collections.defaultdict):
    """A default dict for resources."""
    def __missing__(self, key):
        """Handle missing value."""

class FilenameExtension(Unicode):
    """A trait for filename extensions."""
    default_value: str
    info_text: str
    def validate(self, obj, value):
        """Validate the file name."""

class Exporter(LoggingConfigurable):
    """
    Class containing methods that sequentially run a list of preprocessors on a
    NotebookNode object and then return the modified NotebookNode object and
    accompanying resources dict.
    """
    enabled: Incomplete
    file_extension: Incomplete
    optimistic_validation: Incomplete
    output_mimetype: str
    export_from_notebook: str
    preprocessors: Incomplete
    default_preprocessors: Incomplete
    def __init__(self, config: Incomplete | None = None, **kw) -> None:
        """
        Public constructor

        Parameters
        ----------
        config : ``traitlets.config.Config``
            User configuration instance.
        `**kw`
            Additional keyword arguments passed to parent __init__

        """
    @property
    def default_config(self): ...
    def from_notebook_node(self, nb: NotebookNode, resources: t.Any | None = None, **kw: t.Any) -> tuple[NotebookNode, dict[str, t.Any]]:
        """
        Convert a notebook from a notebook node instance.

        Parameters
        ----------
        nb : :class:`~nbformat.NotebookNode`
            Notebook node (dict-like with attr-access)
        resources : dict
            Additional resources that can be accessed read/write by
            preprocessors and filters.
        `**kw`
            Ignored

        """
    def from_filename(self, filename: str, resources: dict[str, t.Any] | None = None, **kw: t.Any) -> tuple[NotebookNode, dict[str, t.Any]]:
        """
        Convert a notebook from a notebook file.

        Parameters
        ----------
        filename : str
            Full filename of the notebook file to open and convert.
        resources : dict
            Additional resources that can be accessed read/write by
            preprocessors and filters.
        `**kw`
            Ignored

        """
    def from_file(self, file_stream: t.Any, resources: dict[str, t.Any] | None = None, **kw: t.Any) -> tuple[NotebookNode, dict[str, t.Any]]:
        """
        Convert a notebook from a notebook file.

        Parameters
        ----------
        file_stream : file-like object
            Notebook file-like object to convert.
        resources : dict
            Additional resources that can be accessed read/write by
            preprocessors and filters.
        `**kw`
            Ignored

        """
    def register_preprocessor(self, preprocessor, enabled: bool = False):
        """
        Register a preprocessor.
        Preprocessors are classes that act upon the notebook before it is
        passed into the Jinja templating engine. Preprocessors are also
        capable of passing additional information to the Jinja
        templating engine.

        Parameters
        ----------
        preprocessor : `nbconvert.preprocessors.Preprocessor`
            A dotted module name, a type, or an instance
        enabled : bool
            Mark the preprocessor as enabled

        """
