from .._constants import EnvironmentVariables as EnvironmentVariables
from .client_assertion import ClientAssertionCredential as ClientAssertionCredential
from typing import Any

class TokenFileMixin:
    def __init__(self, token_file_path: str, **_: Any) -> None: ...

class WorkloadIdentityCredential(ClientAssertionCredential, TokenFileMixin):
    '''Authenticates using an Azure Active Directory workload identity.

    Workload identity authentication is a feature in Azure that allows applications running on virtual machines (VMs)
    to access other Azure resources without the need for a service principal or managed identity. With workload
    identity authentication, applications authenticate themselves using their own identity, rather than using a shared
    service principal or managed identity. Under the hood, workload identity authentication uses the concept of Service
    Account Credentials (SACs), which are automatically created by Azure and stored securely in the VM. By using
    workload identity authentication, you can avoid the need to manage and rotate service principals or managed
    identities for each application on each VM. Additionally, because SACs are created automatically and managed by
    Azure, you don\'t need to worry about storing and securing sensitive credentials themselves.

    The WorkloadIdentityCredential supports Azure workload identity authentication on Azure Kubernetes and acquires
    a token using the service account credentials available in the Azure Kubernetes environment. Refer
    to `this workload identity overview <https://learn.microsoft.com/azure/aks/workload-identity-overview>`__
    for more information.

    :keyword str tenant_id: ID of the application\'s Azure Active Directory tenant. Also called its "directory" ID.
    :keyword str client_id: The client ID of an Azure AD app registration.
    :keyword str token_file_path: The path to a file containing a Kubernetes service account token that authenticates
        the identity.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START workload_identity_credential]
            :end-before: [END workload_identity_credential]
            :language: python
            :dedent: 4
            :caption: Create a WorkloadIdentityCredential.
    '''
    def __init__(self, *, tenant_id: str | None = None, client_id: str | None = None, token_file_path: str | None = None, **kwargs: Any) -> None: ...
