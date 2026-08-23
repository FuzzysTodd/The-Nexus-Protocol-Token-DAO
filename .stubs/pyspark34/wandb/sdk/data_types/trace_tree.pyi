from ..wandb_run import Run as LocalRun
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List
from wandb.sdk.artifacts.artifact import Artifact as Artifact
from wandb.sdk.data_types import _dtypes
from wandb.sdk.data_types.base_types.media import Media as Media

class StatusCode(str, Enum):
    SUCCESS: str
    ERROR: str

class SpanKind(str, Enum):
    LLM: str
    CHAIN: str
    AGENT: str
    TOOL: str

@dataclass()
class Result:
    inputs: Dict[str, Any] | None = ...
    outputs: Dict[str, Any] | None = ...
    def __init__(self, inputs, outputs) -> None: ...

@dataclass()
class Span:
    span_id: str | None = ...
    name: str | None = ...
    start_time_ms: int | None = ...
    end_time_ms: int | None = ...
    status_code: StatusCode | None = ...
    status_message: str | None = ...
    attributes: Dict[str, Any] | None = ...
    results: List[Result] | None = ...
    child_spans: List['Span'] | None = ...
    span_kind: SpanKind | None = ...
    def add_attribute(self, key: str, value: Any) -> None: ...
    def add_named_result(self, inputs: Dict[str, Any], outputs: Dict[str, Any]) -> None: ...
    def add_child_span(self, span: Span) -> None: ...
    def __init__(self, span_id, name, start_time_ms, end_time_ms, status_code, status_message, attributes, results, child_spans, span_kind) -> None: ...

class WBTraceTree(Media):
    """Media object for trace tree data.

    Arguments:
        root_span (Span): The root span of the trace tree.
        model_dict (dict, optional): A dictionary containing the model dump.
            NOTE: model_dict is a completely-user-defined dict. The UI will render
            a JSON viewer for this dict, giving special treatment to dictionaries
            with a `_kind` key. This is because model vendors have such different
            serialization formats that we need to be flexible here.
    """
    def __init__(self, root_span: Span, model_dict: dict | None = None) -> None: ...
    @classmethod
    def get_media_subdir(cls) -> str: ...
    def to_json(self, run: LocalRun | Artifact | None) -> dict: ...
    def is_bound(self) -> bool: ...

class _WBTraceTreeFileType(_dtypes.Type):
    name: str
    types: Incomplete

class TraceAttribute:
    """Descriptor for accessing and setting attributes of the `Trace` class."""
    name: Incomplete
    def __set_name__(self, owner: type, name: str) -> None: ...
    def __get__(self, instance: Trace, owner: type) -> Any: ...
    def __set__(self, instance: Trace, value: Any) -> None: ...

class Trace:
    '''A simplification of WBTraceTree and Span to manage a trace - a collection of spans, their metadata and hierarchy.

    Args:
        name: (str) The name of the root span.
        kind: (str, optional) The kind of the root span.
        status_code: (str, optional) The status of the root span, either "error" or "success".
        status_message: (str, optional) Any status message associated with the root span.
        metadata: (dict, optional) Any additional metadata for the root span.
        start_time_ms: (int, optional) The start time of the root span in milliseconds.
        end_time_ms: (int, optional) The end time of the root span in milliseconds.
        inputs: (dict, optional) The named inputs of the root span.
        outputs: (dict, optional) The named outputs of the root span.
        model_dict: (dict, optional) A json serializable dictionary containing the model architecture details.

    Example:
        .. code-block:: python
        ```
        trace = Trace(
            name="My awesome Model",
            kind="LLM",
            status_code= "SUCCESS",
            metadata={"attr_1": 1, "attr_2": 2,},
            start_time_ms=int(round(time.time() * 1000)),
            end_time_ms=int(round(time.time() * 1000))+1000,
            inputs={"user": "How old is google?"},
            outputs={"assistant": "25 years old"},
            model_dict={"_kind": "openai", "api_type": "azure"}
              )
        run = wandb.init(project=<my_awesome_project>,)
        trace.log("my_trace")
        wandb.finish()
        ```
    '''
    name: Incomplete
    status_code: Incomplete
    status_message: Incomplete
    start_time_ms: Incomplete
    end_time_ms: Incomplete
    def __init__(self, name: str, kind: str | None = None, status_code: str | None = None, status_message: str | None = None, metadata: dict | None = None, start_time_ms: int | None = None, end_time_ms: int | None = None, inputs: dict | None = None, outputs: dict | None = None, model_dict: dict | None = None) -> None: ...
    def add_child(self, child: Trace) -> Trace:
        """Utility to add a child span to the current span of the trace.

        Args:
            child: The child span to be added to the current span of the trace.

        Returns:
            The current trace object with the child span added to it.
        """
    def add_inputs_and_outputs(self, inputs: dict, outputs: dict) -> Trace:
        """Add a result to the span of the current trace.

        Args:
            inputs: Dictionary of inputs to be logged with the span.
            outputs: Dictionary of outputs to be logged with the span.

        Returns:
            The current trace object with the result added to it.
        """
    def add_metadata(self, metadata: dict) -> Trace:
        """Add metadata to the span of the current trace."""
    @property
    def metadata(self) -> Dict[str, str] | None:
        """Get the metadata of the trace.

        Returns:
            Dictionary of metadata.
        """
    @metadata.setter
    def metadata(self, value: Dict[str, str]) -> None:
        """Set the metadata of the trace.

        Args:
            value: Dictionary of metadata to be set.
        """
    @property
    def inputs(self) -> Dict[str, str] | None:
        """Get the inputs of the trace.

        Returns:
            Dictionary of inputs.
        """
    @inputs.setter
    def inputs(self, value: Dict[str, str]) -> None:
        """Set the inputs of the trace.

        Args:
            value: Dictionary of inputs to be set.
        """
    @property
    def outputs(self) -> Dict[str, str] | None:
        """Get the outputs of the trace.

        Returns:
            Dictionary of outputs.
        """
    @outputs.setter
    def outputs(self, value: Dict[str, str]) -> None:
        """Set the outputs of the trace.

        Args:
            value: Dictionary of outputs to be set.
        """
    @property
    def kind(self) -> str | None:
        """Get the kind of the trace.

        Returns:
            The kind of the trace.
        """
    @kind.setter
    def kind(self, value: str) -> None:
        """Set the kind of the trace.

        Args:
            value: The kind of the trace to be set.
        """
    def log(self, name: str) -> None:
        """Log the trace to a wandb run.

        Args:
            name: The name of the trace to be logged
        """
