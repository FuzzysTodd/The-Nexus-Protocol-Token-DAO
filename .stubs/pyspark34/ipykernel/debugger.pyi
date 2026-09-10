from .compiler import get_file_name as get_file_name, get_tmp_directory as get_tmp_directory, get_tmp_hash_seed as get_tmp_hash_seed
from _typeshed import Incomplete
from debugpy.server import api as api

ROUTING_ID: Incomplete

class _FakeCode:
    """Fake code class."""
    co_filename: Incomplete
    co_name: Incomplete
    def __init__(self, co_filename, co_name) -> None:
        """Init."""

class _FakeFrame:
    """Fake frame class."""
    f_code: Incomplete
    f_globals: Incomplete
    f_locals: Incomplete
    f_back: Incomplete
    def __init__(self, f_code, f_globals, f_locals) -> None:
        """Init."""

class _DummyPyDB:
    """Fake PyDb class."""
    variable_presentation: Incomplete
    def __init__(self) -> None:
        """Init."""

class VariableExplorer:
    """A variable explorer."""
    suspended_frame_manager: Incomplete
    py_db: Incomplete
    tracker: Incomplete
    frame: Incomplete
    def __init__(self) -> None:
        """Initialize the explorer."""
    def track(self) -> None:
        """Start tracking."""
    def untrack_all(self) -> None:
        """Stop tracking."""
    def get_children_variables(self, variable_ref: Incomplete | None = None):
        """Get the child variables for a variable reference."""

class DebugpyMessageQueue:
    """A debugpy message queue."""
    HEADER: str
    HEADER_LENGTH: int
    SEPARATOR: str
    SEPARATOR_LENGTH: int
    tcp_buffer: str
    event_callback: Incomplete
    message_queue: Incomplete
    log: Incomplete
    def __init__(self, event_callback, log) -> None:
        """Init the queue."""
    header_pos: Incomplete
    separator_pos: Incomplete
    message_pos: Incomplete
    message_size: Incomplete
    def put_tcp_frame(self, frame) -> None:
        """Put a tcp frame in the queue."""
    async def get_message(self):
        """Get a message from the queue."""

class DebugpyClient:
    """A client for debugpy."""
    log: Incomplete
    debugpy_stream: Incomplete
    event_callback: Incomplete
    message_queue: Incomplete
    debugpy_host: str
    debugpy_port: int
    routing_id: Incomplete
    wait_for_attach: bool
    init_event: Incomplete
    init_event_seq: int
    def __init__(self, log, debugpy_stream, event_callback) -> None:
        """Initialize the client."""
    endpoint: Incomplete
    def get_host_port(self):
        """Get the host debugpy port."""
    def connect_tcp_socket(self) -> None:
        """Connect to the tcp socket."""
    def disconnect_tcp_socket(self) -> None:
        """Disconnect from the tcp socket."""
    def receive_dap_frame(self, frame) -> None:
        """Receive a dap frame."""
    async def send_dap_request(self, msg):
        """Send a dap request."""

class Debugger:
    """The debugger class."""
    started_debug_msg_types: Incomplete
    static_debug_msg_types: Incomplete
    log: Incomplete
    debugpy_client: Incomplete
    shell_socket: Incomplete
    session: Incomplete
    is_started: bool
    event_callback: Incomplete
    just_my_code: Incomplete
    stopped_queue: Incomplete
    started_debug_handlers: Incomplete
    static_debug_handlers: Incomplete
    breakpoint_list: Incomplete
    stopped_threads: Incomplete
    debugpy_initialized: bool
    debugpy_host: str
    debugpy_port: int
    endpoint: Incomplete
    variable_explorer: Incomplete
    def __init__(self, log, debugpy_stream, event_callback, shell_socket, session, just_my_code: bool = True) -> None:
        """Initialize the debugger."""
    async def handle_stopped_event(self) -> None:
        """Handle a stopped event."""
    @property
    def tcp_client(self): ...
    def start(self):
        """Start the debugger."""
    def stop(self) -> None:
        """Stop the debugger."""
    async def dumpCell(self, message):
        """Handle a dump cell message."""
    async def setBreakpoints(self, message):
        """Handle a set breakpoints message."""
    async def source(self, message):
        """Handle a source message."""
    async def stackTrace(self, message):
        """Handle a stack trace message."""
    def accept_variable(self, variable_name):
        """Accept a variable by name."""
    async def variables(self, message):
        """Handle a variables message."""
    async def attach(self, message):
        """Handle an attach message."""
    async def configurationDone(self, message):
        """Handle a configuration done message."""
    async def debugInfo(self, message):
        """Handle a debug info message."""
    async def inspectVariables(self, message):
        """Handle an insepct variables message."""
    async def richInspectVariables(self, message):
        """Handle a rich inspect variables message."""
    async def copyToGlobals(self, message): ...
    async def modules(self, message):
        """Handle a modules message."""
    async def process_request(self, message):
        """Process a request."""
