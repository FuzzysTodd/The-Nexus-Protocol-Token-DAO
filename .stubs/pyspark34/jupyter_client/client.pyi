import typing as t
from .channels import major_protocol_version as major_protocol_version
from .channelsabc import ChannelABC as ChannelABC, HBChannelABC as HBChannelABC
from .clientabc import KernelClientABC as KernelClientABC
from .connect import ConnectionFileMixin as ConnectionFileMixin
from .session import Session as Session
from _typeshed import Incomplete

def validate_string_dict(dct: t.Dict[str, str]) -> None:
    """Validate that the input is a dict with string keys and values.

    Raises ValueError if not."""
def reqrep(wrapped: t.Callable, meth: t.Callable, channel: str = 'shell') -> t.Callable: ...

class KernelClient(ConnectionFileMixin):
    """Communicates with a single kernel on any host via zmq channels.

    There are five channels associated with each kernel:

    * shell: for request/reply calls to the kernel.
    * iopub: for the kernel to publish results to frontends.
    * hb: for monitoring the kernel's heartbeat.
    * stdin: for frontends to reply to raw_input calls in the kernel.
    * control: for kernel management calls to the kernel.

    The messages that can be sent on these channels are exposed as methods of the
    client (KernelClient.execute, complete, history, etc.). These methods only
    send the message, they don't wait for a reply. To get results, use e.g.
    :meth:`get_shell_msg` to fetch messages from the shell channel.
    """
    context: Incomplete
    shell_channel_class: Incomplete
    iopub_channel_class: Incomplete
    stdin_channel_class: Incomplete
    hb_channel_class: Incomplete
    control_channel_class: Incomplete
    allow_stdin: bool
    def __del__(self) -> None:
        """Handle garbage collection.  Destroy context if applicable."""
    def start_channels(self, shell: bool = True, iopub: bool = True, stdin: bool = True, hb: bool = True, control: bool = True) -> None:
        """Starts the channels for this kernel.

        This will create the channels if they do not exist and then start
        them (their activity runs in a thread). If port numbers of 0 are
        being used (random ports) then you must first call
        :meth:`start_kernel`. If the channels have been stopped and you
        call this, :class:`RuntimeError` will be raised.
        """
    def stop_channels(self) -> None:
        """Stops all the running channels for this kernel.

        This stops their event loops and joins their threads.
        """
    @property
    def channels_running(self) -> bool:
        """Are any of the channels created and running?"""
    ioloop: Incomplete
    @property
    def shell_channel(self) -> t.Any:
        """Get the shell channel object for this kernel."""
    @property
    def iopub_channel(self) -> t.Any:
        """Get the iopub channel object for this kernel."""
    @property
    def stdin_channel(self) -> t.Any:
        """Get the stdin channel object for this kernel."""
    @property
    def hb_channel(self) -> t.Any:
        """Get the hb channel object for this kernel."""
    @property
    def control_channel(self) -> t.Any:
        """Get the control channel object for this kernel."""
    def execute(self, code: str, silent: bool = False, store_history: bool = True, user_expressions: t.Dict[str, t.Any] | None = None, allow_stdin: bool | None = None, stop_on_error: bool = True) -> str:
        """Execute code in the kernel.

        Parameters
        ----------
        code : str
            A string of code in the kernel's language.

        silent : bool, optional (default False)
            If set, the kernel will execute the code as quietly possible, and
            will force store_history to be False.

        store_history : bool, optional (default True)
            If set, the kernel will store command history.  This is forced
            to be False if silent is True.

        user_expressions : dict, optional
            A dict mapping names to expressions to be evaluated in the user's
            dict. The expression values are returned as strings formatted using
            :func:`repr`.

        allow_stdin : bool, optional (default self.allow_stdin)
            Flag for whether the kernel can send stdin requests to frontends.

            Some frontends (e.g. the Notebook) do not support stdin requests.
            If raw_input is called from code executed from such a frontend, a
            StdinNotImplementedError will be raised.

        stop_on_error: bool, optional (default True)
            Flag whether to abort the execution queue, if an exception is encountered.

        Returns
        -------
        The msg_id of the message sent.
        """
    def complete(self, code: str, cursor_pos: int | None = None) -> str:
        """Tab complete text in the kernel's namespace.

        Parameters
        ----------
        code : str
            The context in which completion is requested.
            Can be anything between a variable name and an entire cell.
        cursor_pos : int, optional
            The position of the cursor in the block of code where the completion was requested.
            Default: ``len(code)``

        Returns
        -------
        The msg_id of the message sent.
        """
    def inspect(self, code: str, cursor_pos: int | None = None, detail_level: int = 0) -> str:
        """Get metadata information about an object in the kernel's namespace.

        It is up to the kernel to determine the appropriate object to inspect.

        Parameters
        ----------
        code : str
            The context in which info is requested.
            Can be anything between a variable name and an entire cell.
        cursor_pos : int, optional
            The position of the cursor in the block of code where the info was requested.
            Default: ``len(code)``
        detail_level : int, optional
            The level of detail for the introspection (0-2)

        Returns
        -------
        The msg_id of the message sent.
        """
    def history(self, raw: bool = True, output: bool = False, hist_access_type: str = 'range', **kwargs: t.Any) -> str:
        """Get entries from the kernel's history list.

        Parameters
        ----------
        raw : bool
            If True, return the raw input.
        output : bool
            If True, then return the output as well.
        hist_access_type : str
            'range' (fill in session, start and stop params), 'tail' (fill in n)
             or 'search' (fill in pattern param).

        session : int
            For a range request, the session from which to get lines. Session
            numbers are positive integers; negative ones count back from the
            current session.
        start : int
            The first line number of a history range.
        stop : int
            The final (excluded) line number of a history range.

        n : int
            The number of lines of history to get for a tail request.

        pattern : str
            The glob-syntax pattern for a search request.

        Returns
        -------
        The ID of the message sent.
        """
    def kernel_info(self) -> str:
        """Request kernel info

        Returns
        -------
        The msg_id of the message sent
        """
    def comm_info(self, target_name: str | None = None) -> str:
        """Request comm info

        Returns
        -------
        The msg_id of the message sent
        """
    def is_complete(self, code: str) -> str:
        """Ask the kernel whether some code is complete and ready to execute.

        Returns
        -------
        The ID of the message sent.
        """
    def input(self, string: str) -> None:
        """Send a string of raw input to the kernel.

        This should only be called in response to the kernel sending an
        ``input_request`` message on the stdin channel.

        Returns
        -------
        The ID of the message sent.
        """
    def shutdown(self, restart: bool = False) -> str:
        """Request an immediate kernel shutdown on the control channel.

        Upon receipt of the (empty) reply, client code can safely assume that
        the kernel has shut down and it's safe to forcefully terminate it if
        it's still alive.

        The kernel will send the reply via a function registered with Python's
        atexit module, ensuring it's truly done as the kernel is done with all
        normal operation.

        Returns
        -------
        The msg_id of the message sent
        """
