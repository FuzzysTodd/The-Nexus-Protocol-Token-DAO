from .latex import LatexExporter as LatexExporter
from _typeshed import Incomplete

class LatexFailed(IOError):
    """Exception for failed latex run

    Captured latex output is in error.output.
    """
    output: Incomplete
    def __init__(self, output) -> None:
        """Initialize the error."""
    def __unicode__(self):
        """Unicode representation."""

def prepend_to_env_search_path(varname, value, envdict) -> None:
    """Add value to the environment variable varname in envdict

    e.g. prepend_to_env_search_path('BIBINPUTS', '/home/sally/foo', os.environ)
    """

class PDFExporter(LatexExporter):
    """Writer designed to write to PDF files.

    This inherits from `LatexExporter`. It creates a LaTeX file in
    a temporary directory using the template machinery, and then runs LaTeX
    to create a pdf.
    """
    export_from_notebook: str
    latex_count: Incomplete
    latex_command: Incomplete
    bib_command: Incomplete
    verbose: Incomplete
    texinputs: Incomplete
    writer: Incomplete
    output_mimetype: str
    def run_command(self, command_list, filename, count, log_function, raise_on_failure: Incomplete | None = None):
        """Run command_list count times.

        Parameters
        ----------
        command_list : list
            A list of args to provide to Popen. Each element of this
            list will be interpolated with the filename to convert.
        filename : unicode
            The name of the file to convert.
        count : int
            How many times to run the command.
        raise_on_failure: Exception class (default None)
            If provided, will raise the given exception for if an instead of
            returning False on command failure.

        Returns
        -------
        success : bool
            A boolean indicating if the command was successful (True)
            or failed (False).
        """
    def run_latex(self, filename, raise_on_failure=...):
        """Run xelatex self.latex_count times."""
    def run_bib(self, filename, raise_on_failure: bool = False):
        """Run bibtex one time."""
    def from_notebook_node(self, nb, resources: Incomplete | None = None, **kw):
        """Convert from notebook node."""
