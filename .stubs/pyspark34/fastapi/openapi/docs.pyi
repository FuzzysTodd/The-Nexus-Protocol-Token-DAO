from _typeshed import Incomplete
from fastapi.encoders import jsonable_encoder as jsonable_encoder
from starlette.responses import HTMLResponse
from typing import Any, Dict

swagger_ui_default_parameters: Incomplete

def get_swagger_ui_html(*, openapi_url: str, title: str, swagger_js_url: str = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js', swagger_css_url: str = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css', swagger_favicon_url: str = 'https://fastapi.tiangolo.com/img/favicon.png', oauth2_redirect_url: str | None = None, init_oauth: Dict[str, Any] | None = None, swagger_ui_parameters: Dict[str, Any] | None = None) -> HTMLResponse: ...
def get_redoc_html(*, openapi_url: str, title: str, redoc_js_url: str = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js', redoc_favicon_url: str = 'https://fastapi.tiangolo.com/img/favicon.png', with_google_fonts: bool = True) -> HTMLResponse: ...
def get_swagger_ui_oauth2_redirect_html() -> HTMLResponse: ...
