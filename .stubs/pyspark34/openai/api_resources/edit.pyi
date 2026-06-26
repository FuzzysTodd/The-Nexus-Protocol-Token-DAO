from openai import error as error, util as util
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource as EngineAPIResource
from openai.error import TryAgain as TryAgain

class Edit(EngineAPIResource):
    OBJECT_NAME: str
    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new edit for the provided input, instruction, and parameters.
        """
    @classmethod
    async def acreate(cls, *args, **kwargs):
        """
        Creates a new edit for the provided input, instruction, and parameters.
        """
