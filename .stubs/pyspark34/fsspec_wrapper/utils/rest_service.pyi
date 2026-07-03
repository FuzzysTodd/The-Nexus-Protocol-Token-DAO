from .common import SynapseCredential as SynapseCredential
from _typeshed import Incomplete

aad_ep: str
linked_service_ep: str
cache: Incomplete

class RestServiceClient:
    """
    Swagger UI documentation: https://tokenservice.northeurope.azuresynapse-dogfood.net/swagger/index.html
    """
    time_delta: int
    sparkconf: Incomplete
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
