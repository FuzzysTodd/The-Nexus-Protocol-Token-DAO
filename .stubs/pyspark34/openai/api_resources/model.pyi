from openai.api_resources.abstract import DeletableAPIResource as DeletableAPIResource, ListableAPIResource as ListableAPIResource

class Model(ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME: str
