import typing as t
from .exceptions import CellControlSignal as CellControlSignal, CellExecutionComplete as CellExecutionComplete, CellExecutionError as CellExecutionError, CellTimeoutError as CellTimeoutError, DeadKernelError as DeadKernelError
from .output_widget import OutputWidget as OutputWidget
from .util import ensure_async as ensure_async, run_hook as run_hook, run_sync as run_sync
from _typeshed import Incomplete
from jupyter_client import KernelManager
from jupyter_client.client import KernelClient as KernelClient
from nbformat import NotebookNode as NotebookNode
from traitlets.config.configurable import LoggingConfigurable

def timestamp(msg: t.Dict | None = None) -> str:
    """Get the timestamp for a message."""

class NotebookClient(LoggingConfigurable):
    """
    Encompasses a Client for executing cells in a notebook
    """
    timeout: int
    timeout_func: t.Callable[..., int | None]
    interrupt_on_timeout: bool
    error_on_timeout: t.Dict | None
    startup_timeout: int
    allow_errors: bool
    allow_error_names: t.List[str]
    force_raise_errors: bool
    skip_cells_with_tag: str
    extra_arguments: t.List
    kernel_name: str
    raise_on_iopub_timeout: bool
    store_widget_state: bool
    record_timing: bool
    iopub_timeout: int
    shell_timeout_interval: int
    shutdown_kernel: Incomplete
    ipython_hist_file: str
    kernel_manager_class: Incomplete
    on_notebook_start: t.Callable | None
    on_notebook_complete: t.Callable | None
    on_notebook_error: t.Callable | None
    on_cell_start: t.Callable | None
    on_cell_execute: t.Callable | None
    on_cell_complete: t.Callable | None
    on_cell_executed: t.Callable | None
    on_cell_error: t.Callable | None
    display_data_priority: t.List
    resources: Incomplete
    coalesce_streams: Incomplete
    nb: Incomplete
    km: Incomplete
    owns_km: Incomplete
    kc: Incomplete
    widget_registry: Incomplete
    comm_open_handlers: Incomplete
    def __init__(self, nb: NotebookNode, km: KernelManager | None = None, **kw: t.Any) -> None:
        """Initializes the execution manager.

        Parameters
        ----------
        nb : NotebookNode
            Notebook being executed.
        km : KernelManager (optional)
            Optional kernel manager. If none is provided, a kernel manager will
            be created.
        """
    task_poll_for_reply: Incomplete
    code_cells_executed: int
    widget_state: Incomplete
    widget_buffers: Incomplete
    output_hook_stack: Incomplete
    comm_objects: Incomplete
    def reset_execution_trackers(self) -> None:
        """Resets any per-execution trackers."""
    def create_kernel_manager(self) -> KernelManager:
        """Creates a new kernel manager.

        Returns
        -------
        km : KernelManager
            Kernel manager whose client class is asynchronous.
        """
    async def async_start_new_kernel(self, **kwargs: t.Any) -> None:
        """Creates a new kernel.

        Parameters
        ----------
        kwargs :
            Any options for ``self.kernel_manager_class.start_kernel()``. Because
            that defaults to AsyncKernelManager, this will likely include options
            accepted by ``AsyncKernelManager.start_kernel()``, which includes ``cwd``.
        """
    start_new_kernel: Incomplete
    async def async_start_new_kernel_client(self) -> KernelClient:
        """Creates a new kernel client.

        Returns
        -------
        kc : KernelClient
            Kernel client as created by the kernel manager ``km``.
        """
    start_new_kernel_client: Incomplete
    def setup_kernel(self, **kwargs: t.Any) -> t.Generator:
        """
        Context manager for setting up the kernel to execute a notebook.

        The assigns the Kernel Manager (``self.km``) if missing and Kernel Client(``self.kc``).

        When control returns from the yield it stops the client's zmq channels, and shuts
        down the kernel.
        """
    async def async_setup_kernel(self, **kwargs: t.Any) -> t.AsyncGenerator:
        """
        Context manager for setting up the kernel to execute a notebook.

        This assigns the Kernel Manager (``self.km``) if missing and Kernel Client(``self.kc``).

        When control returns from the yield it stops the client's zmq channels, and shuts
        down the kernel.

        Handlers for SIGINT and SIGTERM are also added to cleanup in case of unexpected shutdown.
        """
    async def async_execute(self, reset_kc: bool = False, **kwargs: t.Any) -> NotebookNode:
        """
        Executes each code cell.

        Parameters
        ----------
        kwargs :
            Any option for ``self.kernel_manager_class.start_kernel()``. Because
            that defaults to AsyncKernelManager, this will likely include options
            accepted by ``jupyter_client.AsyncKernelManager.start_kernel()``,
            which includes ``cwd``.

            ``reset_kc`` if True, the kernel client will be reset and a new one
            will be created (default: False).

        Returns
        -------
        nb : NotebookNode
            The executed notebook.
        """
    execute: Incomplete
    def set_widgets_metadata(self) -> None:
        """Set with widget metadata."""
    async def async_wait_for_reply(self, msg_id: str, cell: NotebookNode | None = None) -> t.Dict | None:
        """Wait for a message reply."""
    wait_for_reply: Incomplete
    clear_before_next_output: bool
    async def async_execute_cell(self, cell: NotebookNode, cell_index: int, execution_count: int | None = None, store_history: bool = True) -> NotebookNode:
        """
        Executes a single code cell.

        To execute all cells see :meth:`execute`.

        Parameters
        ----------
        cell : nbformat.NotebookNode
            The cell which is currently being processed.
        cell_index : int
            The position of the cell within the notebook object.
        execution_count : int
            The execution count to be assigned to the cell (default: Use kernel response)
        store_history : bool
            Determines if history should be stored in the kernel (default: False).
            Specific to ipython kernels, which can store command histories.

        Returns
        -------
        output : dict
            The execution output payload (or None for no output).

        Raises
        ------
        CellExecutionError
            If execution failed and should raise an exception, this will be raised
            with defaults about the failure.

        Returns
        -------
        cell : NotebookNode
            The cell which was just processed.
        """
    execute_cell: Incomplete
    def process_message(self, msg: t.Dict, cell: NotebookNode, cell_index: int) -> NotebookNode | None:
        """
        Processes a kernel message, updates cell state, and returns the
        resulting output object that was appended to cell.outputs.

        The input argument *cell* is modified in-place.

        Parameters
        ----------
        msg : dict
            The kernel message being processed.
        cell : nbformat.NotebookNode
            The cell which is currently being processed.
        cell_index : int
            The position of the cell within the notebook object.

        Returns
        -------
        output : NotebookNode
            The execution output payload (or None for no output).

        Raises
        ------
        CellExecutionComplete
          Once a message arrives which indicates computation completeness.

        """
    def output(self, outs: t.List, msg: t.Dict, display_id: str, cell_index: int) -> NotebookNode | None:
        """Handle output."""
    def clear_output(self, outs: t.List, msg: t.Dict, cell_index: int) -> None:
        """Clear output."""
    def clear_display_id_mapping(self, cell_index: int) -> None:
        """Clear a display id mapping for a cell."""
    def handle_comm_msg(self, outs: t.List, msg: t.Dict, cell_index: int) -> None:
        """Handle a comm message."""
    def register_output_hook(self, msg_id: str, hook: OutputWidget) -> None:
        """Registers an override object that handles output/clear_output instead.

        Multiple hooks can be registered, where the last one will be used (stack based)
        """
    def remove_output_hook(self, msg_id: str, hook: OutputWidget) -> None:
        """Unregisters an override object that handles output/clear_output instead"""
    def on_comm_open_jupyter_widget(self, msg: t.Dict) -> t.Any | None:
        """Handle a jupyter widget comm open."""

def execute(nb: NotebookNode, cwd: str | None = None, km: KernelManager | None = None, **kwargs: t.Any) -> NotebookNode:
    """Execute a notebook's code, updating outputs within the notebook object.

    This is a convenient wrapper around NotebookClient. It returns the
    modified notebook object.

    Parameters
    ----------
    nb : NotebookNode
      The notebook object to be executed
    cwd : str, optional
      If supplied, the kernel will run in this directory
    km : AsyncKernelManager, optional
      If supplied, the specified kernel manager will be used for code execution.
    kwargs :
      Any other options for NotebookClient, e.g. timeout, kernel_name
    """
