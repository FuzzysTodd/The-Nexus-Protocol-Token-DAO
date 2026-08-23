from .exceptions import FileNotFoundError as FileNotFoundError
from .utils import CountUpDownLatch as CountUpDownLatch
from _typeshed import Incomplete

WORKER_THREAD_PER_PROCESS: int
QUEUE_BUCKET_SIZE: int
END_QUEUE_SENTINEL: Incomplete
GLOBAL_EXCEPTION: Incomplete
GLOBAL_EXCEPTION_LOCK: Incomplete

def monitor_exception(exception_queue, process_ids) -> None: ...
def log_listener_process(queue) -> None: ...
def multi_processor_change_acl(adl, path: Incomplete | None = None, method_name: str = '', acl_spec: str = '', number_of_sub_process: Incomplete | None = None): ...
def processor(adl, file_path_queue, finish_queue_processing_flag, method_name, acl_spec, log_queue, exception_queue) -> None: ...
