from openai import util as util
from openai.api_resources.abstract import CreateableAPIResource as CreateableAPIResource, DeletableAPIResource as DeletableAPIResource, ListableAPIResource as ListableAPIResource
from openai.error import APIError as APIError, InvalidRequestError as InvalidRequestError

class Deployment(CreateableAPIResource, ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME: str
    @classmethod
    def create(cls, *args, **kwargs):
        """
        Creates a new deployment for the provided prompt and parameters.
        """
    @classmethod
    def acreate(cls, *args, **kwargs):
        """
        Creates a new deployment for the provided prompt and parameters.
        """
    @classmethod
    def list(cls, *args, **kwargs): ...
    @classmethod
    def alist(cls, *args, **kwargs): ...
    @classmethod
    def delete(cls, *args, **kwargs): ...
    @classmethod
    def adelete(cls, *args, **kwargs): ...
    @classmethod
    def retrieve(cls, *args, **kwargs): ...
    @classmethod
    def aretrieve(cls, *args, **kwargs): ...
