from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.client import session as session_lib
from tensorflow.python.framework import meta_graph as meta_graph, ops as ops
from tensorflow.python.saved_model.pywrap_saved_model import metrics as metrics
from tensorflow.python.training import basic_session_run_hooks as basic_session_run_hooks, monitored_session as monitored_session, saver as saver_lib, session_run_hook as session_run_hook, training_util as training_util
from tensorflow.python.training.summary_io import SummaryWriterCache as SummaryWriterCache
from typing import Any, List, Optional, Text

class AsyncCheckpointSaverHook(basic_session_run_hooks.CheckpointSaverHook):
    """Saves checkpoints every N steps or seconds."""
    def __init__(self, checkpoint_dir: Text, save_secs: Optional[int] = None, save_steps: Optional[int] = None, saver: Optional[saver_lib.Saver] = None, checkpoint_basename: Text = 'model.ckpt', scaffold: Optional[monitored_session.Scaffold] = None, listeners: Optional[List[basic_session_run_hooks.CheckpointSaverListener]] = None) -> None:
        """Initializes a `CheckpointSaverHook`.

    Args:
      checkpoint_dir: `str`, base directory for the checkpoint files.
      save_secs: `int`, save every N secs.
      save_steps: `int`, save every N steps.
      saver: `Saver` object, used for saving.
      checkpoint_basename: `str`, base name for the checkpoint files.
      scaffold: `Scaffold`, use to get saver object.
      listeners: List of `CheckpointSaverListener` subclass instances. Used for
        callbacks that run immediately before or after this hook saves the
        checkpoint.

    Raises:
      ValueError: One of `save_steps` or `save_secs` should be set.
      ValueError: At most one of `saver` or `scaffold` should be set.
    """
    def begin(self) -> None: ...
    def after_create_session(self, session: session_lib.Session, coord: Any): ...
    def before_run(self, run_context: Any): ...
    def after_run(self, run_context: session_run_hook.SessionRunContext, run_values: Any): ...
    def end(self, session: session_lib.Session): ...
