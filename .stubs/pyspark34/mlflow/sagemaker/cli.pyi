from mlflow.utils import cli_args as cli_args

def commands() -> None:
    """
    Serve models on SageMaker.

    To serve a model associated with a run on a tracking server, set the MLFLOW_TRACKING_URI
    environment variable to the URL of the desired server.
    """
def deploy_transform_job(job_name, model_uri, input_data_type, input_uri, content_type, output_path, compression_type, split_type, accept, assemble_with, input_filter, output_filter, join_resource, execution_role_arn, bucket, image_url, region_name, instance_type, instance_count, vpc_config, flavor, archive, asynchronous, timeout) -> None:
    """
    Deploy model on Sagemaker as a batch transform job. Current active AWS account needs to have
    correct permissions setup.

    By default, unless the ``--async`` flag is specified, this command will block until
    either the batch transform job completes (definitively succeeds or fails) or the specified
    timeout elapses.
    """
def terminate_transform_job(job_name, region_name, archive, asynchronous, timeout) -> None:
    """
    Terminate the specified Sagemaker batch transform job. Unless ``--archive`` is specified,
    all SageMaker resources associated with the batch transform job are deleted as well.

    By default, unless the ``--async`` flag is specified, this command will block until
    either the termination process completes (definitively succeeds or fails) or the specified
    timeout elapses.
    """
def push_model_to_sagemaker(model_name, model_uri, execution_role_arn, bucket, image_url, region_name, vpc_config, flavor) -> None:
    """
    Push an MLflow model to Sagemaker model registry. Current active AWS account needs to have
    correct permissions setup.
    """
def build_and_push_container(build, push, container, env_manager, mlflow_home):
    """
    Build new MLflow Sagemaker image, assign it a name, and push to ECR.

    This function builds an MLflow Docker image.
    The image is built locally and it requires Docker to run.
    The image is pushed to ECR under current active AWS account and to current active AWS region.
    """
