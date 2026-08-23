from _typeshed import Incomplete

SUPPORTED_VERSIONS: Incomplete

class AuthenticationRecord:
    """Non-secret account information for an authenticated user

    This class enables :class:`DeviceCodeCredential` and :class:`InteractiveBrowserCredential` to access
    previously cached authentication data. Applications shouldn't construct instances of this class. They should
    instead acquire one from a credential's **authenticate** method, such as
    :func:`InteractiveBrowserCredential.authenticate`. See the user_authentication sample for more details.

    :param str tenant_id: The tenant the account should authenticate in.
    :param str client_id: The client ID of the application which performed the original authentication.
    :param str authority: The authority host used to authenticate the account.
    :param str home_account_id: A unique identifier of the account.
    :param str username: The user principal or service principal name of the account.
    """
    def __init__(self, tenant_id: str, client_id: str, authority: str, home_account_id: str, username: str) -> None: ...
    @property
    def authority(self) -> str:
        """The authority host used to authenticate the account.

        :rtype: str
        """
    @property
    def client_id(self) -> str:
        """The client ID of the application which performed the original authentication.

        :rtype: str
        """
    @property
    def home_account_id(self) -> str:
        """A unique identifier of the account.

        :rtype: str
        """
    @property
    def tenant_id(self) -> str:
        """The tenant the account should authenticate in.

        :rtype: str
        """
    @property
    def username(self) -> str:
        """The user principal or service principal name of the account.

        :rtype: str
        """
    @classmethod
    def deserialize(cls, data: str) -> AuthenticationRecord:
        """Deserialize a record.

        :param str data: A serialized record.
        :return: The deserialized record.
        :rtype: ~azure.identity.AuthenticationRecord
        """
    def serialize(self) -> str:
        """Serialize the record.

        :return: The serialized record.
        :rtype: str
        """
