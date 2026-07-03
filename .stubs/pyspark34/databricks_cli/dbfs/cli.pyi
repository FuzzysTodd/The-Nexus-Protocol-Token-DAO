from databricks_cli.configure.cli import configure_cli as configure_cli
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.dbfs.api import DbfsApi as DbfsApi
from databricks_cli.dbfs.dbfs_path import DbfsPath as DbfsPath, DbfsPathClickType as DbfsPathClickType
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, error_and_quit as error_and_quit
from databricks_cli.version import print_version_callback as print_version_callback, version as version

def ls_cli(api_client, l, absolute, dbfs_path) -> None:
    """
    List files in DBFS.
    """
def mkdirs_cli(api_client, dbfs_path) -> None:
    """
    Make directories in DBFS.

    Mkdirs will create directories along the path to the argument directory.
    """
def rm_cli(api_client, recursive, dbfs_path) -> None:
    """
    Remove files from dbfs.

    To remove a directory you must provide the --recursive flag.
    """
def cp_cli(api_client, recursive, overwrite, src, dst) -> None:
    """
    Copy files to and from DBFS.

    Note that this function will fail if the src and dst are both on the local filesystem.

    For non-recursive copies, if the dst is a directory, the file will be placed inside the
    directory. For example ``dbfs cp dbfs:/apple.txt .`` will create a file at `./apple.txt`.

    For recursive copies, files inside of the src directory will be copied inside the dst directory
    with the same name. If the dst path does not exist, a directory will be created. For example
    ``dbfs cp -r dbfs:/foo foo`` will create a directory foo and place the files ``dbfs:/foo/a`` at
    ``foo/a``. If ``foo/a`` already exists, the file will not be overridden unless the --overwrite
    flag is provided -- however, dbfs cp --recursive will continue to try and copy other files.
    """
def mv_cli(api_client, src, dst) -> None:
    """
    Moves a file between two DBFS paths.
    """
def dbfs_group() -> None:
    """
    Utility to interact with DBFS.

    DBFS paths are all prefixed with dbfs:/. Local paths can be absolute or local.
    """
def cat_cli(api_client, src) -> None:
    """
    Show the contents of a file. Does not work for directories.
    """
