import typing
from absl.flags import _argument_parser, _flag, _flagvalues
from typing import Any, Iterable, List, Text, Type, overload

@overload
def DEFINE(parser: _argument_parser.ArgumentParser[_T], name: Text, default: Any, help: Text | None, flag_values: _flagvalues.FlagValues = ..., serializer: _argument_parser.ArgumentSerializer[_T] | None = ..., module_name: Text | None = ..., required: typing.Literal[True] = ..., **args: Any) -> _flagvalues.FlagHolder[_T]: ...
@overload
def DEFINE(parser: _argument_parser.ArgumentParser[_T], name: Text, default: Any | None, help: Text | None, flag_values: _flagvalues.FlagValues = ..., serializer: _argument_parser.ArgumentSerializer[_T] | None = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[_T | None]: ...
@overload
def DEFINE_flag(flag: _flag.Flag[_T], flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: typing.Literal[True] = ...) -> _flagvalues.FlagHolder[_T]: ...
@overload
def DEFINE_flag(flag: _flag.Flag[_T], flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ...) -> _flagvalues.FlagHolder[_T | None]: ...
def set_default(flag_holder: _flagvalues.FlagHolder[_T], value: _T) -> None:
    """Changes the default value of the provided flag object.

  The flag's current value is also updated if the flag is currently using
  the default value, i.e. not specified in the command line, and not set
  by FLAGS.name = value.

  Args:
    flag_holder: FlagHolder, the flag to modify.
    value: The new default value.

  Raises:
    IllegalFlagValueError: Raised when value is not valid.
  """
def declare_key_flag(flag_name: Text | _flagvalues.FlagHolder, flag_values: _flagvalues.FlagValues = ...) -> None:
    """Declares one flag as key to the current module.

  Key flags are flags that are deemed really important for a module.
  They are important when listing help messages; e.g., if the
  --helpshort command-line flag is used, then only the key flags of the
  main module are listed (instead of all flags, as in the case of
  --helpfull).

  Sample usage::

      flags.declare_key_flag('flag_1')

  Args:
    flag_name: str | :class:`FlagHolder`, the name or holder of an already
      declared flag. (Redeclaring flags as key, including flags implicitly key
      because they were declared in this module, is a no-op.)
      Positional-only parameter.
    flag_values: :class:`FlagValues`, the FlagValues instance in which the
      flag will be declared as a key flag. This should almost never need to be
      overridden.

  Raises:
    ValueError: Raised if flag_name not defined as a Python flag.
  """
def adopt_module_key_flags(module: Any, flag_values: _flagvalues.FlagValues = ...) -> None:
    """Declares that all flags key to a module are key to the current module.

  Args:
    module: module, the module object from which all key flags will be declared
      as key flags to the current module.
    flag_values: :class:`FlagValues`, the FlagValues instance in which the
      flags will be declared as key flags. This should almost never need to be
      overridden.

  Raises:
    Error: Raised when given an argument that is a module name (a string),
        instead of a module object.
  """
def disclaim_key_flags() -> None:
    """Declares that the current module will not define any more key flags.

  Normally, the module that calls the DEFINE_xxx functions claims the
  flag to be its key flag.  This is undesirable for modules that
  define additional DEFINE_yyy functions with its own flag parsers and
  serializers, since that module will accidentally claim flags defined
  by DEFINE_yyy as its key flags.  After calling this function, the
  module disclaims flag definitions thereafter, so the key flags will
  be correctly attributed to the caller of DEFINE_yyy.

  After calling this function, the module will not be able to define
  any more flags.  This function will affect all FlagValues objects.
  """
@overload
def DEFINE_string(name: Text, default: Text | None, help: Text | None, flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[Text]: ...
@overload
def DEFINE_string(name: Text, default: None, help: Text | None, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[Text | None]: ...
@overload
def DEFINE_string(name: Text, default: Text, help: Text | None, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[Text]: ...
@overload
def DEFINE_boolean(name: Text, default: None | Text | bool | int, help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[bool]: ...
@overload
def DEFINE_boolean(name: Text, default: None, help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[bool | None]: ...
@overload
def DEFINE_boolean(name: Text, default: Text | bool | int, help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[bool]: ...
@overload
def DEFINE_float(name: Text, default: None | float | Text, help: Text | None, lower_bound: float | None = ..., upper_bound: float | None = ..., flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[float]: ...
@overload
def DEFINE_float(name: Text, default: None, help: Text | None, lower_bound: float | None = ..., upper_bound: float | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[float | None]: ...
@overload
def DEFINE_float(name: Text, default: float | Text, help: Text | None, lower_bound: float | None = ..., upper_bound: float | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[float]: ...
@overload
def DEFINE_integer(name: Text, default: None | int | Text, help: Text | None, lower_bound: int | None = ..., upper_bound: int | None = ..., flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[int]: ...
@overload
def DEFINE_integer(name: Text, default: None, help: Text | None, lower_bound: int | None = ..., upper_bound: int | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[int | None]: ...
@overload
def DEFINE_integer(name: Text, default: int | Text, help: Text | None, lower_bound: int | None = ..., upper_bound: int | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[int]: ...
@overload
def DEFINE_enum(name: Text, default: Text | None, enum_values: Iterable[Text], help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[Text]: ...
@overload
def DEFINE_enum(name: Text, default: None, enum_values: Iterable[Text], help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[Text | None]: ...
@overload
def DEFINE_enum(name: Text, default: Text, enum_values: Iterable[Text], help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[Text]: ...
@overload
def DEFINE_enum_class(name: Text, default: None | _ET | Text, enum_class: Type[_ET], help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., case_sensitive: bool = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[_ET]: ...
@overload
def DEFINE_enum_class(name: Text, default: None, enum_class: Type[_ET], help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., case_sensitive: bool = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[_ET | None]: ...
@overload
def DEFINE_enum_class(name: Text, default: _ET | Text, enum_class: Type[_ET], help: Text | None, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., case_sensitive: bool = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[_ET]: ...
@overload
def DEFINE_list(name: Text, default: None | Iterable[Text] | Text, help: Text, flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_list(name: Text, default: None, help: Text, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text] | None]: ...
@overload
def DEFINE_list(name: Text, default: Iterable[Text] | Text, help: Text, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_spaceseplist(name: Text, default: None | Iterable[Text] | Text, help: Text, comma_compat: bool = ..., flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_spaceseplist(name: Text, default: None, help: Text, comma_compat: bool = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text] | None]: ...
@overload
def DEFINE_spaceseplist(name: Text, default: Iterable[Text] | Text, help: Text, comma_compat: bool = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_multi(parser: _argument_parser.ArgumentParser[_T], serializer: _argument_parser.ArgumentSerializer[_T], name: Text, default: Iterable[_T], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[_T]]: ...
@overload
def DEFINE_multi(parser: _argument_parser.ArgumentParser[_T], serializer: _argument_parser.ArgumentSerializer[_T], name: Text, default: None | _T, help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[_T]]: ...
@overload
def DEFINE_multi(parser: _argument_parser.ArgumentParser[_T], serializer: _argument_parser.ArgumentSerializer[_T], name: Text, default: None, help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[_T] | None]: ...
@overload
def DEFINE_multi(parser: _argument_parser.ArgumentParser[_T], serializer: _argument_parser.ArgumentSerializer[_T], name: Text, default: Iterable[_T], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[_T]]: ...
@overload
def DEFINE_multi(parser: _argument_parser.ArgumentParser[_T], serializer: _argument_parser.ArgumentSerializer[_T], name: Text, default: _T, help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[_T]]: ...
@overload
def DEFINE_multi_string(name: Text, default: None | Iterable[Text] | Text, help: Text, flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_multi_string(name: Text, default: None, help: Text, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text] | None]: ...
@overload
def DEFINE_multi_string(name: Text, default: Iterable[Text] | Text, help: Text, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_multi_integer(name: Text, default: None | Iterable[int] | int | Text, help: Text, lower_bound: int | None = ..., upper_bound: int | None = ..., flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[int]]: ...
@overload
def DEFINE_multi_integer(name: Text, default: None, help: Text, lower_bound: int | None = ..., upper_bound: int | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[int] | None]: ...
@overload
def DEFINE_multi_integer(name: Text, default: Iterable[int] | int | Text, help: Text, lower_bound: int | None = ..., upper_bound: int | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[int]]: ...
@overload
def DEFINE_multi_float(name: Text, default: None | Iterable[float] | float | Text, help: Text, lower_bound: float | None = ..., upper_bound: float | None = ..., flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[float]]: ...
@overload
def DEFINE_multi_float(name: Text, default: None, help: Text, lower_bound: float | None = ..., upper_bound: float | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[float] | None]: ...
@overload
def DEFINE_multi_float(name: Text, default: Iterable[float] | float | Text, help: Text, lower_bound: float | None = ..., upper_bound: float | None = ..., flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[float]]: ...
@overload
def DEFINE_multi_enum(name: Text, default: None | Iterable[Text] | Text, enum_values: Iterable[Text], help: Text, flag_values: _flagvalues.FlagValues = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_multi_enum(name: Text, default: None, enum_values: Iterable[Text], help: Text, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text] | None]: ...
@overload
def DEFINE_multi_enum(name: Text, default: Iterable[Text] | Text, enum_values: Iterable[Text], help: Text, flag_values: _flagvalues.FlagValues = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[Text]]: ...
@overload
def DEFINE_multi_enum_class(name: Text, default: Iterable[_ET], enum_class: Type[_ET], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[_ET]]: ...
@overload
def DEFINE_multi_enum_class(name: Text, default: None | _ET | Iterable[Text] | Text, enum_class: Type[_ET], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., *, required: typing.Literal[True], **args: Any) -> _flagvalues.FlagHolder[List[_ET]]: ...
@overload
def DEFINE_multi_enum_class(name: Text, default: None, enum_class: Type[_ET], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[_ET] | None]: ...
@overload
def DEFINE_multi_enum_class(name: Text, default: Iterable[_ET], enum_class: Type[_ET], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[_ET]]: ...
@overload
def DEFINE_multi_enum_class(name: Text, default: _ET | Iterable[Text] | Text, enum_class: Type[_ET], help: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = ..., required: bool = ..., **args: Any) -> _flagvalues.FlagHolder[List[_ET]]: ...
def DEFINE_alias(name: Text, original_name: Text, flag_values: _flagvalues.FlagValues = ..., module_name: Text | None = None) -> _flagvalues.FlagHolder[Any]:
    """Defines an alias flag for an existing one.

  Args:
    name: str, the flag name.
    original_name: str, the original flag name.
    flag_values: :class:`FlagValues`, the FlagValues instance with which the
      flag will be registered. This should almost never need to be overridden.
    module_name: A string, the name of the module that defines this flag.

  Returns:
    a handle to defined flag.

  Raises:
    flags.FlagError:
      UnrecognizedFlagError: if the referenced flag doesn't exist.
      DuplicateFlagError: if the alias name has been used by some existing flag.
  """
