from _typeshed import Incomplete
from torch.testing._internal.common_utils import FILE_SCHEMA as FILE_SCHEMA, TEST_WITH_TSAN as TEST_WITH_TSAN
from typing import Tuple

INIT_METHOD_TEMPLATE: Incomplete

def dist_init(old_test_method: Incomplete | None = None, setup_rpc: bool = True, clean_shutdown: bool = True, faulty_messages: Incomplete | None = None, messages_to_delay: Incomplete | None = None):
    '''
    We use this decorator for setting up and tearing down state since
    MultiProcessTestCase runs each `test*` method in a separate process and
    each process just runs the `test*` method without actually calling
    \'setUp\' and \'tearDown\' methods of unittest.

    Note: pass the string representation of MessageTypes that should be used
    with the faulty agent\'s send function. By default, all retriable messages
    ("RREF_FORK_REQUEST", "RREF_CHILD_ACCEPT", "RREF_USER_DELETE",
    "CLEANUP_AUTOGRAD_CONTEXT_REQ") will use the faulty send (this default is
    set from faulty_rpc_agent_test_fixture.py).
    '''
def noop() -> None: ...
def wait_until_node_failure(rank: int, expected_error_regex: str = '.*') -> str:
    """
    Loops until an RPC to the given rank fails. This is used to
    indicate that the node has failed in unit tests.
    Args:
    rank (int): Rank of the node expected to fail
    expected_error_regex (optional, str): Regex of exception message expected. Useful to ensure a specific failure
    occurs, not just any.
    """
def wait_until_pending_futures_and_users_flushed(timeout: int = 20) -> None:
    """
    The RRef protocol holds forkIds of rrefs in a map until those forks are
    confirmed by the owner. The message confirming the fork may arrive after
    our tests check whether this map is empty, which leads to failures and
    flaky tests. to_here also does not guarantee that we have finished
    processind the owner's confirmation message for the RRef. This function
    loops until the map is empty, which means the messages have been received
    as processed. Call this function before asserting the map returned by
    _get_debug_info is empty.
    """
def get_num_owners_and_forks() -> Tuple[str, str]:
    """
    Retrieves number of OwnerRRefs and forks on this node from
    _rref_context_get_debug_info.
    """
def wait_until_owners_and_forks_on_rank(num_owners: int, num_forks: int, rank: int, timeout: int = 20) -> None:
    """
    Waits until timeout for num_forks and num_owners to exist on the rank. Used
    to ensure proper deletion of RRefs in tests.
    """
def initialize_pg(init_method, rank: int, world_size: int) -> None: ...
def worker_name(rank: int) -> str: ...
def get_function_event(function_events, partial_event_name):
    """
    Returns the first event that matches partial_event_name in the provided
    function_events. These function_events should be the output of
    torch.autograd.profiler.function_events().

    Args:
    function_events: function_events returned by the profiler.
    event_name (str): partial key that the event was profiled with.
    """
