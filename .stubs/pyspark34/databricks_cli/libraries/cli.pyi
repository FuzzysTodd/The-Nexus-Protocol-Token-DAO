from _typeshed import Incomplete
from databricks_cli.click_types import ClusterIdClickType as ClusterIdClickType, OneOfOption as OneOfOption, OptionalOneOfOption as OptionalOneOfOption
from databricks_cli.clusters.api import ClusterApi as ClusterApi
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.libraries.api import LibrariesApi as LibrariesApi
from databricks_cli.utils import CLUSTER_OPTIONS as CLUSTER_OPTIONS, CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, pretty_format as pretty_format
from databricks_cli.version import print_version_callback as print_version_callback, version as version

def all_cluster_statuses_cli(api_client) -> None:
    """
    Get the status of all libraries on all clusters. A status will be available for all libraries
    installed on this cluster via the API or the libraries UI as well as libraries set to be
    installed on all clusters via the libraries UI. If a library has been set to be installed on
    all clusters, is_library_for_all_clusters will be true.
    """
def cluster_status_cli(api_client, cluster_id, cluster_name) -> None:
    """
    Get the status of all libraries for a specified cluster. A status will be available for all
    libraries installed on this cluster via the API or the libraries UI as well as libraries set to
    be installed on all clusters via the libraries UI. If a library has been set to be installed on
    all clusters, is_library_for_all_clusters will be true.
    """
def list_cli(api_client, cluster_id, cluster_name) -> None:
    """
    Get the statuses of all libraries for all clusters or for a specified cluster.
    If the option --cluster-id is provided, then all libraries on that cluster will be listed,
    (cluster-status). If the option --cluster-id is omitted, then all libraries on all clusters
    will be listed (all-cluster-statuses).
    """

INSTALL_OPTIONS: Incomplete
UNINSTALL_OPTIONS: Incomplete
JAR_HELP: str
EGG_HELP: str
WHEEL_HELP: str
MAVEN_COORDINATES_HELP: str
MAVEN_REPO_HELP: str
MAVEN_EXCLUSION_HELP: str
PYPI_PACKAGE_HELP: str
PYPI_REPO_HELP: str
CRAN_PACKAGE_HELP: str
CRAN_REPO_HELP: str

def install_cli(api_client, cluster_id, jar, egg, whl, maven_coordinates, maven_repo, maven_exclusion, pypi_package, pypi_repo, cran_package, cran_repo) -> None:
    """
    Install a library on a cluster. Libraries must be first uploaded to dbfs or s3
    (see `dbfs cp -h`). Unlike the API, only one library can be installed for each execution of
    `databricks libraries install`.

    Users should only provide one of
    [--jar, --egg, --whl, --maven-coordinates, --pypi-package, --cran-package].

    Installing a whl library on clusters running Databricks Runtime 4.2 or higher effectively runs
    the pip command against the wheel file directly on driver and executors.The library must satisfy
    the wheel file name convention.
    To install multiple wheel files, use the .wheelhouse.zip file that includes all the wheel files
    with the --whl option.

    Installing a wheel library on clusters running Databricks Runtime lower than 4.2 just adds the
    file to the PYTHONPATH variable, without installing the dependencies.
    More information is available here:
    https://docs.databricks.com/api/latest/libraries.html#managedlibrariesmanagedlibraryserviceinstalllibraries
    """
def uninstall_cli(api_client, cluster_id, all, jar, egg, whl, maven_coordinates, maven_repo, maven_exclusion, pypi_package, pypi_repo, cran_package, cran_repo) -> None:
    """
    Mark libraries on a cluster to be uninstalled. Libraries which are marked to be uninstalled
    will stay attached until the cluster is restarted. (see `databricks clusters restart -h`).
    """
def libraries_group() -> None:
    """
    Utility to interact with libraries.

    This is a wrapper around the libraries API
    (https://docs.databricks.com/api/latest/libraries.html).
    """
