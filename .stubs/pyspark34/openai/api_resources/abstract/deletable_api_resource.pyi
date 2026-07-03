from _typeshed import Incomplete
from openai import error as error
from openai.api_resources.abstract.api_resource import APIResource as APIResource
from openai.util import ApiType as ApiType
from typing import Awaitable

class DeletableAPIResource(APIResource):
    @classmethod
    def delete(cls, sid, api_type: Incomplete | None = None, api_version: Incomplete | None = None, **params): ...
    @classmethod
    def adelete(cls, sid, api_type: Incomplete | None = None, api_version: Incomplete | None = None, **params) -> Awaitable: ...
