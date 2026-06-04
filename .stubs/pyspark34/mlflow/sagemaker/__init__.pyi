from _typeshed import Incomplete
from mlflow import mleap as mleap, pyfunc as pyfunc
from mlflow.deployments import BaseDeploymentClient as BaseDeploymentClient, PredictionsResponse as PredictionsResponse
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model
from mlflow.models.container import DEPLOYMENT_CONFIG_KEY_FLAVOR_NAME as DEPLOYMENT_CONFIG_KEY_FLAVOR_NAME, SERVING_ENVIRONMENT as SERVING_ENVIRONMENT
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.utils import get_unique_resource_id as get_unique_resource_id
from mlflow.utils.file_utils import TempDir as TempDir
from mlflow.utils.proto_json_utils import dump_input_data as dump_input_data
from typing import Any, Dict

DEFAULT_IMAGE_NAME: str
DEPLOYMENT_MODE_ADD: str
DEPLOYMENT_MODE_REPLACE: str
DEPLOYMENT_MODE_CREATE: str
DEPLOYMENT_MODES: Incomplete
IMAGE_NAME_ENV_VAR: str
DEFAULT_BUCKET_NAME_PREFIX: str
DEFAULT_SAGEMAKER_INSTANCE_TYPE: str
DEFAULT_SAGEMAKER_INSTANCE_COUNT: int
DEFAULT_REGION_NAME: str
SAGEMAKER_SERVING_ENVIRONMENT: str

def push_image_to_ecr(image=...) -> None:
    """
    Push local Docker image to AWS ECR.

    The image is pushed under currently active AWS account and to the currently active AWS region.

    :param image: Docker image name.
    """
def deploy_transform_job(job_name, model_uri, s3_input_data_type, s3_input_uri, content_type, s3_output_path, compression_type: str = 'None', split_type: str = 'Line', accept: str = 'text/csv', assemble_with: str = 'Line', input_filter: str = '$', output_filter: str = '$', join_resource: str = 'None', execution_role_arn: Incomplete | None = None, assume_role_arn: Incomplete | None = None, bucket: Incomplete | None = None, image_url: Incomplete | None = None, region_name: str = 'us-west-2', instance_type=..., instance_count=..., vpc_config: Incomplete | None = None, flavor: Incomplete | None = None, archive: bool = False, synchronous: bool = True, timeout_seconds: int = 1200) -> None:
    '''
    Deploy an MLflow model on AWS SageMaker and create the corresponding batch transform job.
    The currently active AWS account must have correct permissions set up.

    :param job_name: Name of the deployed Sagemaker batch transform job.
    :param model_uri: The location, in URI format, of the MLflow model to deploy to SageMaker.
                      For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.

    :param s3_input_data_type: Input data type for the transform job.
    :param s3_input_uri: S3 key name prefix or a manifest of the input data.
    :param content_type: The multipurpose internet mail extension (MIME) type of the data.
    :param s3_output_path: The S3 path to store the output results of the Sagemaker transform job.
    :param compression_type: The compression type of the transform data.
    :param split_type: The method to split the transform job\'s data files into smaller batches.
    :param accept: The multipurpose internet mail extension (MIME) type of the output data.
    :param assemble_with: The method to assemble the results of the transform job as
            a single S3 object.
    :param input_filter: A JSONPath expression used to select a portion of the input data for
            the transform job.
    :param output_filter: A JSONPath expression used to select a portion of the output data from
            the transform job.
    :param join_resource: The source of the data to join with the transformed data.

    :param execution_role_arn: The name of an IAM role granting the SageMaker service permissions to
                               access the specified Docker image and S3 bucket containing MLflow
                               model artifacts. If unspecified, the currently-assumed role will be
                               used. This execution role is passed to the SageMaker service when
                               creating a SageMaker model from the specified MLflow model. It is
                               passed as the ``ExecutionRoleArn`` parameter of the `SageMaker
                               CreateModel API call <https://docs.aws.amazon.com/sagemaker/latest/
                               dg/API_CreateModel.html>`_. This role is *not* assumed for any other
                               call. For more information about SageMaker execution roles for model
                               creation, see
                               https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html.
    :param assume_role_arn: The name of an IAM cross-account role to be assumed to deploy SageMaker
                            to another AWS account. If unspecified, SageMaker will be deployed to
                            the the currently active AWS account.
    :param bucket: S3 bucket where model artifacts will be stored. Defaults to a
                   SageMaker-compatible bucket name.
    :param image_url: URL of the ECR-hosted Docker image the model should be deployed into, produced
                      by ``mlflow sagemaker build-and-push-container``. This parameter can also
                      be specified by the environment variable ``MLFLOW_SAGEMAKER_DEPLOY_IMG_URL``.
    :param region_name: Name of the AWS region to which to deploy the application.
    :param instance_type: The type of SageMaker ML instance on which to deploy the model. For a list
                          of supported instance types, see
                          https://aws.amazon.com/sagemaker/pricing/instance-types/.
    :param instance_count: The number of SageMaker ML instances on which to deploy the model.
    :param vpc_config: A dictionary specifying the VPC configuration to use when creating the
                       new SageMaker model associated with this batch transform job. The acceptable
                       values for this parameter are identical to those of the ``VpcConfig``
                       parameter in the `SageMaker boto3 client\'s create_model method
                       <https://boto3.readthedocs.io/en/latest/reference/services/sagemaker.html
                       #SageMaker.Client.create_model>`_. For more information, see
                       https://docs.aws.amazon.com/sagemaker/latest/dg/API_VpcConfig.html.

                       .. code-block:: python
                           :caption: Example

                            import mlflow.sagemaker as mfs

                            vpc_config = {
                                "SecurityGroupIds": [
                                    "sg-123456abc",
                                ],
                                "Subnets": [
                                    "subnet-123456abc",
                                ],
                            }
                            mfs.deploy_transform_job(..., vpc_config=vpc_config)

    :param flavor: The name of the flavor of the model to use for deployment. Must be either
                   ``None`` or one of mlflow.sagemaker.SUPPORTED_DEPLOYMENT_FLAVORS. If ``None``,
                   a flavor is automatically selected from the model\'s available flavors. If the
                   specified flavor is not present or not supported for deployment, an exception
                   will be thrown.
    :param archive: If ``True``, resources like Sagemaker models and model artifacts in S3 are
                    preserved after the finished batch transform job. If ``False``, these resources
                    are deleted. In order to use ``archive=False``, ``deploy_transform_job()`` must
                    be executed synchronously with ``synchronous=True``.
    :param synchronous: If ``True``, this function will block until the deployment process succeeds
                        or encounters an irrecoverable failure. If ``False``, this function will
                        return immediately after starting the deployment process. It will not wait
                        for the deployment process to complete; in this case, the caller is
                        responsible for monitoring the health and status of the pending deployment
                        via native SageMaker APIs or the AWS console.
    :param timeout_seconds: If ``synchronous`` is ``True``, the deployment process will return after
                            the specified number of seconds if no definitive result (success or
                            failure) is achieved. Once the function returns, the caller is
                            responsible for monitoring the health and status of the pending
                            deployment using native SageMaker APIs or the AWS console. If
                            ``synchronous`` is ``False``, this parameter is ignored.
    '''
def terminate_transform_job(job_name, region_name: str = 'us-west-2', assume_role_arn: Incomplete | None = None, archive: bool = False, synchronous: bool = True, timeout_seconds: int = 300):
    """
    Terminate a SageMaker batch transform job.

    :param job_name: Name of the deployed Sagemaker batch transform job.
    :param region_name: Name of the AWS region in which the batch transform job is deployed.
    :param assume_role_arn: The name of an IAM cross-account role to be assumed to deploy SageMaker
                            to another AWS account. If unspecified, SageMaker will be deployed to
                            the the currently active AWS account.
    :param archive: If ``True``, resources associated with the specified batch transform job,
                    such as its associated models and model artifacts, are preserved.
                    If ``False``, these resources are deleted. In order to use ``archive=False``,
                    ``terminate_transform_job()`` must be executed synchronously
                    with ``synchronous=True``.
    :param synchronous: If `True`, this function blocks until the termination process succeeds
                        or encounters an irrecoverable failure. If `False`, this function
                        returns immediately after starting the termination process. It will not
                        wait for the termination process to complete; in this case, the caller is
                        responsible for monitoring the status of the termination process via native
                        SageMaker APIs or the AWS console.
    :param timeout_seconds: If `synchronous` is `True`, the termination process returns after the
                            specified number of seconds if no definitive result (success or failure)
                            is achieved. Once the function returns, the caller is responsible
                            for monitoring the status of the termination process via native
                            SageMaker APIs or the AWS console. If `synchronous` is False, this
                            parameter is ignored.
    """
def push_model_to_sagemaker(model_name, model_uri, execution_role_arn: Incomplete | None = None, assume_role_arn: Incomplete | None = None, bucket: Incomplete | None = None, image_url: Incomplete | None = None, region_name: str = 'us-west-2', vpc_config: Incomplete | None = None, flavor: Incomplete | None = None) -> None:
    '''
    Create a SageMaker Model from an MLflow model artifact.
    The currently active AWS account must have correct permissions set up.

    :param model_name: Name of the Sagemaker model.
    :param model_uri: The location, in URI format, of the MLflow model to deploy to SageMaker.
                      For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.

    :param execution_role_arn: The name of an IAM role granting the SageMaker service permissions to
                               access the specified Docker image and S3 bucket containing MLflow
                               model artifacts. If unspecified, the currently-assumed role will be
                               used. This execution role is passed to the SageMaker service when
                               creating a SageMaker model from the specified MLflow model. It is
                               passed as the ``ExecutionRoleArn`` parameter of the `SageMaker
                               CreateModel API call <https://docs.aws.amazon.com/sagemaker/latest/
                               dg/API_CreateModel.html>`_. This role is *not* assumed for any other
                               call. For more information about SageMaker execution roles for model
                               creation, see
                               https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html.
    :param assume_role_arn: The name of an IAM cross-account role to be assumed to deploy SageMaker
                            to another AWS account. If unspecified, SageMaker will be deployed to
                            the the currently active AWS account.
    :param bucket: S3 bucket where model artifacts will be stored. Defaults to a
                   SageMaker-compatible bucket name.
    :param image_url: URL of the ECR-hosted Docker image the model should be deployed into, produced
                      by ``mlflow sagemaker build-and-push-container``. This parameter can also
                      be specified by the environment variable ``MLFLOW_SAGEMAKER_DEPLOY_IMG_URL``.
    :param region_name: Name of the AWS region to which to deploy the application.
    :param vpc_config: A dictionary specifying the VPC configuration to use when creating the
                       new SageMaker model. The acceptable values for this parameter are identical
                       to those of the ``VpcConfig`` parameter in the `SageMaker boto3 client\'s
                       create_model method
                       <https://boto3.readthedocs.io/en/latest/reference/services/sagemaker.html
                       #SageMaker.Client.create_model>`_. For more information, see
                       https://docs.aws.amazon.com/sagemaker/latest/dg/API_VpcConfig.html.

                       .. code-block:: python
                           :caption: Example

                            import mlflow.sagemaker as mfs

                            vpc_config = {
                                "SecurityGroupIds": [
                                    "sg-123456abc",
                                ],
                                "Subnets": [
                                    "subnet-123456abc",
                                ],
                            }
                            mfs.push_model_to_sagemaker(..., vpc_config=vpc_config)

    :param flavor: The name of the flavor of the model to use for deployment. Must be either
                   ``None`` or one of mlflow.sagemaker.SUPPORTED_DEPLOYMENT_FLAVORS. If ``None``,
                   a flavor is automatically selected from the model\'s available flavors. If the
                   specified flavor is not present or not supported for deployment, an exception
                   will be thrown.
    '''
def run_local(name, model_uri, flavor: Incomplete | None = None, config: Incomplete | None = None) -> None:
    '''
    Serve the model locally in a SageMaker compatible Docker container.

    Note that models deployed locally cannot be managed by other deployment APIs
    (e.g. ``update_deployment``, ``delete_deployment``, etc).

    :param name: Name of the local serving application.
    :param model_uri: The location, in URI format, of the MLflow model to deploy locally.
                      For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.
    :param flavor: The name of the flavor of the model to use for deployment. Must be either
                   ``None`` or one of mlflow.sagemaker.SUPPORTED_DEPLOYMENT_FLAVORS.
                   If ``None``, a flavor is automatically selected from the model\'s available
                   flavors. If the specified flavor is not present or not supported for
                   deployment, an exception will be thrown.
    :param config: Configuration parameters. The supported parameters are:

                   - ``image``: The name of the Docker image to use for model serving. Defaults
                                to ``"mlflow-pyfunc"``.
                   - ``port``: The port at which to expose the model server on the local host.
                               Defaults to ``5000``.

    .. code-block:: python
        :caption: Python example

        from mlflow.models import build_docker
        from mlflow.deployments import get_deploy_client

        build_docker(name="mlflow-pyfunc")

        client = get_deploy_client("sagemaker")
        client.run_local(
            name="my-local-deployment",
            model_uri="/mlruns/0/abc/model",
            flavor="python_function",
            config={
                "port": 5000,
                "image": "mlflow-pyfunc",
            },
        )

    .. code-block:: bash
        :caption:  Command-line example

        mlflow models build-docker --name "mlflow-pyfunc"
        mlflow deployments run-local --target sagemaker \\\n                --name my-local-deployment \\\n                --model-uri "/mlruns/0/abc/model" \\\n                --flavor python_function \\\n                -C port=5000 \\\n                -C image="mlflow-pyfunc"
    '''
def target_help():
    """
    Provide help information for the SageMaker deployment client.
    """

class SageMakerDeploymentClient(BaseDeploymentClient):
    """
    Initialize a deployment client for SageMaker. The default region and assumed role ARN will
    be set according to the value of the `target_uri`.

    This class is meant to supercede the other ``mlflow.sagemaker`` real-time serving API's.
    It is also designed to be used through the :py:mod:`mlflow.deployments` module.
    This means that you can deploy to SageMaker using the
    `mlflow deployments CLI <https://www.mlflow.org/docs/latest/cli.html#mlflow-deployments>`_ and
    get a client through the :py:mod:`mlflow.deployments.get_deploy_client` function.

    :param target_uri: A URI that follows one of the following formats:

                       - ``sagemaker``: This will set the default region to `us-west-2` and
                         the default assumed role ARN to `None`.

                       - ``sagemaker:/region_name``: This will set the default region to
                         `region_name` and the default assumed role ARN to `None`.

                       - ``sagemaker:/region_name/assumed_role_arn``: This will set the default
                         region to `region_name` and the default assumed role ARN to
                         `assumed_role_arn`.

                       When an `assumed_role_arn` is provided without a `region_name`,
                       an MlflowException will be raised.
    """
    region_name: Incomplete
    assumed_role_arn: Incomplete
    def __init__(self, target_uri) -> None: ...
    def create_deployment(self, name, model_uri, flavor: Incomplete | None = None, config: Incomplete | None = None, endpoint: Incomplete | None = None):
        '''
        Deploy an MLflow model on AWS SageMaker.
        The currently active AWS account must have correct permissions set up.

        This function creates a SageMaker endpoint. For more information about the input data
        formats accepted by this endpoint, see the
        :ref:`MLflow deployment tools documentation <sagemaker_deployment>`.

        :param name: Name of the deployed application.
        :param model_uri: The location, in URI format, of the MLflow model to deploy to SageMaker.
                          For example:

                          - ``/Users/me/path/to/local/model``
                          - ``relative/path/to/local/model``
                          - ``s3://my_bucket/path/to/model``
                          - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                          - ``models:/<model_name>/<model_version>``
                          - ``models:/<model_name>/<stage>``

                          For more information about supported URI schemes, see
                          `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                          artifact-locations>`_.
        :param flavor: The name of the flavor of the model to use for deployment. Must be either
                       ``None`` or one of mlflow.sagemaker.SUPPORTED_DEPLOYMENT_FLAVORS.
                       If ``None``, a flavor is automatically selected from the model\'s available
                       flavors. If the specified flavor is not present or not supported for
                       deployment, an exception will be thrown.
        :param config: Configuration parameters. The supported parameters are:

                       - ``assume_role_arn``: The name of an IAM cross-account role to be assumed
                         to deploy SageMaker to another AWS account. If this parameter is not
                         specified, the role given in the ``target_uri`` will be used. If the
                         role is not given in the ``target_uri``, defaults to ``us-west-2``.

                       - ``execution_role_arn``: The name of an IAM role granting the SageMaker
                         service permissions to access the specified Docker image and S3 bucket
                         containing MLflow model artifacts. If unspecified, the currently-assumed
                         role will be used. This execution role is passed to the SageMaker service
                         when creating a SageMaker model from the specified MLflow model. It is
                         passed as the ``ExecutionRoleArn`` parameter of the `SageMaker
                         CreateModel API call <https://docs.aws.amazon.com/sagemaker/latest/
                         dg/API_CreateModel.html>`_. This role is *not* assumed for any other
                         call. For more information about SageMaker execution roles for model
                         creation, see
                         https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html.

                       - ``bucket``: S3 bucket where model artifacts will be stored. Defaults to a
                         SageMaker-compatible bucket name.

                       - ``image_url``: URL of the ECR-hosted Docker image the model should be
                         deployed into, produced by ``mlflow sagemaker build-and-push-container``.
                         This parameter can also be specified by the environment variable
                         ``MLFLOW_SAGEMAKER_DEPLOY_IMG_URL``.

                       - ``region_name``: Name of the AWS region to which to deploy the application.
                         If unspecified, use the region name given in the ``target_uri``.
                         If it is also not specified in the ``target_uri``,
                         defaults to ``us-west-2``.

                       - ``archive``: If ``True``, any pre-existing SageMaker application resources
                         that become inactive (i.e. as a result of deploying in
                         ``mlflow.sagemaker.DEPLOYMENT_MODE_REPLACE`` mode) are preserved.
                         These resources may include unused SageMaker models and endpoint
                         configurations that were associated with a prior version of the
                         application endpoint. If ``False``, these resources are deleted.
                         In order to use ``archive=False``, ``create_deployment()`` must be executed
                         synchronously with ``synchronous=True``. Defaults to ``False``.

                       - ``instance_type``: The type of SageMaker ML instance on which to deploy the
                         model. For a list of supported instance types, see
                         https://aws.amazon.com/sagemaker/pricing/instance-types/.
                         Defaults to ``ml.m4.xlarge``.

                       - ``instance_count``: The number of SageMaker ML instances on which to deploy
                         the model. Defaults to ``1``.

                       - ``synchronous``: If ``True``, this function will block until the deployment
                         process succeeds or encounters an irrecoverable failure. If ``False``,
                         this function will return immediately after starting the deployment
                         process. It will not wait for the deployment process to complete;
                         in this case, the caller is responsible for monitoring the health and
                         status of the pending deployment via native SageMaker APIs or the AWS
                         console. Defaults to ``True``.

                       - ``timeout_seconds``: If ``synchronous`` is ``True``, the deployment process
                         will return after the specified number of seconds if no definitive result
                         (success or failure) is achieved. Once the function returns, the caller is
                         responsible for monitoring the health and status of the pending
                         deployment using native SageMaker APIs or the AWS console. If
                         ``synchronous`` is ``False``, this parameter is ignored.
                         Defaults to ``300``.

                       - ``vpc_config``: A dictionary specifying the VPC configuration to use when
                         creating the new SageMaker model associated with this application.
                         The acceptable values for this parameter are identical to those of the
                         ``VpcConfig`` parameter in the `SageMaker boto3 client\'s create_model
                         method <https://boto3.readthedocs.io/en/latest/reference/services/sagemaker.html
                         #SageMaker.Client.create_model>`_. For more information, see
                         https://docs.aws.amazon.com/sagemaker/latest/dg/API_VpcConfig.html.
                         Defaults to ``None``.

                       - ``data_capture_config``: A dictionary specifying the data capture
                         configuration to use when creating the new SageMaker model associated with
                         this application.
                         For more information, see
                         https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataCaptureConfig.html.
                         Defaults to ``None``.

                       - ``variant_name``: A string specifying the desired name when creating a
                                           production variant.  Defaults to ``None``.
                       - ``async_inference_config``: A dictionary specifying the async_inference_configuration # pylint: disable=line-too-long

                       - ``env``: A dictionary specifying environment variables as key-value
                         pairs to be set for the deployed model. Defaults to ``None``.

                       - ``tags``: A dictionary of key-value pairs representing additional
                         tags to be set for the deployed model. Defaults to ``None``.

        :param endpoint: (optional) Endpoint to create the deployment under. Currently unsupported

        .. code-block:: python
            :caption: Python example

            from mlflow.deployments import get_deploy_client

            vpc_config = {
                "SecurityGroupIds": [
                    "sg-123456abc",
                ],
                "Subnets": [
                    "subnet-123456abc",
                ],
            }
            config = dict(
                assume_role_arn="arn:aws:123:role/assumed_role",
                execution_role_arn="arn:aws:456:role/execution_role",
                bucket_name="my-s3-bucket",
                image_url="1234.dkr.ecr.us-east-1.amazonaws.com/mlflow-test:1.23.1",
                region_name="us-east-1",
                archive=False,
                instance_type="ml.m5.4xlarge",
                instance_count=1,
                synchronous=True,
                timeout_seconds=300,
                vpc_config=vpc_config,
                variant_name="prod-variant-1",
                env={"DISABLE_NGINX": "true", "GUNICORN_CMD_ARGS": \'"--timeout 60"\'},
                tags={"training_timestamp": "2022-11-01T05:12:26"},
            )
            client = get_deploy_client("sagemaker")
            client.create_deployment(
                "my-deployment",
                model_uri="/mlruns/0/abc/model",
                flavor="python_function",
                config=config,
            )
        .. code-block:: bash
            :caption:  Command-line example

            mlflow deployments create --target sagemaker:/us-east-1/arn:aws:123:role/assumed_role \\\n                    --name my-deployment \\\n                    --model-uri /mlruns/0/abc/model \\\n                    --flavor python_function\\\n                    -C execution_role_arn=arn:aws:456:role/execution_role \\\n                    -C bucket_name=my-s3-bucket \\\n                    -C image_url=1234.dkr.ecr.us-east-1.amazonaws.com/mlflow-test:1.23.1 \\\n                    -C region_name=us-east-1 \\\n                    -C archive=False \\\n                    -C instance_type=ml.m5.4xlarge \\\n                    -C instance_count=1 \\\n                    -C synchronous=True \\\n                    -C timeout_seconds=300 \\\n                    -C variant_name=prod-variant-1 \\\n                    -C vpc_config=\'{"SecurityGroupIds": ["sg-123456abc"], \\\n                    "Subnets": ["subnet-123456abc"]}\' \\\n                    -C data_capture_config=\'{"EnableCapture": True, \\\n                    \'InitalSamplingPercentage\': 100, \'DestinationS3Uri": \'s3://my-bucket/path\', \\\n                    \'CaptureOptions\': [{\'CaptureMode\': \'Output\'}]}\'
                    -C env=\'{"DISABLE_NGINX": "true", "GUNICORN_CMD_ARGS": ""--timeout 60""}\' \\\n                    -C tags=\'{"training_timestamp": "2022-11-01T05:12:26"}\' \\\n        '''
    def update_deployment(self, name, model_uri, flavor: Incomplete | None = None, config: Incomplete | None = None, endpoint: Incomplete | None = None):
        '''
        Update a deployment on AWS SageMaker. This function can replace or add a new model to
        an existing SageMaker endpoint. By default, this function replaces the existing model
        with the new one. The currently active AWS account must have correct permissions set up.

        :param name: Name of the deployed application.
        :param model_uri: The location, in URI format, of the MLflow model to deploy to SageMaker.
                          For example:

                          - ``/Users/me/path/to/local/model``
                          - ``relative/path/to/local/model``
                          - ``s3://my_bucket/path/to/model``
                          - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                          - ``models:/<model_name>/<model_version>``
                          - ``models:/<model_name>/<stage>``

                          For more information about supported URI schemes, see
                          `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                          artifact-locations>`_.

        :param flavor: The name of the flavor of the model to use for deployment. Must be either
                       ``None`` or one of mlflow.sagemaker.SUPPORTED_DEPLOYMENT_FLAVORS.
                       If ``None``, a flavor is automatically selected from the model\'s available
                       flavors. If the specified flavor is not present or not supported for
                       deployment, an exception will be thrown.

        :param config: Configuration parameters. The supported parameters are:

                       - ``assume_role_arn``: The name of an IAM cross-account role to be assumed
                         to deploy SageMaker to another AWS account. If this parameter is not
                         specified, the role given in the ``target_uri`` will be used. If the
                         role is not given in the ``target_uri``, defaults to ``us-west-2``.

                       - ``execution_role_arn``: The name of an IAM role granting the SageMaker
                         service permissions to access the specified Docker image and S3 bucket
                         containing MLflow model artifacts. If unspecified, the currently-assumed
                         role will be used. This execution role is passed to the SageMaker service
                         when creating a SageMaker model from the specified MLflow model. It is
                         passed as the ``ExecutionRoleArn`` parameter of the `SageMaker
                         CreateModel API call <https://docs.aws.amazon.com/sagemaker/latest/
                         dg/API_CreateModel.html>`_. This role is *not* assumed for any other
                         call. For more information about SageMaker execution roles for model
                         creation, see
                         https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html.

                       - ``bucket``: S3 bucket where model artifacts will be stored. Defaults to a
                         SageMaker-compatible bucket name.

                       - ``image_url``: URL of the ECR-hosted Docker image the model should be
                         deployed into, produced by ``mlflow sagemaker build-and-push-container``.
                         This parameter can also be specified by the environment variable
                         ``MLFLOW_SAGEMAKER_DEPLOY_IMG_URL``.

                       - ``region_name``: Name of the AWS region to which to deploy the application.
                         If unspecified, use the region name given in the ``target_uri``.
                         If it is also not specified in the ``target_uri``,
                         defaults to ``us-west-2``.

                       - ``mode``: The mode in which to deploy the application.
                         Must be one of the following:

                         ``mlflow.sagemaker.DEPLOYMENT_MODE_REPLACE``
                             If an application of the specified name exists, its model(s) is
                             replaced with the specified model. If no such application exists,
                             it is created with the specified name and model.
                             This is the default mode.

                         ``mlflow.sagemaker.DEPLOYMENT_MODE_ADD``
                             Add the specified model to a pre-existing application with the
                             specified name, if one exists. If the application does not exist,
                             a new application is created with the specified name and model.
                             NOTE: If the application **already exists**, the specified model is
                             added to the application\'s corresponding SageMaker endpoint with an
                             initial weight of zero (0). To route traffic to the model,
                             update the application\'s associated endpoint configuration using
                             either the AWS console or the ``UpdateEndpointWeightsAndCapacities``
                             function defined in https://docs.aws.amazon.com/sagemaker/latest/dg/API_UpdateEndpointWeightsAndCapacities.html.

                       - ``archive``: If ``True``, any pre-existing SageMaker application resources
                         that become inactive (i.e. as a result of deploying in
                         ``mlflow.sagemaker.DEPLOYMENT_MODE_REPLACE`` mode) are preserved.
                         These resources may include unused SageMaker models and endpoint
                         configurations that were associated with a prior version of the
                         application endpoint. If ``False``, these resources are deleted.
                         In order to use ``archive=False``, ``update_deployment()`` must be executed
                         synchronously with ``synchronous=True``. Defaults to ``False``.

                       - ``instance_type``: The type of SageMaker ML instance on which to deploy the
                         model. For a list of supported instance types, see
                         https://aws.amazon.com/sagemaker/pricing/instance-types/.
                         Defaults to ``ml.m4.xlarge``.

                       - ``instance_count``: The number of SageMaker ML instances on which to deploy
                         the model. Defaults to ``1``.

                       - ``synchronous``: If ``True``, this function will block until the deployment
                         process succeeds or encounters an irrecoverable failure. If ``False``,
                         this function will return immediately after starting the deployment
                         process. It will not wait for the deployment process to complete;
                         in this case, the caller is responsible for monitoring the health and
                         status of the pending deployment via native SageMaker APIs or the AWS
                         console. Defaults to ``True``.

                       - ``timeout_seconds``: If ``synchronous`` is ``True``, the deployment process
                         will return after the specified number of seconds if no definitive result
                         (success or failure) is achieved. Once the function returns, the caller is
                         responsible for monitoring the health and status of the pending
                         deployment using native SageMaker APIs or the AWS console. If
                         ``synchronous`` is ``False``, this parameter is ignored.
                         Defaults to ``300``.

                       - ``variant_name``: A string specifying the desired name when creating a
                                           production variant.  Defaults to ``None``.

                       - ``vpc_config``: A dictionary specifying the VPC configuration to use when
                         creating the new SageMaker model associated with this application.
                         The acceptable values for this parameter are identical to those of the
                         ``VpcConfig`` parameter in the `SageMaker boto3 client\'s create_model
                         method <https://boto3.readthedocs.io/en/latest/reference/services/sagemaker.html
                         #SageMaker.Client.create_model>`_. For more information, see
                         https://docs.aws.amazon.com/sagemaker/latest/dg/API_VpcConfig.html.
                         Defaults to ``None``.

                       - ``data_capture_config``: A dictionary specifying the data capture
                         configuration to use when creating the new SageMaker model associated with
                         this application.
                         For more information, see
                         https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataCaptureConfig.html.
                         Defaults to ``None``.

                       - ``variant_name``: A string specifying the desired name when creating a
                                           production variant.  Defaults to ``None``.                                           
                       - ``async_inference_config``: A dictionary specifying the async config 
                                                     configuration. Defaults to ``None``.
                       - ``env``: A dictionary specifying environment variables as key-value pairs
                         to be set for the deployed model. Defaults to ``None``.

                       - ``tags``: A dictionary of key-value pairs representing additional tags
                         to be set for the deployed model. Defaults to ``None``.

        :param endpoint: (optional) Endpoint containing the deployment to update. Currently
                         unsupported

        .. code-block:: python
            :caption: Python example

            from mlflow.deployments import get_deploy_client

            vpc_config = {
                "SecurityGroupIds": [
                    "sg-123456abc",
                ],
                "Subnets": [
                    "subnet-123456abc",
                ],
            }
            data_capture_config = {
                "EnableCapture": True,
                "InitalSamplingPercentage": 100,
                "DestinationS3Uri": "s3://my-bucket/path",
                "CaptureOptions": [{"CaptureMode": "Output"}],
            }
            config = dict(
                assume_role_arn="arn:aws:123:role/assumed_role",
                execution_role_arn="arn:aws:456:role/execution_role",
                bucket_name="my-s3-bucket",
                image_url="1234.dkr.ecr.us-east-1.amazonaws.com/mlflow-test:1.23.1",
                region_name="us-east-1",
                mode="replace",
                archive=False,
                instance_type="ml.m5.4xlarge",
                instance_count=1,
                synchronous=True,
                timeout_seconds=300,
                variant_name="prod-variant-1",
                vpc_config=vpc_config,
                data_capture_config=data_capture_config,
                env={"DISABLE_NGINX": "true", "GUNICORN_CMD_ARGS": \'"--timeout 60"\'},
                tags={"training_timestamp": "2022-11-01T05:12:26"},
            )
            client = get_deploy_client("sagemaker")
            client.update_deployment(
                "my-deployment",
                model_uri="/mlruns/0/abc/model",
                flavor="python_function",
                config=config,
            )
        .. code-block:: bash
            :caption:  Command-line example

            mlflow deployments update --target sagemaker:/us-east-1/arn:aws:123:role/assumed_role \\\n                    --name my-deployment \\\n                    --model-uri /mlruns/0/abc/model \\\n                    --flavor python_function\\\n                    -C execution_role_arn=arn:aws:456:role/execution_role \\\n                    -C bucket_name=my-s3-bucket \\\n                    -C image_url=1234.dkr.ecr.us-east-1.amazonaws.com/mlflow-test:1.23.1 \\\n                    -C region_name=us-east-1 \\\n                    -C mode=replace \\\n                    -C archive=False \\\n                    -C instance_type=ml.m5.4xlarge \\\n                    -C instance_count=1 \\\n                    -C synchronous=True \\\n                    -C timeout_seconds=300 \\\n                    -C variant_name=prod-variant-1 \\\n                    -C vpc_config=\'{"SecurityGroupIds": ["sg-123456abc"], \\\n                    "Subnets": ["subnet-123456abc"]}\' \\\n                    -C data_capture_config=\'{"EnableCapture": True, \\\n                    "InitalSamplingPercentage": 100, "DestinationS3Uri": "s3://my-bucket/path", \\\n                    "CaptureOptions": [{"CaptureMode": "Output"}]}\'
                    -C env=\'{"DISABLE_NGINX": "true", "GUNICORN_CMD_ARGS": ""--timeout 60""}\' \\\n                    -C tags=\'{"training_timestamp": "2022-11-01T05:12:26"}\' \\\n        '''
    def delete_deployment(self, name, config: Incomplete | None = None, endpoint: Incomplete | None = None) -> None:
        '''
        Delete a SageMaker application.

        :param name: Name of the deployed application.
        :param config: Configuration parameters. The supported parameters are:

                       - ``assume_role_arn``: The name of an IAM role to be assumed to delete
                         the SageMaker deployment.

                       - ``region_name``: Name of the AWS region in which the application
                         is deployed. Defaults to ``us-west-2`` or the region provided in
                         the `target_uri`.

                       - ``archive``: If `True`, resources associated with the specified
                         application, such as its associated models and endpoint configuration,
                         are preserved. If `False`, these resources are deleted. In order to use
                         ``archive=False``, ``delete()`` must be executed synchronously with
                         ``synchronous=True``. Defaults to ``False``.

                       - ``synchronous``: If `True`, this function blocks until the deletion process
                         succeeds or encounters an irrecoverable failure. If `False`, this function
                         returns immediately after starting the deletion process. It will not wait
                         for the deletion process to complete; in this case, the caller is
                         responsible for monitoring the status of the deletion process via native
                         SageMaker APIs or the AWS console. Defaults to ``True``.

                       - ``timeout_seconds``: If `synchronous` is `True`, the deletion process
                         returns after the specified number of seconds if no definitive result
                         (success or failure) is achieved. Once the function returns, the caller
                         is responsible for monitoring the status of the deletion process via native
                         SageMaker APIs or the AWS console. If `synchronous` is False, this
                         parameter is ignored. Defaults to ``300``.
        :param endpoint: (optional) Endpoint containing the deployment to delete. Currently
                         unsupported

        .. code-block:: python
            :caption: Python example

            from mlflow.deployments import get_deploy_client

            config = dict(
                assume_role_arn="arn:aws:123:role/assumed_role",
                region_name="us-east-1",
                archive=False,
                synchronous=True,
                timeout_seconds=300,
            )
            client = get_deploy_client("sagemaker")
            client.delete_deployment("my-deployment", config=config)

        .. code-block:: bash
            :caption: Command-line example

            mlflow deployments delete --target sagemaker \\\n                    --name my-deployment \\\n                    -C assume_role_arn=arn:aws:123:role/assumed_role \\\n                    -C region_name=us-east-1 \\\n                    -C archive=False \\\n                    -C synchronous=True \\\n                    -C timeout_seconds=300
        '''
    def list_deployments(self, endpoint: Incomplete | None = None):
        '''
        List deployments. This method returns a list of dictionaries that describes each deployment.

        If a region name needs to be specified, the plugin must be initialized
        with the AWS region in the ``target_uri`` such as ``sagemaker:/us-east-1``.

        To assume an IAM role, the plugin must be initialized
        with the AWS region and the role ARN in the ``target_uri`` such as
        ``sagemaker:/us-east-1/arn:aws:1234:role/assumed_role``.

        :param endpoint: (optional) List deployments in the specified endpoint. Currently
                         unsupported

        :return: A list of dictionaries corresponding to deployments.

        .. code-block:: python
            :caption: Python example

            from mlflow.deployments import get_deploy_client

            client = get_deploy_client("sagemaker:/us-east-1/arn:aws:123:role/assumed_role")
            client.list_deployments()

        .. code-block:: bash
            :caption: Command-line example

            mlflow deployments list --target sagemaker:/us-east-1/arn:aws:1234:role/assumed_role
        '''
    def get_deployment(self, name, endpoint: Incomplete | None = None):
        '''
        Returns a dictionary describing the specified deployment.

        If a region name needs to be specified, the plugin must be initialized
        with the AWS region in the ``target_uri`` such as ``sagemaker:/us-east-1``.

        To assume an IAM role, the plugin must be initialized
        with the AWS region and the role ARN in the ``target_uri`` such as
        ``sagemaker:/us-east-1/arn:aws:1234:role/assumed_role``.

        A :py:class:`mlflow.exceptions.MlflowException` will also be thrown when an error occurs
        while retrieving the deployment.

        :param name: Name of deployment to retrieve
        :param endpoint: (optional) Endpoint containing the deployment to get. Currently
                         unsupported
        :return: A dictionary that describes the specified deployment

        .. code-block:: python
            :caption: Python example

            from mlflow.deployments import get_deploy_client

            client = get_deploy_client("sagemaker:/us-east-1/arn:aws:123:role/assumed_role")
            client.get_deployment("my-deployment")

        .. code-block:: bash
            :caption: Command-line example

            mlflow deployments get --target sagemaker:/us-east-1/arn:aws:1234:role/assumed_role \\\n                --name my-deployment
        '''
    def predict(self, deployment_name: Incomplete | None = None, inputs: Incomplete | None = None, endpoint: Incomplete | None = None, params: Dict[str, Any] | None = None):
        '''
        Compute predictions from the specified deployment using the provided PyFunc input.

        The input/output types of this method match the :ref:`MLflow PyFunc prediction
        interface <pyfunc-inference-api>`.

        If a region name needs to be specified, the plugin must be initialized
        with the AWS region in the ``target_uri`` such as ``sagemaker:/us-east-1``.

        To assume an IAM role, the plugin must be initialized
        with the AWS region and the role ARN in the ``target_uri`` such as
        ``sagemaker:/us-east-1/arn:aws:1234:role/assumed_role``.

        :param deployment_name: Name of the deployment to predict against.
        :param inputs: Input data (or arguments) to pass to the deployment or model endpoint for
                       inference. For a complete list of supported input types, see
                       :ref:`pyfunc-inference-api`.
        :param endpoint: Endpoint to predict against. Currently unsupported
        :return: A PyFunc output, such as a Pandas DataFrame, Pandas Series, or NumPy array.
                 For a complete list of supported output types, see :ref:`pyfunc-inference-api`.

        .. code-block:: python
            :caption: Python example

            import pandas as pd
            from mlflow.deployments import get_deploy_client

            df = pd.DataFrame(data=[[1, 2, 3]], columns=["feat1", "feat2", "feat3"])
            client = get_deploy_client("sagemaker:/us-east-1/arn:aws:123:role/assumed_role")
            client.predict("my-deployment", df)

        .. code-block:: bash
            :caption: Command-line example

            cat > ./input.json <<- input
            {"feat1": {"0": 1}, "feat2": {"0": 2}, "feat3": {"0": 3}}
            input

            mlflow deployments predict \\\n                --target sagemaker:/us-east-1/arn:aws:1234:role/assumed_role \\\n                --name my-deployment \\\n                --input-path ./input.json
        '''
    def explain(self, deployment_name: Incomplete | None = None, df: Incomplete | None = None, endpoint: Incomplete | None = None) -> None:
        """
        *This function has not been implemented and will be coming in the future.*
        """
    def create_endpoint(self, name, config: Incomplete | None = None) -> None:
        """
        Create an endpoint with the specified target. By default, this method should block until
        creation completes (i.e. until it's possible to create a deployment within the endpoint).
        In the case of conflicts (e.g. if it's not possible to create the specified endpoint
        due to conflict with an existing endpoint), raises a
        :py:class:`mlflow.exceptions.MlflowException`. See target-specific plugin documentation
        for additional detail on support for asynchronous creation and other configuration.

        :param name: Unique name to use for endpoint. If another endpoint exists with the same
                     name, raises a :py:class:`mlflow.exceptions.MlflowException`.
        :param config: (optional) Dict containing target-specific configuration for the
                       endpoint.
        :return: Dict corresponding to created endpoint, which must contain the 'name' key.
        """
    def update_endpoint(self, endpoint, config: Incomplete | None = None) -> None:
        """
        Update the endpoint with the specified name. You can update any target-specific attributes
        of the endpoint (via `config`). By default, this method should block until the update
        completes (i.e. until it's possible to create a deployment within the endpoint). See
        target-specific plugin documentation for additional detail on support for asynchronous
        update and other configuration.

        :param endpoint: Unique name of endpoint to update
        :param config: (optional) dict containing target-specific configuration for the
                       endpoint
        :return: None
        """
    def delete_endpoint(self, endpoint) -> None:
        """
        Delete the endpoint from the specified target. Deletion should be idempotent (i.e. deletion
        should not fail if retried on a non-existent deployment).

        :param endpoint: Name of endpoint to delete
        :return: None
        """
    def list_endpoints(self) -> None:
        """
        List endpoints in the specified target. This method is expected to return an
        unpaginated list of all endpoints (an alternative would be to return a dict with
        an 'endpoints' field containing the actual endpoints, with plugins able to specify
        other fields, e.g. a next_page_token field, in the returned dictionary for pagination,
        and to accept a `pagination_args` argument to this method for passing
        pagination-related args).

        :return: A list of dicts corresponding to endpoints. Each dict is guaranteed to
                 contain a 'name' key containing the endpoint name. The other fields of
                 the returned dictionary and their types may vary across targets.
        """
    def get_endpoint(self, endpoint) -> None:
        """
        Returns a dictionary describing the specified endpoint, throwing a
        py:class:`mlflow.exception.MlflowException` if no endpoint exists with the provided
        name.
        The dict is guaranteed to contain an 'name' key containing the endpoint name.
        The other fields of the returned dictionary and their types may vary across targets.

        :param endpoint: Name of endpoint to fetch
        """

class _SageMakerOperation:
    status_check_fn: Incomplete
    cleanup_fn: Incomplete
    start_time: Incomplete
    status: Incomplete
    cleaned_up: bool
    def __init__(self, status_check_fn, cleanup_fn) -> None: ...
    def await_completion(self, timeout_seconds): ...
    def clean_up(self) -> None: ...

class _SageMakerOperationStatus:
    STATE_SUCCEEDED: str
    STATE_FAILED: str
    STATE_IN_PROGRESS: str
    STATE_TIMED_OUT: str
    state: Incomplete
    message: Incomplete
    def __init__(self, state, message) -> None: ...
    @classmethod
    def in_progress(cls, message: Incomplete | None = None): ...
    @classmethod
    def timed_out(cls, duration_seconds): ...
    @classmethod
    def failed(cls, message): ...
    @classmethod
    def succeeded(cls, message): ...
