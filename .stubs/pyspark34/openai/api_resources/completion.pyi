from openai import util as util
from openai.api_resources.abstract import DeletableAPIResource as DeletableAPIResource, ListableAPIResource as ListableAPIResource
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource as EngineAPIResource
from openai.error import TryAgain as TryAgain

class Completion(EngineAPIResource):
    OBJECT_NAME: str
    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new completion for the provided prompt and parameters.

        See https://platform.openai.com/docs/api-reference/completions/create for a list
        of valid parameters.
        """
    @classmethod
    async def acreate(cls, *args, **kwargs):
        """
        Creates a new completion for the provided prompt and parameters.

        See https://platform.openai.com/docs/api-reference/completions/create for a list
        of valid parameters.
        """
