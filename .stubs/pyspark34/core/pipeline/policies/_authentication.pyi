from . import HTTPPolicy as HTTPPolicy, SansIOHTTPPolicy as SansIOHTTPPolicy
from ...exceptions import ServiceRequestError as ServiceRequestError
from azure.core.credentials import AccessToken as AccessToken, AzureKeyCredential as AzureKeyCredential, AzureSasCredential as AzureSasCredential, TokenCredential as TokenCredential
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.transport import HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from azure.core.rest import HttpRequest, HttpResponse
from typing import Any, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType', HttpResponse, LegacyHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)

class _BearerTokenCredentialPolicyBase:
    """Base class for a Bearer Token Credential Policy.

    :param credential: The credential.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str scopes: Lets you specify the type of access needed.
    :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) on all requested
        tokens. Defaults to False.
    """
    def __init__(self, credential: TokenCredential, *scopes: str, **kwargs: Any) -> None: ...

class BearerTokenCredentialPolicy(_BearerTokenCredentialPolicyBase, HTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Adds a bearer token Authorization header to requests.

    :param credential: The credential.
    :type credential: ~azure.core.TokenCredential
    :param str scopes: Lets you specify the type of access needed.
    :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) on all requested
        tokens. Defaults to False.
    :raises: :class:`~azure.core.exceptions.ServiceRequestError`
    """
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Called before the policy sends a request.

        The base implementation authorizes the request with a bearer token.

        :param ~azure.core.pipeline.PipelineRequest request: the request
        """
    def authorize_request(self, request: PipelineRequest[HTTPRequestType], *scopes: str, **kwargs: Any) -> None:
        """Acquire a token from the credential and authorize the request with it.

        Keyword arguments are passed to the credential's get_token method. The token will be cached and used to
        authorize future requests.

        :param ~azure.core.pipeline.PipelineRequest request: the request
        :param str scopes: required scopes of authentication
        """
    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Authorize request with a bearer token and send it to the next policy

        :param request: The pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The pipeline response object
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
    def on_challenge(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> bool:
        """Authorize request according to an authentication challenge

        This method is called when the resource provider responds 401 with a WWW-Authenticate header.

        :param ~azure.core.pipeline.PipelineRequest request: the request which elicited an authentication challenge
        :param ~azure.core.pipeline.PipelineResponse response: the resource provider's response
        :returns: a bool indicating whether the policy should send the request
        :rtype: bool
        """
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None:
        """Executed after the request comes back from the next policy.

        :param request: Request to be modified after returning from the policy.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: Pipeline response object
        :type response: ~azure.core.pipeline.PipelineResponse
        """
    def on_exception(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Executed when an exception is raised while executing the next policy.

        This method is executed inside the exception handler.

        :param request: The Pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        """

class AzureKeyCredentialPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Adds a key header for the provided credential.

    :param credential: The credential used to authenticate requests.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :param str name: The name of the key header used for the credential.
    :keyword str prefix: The name of the prefix for the header value if any.
    :raises: ValueError or TypeError
    """
    def __init__(self, credential: AzureKeyCredential, name: str, *, prefix: str | None = None, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None: ...

class AzureSasCredentialPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Adds a shared access signature to query for the provided credential.

    :param credential: The credential used to authenticate requests.
    :type credential: ~azure.core.credentials.AzureSasCredential
    :raises: ValueError or TypeError
    """
    def __init__(self, credential: AzureSasCredential, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None: ...
