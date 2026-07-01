from ..base_models import RequestModel as RequestModel, ResponseModel as ResponseModel
from ..config import RouteType as RouteType
from _typeshed import Incomplete
from typing import List

class RequestPayload(RequestModel):
    text: str | List[str]
    class Config:
        schema_extra: Incomplete

class Metadata(ResponseModel):
    input_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None
    model: str
    route_type: RouteType

class ResponsePayload(ResponseModel):
    embeddings: List[List[float]]
    metadata: Metadata
    class Config:
        schema_extra: Incomplete
