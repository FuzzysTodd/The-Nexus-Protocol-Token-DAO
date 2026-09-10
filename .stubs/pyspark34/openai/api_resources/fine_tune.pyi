from _typeshed import Incomplete
from openai import api_requestor as api_requestor, error as error, util as util
from openai.api_resources.abstract import CreateableAPIResource as CreateableAPIResource, ListableAPIResource as ListableAPIResource, nested_resource_class_methods as nested_resource_class_methods
from openai.api_resources.abstract.deletable_api_resource import DeletableAPIResource as DeletableAPIResource
from openai.openai_response import OpenAIResponse as OpenAIResponse
from openai.util import ApiType as ApiType

class FineTune(ListableAPIResource, CreateableAPIResource, DeletableAPIResource):
    OBJECT_NAME: str
    @classmethod
    def cancel(cls, id, api_key: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, **params): ...
    @classmethod
    def acancel(cls, id, api_key: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, **params): ...
    @classmethod
    def stream_events(cls, id, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, **params): ...
    @classmethod
    async def astream_events(cls, id, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, **params): ...
