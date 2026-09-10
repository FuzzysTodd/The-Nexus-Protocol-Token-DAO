from databricks_cli.click_types import JobIdClickType as JobIdClickType, JsonClickType as JsonClickType, OutputClickType as OutputClickType
from databricks_cli.configure.config import api_version_option as api_version_option, debug_option as debug_option, get_config as get_config, get_profile_from_context as get_profile_from_context, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.configure.provider import DatabricksConfig as DatabricksConfig, ProfileConfigProvider as ProfileConfigProvider, update_and_persist_config as update_and_persist_config
from databricks_cli.jobs.api import JobsApi as JobsApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, eat_exceptions as eat_exceptions, json_cli_base as json_cli_base, pretty_format as pretty_format, truncate_string as truncate_string
from databricks_cli.version import print_version_callback as print_version_callback

def create_cli(api_client, json_file, json, version):
    """
    Creates a job.

    The specification for the json option can be found
    https://docs.databricks.com/api/latest/jobs.html#create
    """
def reset_cli(api_client, json_file, json, job_id, version) -> None:
    """
    Resets (edits) the definition of a job.

    The specification for the json option can be found
    https://docs.databricks.com/api/latest/jobs.html#jobsjobsettings
    """
def list_cli(api_client, output, job_type, version, expand_tasks, offset, limit, _all, name) -> None:
    '''
    Lists the jobs in the Databricks Job Service.

    By default the output format will be a human readable table with the following fields

      - Job ID

      - Job name

    A JSON formatted output can also be requested by setting the --output parameter to "JSON"

    In table mode, the jobs are sorted by their name.
    '''
def delete_cli(api_client, job_id, version) -> None:
    """
    Deletes the specified job.
    """
def get_cli(api_client, job_id, version) -> None:
    """
    Describes the metadata for a job.
    """
def run_now_cli(api_client, job_id, jar_params, notebook_params, python_params, python_named_params, spark_submit_params, idempotency_token, version) -> None:
    """
    Runs a job with optional per-run parameters.

    Parameter options are specified in json and the format is documented in
    https://docs.databricks.com/api/latest/jobs.html#jobsrunnow.
    """
def configure(version) -> None: ...
def jobs_group() -> None:
    """
    Utility to interact with jobs.

    This is a wrapper around the jobs API (https://docs.databricks.com/api/latest/jobs.html).
    Job runs are handled by ``databricks runs``.
    """
def check_version(api_client, version) -> None: ...
