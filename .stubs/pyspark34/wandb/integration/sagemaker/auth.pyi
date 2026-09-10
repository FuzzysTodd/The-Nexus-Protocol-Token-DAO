from _typeshed import Incomplete
from wandb import env as env

def sagemaker_auth(overrides: Incomplete | None = None, path: str = '.', api_key: Incomplete | None = None) -> None:
    """Write a secrets.env file with the W&B ApiKey and any additional secrets passed.

    Arguments:
        overrides (dict, optional): Additional environment variables to write
                                    to secrets.env
        path (str, optional): The path to write the secrets file.
    """
