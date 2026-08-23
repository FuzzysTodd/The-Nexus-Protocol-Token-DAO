from pydantic import BaseModel, Extra

class RequestModel(BaseModel, extra=Extra.allow):
    """
    A pydantic model representing Gateway request data, such as a chat or completions request
    """
class ResponseModel(BaseModel, extra=Extra.ignore):
    """
    A pydantic model representing Gateway response data, such as information about a Gateway
    Route returned in response to a GetRoute request
    """
class ConfigModel(BaseModel, extra=Extra.ignore):
    """
    A pydantic model representing Gateway configuration data, such as an OpenAI completions
    route definition including route name, model name, API keys, etc.
    """
