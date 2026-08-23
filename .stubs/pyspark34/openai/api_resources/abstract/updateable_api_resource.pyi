from openai.api_resources.abstract.api_resource import APIResource as APIResource
from typing import Awaitable

class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls, sid, **params): ...
    @classmethod
    def amodify(cls, sid, **params) -> Awaitable: ...
