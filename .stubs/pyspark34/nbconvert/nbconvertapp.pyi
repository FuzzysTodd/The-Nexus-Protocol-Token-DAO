from .exporters.base import get_export_names as get_export_names, get_exporter as get_exporter
from .filters.markdown_mistune import InvalidNotebook as InvalidNotebook
from .utils.base import NbConvertBase as NbConvertBase
from .utils.exceptions import ConversionException as ConversionException
from .utils.io import unicode_stdin_stream as unicode_stdin_stream
from _typeshed import Incomplete
from jupyter_core.application import JupyterApp
from nbconvert import __version__ as __version__, exporters as exporters, postprocessors as postprocessors, preprocessors as preprocessors, writers as writers
from nbconvert.utils.text import indent as indent
from traitlets import DottedObjectName

class DottedOrNone(DottedObjectName):
    """A string holding a valid dotted object name in Python, such as A.b3._c
    Also allows for None type.
    """
    default_value: str
    def validate(self, obj, value):
        """Validate an input."""

nbconvert_aliases: Incomplete
nbconvert_flags: Incomplete

class NbConvertApp(JupyterApp):
    """Application used to convert from notebook file type (``*.ipynb``)"""
    version = __version__
    name: str
    aliases = nbconvert_aliases
    flags = nbconvert_flags
    classes: Incomplete
    description: Incomplete
    output_base: Incomplete
    use_output_suffix: Incomplete
    output_files_dir: Incomplete
    examples: Incomplete
    writer: Incomplete
    writer_class: Incomplete
    writer_aliases: Incomplete
    writer_factory: Incomplete
    postprocessor: Incomplete
    postprocessor_class: Incomplete
    postprocessor_aliases: Incomplete
    postprocessor_factory: Incomplete
    export_format: Incomplete
    notebooks: Incomplete
    from_stdin: Incomplete
    recursive_glob: Incomplete
    def initialize(self, argv: Incomplete | None = None) -> None:
        """Initialize application, notebooks, writer, and postprocessor"""
    def init_syspath(self) -> None:
        """Add the cwd to the sys.path ($PYTHONPATH)"""
    def init_notebooks(self) -> None:
        """Construct the list of notebooks.

        If notebooks are passed on the command-line,
        they override (rather than add) notebooks specified in config files.
        Glob each notebook to replace notebook patterns with filenames.
        """
    def init_writer(self) -> None:
        """Initialize the writer (which is stateless)"""
    def init_postprocessor(self) -> None:
        """Initialize the postprocessor (which is stateless)"""
    def start(self) -> None:
        """Run start after initialization process has completed"""
    def init_single_notebook_resources(self, notebook_filename):
        """Step 1: Initialize resources

        This initializes the resources dictionary for a single notebook.

        Returns
        -------
        dict
            resources dictionary for a single notebook that MUST include the following keys:
                - config_dir: the location of the Jupyter config directory
                - unique_key: the notebook name
                - output_files_dir: a directory where output files (not
                  including the notebook itself) should be saved
        """
    def export_single_notebook(self, notebook_filename, resources, input_buffer: Incomplete | None = None):
        """Step 2: Export the notebook

        Exports the notebook to a particular format according to the specified
        exporter. This function returns the output and (possibly modified)
        resources from the exporter.

        Parameters
        ----------
        notebook_filename : str
            name of notebook file.
        resources : dict
        input_buffer :
            readable file-like object returning unicode.
            if not None, notebook_filename is ignored

        Returns
        -------
        output
        dict
            resources (possibly modified)
        """
    def write_single_notebook(self, output, resources):
        """Step 3: Write the notebook to file

        This writes output from the exporter to file using the specified writer.
        It returns the results from the writer.

        Parameters
        ----------
        output :
        resources : dict
            resources for a single notebook including name, config directory
            and directory to save output

        Returns
        -------
        file
            results from the specified writer output of exporter
        """
    def postprocess_single_notebook(self, write_results) -> None:
        """Step 4: Post-process the written file

        Only used if a postprocessor has been specified. After the
        converted notebook is written to a file in Step 3, this post-processes
        the notebook.
        """
    def convert_single_notebook(self, notebook_filename, input_buffer: Incomplete | None = None) -> None:
        """Convert a single notebook.

        Performs the following steps:

            1. Initialize notebook resources
            2. Export the notebook to a particular format
            3. Write the exported notebook to file
            4. (Maybe) postprocess the written file

        Parameters
        ----------
        notebook_filename : str
        input_buffer :
            If input_buffer is not None, conversion is done and the buffer is
            used as source into a file basenamed by the notebook_filename
            argument.
        """
    exporter: Incomplete
    def convert_notebooks(self) -> None:
        """Convert the notebooks in the self.notebooks traitlet"""
    def document_flag_help(self):
        """
        Return a string containing descriptions of all the flags.
        """
    def document_alias_help(self):
        """Return a string containing all of the aliases"""
    def document_config_options(self):
        """
        Provides a much improves version of the configuration documentation by
        breaking the configuration options into app, exporter, writer,
        preprocessor, postprocessor, and other sections.
        """

class DejavuApp(NbConvertApp):
    """A deja vu app."""
    def initialize(self, argv: Incomplete | None = None) -> None:
        """Initialize the app."""

main: Incomplete

launch_new_instance: Incomplete
dejavu_main: Incomplete
