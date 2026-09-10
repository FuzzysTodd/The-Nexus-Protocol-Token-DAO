from sentry_sdk import Hub as Hub
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from typing import Any, Dict

def get_template_frame_from_exception(exc_value: BaseException | None) -> Dict[str, Any] | None: ...
def patch_templates() -> None: ...
