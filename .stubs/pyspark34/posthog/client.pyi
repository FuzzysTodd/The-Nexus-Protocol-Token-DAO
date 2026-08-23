from _typeshed import Incomplete
from posthog.consumer import Consumer as Consumer
from posthog.feature_flags import InconclusiveMatchError as InconclusiveMatchError, match_feature_flag_properties as match_feature_flag_properties
from posthog.poller import Poller as Poller
from posthog.request import APIError as APIError, batch_post as batch_post, decide as decide, get as get
from posthog.utils import SizeLimitedDict as SizeLimitedDict, clean as clean, guess_timezone as guess_timezone
from posthog.version import VERSION as VERSION

ID_TYPES: Incomplete
MAX_DICT_SIZE: int

class Client:
    """Create a new PostHog client."""
    log: Incomplete
    queue: Incomplete
    api_key: Incomplete
    on_error: Incomplete
    debug: Incomplete
    send: Incomplete
    sync_mode: Incomplete
    host: Incomplete
    gzip: Incomplete
    timeout: Incomplete
    feature_flags: Incomplete
    feature_flags_by_key: Incomplete
    group_type_mapping: Incomplete
    cohorts: Incomplete
    poll_interval: Incomplete
    poller: Incomplete
    distinct_ids_feature_flags_reported: Incomplete
    disabled: Incomplete
    disable_geoip: Incomplete
    personal_api_key: Incomplete
    consumers: Incomplete
    def __init__(self, api_key: Incomplete | None = None, host: Incomplete | None = None, debug: bool = False, max_queue_size: int = 10000, send: bool = True, on_error: Incomplete | None = None, flush_at: int = 100, flush_interval: float = 0.5, gzip: bool = False, max_retries: int = 3, sync_mode: bool = False, timeout: int = 15, thread: int = 1, poll_interval: int = 30, personal_api_key: Incomplete | None = None, project_api_key: Incomplete | None = None, disabled: bool = False, disable_geoip: bool = True) -> None: ...
    def identify(self, distinct_id: Incomplete | None = None, properties: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def get_feature_variants(self, distinct_id, groups: Incomplete | None = None, person_properties: Incomplete | None = None, group_properties: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def get_feature_payloads(self, distinct_id, groups: Incomplete | None = None, person_properties: Incomplete | None = None, group_properties: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def get_decide(self, distinct_id, groups: Incomplete | None = None, person_properties: Incomplete | None = None, group_properties: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def capture(self, distinct_id: Incomplete | None = None, event: Incomplete | None = None, properties: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, groups: Incomplete | None = None, send_feature_flags: bool = False, disable_geoip: Incomplete | None = None): ...
    def set(self, distinct_id: Incomplete | None = None, properties: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def set_once(self, distinct_id: Incomplete | None = None, properties: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def group_identify(self, group_type: Incomplete | None = None, group_key: Incomplete | None = None, properties: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def alias(self, previous_id: Incomplete | None = None, distinct_id: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def page(self, distinct_id: Incomplete | None = None, url: Incomplete | None = None, properties: Incomplete | None = None, context: Incomplete | None = None, timestamp: Incomplete | None = None, uuid: Incomplete | None = None, disable_geoip: Incomplete | None = None): ...
    def flush(self) -> None:
        """Forces a flush from the internal queue to the server"""
    def join(self) -> None:
        """Ends the consumer thread once the queue is empty.
        Blocks execution until finished
        """
    def shutdown(self) -> None:
        """Flush all messages and cleanly shutdown the client"""
    def load_feature_flags(self) -> None: ...
    def feature_enabled(self, key, distinct_id, *, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, send_feature_flag_events: bool = True, disable_geoip: Incomplete | None = None): ...
    def get_feature_flag(self, key, distinct_id, *, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, send_feature_flag_events: bool = True, disable_geoip: Incomplete | None = None): ...
    def get_feature_flag_payload(self, key, distinct_id, *, match_value: Incomplete | None = None, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, send_feature_flag_events: bool = True, disable_geoip: Incomplete | None = None): ...
    def get_all_flags(self, distinct_id, *, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, disable_geoip: Incomplete | None = None): ...
    def get_all_flags_and_payloads(self, distinct_id, *, groups={}, person_properties={}, group_properties={}, only_evaluate_locally: bool = False, disable_geoip: Incomplete | None = None): ...
    def feature_flag_definitions(self): ...

def require(name, field, data_type) -> None:
    """Require that the named `field` has the right `data_type`"""
def stringify_id(val): ...
