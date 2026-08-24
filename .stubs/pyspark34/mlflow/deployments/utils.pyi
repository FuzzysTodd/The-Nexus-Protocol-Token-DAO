from mlflow.exceptions import MlflowException as MlflowException

def parse_target_uri(target_uri):
    """Parse out the deployment target from the provided target uri"""
