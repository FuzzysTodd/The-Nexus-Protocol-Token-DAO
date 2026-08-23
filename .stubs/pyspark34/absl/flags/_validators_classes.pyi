from _typeshed import Incomplete

class Validator:
    """Base class for flags validators.

  Users should NOT overload these classes, and use flags.Register...
  methods instead.
  """
    validators_count: int
    checker: Incomplete
    message: Incomplete
    insertion_index: Incomplete
    def __init__(self, checker, message) -> None:
        """Constructor to create all validators.

    Args:
      checker: function to verify the constraint.
          Input of this method varies, see SingleFlagValidator and
          multi_flags_validator for a detailed description.
      message: str, error message to be shown to the user.
    """
    def verify(self, flag_values) -> None:
        """Verifies that constraint is satisfied.

    flags library calls this method to verify Validator's constraint.

    Args:
      flag_values: flags.FlagValues, the FlagValues instance to get flags from.
    Raises:
      Error: Raised if constraint is not satisfied.
    """
    def get_flags_names(self) -> None:
        """Returns the names of the flags checked by this validator.

    Returns:
      [string], names of the flags.
    """
    def print_flags_with_values(self, flag_values) -> None: ...

class SingleFlagValidator(Validator):
    """Validator behind register_validator() method.

  Validates that a single flag passes its checker function. The checker function
  takes the flag value and returns True (if value looks fine) or, if flag value
  is not valid, either returns False or raises an Exception.
  """
    flag_name: Incomplete
    def __init__(self, flag_name, checker, message) -> None:
        """Constructor.

    Args:
      flag_name: string, name of the flag.
      checker: function to verify the validator.
          input  - value of the corresponding flag (string, boolean, etc).
          output - bool, True if validator constraint is satisfied.
              If constraint is not satisfied, it should either return False or
              raise flags.ValidationError(desired_error_message).
      message: str, error message to be shown to the user if validator's
          condition is not satisfied.
    """
    def get_flags_names(self): ...
    def print_flags_with_values(self, flag_values): ...

class MultiFlagsValidator(Validator):
    """Validator behind register_multi_flags_validator method.

  Validates that flag values pass their common checker function. The checker
  function takes flag values and returns True (if values look fine) or,
  if values are not valid, either returns False or raises an Exception.
  """
    flag_names: Incomplete
    def __init__(self, flag_names, checker, message) -> None:
        """Constructor.

    Args:
      flag_names: [str], containing names of the flags used by checker.
      checker: function to verify the validator.
          input  - dict, with keys() being flag_names, and value for each
              key being the value of the corresponding flag (string, boolean,
              etc).
          output - bool, True if validator constraint is satisfied.
              If constraint is not satisfied, it should either return False or
              raise flags.ValidationError(desired_error_message).
      message: str, error message to be shown to the user if validator's
          condition is not satisfied
    """
    def print_flags_with_values(self, flag_values): ...
    def get_flags_names(self): ...
