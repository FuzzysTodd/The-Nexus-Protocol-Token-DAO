from openai.openai_object import OpenAIObject as OpenAIObject
from typing import List

class Moderation(OpenAIObject):
    VALID_MODEL_NAMES: List[str]
    @classmethod
    def get_url(cls): ...
    @classmethod
    def create(cls, input: str | List[str], model: str | None = None, api_key: str | None = None): ...
    @classmethod
    def acreate(cls, input: str | List[str], model: str | None = None, api_key: str | None = None): ...
