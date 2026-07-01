from ..base_models import ResponseModel as ResponseModel
from ..config import RouteType as RouteType
from .chat import BaseRequestPayload as BaseRequestPayload, FinishReason as FinishReason
from _typeshed import Incomplete
from typing import Dict, List

class RequestPayload(BaseRequestPayload):
    prompt: str
    class Config:
        schema_extra: Incomplete

class CandidateMetadata(ResponseModel):
    finish_reason: FinishReason | None

class Candidate(ResponseModel):
    text: str
    metadata: Dict[str, str] | None

class Metadata(ResponseModel):
    input_tokens: int | None
    output_tokens: int | None
    total_tokens: int | None
    model: str
    route_type: RouteType

class ResponsePayload(ResponseModel):
    candidates: List[Candidate]
    metadata: Metadata
    class Config:
        schema_extra: Incomplete
