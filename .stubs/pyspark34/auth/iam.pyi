from google.auth import crypt

class Signer(crypt.Signer):
    """Signs messages using the IAM `signBlob API`_.

    This is useful when you need to sign bytes but do not have access to the
    credential's private key file.

    .. _signBlob API:
        https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts
        /signBlob
    """
    def __init__(self, request, credentials, service_account_email) -> None:
        """
        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.
            credentials (google.auth.credentials.Credentials): The credentials
                that will be used to authenticate the request to the IAM API.
                The credentials must have of one the following scopes:

                - https://www.googleapis.com/auth/iam
                - https://www.googleapis.com/auth/cloud-platform
            service_account_email (str): The service account email identifying
                which service account to use to sign bytes. Often, this can
                be the same as the service account email in the given
                credentials.
        """
    @property
    def key_id(self) -> None:
        """Optional[str]: The key ID used to identify this private key.

        .. warning::
           This is always ``None``. The key ID used by IAM can not
           be reliably determined ahead of time.
        """
    def sign(self, message): ...
