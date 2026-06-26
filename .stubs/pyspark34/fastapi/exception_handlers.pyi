from fastapi.encoders import jsonable_encoder as jsonable_encoder
from fastapi.exceptions import RequestValidationError as RequestValidationError, WebSocketRequestValidationError as WebSocketRequestValidationError
from fastapi.utils import is_body_allowed_for_status_code as is_body_allowed_for_status_code
from fastapi.websockets import WebSocket as WebSocket
from starlette.exceptions import HTTPException as HTTPException
from starlette.requests import Request as Request
from starlette.responses import JSONResponse, Response

async def http_exception_handler(request: Request, exc: HTTPException) -> Response: ...
async def request_validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse: ...
async def websocket_request_validation_exception_handler(websocket: WebSocket, exc: WebSocketRequestValidationError) -> None: ...
