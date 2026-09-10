import json
from databricks_cli.click_types import PipelineIdClickType as PipelineIdClickType, PipelineSettingClickType as PipelineSettingClickType, PipelineSpecClickType as PipelineSpecClickType
from databricks_cli.configure.config import debug_option as debug_option, profile_option as profile_option, provide_api_client as provide_api_client
from databricks_cli.pipelines.api import PipelinesApi as PipelinesApi
from databricks_cli.utils import CONTEXT_SETTINGS as CONTEXT_SETTINGS, error_and_quit as error_and_quit, pipelines_exception_eater as pipelines_exception_eater, pretty_format as pretty_format
from databricks_cli.version import print_version_callback as print_version_callback, version as version

json_parse_exception = json.decoder.JSONDecodeError
json_parse_exception = ValueError

def create_cli(api_client, settings_arg, settings, allow_duplicate_names) -> None:
    '''
    Creates a pipeline specified by the pipeline settings. The pipeline settings are a
    JSON document that defines a Delta Live Tables pipeline on Databricks.

    To use a file containing the pipeline settings, pass the file path to the command as
    an argument or with the --settings option. If the pipeline creation is successful, logs
    the URL and the ID of the new pipeline to STDOUT.

    Specification for the pipeline settings JSON can be found at
    https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-configuration.html

    If a pipeline with the same name already exists, the pipeline will not be created.
    This check can be disabled by adding the --allow-duplicate-names option.

    If the pipeline settings contain an "id" field, this command will fail.

    Usage:

    databricks pipelines create example.json

    OR

    databricks pipelines create --settings example.json
    '''
def edit_cli(api_client, settings_arg, settings, pipeline_id, allow_duplicate_names) -> None:
    """
    Edits a pipeline specified by the pipeline settings. The pipeline settings are a
    JSON document that defines a Delta Live Tables pipeline on Databricks. To use a
    file containing the pipeline settings, pass the file path to the command as an
    argument or with the --settings option.

    Specification for the pipeline settings JSON can be found at
    https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-configuration.html

    If another pipeline with the same name exists, pipeline settings will not be edited.
    This check can be disabled by adding the --allow-duplicate-names option.

    Note that if an ID is specified in both the settings and passed with the --pipeline-id argument,
    the two ids must be the same, or the command will fail.

    Usage:

    databricks pipelines edit example.json

    OR

    databricks pipelines edit --settings example.json
    """
def deploy_cli(api_client, settings_arg, settings, spec, allow_duplicate_names, pipeline_id) -> None:
    '''
    [Deprecated] This command is deprecated, use create and edit commands instead.

    Creates or edits a pipeline specified by the pipeline settings. The pipeline settings
    are a JSON document that defines a Delta Live Tables pipeline on Databricks. To use a
    file containing the pipeline settings, pass the file path to the command as an
    argument or with the --settings option.

    Specification for the pipeline settings JSON can be found at
    https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-configuration.html

    If the pipeline settings contains an "id" field, or if a pipeline ID is specified directly
    (using the  --pipeline-id argument), attempts to update an existing pipeline
    with that ID. If it does not, creates a new pipeline and logs the URL and the ID of the
    new pipeline to STDOUT. Note that if an ID is specified in both the settings and passed
    with the --pipeline-id argument, the two IDs must be the same, or the command will fail.

    The deploy command will not create a new pipeline if a pipeline with the same name already
    exists. This check can be disabled by adding the --allow-duplicate-names option.

    Usage:

    databricks pipelines deploy example.json

    OR

    databricks pipelines deploy --settings example.json

    OR

    databricks pipelines deploy --pipeline-id 1234 --settings example.json
    '''
def delete_cli(api_client, pipeline_id) -> None:
    """
    Deletes the pipeline and cancels any active updates.

    Usage:

    databricks pipelines delete --pipeline-id 1234
    """
def get_cli(api_client, pipeline_id) -> None:
    """
    Gets a pipeline's current settings and status.

    Usage:

    databricks pipelines get --pipeline-id 1234
    """
def list_cli(api_client) -> None:
    """
    Lists all pipelines and their statuses.

    Usage:

    databricks pipelines list
    """
def reset_cli(api_client, pipeline_id) -> None:
    '''
    [Deprecated] Use the "start --full-refresh" command instead.

    Resets a pipeline by truncating tables and creating new checkpoint folders so that data is
    reprocessed from the beginning.

    Usage:

    databricks pipelines reset --pipeline-id 1234
    '''
def run_cli(api_client, pipeline_id) -> None:
    '''
    [Deprecated] Use the "start" command instead.

    Starts a pipeline update.

    Usage:

    databricks pipelines run --pipeline-id 1234
    '''
def start_cli(api_client, pipeline_id, full_refresh) -> None:
    """
    Starts a pipeline update.

    Usage:

    databricks pipelines start --pipeline-id 1234 --full-refresh
    """
def stop_cli(api_client, pipeline_id) -> None:
    """
    Stops the pipeline by cancelling any active update.

    Usage:

    databricks pipelines stop --pipeline-id 1234
    """
def pipelines_group() -> None:
    """
    Utility to interact with Databricks Delta Live Tables Pipelines.
    """
