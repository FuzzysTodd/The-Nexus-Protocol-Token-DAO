from .exporter import Exporter as Exporter

__all__ = ['export', 'Exporter', 'get_exporter', 'get_export_names', 'ExporterNameError']

class ExporterNameError(NameError):
    """An exporter name error."""
class ExporterDisabledError(ValueError):
    """An exporter disabled error."""

def export(exporter, nb, **kw):
    """
    Export a notebook object using specific exporter class.

    Parameters
    ----------
    exporter : ``Exporter`` class or instance
        Class or instance of the exporter that should be used.  If the
        method initializes its own instance of the class, it is ASSUMED that
        the class type provided exposes a constructor (``__init__``) with the same
        signature as the base Exporter class.
    nb : :class:`~nbformat.NotebookNode`
        The notebook to export.
    config : config (optional, keyword arg)
        User configuration instance.
    resources : dict (optional, keyword arg)
        Resources used in the conversion process.

    Returns
    -------
    tuple
        output : str
            The resulting converted notebook.
        resources : dictionary
            Dictionary of resources used prior to and during the conversion
            process.
    """
def get_exporter(name, config=...):
    """Given an exporter name or import path, return a class ready to be instantiated

    Raises ExporterName if exporter is not found or ExporterDisabledError if not enabled
    """
def get_export_names(config=...):
    """Return a list of the currently supported export targets

    Exporters can be found in external packages by registering
    them as an nbconvert.exporter entrypoint.
    """
