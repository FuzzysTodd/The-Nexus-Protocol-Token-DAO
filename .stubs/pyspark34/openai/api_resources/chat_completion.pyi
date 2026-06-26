from openai import util as util
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource as EngineAPIResource
from openai.error import TryAgain as TryAgain

class ChatCompletion(EngineAPIResource):
    engine_required: bool
    OBJECT_NAME: str
    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://platform.openai.com/docs/api-reference/chat-completions/create
        for a list of valid parameters.
        """
    @classmethod
    async def acreate(cls, *args, **kwargs):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://platform.openai.com/docs/api-reference/chat-completions/create
        for a list of valid parameters.
        """
