from _typeshed import Incomplete
from mlflow.deployments.base import BaseDeploymentClient as BaseDeploymentClient
from mlflow.deployments.plugin_manager import DeploymentPlugins as DeploymentPlugins
from mlflow.deployments.utils import parse_target_uri as parse_target_uri

plugin_store: Incomplete

def get_deploy_client(target_uri):
    '''
    Returns a subclass of :py:class:`mlflow.deployments.BaseDeploymentClient` exposing standard
    APIs for deploying models to the specified target. See available deployment APIs
    by calling ``help()`` on the returned object or viewing docs for
    :py:class:`mlflow.deployments.BaseDeploymentClient`. You can also run
    ``mlflow deployments help -t <target-uri>`` via the CLI for more details on target-specific
    configuration options.

    :param target_uri: URI of target to deploy to.


    .. code-block:: python
        :caption: Example

        from mlflow.deployments import get_deploy_client
        import pandas as pd

        client = get_deploy_client("redisai")
        # Deploy the model stored at artifact path \'myModel\' under run with ID \'someRunId\'. The
        # model artifacts are fetched from the current tracking server and then used for deployment.
        client.create_deployment("spamDetector", "runs:/someRunId/myModel")
        # Load a CSV of emails and score it against our deployment
        emails_df = pd.read_csv("...")
        prediction_df = client.predict_deployment("spamDetector", emails_df)
        # List all deployments, get details of our particular deployment
        print(client.list_deployments())
        print(client.get_deployment("spamDetector"))
        # Update our deployment to serve a different model
        client.update_deployment("spamDetector", "runs:/anotherRunId/myModel")
        # Delete our deployment
        client.delete_deployment("spamDetector")
    '''
def run_local(target, name, model_uri, flavor: Incomplete | None = None, config: Incomplete | None = None):
    """
    Deploys the specified model locally, for testing. Note that models deployed locally cannot
    be managed by other deployment APIs (e.g. ``update_deployment``, ``delete_deployment``, etc).

    :param target: Target to deploy to.
    :param name:  Name to use for deployment
    :param model_uri: URI of model to deploy
    :param flavor: (optional) Model flavor to deploy. If unspecified, a default flavor
                   will be chosen.
    :param config: (optional) Dict containing updated target-specific configuration for
                   the deployment
    :return: None
    """
