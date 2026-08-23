from . import sign_string as sign_string, url_quote as url_quote
from .constants import X_MS_VERSION as X_MS_VERSION
from _typeshed import Incomplete

class QueryStringConstants:
    SIGNED_SIGNATURE: str
    SIGNED_PERMISSION: str
    SIGNED_START: str
    SIGNED_EXPIRY: str
    SIGNED_RESOURCE: str
    SIGNED_IDENTIFIER: str
    SIGNED_IP: str
    SIGNED_PROTOCOL: str
    SIGNED_VERSION: str
    SIGNED_CACHE_CONTROL: str
    SIGNED_CONTENT_DISPOSITION: str
    SIGNED_CONTENT_ENCODING: str
    SIGNED_CONTENT_LANGUAGE: str
    SIGNED_CONTENT_TYPE: str
    START_PK: str
    START_RK: str
    END_PK: str
    END_RK: str
    SIGNED_RESOURCE_TYPES: str
    SIGNED_SERVICES: str
    SIGNED_OID: str
    SIGNED_TID: str
    SIGNED_KEY_START: str
    SIGNED_KEY_EXPIRY: str
    SIGNED_KEY_SERVICE: str
    SIGNED_KEY_VERSION: str
    SIGNED_ENCRYPTION_SCOPE: str
    SIGNED_AUTHORIZED_OID: str
    SIGNED_UNAUTHORIZED_OID: str
    SIGNED_CORRELATION_ID: str
    SIGNED_DIRECTORY_DEPTH: str
    @staticmethod
    def to_list(): ...

class SharedAccessSignature:
    """
    Provides a factory for creating account access
    signature tokens with an account name and account key. Users can either
    use the factory or can construct the appropriate service and use the
    generate_*_shared_access_signature method directly.
    """
    account_name: Incomplete
    account_key: Incomplete
    x_ms_version: Incomplete
    def __init__(self, account_name, account_key, x_ms_version=...) -> None:
        """
        :param str account_name:
            The storage account name used to generate the shared access signatures.
        :param str account_key:
            The access key to generate the shares access signatures.
        :param str x_ms_version:
            The service version used to generate the shared access signatures.
        """
    def generate_account(self, services, resource_types, permission, expiry, start: Incomplete | None = None, ip: Incomplete | None = None, protocol: Incomplete | None = None, **kwargs):
        """
        Generates a shared access signature for the account.
        Use the returned signature with the sas_token parameter of the service
        or to create a new account object.

        :param Any services: The specified services associated with the shared access signature.
        :param ResourceTypes resource_types:
            Specifies the resource types that are accessible with the account
            SAS. You can combine values to provide access to more than one
            resource type.
        :param AccountSasPermissions permission:
            The permissions associated with the shared access signature. The
            user is restricted to operations allowed by the permissions.
            Required unless an id is given referencing a stored access policy
            which contains this field. This field must be omitted if it has been
            specified in an associated stored access policy. You can combine
            values to provide more than one permission.
        :param expiry:
            The time at which the shared access signature becomes invalid.
            Required unless an id is given referencing a stored access policy
            which contains this field. This field must be omitted if it has
            been specified in an associated stored access policy. Azure will always
            convert values to UTC. If a date is passed in without timezone info, it
            is assumed to be UTC.
        :type expiry: datetime or str
        :param start:
            The time at which the shared access signature becomes valid. If
            omitted, start time for this call is assumed to be the time when the
            storage service receives the request. Azure will always convert values
            to UTC. If a date is passed in without timezone info, it is assumed to
            be UTC.
        :type start: datetime or str
        :param str ip:
            Specifies an IP address or a range of IP addresses from which to accept requests.
            If the IP address from which the request originates does not match the IP address
            or address range specified on the SAS token, the request is not authenticated.
            For example, specifying sip=168.1.5.65 or sip=168.1.5.60-168.1.5.70 on the SAS
            restricts the request to those IP addresses.
        :param str protocol:
            Specifies the protocol permitted for a request made. The default value
            is https,http. See :class:`~azure.storage.common.models.Protocol` for possible values.
        :keyword str encryption_scope:
            Optional. If specified, this is the encryption scope to use when sending requests
            authorized with this SAS URI.
        :returns: The generated SAS token for the account.
        :rtype: str
        """

class _SharedAccessHelper:
    query_dict: Incomplete
    def __init__(self) -> None: ...
    def add_encryption_scope(self, **kwargs) -> None: ...
    def add_base(self, permission, expiry, start, ip, protocol, x_ms_version) -> None: ...
    def add_resource(self, resource) -> None: ...
    def add_id(self, policy_id) -> None: ...
    def add_account(self, services, resource_types) -> None: ...
    def add_override_response_headers(self, cache_control, content_disposition, content_encoding, content_language, content_type) -> None: ...
    def add_account_signature(self, account_name, account_key): ...
    def get_token(self): ...
