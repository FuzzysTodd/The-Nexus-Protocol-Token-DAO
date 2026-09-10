def register_validator(flag_name, checker, message: str = 'Flag validation failed', flag_values=...) -> None:
    """Adds a constraint, which will be enforced during program execution.

  The constraint is validated when flags are initially parsed, and after each
  change of the corresponding flag's value.

  Args:
    flag_name: str | FlagHolder, name or holder of the flag to be checked.
        Positional-only parameter.
    checker: callable, a function to validate the flag.

        * input - A single positional argument: The value of the corresponding
          flag (string, boolean, etc.  This value will be passed to checker
          by the library).
        * output - bool, True if validator constraint is satisfied.
          If constraint is not satisfied, it should either ``return False`` or
          ``raise flags.ValidationError(desired_error_message)``.

    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.

  Raises:
    AttributeError: Raised when flag_name is not registered as a valid flag
        name.
    ValueError: Raised when flag_values is non-default and does not match the
        FlagValues of the provided FlagHolder instance.
  """
def validator(flag_name, message: str = 'Flag validation failed', flag_values=...):
    """A function decorator for defining a flag validator.

  Registers the decorated function as a validator for flag_name, e.g.::

      @flags.validator('foo')
      def _CheckFoo(foo):
        ...

  See :func:`register_validator` for the specification of checker function.

  Args:
    flag_name: str | FlagHolder, name or holder of the flag to be checked.
        Positional-only parameter.
    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.
  Returns:
    A function decorator that registers its function argument as a validator.
  Raises:
    AttributeError: Raised when flag_name is not registered as a valid flag
        name.
  """
def register_multi_flags_validator(flag_names, multi_flags_checker, message: str = 'Flags validation failed', flag_values=...) -> None:
    """Adds a constraint to multiple flags.

  The constraint is validated when flags are initially parsed, and after each
  change of the corresponding flag's value.

  Args:
    flag_names: [str | FlagHolder], a list of the flag names or holders to be
        checked. Positional-only parameter.
    multi_flags_checker: callable, a function to validate the flag.

        * input - dict, with keys() being flag_names, and value for each key
            being the value of the corresponding flag (string, boolean, etc).
        * output - bool, True if validator constraint is satisfied.
            If constraint is not satisfied, it should either return False or
            raise flags.ValidationError.

    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.

  Raises:
    AttributeError: Raised when a flag is not registered as a valid flag name.
    ValueError: Raised when multiple FlagValues are used in the same
        invocation. This can occur when FlagHolders have different `_flagvalues`
        or when str-type flag_names entries are present and the `flag_values`
        argument does not match that of provided FlagHolder(s).
  """
def multi_flags_validator(flag_names, message: str = 'Flag validation failed', flag_values=...):
    """A function decorator for defining a multi-flag validator.

  Registers the decorated function as a validator for flag_names, e.g.::

      @flags.multi_flags_validator(['foo', 'bar'])
      def _CheckFooBar(flags_dict):
        ...

  See :func:`register_multi_flags_validator` for the specification of checker
  function.

  Args:
    flag_names: [str | FlagHolder], a list of the flag names or holders to be
        checked. Positional-only parameter.
    message: str, error text to be shown to the user if checker returns False.
        If checker raises flags.ValidationError, message from the raised
        error will be shown.
    flag_values: flags.FlagValues, optional FlagValues instance to validate
        against.

  Returns:
    A function decorator that registers its function argument as a validator.

  Raises:
    AttributeError: Raised when a flag is not registered as a valid flag name.
  """
def mark_flag_as_required(flag_name, flag_values=...):
    """Ensures that flag is not None during program execution.

  Registers a flag validator, which will follow usual validator rules.
  Important note: validator will pass for any non-``None`` value, such as
  ``False``, ``0`` (zero), ``''`` (empty string) and so on.

  If your module might be imported by others, and you only wish to make the flag
  required when the module is directly executed, call this method like this::

      if __name__ == '__main__':
        flags.mark_flag_as_required('your_flag_name')
        app.run()

  Args:
    flag_name: str | FlagHolder, name or holder of the flag.
        Positional-only parameter.
    flag_values: flags.FlagValues, optional :class:`~absl.flags.FlagValues`
        instance where the flag is defined.
  Raises:
    AttributeError: Raised when flag_name is not registered as a valid flag
        name.
    ValueError: Raised when flag_values is non-default and does not match the
        FlagValues of the provided FlagHolder instance.
  """
def mark_flags_as_required(flag_names, flag_values=...) -> None:
    """Ensures that flags are not None during program execution.

  If your module might be imported by others, and you only wish to make the flag
  required when the module is directly executed, call this method like this::

      if __name__ == '__main__':
        flags.mark_flags_as_required(['flag1', 'flag2', 'flag3'])
        app.run()

  Args:
    flag_names: Sequence[str | FlagHolder], names or holders of the flags.
    flag_values: flags.FlagValues, optional FlagValues instance where the flags
        are defined.
  Raises:
    AttributeError: If any of flag name has not already been defined as a flag.
  """
def mark_flags_as_mutual_exclusive(flag_names, required: bool = False, flag_values=...):
    """Ensures that only one flag among flag_names is not None.

  Important note: This validator checks if flag values are ``None``, and it does
  not distinguish between default and explicit values. Therefore, this validator
  does not make sense when applied to flags with default values other than None,
  including other false values (e.g. ``False``, ``0``, ``''``, ``[]``). That
  includes multi flags with a default value of ``[]`` instead of None.

  Args:
    flag_names: [str | FlagHolder], names or holders of flags.
        Positional-only parameter.
    required: bool. If true, exactly one of the flags must have a value other
        than None. Otherwise, at most one of the flags can have a value other
        than None, and it is valid for all of the flags to be None.
    flag_values: flags.FlagValues, optional FlagValues instance where the flags
        are defined.

  Raises:
    ValueError: Raised when multiple FlagValues are used in the same
        invocation. This can occur when FlagHolders have different `_flagvalues`
        or when str-type flag_names entries are present and the `flag_values`
        argument does not match that of provided FlagHolder(s).
  """
def mark_bool_flags_as_mutual_exclusive(flag_names, required: bool = False, flag_values=...):
    """Ensures that only one flag among flag_names is True.

  Args:
    flag_names: [str | FlagHolder], names or holders of flags.
        Positional-only parameter.
    required: bool. If true, exactly one flag must be True. Otherwise, at most
        one flag can be True, and it is valid for all flags to be False.
    flag_values: flags.FlagValues, optional FlagValues instance where the flags
        are defined.

  Raises:
    ValueError: Raised when multiple FlagValues are used in the same
        invocation. This can occur when FlagHolders have different `_flagvalues`
        or when str-type flag_names entries are present and the `flag_values`
        argument does not match that of provided FlagHolder(s).
  """
