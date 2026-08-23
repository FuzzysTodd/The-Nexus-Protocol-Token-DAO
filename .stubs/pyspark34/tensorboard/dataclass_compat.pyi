from tensorboard.compat.proto import event_pb2 as event_pb2, summary_pb2 as summary_pb2
from tensorboard.util import tensor_util as tensor_util

def migrate_event(event, initial_metadata):
    """Migrate an event to a sequence of events.

    Args:
      event: An `event_pb2.Event`. The caller transfers ownership of the
        event to this method; the event may be mutated, and may or may
        not appear in the returned sequence.
      initial_metadata: Map from tag name (string) to `SummaryMetadata`
        proto for the initial occurrence of the given tag within the
        enclosing run. While loading a given run, the caller should
        always pass the same dictionary here, initially `{}`; this
        function will mutate it and reuse it for future calls.

    Returns:
      A sequence of `event_pb2.Event`s to use instead of `event`.
    """
