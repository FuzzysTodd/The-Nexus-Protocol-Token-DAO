from _typeshed import Incomplete
from absl import flags as flags
from typing import Any, Mapping, Sequence, Tuple, overload

FLAGS: Incomplete

@overload
def flagsaver(*args: Tuple[flags.FlagHolder, Any], **kwargs: Any) -> _FlagOverrider: ...
@overload
def flagsaver(func: _CallableT) -> _CallableT: ...
@overload
def as_parsed(*args: Tuple[flags.FlagHolder, str | Sequence[str]], **kwargs: str | Sequence[str]) -> _ParsingFlagOverrider: ...
@overload
def as_parsed(func: _CallableT) -> _CallableT: ...
def save_flag_values(flag_values: flags.FlagValues = ...) -> Mapping[str, Mapping[str, Any]]:
    """Returns copy of flag values as a dict.

  Args:
    flag_values: FlagValues, the FlagValues instance with which the flag will be
      saved. This should almost never need to be overridden.

  Returns:
    Dictionary mapping keys to values. Keys are flag names, values are
    corresponding ``__dict__`` members. E.g. ``{'key': value_dict, ...}``.
  """
def restore_flag_values(saved_flag_values: Mapping[str, Mapping[str, Any]], flag_values: flags.FlagValues = ...):
    """Restores flag values based on the dictionary of flag values.

  Args:
    saved_flag_values: {'flag_name': value_dict, ...}
    flag_values: FlagValues, the FlagValues instance from which the flag will be
      restored. This should almost never need to be overridden.
  """

class _FlagOverrider:
    """Overrides flags for the duration of the decorated function call.

  It also restores all original values of flags after decorated method
  completes.
  """
    def __init__(self, **overrides: Any) -> None: ...
    def __call__(self, func: _CallableT) -> _CallableT: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class _ParsingFlagOverrider(_FlagOverrider):
    """Context manager for overriding flags.

  Simulates command line parsing.

  This is simlar to _FlagOverrider except that all **overrides should be
  strings or sequences of strings, and when context is entered this class calls
  .parse(value)

  This results in the flags having .present set properly.
  """
    def __init__(self, **overrides: str | Sequence[str]) -> None: ...
    def __enter__(self) -> None: ...
