from ..base_models import RequestModel as RequestModel, ResponseModel as ResponseModel
from ..config import RouteType as RouteType
from _typeshed import Incomplete
from enum import Enum
from pydantic import Extra
from typing import List

class RequestMessage(RequestModel):
    role: str
    content: str

class BaseRequestPayload(RequestModel):
    temperature: float
    candidate_count: int
    stop: List[str] | None
    max_tokens: int | None

class RequestPayload(BaseRequestPayload):
    messages: List[RequestMessage]
    class Config:
        schema_extra: Incomplete

class FinishReason(str, Enum):
    STOP: str
    LENGTH: str

class ResponseMessage(ResponseModel):
    role: str
    content: str

class CandidateMetadata(ResponseModel, extra=Extra.allow):
    finish_reason: FinishReason | None

class Candidate(ResponseModel):
    message: ResponseMessage
    metadata: CandidateMetadata

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
