from _typeshed import Incomplete
from grpc.framework.interfaces.base import base as base
from typing import NamedTuple

class _Completion(base.Completion, NamedTuple('_Completion', [('terminal_metadata', Incomplete), ('code', Incomplete), ('message', Incomplete)])):
    """A trivial implementation of base.Completion."""
class _Subscription(base.Subscription, NamedTuple('_Subscription', [('kind', Incomplete), ('termination_callback', Incomplete), ('allowance', Incomplete), ('operator', Incomplete), ('protocol_receiver', Incomplete)])):
    """A trivial implementation of base.Subscription."""

def completion(terminal_metadata, code, message):
    """Creates a base.Completion aggregating the given operation values.

  Args:
    terminal_metadata: A terminal metadata value for an operaton.
    code: A code value for an operation.
    message: A message value for an operation.

  Returns:
    A base.Completion aggregating the given operation values.
  """
def full_subscription(operator, protocol_receiver):
    '''Creates a "full" base.Subscription for the given base.Operator.

  Args:
    operator: A base.Operator to be used in an operation.
    protocol_receiver: A base.ProtocolReceiver to be used in an operation.

  Returns:
    A base.Subscription of kind base.Subscription.Kind.FULL wrapping the given
      base.Operator and base.ProtocolReceiver.
  '''
