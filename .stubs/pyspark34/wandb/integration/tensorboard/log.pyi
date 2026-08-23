import numpy as np
from _typeshed import Incomplete
from typing import Any, Dict
from wandb.sdk.internal.tb_watcher import TBHistory as TBHistory
from wandb.sdk.lib import telemetry as telemetry
from wandb.viz import custom_chart as custom_chart

STEPS: Dict[str, Dict[str, Any]]
RATE_LIMIT_SECONDS: float | int | None
IGNORE_KINDS: Incomplete
tensor_util: Incomplete
pb: Incomplete
Summary: Incomplete

def make_ndarray(tensor: Any) -> np.ndarray | None: ...
def namespaced_tag(tag: str, namespace: str = '') -> str: ...
def history_image_key(key: str, namespace: str = '') -> str:
    """Convert invalid filesystem characters to _ for use in History keys.

    Unfortunately this means currently certain image keys will collide silently. We
    implement this mapping up here in the TensorFlow stuff rather than in the History
    stuff so that we don't have to store a mapping anywhere from the original keys to
    the safe ones.
    """
def tf_summary_to_dict(tf_summary_str_or_pb: Any, namespace: str = '') -> Dict[str, Any] | None:
    """Convert a Tensorboard Summary to a dictionary.

    Accepts a tensorflow.summary.Summary, one encoded as a string,
    or a list of such encoded as strings.
    """
def reset_state() -> None:
    """Internal method for resetting state, called by wandb.finish()."""
def log(tf_summary_str_or_pb: Any, step: int = 0, namespace: str = '') -> None: ...
