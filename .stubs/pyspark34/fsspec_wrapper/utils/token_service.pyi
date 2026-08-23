from .common import IS_PYTHON_RUNTIME as IS_PYTHON_RUNTIME, SynapseCredential as SynapseCredential
from _typeshed import Incomplete

logger: Incomplete

class TokenServiceClient:
    def __init__(self, *args, **kwargs) -> None: ...
    def get_account_name_and_credential_of_linked_service(self, linked_service: str = '') -> tuple[str, SynapseCredential]:
        """Gets account_name and credentials for the given linked service.

        Args:
        linked_service: Linked service name.

        Returns:
        account_name and credentials.

        Raises:
        Exception: If unable to fetch credentials and other details.
        """
    def get_aad_credential(self, audience: str) -> SynapseCredential:
        """Gets AAD credentials.

        Args:
        audience: Audience for resource template.

        Returns:
        credentials.

        Raises:
        Exception: If unable to fetch credentials.
        """
    def get_valid_token(self): ...
