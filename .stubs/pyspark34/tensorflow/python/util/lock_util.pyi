class GroupLock:
    """A lock to allow many members of a group to access a resource exclusively.

  This lock provides a way to allow access to a resource by multiple threads
  belonging to a logical group at the same time, while restricting access to
  threads from all other groups. You can think of this as an extension of a
  reader-writer lock, where you allow multiple writers at the same time. We
  made it generic to support multiple groups instead of just two - readers and
  writers.

  Simple usage example with two groups accessing the same resource:

  ```python
  lock = GroupLock(num_groups=2)

  # In a member of group 0:
  with lock.group(0):
    # do stuff, access the resource
    # ...

  # In a member of group 1:
  with lock.group(1):
    # do stuff, access the resource
    # ...
  ```

  Using as a context manager with `.group(group_id)` is the easiest way. You
  can also use the `acquire` and `release` method directly.
  """
    def __init__(self, num_groups: int = 2) -> None:
        """Initialize a group lock.

    Args:
      num_groups: The number of groups that will be accessing the resource under
        consideration. Should be a positive number.

    Returns:
      A group lock that can then be used to synchronize code.

    Raises:
      ValueError: If num_groups is less than 1.
    """
    def group(self, group_id):
        """Enter a context where the lock is with group `group_id`.

    Args:
      group_id: The group for which to acquire and release the lock.

    Returns:
      A context manager which will acquire the lock for `group_id`.
    """
    def acquire(self, group_id) -> None:
        """Acquire the group lock for a specific group `group_id`."""
    def release(self, group_id) -> None:
        """Release the group lock for a specific group `group_id`."""
    class _Context:
        """Context manager helper for `GroupLock`."""
        def __init__(self, lock, group_id) -> None: ...
        def __enter__(self) -> None: ...
        def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None) -> None: ...
