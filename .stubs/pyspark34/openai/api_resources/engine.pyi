from _typeshed import Incomplete
from openai import util as util
from openai.api_resources.abstract import ListableAPIResource as ListableAPIResource, UpdateableAPIResource as UpdateableAPIResource
from openai.error import TryAgain as TryAgain

class Engine(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME: str
    def generate(self, timeout: Incomplete | None = None, **params): ...
    async def agenerate(self, timeout: Incomplete | None = None, **params): ...
    def embeddings(self, **params): ...
