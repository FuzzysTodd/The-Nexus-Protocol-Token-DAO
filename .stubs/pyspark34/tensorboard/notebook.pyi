from _typeshed import Incomplete
from tensorboard import manager as manager

def load_ipython_extension(ipython) -> None:
    """Deprecated: use `%load_ext tensorboard` instead.

    Raises:
      RuntimeError: Always.
    """
def start(args_string):
    '''Launch and display a TensorBoard instance as if at the command line.

    Args:
      args_string: Command-line arguments to TensorBoard, to be
        interpreted by `shlex.split`: e.g., "--logdir ./logs --port 0".
        Shell metacharacters are not supported: e.g., "--logdir 2>&1" will
        point the logdir at the literal directory named "2>&1".
    '''
def display(port: Incomplete | None = None, height: Incomplete | None = None) -> None:
    """Display a TensorBoard instance already running on this machine.

    Args:
      port: The port on which the TensorBoard server is listening, as an
        `int`, or `None` to automatically select the most recently
        launched TensorBoard.
      height: The height of the frame into which to render the TensorBoard
        UI, as an `int` number of pixels, or `None` to use a default value
        (currently 800).
    """
def list() -> None:
    """Print a listing of known running TensorBoard instances.

    TensorBoard instances that were killed uncleanly (e.g., with SIGKILL
    or SIGQUIT) may appear in this list even if they are no longer
    running. Conversely, this list may be missing some entries if your
    operating system's temporary directory has been cleared since a
    still-running TensorBoard instance started.
    """
