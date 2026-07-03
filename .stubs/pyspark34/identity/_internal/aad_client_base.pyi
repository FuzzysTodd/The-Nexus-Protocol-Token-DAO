import abc
from .aadclient_certificate import AadClientCertificate as AadClientCertificate
from .utils import get_default_authority as get_default_authority, normalize_authority as normalize_authority, resolve_tenant as resolve_tenant
from _typeshed import Incomplete
from azure.core.credentials import AccessToken
from azure.core.pipeline import AsyncPipeline, Pipeline, PipelineResponse as PipelineResponse
from azure.core.pipeline.policies import AsyncHTTPPolicy, HTTPPolicy, SansIOHTTPPolicy
from azure.core.pipeline.transport import AsyncHttpTransport, HttpTransport
from msal import TokenCache
from typing import Any, Dict, Iterable, List

PipelineType = AsyncPipeline | Pipeline
PolicyType = AsyncHTTPPolicy | HTTPPolicy | SansIOHTTPPolicy
TransportType = AsyncHttpTransport | HttpTransport
JWT_BEARER_ASSERTION: str

class AadClientBase(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self, tenant_id: str, client_id: str, authority: str | None = None, cache: TokenCache | None = None, cae_cache: TokenCache | None = None, *, additionally_allowed_tenants: List[str] | None = None, **kwargs: Any) -> None: ...
    def get_cached_access_token(self, scopes: Iterable[str], **kwargs: Any) -> AccessToken | None: ...
    def get_cached_refresh_tokens(self, scopes: Iterable[str], **kwargs) -> List[Dict]: ...
    @abc.abstractmethod
    def obtain_token_by_authorization_code(self, scopes, code, redirect_uri, client_secret: Incomplete | None = None, **kwargs): ...
    @abc.abstractmethod
    def obtain_token_by_jwt_assertion(self, scopes, assertion, **kwargs): ...
    @abc.abstractmethod
    def obtain_token_by_client_certificate(self, scopes, certificate, **kwargs): ...
    @abc.abstractmethod
    def obtain_token_by_client_secret(self, scopes, secret, **kwargs): ...
    @abc.abstractmethod
    def obtain_token_by_refresh_token(self, scopes, refresh_token, **kwargs): ...
    @abc.abstractmethod
    def obtain_token_on_behalf_of(self, scopes, client_credential, user_assertion, **kwargs): ...
