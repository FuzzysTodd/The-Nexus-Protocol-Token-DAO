from ..trainer_callback import TrainerCallback as TrainerCallback
from ..trainer_utils import IntervalStrategy as IntervalStrategy, has_length as has_length
from _typeshed import Incomplete
from typing import Optional

def format_time(t):
    """Format `t` (in seconds) to (h):mm:ss"""
def html_progress_bar(value, total, prefix, label, width: int = 300): ...
def text_to_html_table(items):
    """Put the texts in `items` in an HTML table."""

class NotebookProgressBar:
    """
    A progress par for display in a notebook.

    Class attributes (overridden by derived classes)

        - **warmup** (`int`) -- The number of iterations to do at the beginning while ignoring `update_every`.
        - **update_every** (`float`) -- Since calling the time takes some time, we only do it every presumed
          `update_every` seconds. The progress bar uses the average time passed up until now to guess the next value
          for which it will call the update.

    Args:
        total (`int`):
            The total number of iterations to reach.
        prefix (`str`, *optional*):
            A prefix to add before the progress bar.
        leave (`bool`, *optional*, defaults to `True`):
            Whether or not to leave the progress bar once it's completed. You can always call the
            [`~utils.notebook.NotebookProgressBar.close`] method to make the bar disappear.
        parent ([`~notebook.NotebookTrainingTracker`], *optional*):
            A parent object (like [`~utils.notebook.NotebookTrainingTracker`]) that spawns progress bars and handle
            their display. If set, the object passed must have a `display()` method.
        width (`int`, *optional*, defaults to 300):
            The width (in pixels) that the bar will take.

    Example:

    ```python
    import time

    pbar = NotebookProgressBar(100)
    for val in range(100):
        pbar.update(val)
        time.sleep(0.07)
    pbar.update(100)
    ```"""
    warmup: int
    update_every: float
    total: Incomplete
    prefix: Incomplete
    leave: Incomplete
    parent: Incomplete
    width: Incomplete
    last_value: Incomplete
    comment: Incomplete
    output: Incomplete
    def __init__(self, total: int, prefix: Optional[str] = None, leave: bool = True, parent: Optional['NotebookTrainingTracker'] = None, width: int = 300) -> None: ...
    value: Incomplete
    start_time: Incomplete
    start_value: Incomplete
    elapsed_time: Incomplete
    first_calls: Incomplete
    wait_for: int
    average_time_per_item: Incomplete
    predicted_remaining: Incomplete
    last_time: Incomplete
    def update(self, value: int, force_update: bool = False, comment: str = None):
        """
        The main method to update the progress bar to `value`.

        Args:
            value (`int`):
                The value to use. Must be between 0 and `total`.
            force_update (`bool`, *optional*, defaults to `False`):
                Whether or not to force and update of the internal state and display (by default, the bar will wait for
                `value` to reach the value it predicted corresponds to a time of more than the `update_every` attribute
                since the last update to avoid adding boilerplate).
            comment (`str`, *optional*):
                A comment to add on the left of the progress bar.
        """
    label: Incomplete
    def update_bar(self, value, comment: Incomplete | None = None) -> None: ...
    html_code: Incomplete
    def display(self) -> None: ...
    def close(self) -> None:
        """Closes the progress bar."""

class NotebookTrainingTracker(NotebookProgressBar):
    """
    An object tracking the updates of an ongoing training with progress bars and a nice table reporting metrics.

    Args:
        num_steps (`int`): The number of steps during training. column_names (`List[str]`, *optional*):
            The list of column names for the metrics table (will be inferred from the first call to
            [`~utils.notebook.NotebookTrainingTracker.write_line`] if not set).
    """
    inner_table: Incomplete
    child_bar: Incomplete
    def __init__(self, num_steps, column_names: Incomplete | None = None) -> None: ...
    html_code: Incomplete
    output: Incomplete
    def display(self) -> None: ...
    def write_line(self, values) -> None:
        """
        Write the values in the inner table.

        Args:
            values (`Dict[str, float]`): The values to display.
        """
    def add_child(self, total, prefix: Incomplete | None = None, width: int = 300):
        """
        Add a child progress bar displayed under the table of metrics. The child progress bar is returned (so it can be
        easily updated).

        Args:
            total (`int`): The number of iterations for the child progress bar.
            prefix (`str`, *optional*): A prefix to write on the left of the progress bar.
            width (`int`, *optional*, defaults to 300): The width (in pixels) of the progress bar.
        """
    def remove_child(self) -> None:
        """
        Closes the child progress bar.
        """

class NotebookProgressCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that displays the progress of training or evaluation, optimized for Jupyter Notebooks or
    Google colab.
    """
    training_tracker: Incomplete
    prediction_bar: Incomplete
    def __init__(self) -> None: ...
    first_column: Incomplete
    training_loss: int
    last_log: int
    def on_train_begin(self, args, state, control, **kwargs) -> None: ...
    def on_step_end(self, args, state, control, **kwargs) -> None: ...
    def on_prediction_step(self, args, state, control, eval_dataloader: Incomplete | None = None, **kwargs) -> None: ...
    def on_predict(self, args, state, control, **kwargs) -> None: ...
    def on_log(self, args, state, control, logs: Incomplete | None = None, **kwargs) -> None: ...
    def on_evaluate(self, args, state, control, metrics: Incomplete | None = None, **kwargs) -> None: ...
    def on_train_end(self, args, state, control, **kwargs) -> None: ...
