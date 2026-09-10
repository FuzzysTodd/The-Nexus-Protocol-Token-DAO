from _typeshed import Incomplete
from traitlets import Undefined as Undefined
from traitlets.utils.text import indent as indent

def setup(app):
    """Registers the Sphinx extension.

    You shouldn't need to call this directly; configure Sphinx to use this
    module instead.
    """
def interesting_default_value(dv): ...
def format_aliases(aliases): ...
def class_config_rst_doc(cls, trait_aliases):
    """Generate rST documentation for this class' config options.

    Excludes traits defined on parent classes.
    """
def reverse_aliases(app):
    """Produce a mapping of trait names to lists of command line aliases."""
def write_doc(path, title, app, preamble: Incomplete | None = None) -> None:
    """Write a rst file documenting config options for a traitlets application.

    Parameters
    ----------
    path : str
        The file to be written
    title : str
        The human-readable title of the document
    app : traitlets.config.Application
        An instance of the application class to be documented
    preamble : str
        Extra text to add just after the title (optional)
    """
