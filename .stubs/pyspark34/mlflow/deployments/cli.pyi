from _typeshed import Incomplete
from mlflow.deployments import interface as interface
from mlflow.utils import cli_args as cli_args
from mlflow.utils.proto_json_utils import NumpyEncoder as NumpyEncoder

installed_targets: Incomplete
supported_targets_msg: Incomplete
target_details: Incomplete
deployment_name: Incomplete
optional_deployment_name: Incomplete
parse_custom_arguments: Incomplete
parse_input: Incomplete
parse_output: Incomplete
required_endpoint_param: Incomplete
optional_endpoint_param: Incomplete

def commands() -> None:
    """
    Deploy MLflow models to custom targets. Support is currently installed for
    the following targets: {targets}. Run `mlflow deployments help --target-name <target-name>` for
    more details on the supported URI format and config options for a given target.

    To deploy to other targets, you must first install an
    appropriate third-party Python plugin. See the list of known community-maintained plugins
    at https://mlflow.org/docs/latest/plugins.html#community-plugins.

    You can also write your own plugin for deployment to a custom target. For instructions on
    writing and distributing a plugin, see
    https://mlflow.org/docs/latest/plugins.html#writing-your-own-mlflow-plugins.
    """
def create_deployment(flavor, model_uri, target, name, config, endpoint) -> None:
    """
    Deploy the model at ``model_uri`` to the specified target.

    Additional plugin-specific arguments may also be passed to this command, via `-C key=value`
    """
def update_deployment(flavor, model_uri, target, name, config, endpoint) -> None:
    """
    Update the deployment with ID `deployment_id` in the specified target.
    You can update the URI of the model and/or the flavor of the deployed model (in which case the
    model URI must also be specified).

    Additional plugin-specific arguments may also be passed to this command, via `-C key=value`.
    """
def delete_deployment(target, name, config, endpoint) -> None:
    """
    Delete the deployment with name given at `--name` from the specified target.
    """
def list_deployment(target, endpoint) -> None:
    """
    List the names of all model deployments in the specified target. These names can be used with
    the `delete`, `update`, and `get` commands.
    """
def get_deployment(target, name, endpoint) -> None:
    """
    Print a detailed description of the deployment with name given at ``--name`` in the specified
    target.
    """
def target_help(target) -> None:
    """
    Display additional help for a specific deployment target, e.g. info on target-specific config
    options and the target's URI format.
    """
def run_local(flavor, model_uri, target, name, config) -> None:
    """
    Deploy the model locally. This has very similar signature to ``create`` API
    """
def predictions_to_json(raw_predictions, output) -> None: ...
def predict(target, name, input_path, output_path, endpoint) -> None:
    """
    Predict the results for the deployed model for the given input(s)
    """
def explain(target, name, input_path, output_path, endpoint) -> None:
    """
    Generate explanations of model predictions on the specified input for
    the deployed model for the given input(s). Explanation output formats vary
    by deployment target, and can include details like feature importance for
    understanding/debugging predictions. Run `mlflow deployments help` or
    consult the documentation for your plugin for details on explanation format.
    For information about the input data formats accepted by this function,
    see the following documentation:
    https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools
    """
def create_endpoint(target, name, config) -> None:
    """
    Create an endpoint with the specified name at the specified target.

    Additional plugin-specific arguments may also be passed to this command, via `-C key=value`
    """
def update_endpoint(target, endpoint, config) -> None:
    """
    Update the specified endpoint at the specified target.

    Additional plugin-specific arguments may also be passed to this command, via `-C key=value`
    """
def delete_endpoint(target, endpoint) -> None:
    """
    Delete the specified endpoint at the specified target
    """
def list_endpoints(target) -> None:
    """
    List all endpoints at the specified target
    """
def get_endpoint(target, endpoint) -> None:
    """
    Get details for the specified endpoint at the specified target
    """
