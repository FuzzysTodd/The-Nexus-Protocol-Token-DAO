from openai import util as util
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource as EngineAPIResource
from openai.datalib.numpy_helper import assert_has_numpy as assert_has_numpy
from openai.error import TryAgain as TryAgain

class Embedding(EngineAPIResource):
    OBJECT_NAME: str
    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new embedding for the provided input and parameters.

        See https://platform.openai.com/docs/api-reference/embeddings for a list
        of valid parameters.
        """
    @classmethod
    async def acreate(cls, *args, **kwargs):
        """
        Creates a new embedding for the provided input and parameters.

        See https://platform.openai.com/docs/api-reference/embeddings for a list
        of valid parameters.
        """
