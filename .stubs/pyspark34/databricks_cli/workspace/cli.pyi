from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions
from databricks_cli.version import print_version_callback as print_version_callback, version as version
from databricks_cli.workspace.api import WorkspaceApi as WorkspaceApi
from databricks_cli.workspace.types import FormatClickType as FormatClickType, LanguageClickType as LanguageClickType, WorkspaceFormat as WorkspaceFormat, WorkspaceLanguage as WorkspaceLanguage

def ls_cli(api_client, is_long_form, with_object_id, absolute, workspace_path) -> None:
    """
    List objects in the Databricks Workspace.
    """
def mkdirs_cli(api_client, workspace_path) -> None:
    """
    Make directories in the Databricks Workspace.

    Mkdirs will create directories along the path to the argument directory.
    """
def import_workspace_cli(api_client, source_path, target_path, language, format, overwrite) -> None:
    """
    Imports a file from local to the Databricks workspace.

    The format is by default SOURCE. Possible formats are SOURCE, HTML, JUPYTER, and DBC. Each
    format is documented at
    https://docs.databricks.com/api/latest/workspace.html#notebookexportformat.
    """
def export_workspace_cli(api_client, source_path, target_path, format, overwrite) -> None:
    """
    Exports a notebook from the Databricks workspace.

    The format is by default SOURCE. Possible formats are SOURCE, HTML, JUPYTER, and DBC. Each
    format is documented at
    https://docs.databricks.com/api/latest/workspace.html#notebookexportformat.
    """
def delete_cli(api_client, workspace_path, recursive) -> None:
    """
    Deletes objects from the Databricks workspace.

    To delete a folder add the recursive flag.
    """
def export_dir_cli(api_client, source_path, target_path, overwrite) -> None:
    """
    Recursively exports a directory from the Databricks workspace.

    Only directories and notebooks are exported. Notebooks are always exported in the SOURCE
    format. Notebooks will also have the extension of .scala, .py, .sql, or .r appended
    depending on the language type.
    """
def import_dir_cli(api_client, source_path, target_path, overwrite, exclude_hidden_files) -> None:
    """
    Recursively imports a directory from local to the Databricks workspace.

    Only directories and files with the extensions .scala, .py, .sql, .r, .R, .ipynb are imported.
    When imported, these extensions will be stripped off the name of the notebook.
    """
def workspace_group() -> None:
    """
    Utility to interact with the Databricks workspace.
    Workspace paths must be absolute and be prefixed with `/`.
    """
