from openai.api_resources.abstract import CreateableAPIResource as CreateableAPIResource, DeletableAPIResource as DeletableAPIResource, ListableAPIResource as ListableAPIResource

class CompletionConfig(CreateableAPIResource, ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME: str
