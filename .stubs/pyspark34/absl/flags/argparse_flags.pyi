import argparse
from _typeshed import Incomplete
from absl import flags as flags

class ArgumentParser(argparse.ArgumentParser):
    """Custom ArgumentParser class to support special absl flags."""
    def __init__(self, **kwargs) -> None:
        """Initializes ArgumentParser.

    Args:
      **kwargs: same as argparse.ArgumentParser, except:
          1. It also accepts `inherited_absl_flags`: the absl flags to inherit.
             The default is the global absl.flags.FLAGS instance. Pass None to
             ignore absl flags.
          2. The `prefix_chars` argument must be the default value '-'.

    Raises:
      ValueError: Raised when prefix_chars is not '-'.
    """
    def parse_known_args(self, args: Incomplete | None = None, namespace: Incomplete | None = None): ...

class _FlagAction(argparse.Action):
    """Action class for Abseil non-boolean flags."""
    def __init__(self, option_strings, dest, help, metavar, flag_instance, default=...) -> None:
        """Initializes _FlagAction.

    Args:
      option_strings: See argparse.Action.
      dest: Ignored. The flag is always defined with dest=argparse.SUPPRESS.
      help: See argparse.Action.
      metavar: See argparse.Action.
      flag_instance: absl.flags.Flag, the absl flag instance.
      default: Ignored. The flag always uses dest=argparse.SUPPRESS so it
          doesn't affect the parsing result.
    """
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None:
        """See https://docs.python.org/3/library/argparse.html#action-classes."""

class _BooleanFlagAction(argparse.Action):
    """Action class for Abseil boolean flags."""
    def __init__(self, option_strings, dest, help, metavar, flag_instance, default=...) -> None:
        """Initializes _BooleanFlagAction.

    Args:
      option_strings: See argparse.Action.
      dest: Ignored. The flag is always defined with dest=argparse.SUPPRESS.
      help: See argparse.Action.
      metavar: See argparse.Action.
      flag_instance: absl.flags.Flag, the absl flag instance.
      default: Ignored. The flag always uses dest=argparse.SUPPRESS so it
          doesn't affect the parsing result.
    """
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None:
        """See https://docs.python.org/3/library/argparse.html#action-classes."""

class _HelpFullAction(argparse.Action):
    """Action class for --helpfull flag."""
    def __init__(self, option_strings, dest, default, help) -> None:
        """Initializes _HelpFullAction.

    Args:
      option_strings: See argparse.Action.
      dest: Ignored. The flag is always defined with dest=argparse.SUPPRESS.
      default: Ignored.
      help: See argparse.Action.
    """
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None:
        """See https://docs.python.org/3/library/argparse.html#action-classes."""
