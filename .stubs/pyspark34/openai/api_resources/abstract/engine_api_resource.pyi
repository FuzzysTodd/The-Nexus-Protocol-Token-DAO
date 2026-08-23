from _typeshed import Incomplete
from openai import api_requestor as api_requestor, error as error, util as util
from openai.api_resources.abstract.api_resource import APIResource as APIResource
from openai.openai_response import OpenAIResponse as OpenAIResponse
from openai.util import ApiType as ApiType
from pydoc import apropos as apropos

MAX_TIMEOUT: int

class EngineAPIResource(APIResource):
    plain_old_data: bool
    def __init__(self, engine: str | None = None, **kwargs) -> None: ...
    @classmethod
    def class_url(cls, engine: str | None = None, api_type: str | None = None, api_version: str | None = None): ...
    @classmethod
    def create(cls, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, **params): ...
    @classmethod
    async def acreate(cls, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, **params): ...
    def instance_url(self): ...
    timeout: Incomplete
    def wait(self, timeout: Incomplete | None = None): ...
    async def await_(self, timeout: Incomplete | None = None):
        """Async version of `EngineApiResource.wait`"""
