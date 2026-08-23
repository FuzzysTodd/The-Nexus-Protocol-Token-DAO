from azure.core.tracing import AbstractSpan
from enum import Enum
from typing import Any, Callable, Generic, Tuple, Type, TypeVar

__all__ = ['settings', 'Settings']

ValidInputType = TypeVar('ValidInputType')
ValueType = TypeVar('ValueType')

class _Unset(Enum):
    token: int

class PrioritizedSetting(Generic[ValidInputType, ValueType]):
    '''Return a value for a global setting according to configuration precedence.

    The following methods are searched in order for the setting:

    4. immediate values
    3. previously user-set value
    2. environment variable
    1. system setting
    0. implicit default

    If a value cannot be determined, a RuntimeError is raised.

    The ``env_var`` argument specifies the name of an environment to check for
    setting values, e.g. ``"AZURE_LOG_LEVEL"``.
    If a ``convert`` function is provided, the result will be converted before being used.

    The optional ``system_hook`` can be used to specify a function that will
    attempt to look up a value for the setting from system-wide configurations.
    If a ``convert`` function is provided, the hook result will be converted before being used.

    The optional ``default`` argument specified an implicit default value for
    the setting that is returned if no other methods provide a value. If a ``convert`` function is provided,
    ``default`` will be converted before being used.

    A ``convert`` argument may be provided to convert values before they are
    returned. For instance to concert log levels in environment variables
    to ``logging`` module values. If a ``convert`` function is provided, it must support
    str as valid input type.

    :param str name: the name of the setting
    :param str env_var: the name of an environment variable to check for the setting
    :param callable system_hook: a function that will attempt to look up a value for the setting
    :param default: an implicit default value for the setting
    :type default: any
    :param callable convert: a function to convert values before they are returned
    '''
    def __init__(self, name: str, env_var: str | None = None, system_hook: Callable[[], ValidInputType] | None = None, default: ValidInputType | _Unset = ..., convert: Callable[[ValidInputType | str], ValueType] | None = None) -> None: ...
    def __call__(self, value: ValidInputType | None = None) -> ValueType:
        """Return the setting value according to the standard precedence.

        :param value: value
        :type value: str or int or float or None
        :returns: the value of the setting
        :rtype: str or int or float
        :raises: RuntimeError if no value can be determined
        """
    def __get__(self, instance: Any, owner: Any | None = None) -> PrioritizedSetting[ValidInputType, ValueType]: ...
    def __set__(self, instance: Any, value: ValidInputType) -> None: ...
    def set_value(self, value: ValidInputType) -> None:
        """Specify a value for this setting programmatically.

        A value set this way takes precedence over all other methods except
        immediate values.

        :param value: a user-set value for this setting
        :type value: str or int or float
        """
    def unset_value(self) -> None:
        """Unset the previous user value such that the priority is reset."""
    @property
    def env_var(self) -> str | None: ...
    @property
    def default(self) -> ValidInputType | _Unset: ...

class Settings:
    """Settings for globally used Azure configuration values.

    You probably don't want to create an instance of this class, but call the singleton instance:

    .. code-block:: python

        from azure.core.settings import settings
        settings.log_level = log_level = logging.DEBUG

    The following methods are searched in order for a setting:

    4. immediate values
    3. previously user-set value
    2. environment variable
    1. system setting
    0. implicit default

    An implicit default is (optionally) defined by the setting attribute itself.

    A system setting value can be obtained from registries or other OS configuration
    for settings that support that method.

    An environment variable value is obtained from ``os.environ``

    User-set values many be specified by assigning to the attribute:

    .. code-block:: python

        settings.log_level = log_level = logging.DEBUG

    Immediate values are (optionally) provided when the setting is retrieved:

    .. code-block:: python

        settings.log_level(logging.DEBUG())

    Immediate values are most often useful to provide from optional arguments
    to client functions. If the argument value is not None, it will be returned
    as-is. Otherwise, the setting searches other methods according to the
    precedence rules.

    Immutable configuration snapshots can be created with the following methods:

    * settings.defaults returns the base defaultsvalues , ignoring any environment or system
      or user settings

    * settings.current returns the current computation of settings including prioritization
      of configuration sources, unless defaults_only is set to True (in which case the result
      is identical to settings.defaults)

    * settings.config can be called with specific values to override what settings.current
      would provide

    .. code-block:: python

        # return current settings with log level overridden
        settings.config(log_level=logging.DEBUG)

    :cvar log_level: a log level to use across all Azure client SDKs (AZURE_LOG_LEVEL)
    :type log_level: PrioritizedSetting
    :cvar tracing_enabled: Whether tracing should be enabled across Azure SDKs (AZURE_TRACING_ENABLED)
    :type tracing_enabled: PrioritizedSetting
    :cvar tracing_implementation: The tracing implementation to use (AZURE_SDK_TRACING_IMPLEMENTATION)
    :type tracing_implementation: PrioritizedSetting

    :Example:

    >>> import logging
    >>> from azure.core.settings import settings
    >>> settings.log_level = logging.DEBUG
    >>> settings.log_level()
    10

    >>> settings.log_level(logging.WARN)
    30

    """
    def __init__(self) -> None: ...
    @property
    def defaults_only(self) -> bool:
        """Whether to ignore environment and system settings and return only base default values.

        :rtype: bool
        :returns: Whether to ignore environment and system settings and return only base default values.
        """
    @defaults_only.setter
    def defaults_only(self, value: bool) -> None: ...
    @property
    def defaults(self) -> Tuple[Any, ...]:
        """Return implicit default values for all settings, ignoring environment and system.

        :rtype: namedtuple
        :returns: The implicit default values for all settings
        """
    @property
    def current(self) -> Tuple[Any, ...]:
        """Return the current values for all settings.

        :rtype: namedtuple
        :returns: The current values for all settings
        """
    def config(self, **kwargs: Any) -> Tuple[Any, ...]:
        """Return the currently computed settings, with values overridden by parameter values.

        :keyword dict kwargs: Settings to override
        :rtype: namedtuple
        :returns: The current values for all settings, with values overridden by parameter values

        Examples:

        .. code-block:: python

           # return current settings with log level overridden
           settings.config(log_level=logging.DEBUG)

        """
    log_level: PrioritizedSetting[str | int, int]
    tracing_enabled: PrioritizedSetting[str | bool, bool]
    tracing_implementation: PrioritizedSetting[str | Type[AbstractSpan] | None, Type[AbstractSpan] | None]

settings: Settings
