from _typeshed import Incomplete

logger: Incomplete
AZURE_US_GOVERNMENT: str
AZURE_CHINA: str
AZURE_PUBLIC: str
WORLD_WIDE: str
WELL_KNOWN_AUTHORITY_HOSTS: Incomplete
WELL_KNOWN_B2C_HOSTS: Incomplete

class AuthorityBuilder:
    def __init__(self, instance, tenant) -> None:
        """A helper to save caller from doing string concatenation.

        Usage is documented in :func:`application.ClientApplication.__init__`.
        """

class Authority:
    '''This class represents an (already-validated) authority.

    Once constructed, it contains members named "*_endpoint" for this instance.
    TODO: It will also cache the previously-validated authority instances.
    '''
    is_adfs: Incomplete
    authorization_endpoint: Incomplete
    token_endpoint: Incomplete
    device_authorization_endpoint: Incomplete
    def __init__(self, authority_url, http_client, validate_authority: bool = True, instance_discovery: Incomplete | None = None) -> None:
        """Creates an authority instance, and also validates it.

        :param validate_authority:
            The Authority validation process actually checks two parts:
            instance (a.k.a. host) and tenant. We always do a tenant discovery.
            This parameter only controls whether an instance discovery will be
            performed.
        """
    def user_realm_discovery(self, username, correlation_id: Incomplete | None = None, response: Incomplete | None = None): ...

def canonicalize(authority_or_auth_endpoint): ...
def tenant_discovery(tenant_discovery_endpoint, http_client, **kwargs): ...
