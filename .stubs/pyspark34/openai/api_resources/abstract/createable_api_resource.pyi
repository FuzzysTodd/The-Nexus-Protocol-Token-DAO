from _typeshed import Incomplete
from openai import api_requestor as api_requestor, error as error, util as util
from openai.api_resources.abstract.api_resource import APIResource as APIResource
from openai.util import ApiType as ApiType

class CreateableAPIResource(APIResource):
    plain_old_data: bool
    @classmethod
    def create(cls, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, **params): ...
    @classmethod
    async def acreate(cls, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, request_id: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, **params): ...
