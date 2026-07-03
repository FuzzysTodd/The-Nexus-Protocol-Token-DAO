from _typeshed import Incomplete
from google.auth import _credentials_async as credentials_async
from google.oauth2 import service_account

class Credentials(service_account.Credentials, credentials_async.Scoped, credentials_async.Credentials):
    """Service account credentials

    Usually, you'll create these credentials with one of the helper
    constructors. To create credentials using a Google service account
    private key JSON file::

        credentials = _service_account_async.Credentials.from_service_account_file(
            'service-account.json')

    Or if you already have the service account file loaded::

        service_account_info = json.load(open('service_account.json'))
        credentials = _service_account_async.Credentials.from_service_account_info(
            service_account_info)

    Both helper methods pass on arguments to the constructor, so you can
    specify additional scopes and a subject if necessary::

        credentials = _service_account_async.Credentials.from_service_account_file(
            'service-account.json',
            scopes=['email'],
            subject='user@example.com')

    The credentials are considered immutable. If you want to modify the scopes
    or the subject used for delegation, use :meth:`with_scopes` or
    :meth:`with_subject`::

        scoped_credentials = credentials.with_scopes(['email'])
        delegated_credentials = credentials.with_subject(subject)

    To add a quota project, use :meth:`with_quota_project`::

        credentials = credentials.with_quota_project('myproject-123')
    """
    token: Incomplete
    expiry: Incomplete
    async def refresh(self, request) -> None: ...

class IDTokenCredentials(service_account.IDTokenCredentials, credentials_async.Signing, credentials_async.Credentials):
    """Open ID Connect ID Token-based service account credentials.

    These credentials are largely similar to :class:`.Credentials`, but instead
    of using an OAuth 2.0 Access Token as the bearer token, they use an Open
    ID Connect ID Token as the bearer token. These credentials are useful when
    communicating to services that require ID Tokens and can not accept access
    tokens.

    Usually, you'll create these credentials with one of the helper
    constructors. To create credentials using a Google service account
    private key JSON file::

        credentials = (
            _service_account_async.IDTokenCredentials.from_service_account_file(
                'service-account.json'))

    Or if you already have the service account file loaded::

        service_account_info = json.load(open('service_account.json'))
        credentials = (
            _service_account_async.IDTokenCredentials.from_service_account_info(
                service_account_info))

    Both helper methods pass on arguments to the constructor, so you can
    specify additional scopes and a subject if necessary::

        credentials = (
            _service_account_async.IDTokenCredentials.from_service_account_file(
                'service-account.json',
                scopes=['email'],
                subject='user@example.com'))

    The credentials are considered immutable. If you want to modify the scopes
    or the subject used for delegation, use :meth:`with_scopes` or
    :meth:`with_subject`::

        scoped_credentials = credentials.with_scopes(['email'])
        delegated_credentials = credentials.with_subject(subject)

    """
    token: Incomplete
    expiry: Incomplete
    async def refresh(self, request) -> None: ...
