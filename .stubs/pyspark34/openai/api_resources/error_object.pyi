from _typeshed import Incomplete
from openai.openai_object import OpenAIObject as OpenAIObject
from openai.util import merge_dicts as merge_dicts

class ErrorObject(OpenAIObject):
    def refresh_from(self, values, api_key: Incomplete | None = None, api_version: Incomplete | None = None, api_type: Incomplete | None = None, organization: Incomplete | None = None, response_ms: int | None = None): ...
