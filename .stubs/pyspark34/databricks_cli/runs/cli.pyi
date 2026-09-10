from databricks_cli.click_types import JsonClickType as JsonClickType, OutputClickType as OutputClickType, RunIdClickType as RunIdClickType
from databricks_cli.configure.config import api_version_option as api_version_option, debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.jobs.cli import check_version as check_version
from databricks_cli.runs.api import RunsApi as RunsApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, backoff_with_jitter as backoff_with_jitter, eat_exceptions as eat_exceptions, error_and_quit as error_and_quit, pretty_format as pretty_format, truncate_string as truncate_string
from databricks_cli.version import print_version_callback as print_version_callback

def submit_cli(api_client, json_file, json, wait, version) -> None:
    """
    Submits a one-time run and optionally waits for its completion.

    The specification for the request json can be found
    https://docs.databricks.com/api/latest/jobs.html#runs-submit
    """
def list_cli(api_client, job_id, active_only, completed_only, offset, limit, output, version) -> None:
    """
    Lists job runs.

    The limit and offset determine which runs will be listed. Runs are always listed
    by descending order of run start time and run ID.

    In the TABLE output mode, the columns are as follows.

      - Run ID

      - Run name

      - Life cycle state

      - Result state (can be n/a)
    """
def get_cli(api_client, run_id, version) -> None:
    """
    Gets the metadata about a run in json form.

    The output schema is documented https://docs.databricks.com/api/latest/jobs.html#runs-get.
    """
def get_output_cli(api_client, run_id, version) -> None:
    """
    Gets the output of a run

    The output schema is documented https://docs.databricks.com/api/latest/jobs.html#runs-get-output
    """
def cancel_cli(api_client, run_id, version) -> None:
    """
    Cancels the run specified.
    """
def runs_group() -> None:
    """
    Utility to interact with jobs runs.
    """
