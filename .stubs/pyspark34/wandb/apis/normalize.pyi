import requests
from typing import List
from wandb import env as env
from wandb.errors import CommError as CommError, Error as Error

def parse_backend_error_messages(response: requests.Response) -> List[str]: ...
def normalize_exceptions(func: _F) -> _F:
    """Function decorator for catching common errors and re-raising as wandb.Error."""
