from sentry_sdk import Hub as Hub, serializer as serializer
from sentry_sdk._types import Event as Event, Hint as Hint, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.scope import add_global_event_processor as add_global_event_processor
from sentry_sdk.utils import iter_stacks as iter_stacks, walk_exception_chain as walk_exception_chain
from types import FrameType
from typing import Any, Dict

class PureEvalIntegration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def pure_eval_frame(frame: FrameType) -> Dict[str, Any]: ...
