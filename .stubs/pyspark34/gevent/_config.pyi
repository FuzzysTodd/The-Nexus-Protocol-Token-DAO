from _typeshed import Incomplete

__all__ = ['config']

class SettingType(type):
    def __new__(cls, name, bases, cls_dict): ...
    def fmt_desc(cls, desc): ...
convert_str_value_as_is = validate_anything

class Setting:
    name: Incomplete
    value: Incomplete
    validate: Incomplete
    default: Incomplete
    environment_key: Incomplete
    document: bool
    desc: str
    def get(self): ...
    def set(self, val) -> None: ...

class Config:
    """
    Global configuration for gevent.

    There is one instance of this object at ``gevent.config``. If you
    are going to make changes in code, instead of using the documented
    environment variables, you need to make the changes before using
    any parts of gevent that might need those settings. For example::

        >>> from gevent import config
        >>> config.fileobject = 'thread'

        >>> from gevent import fileobject
        >>> fileobject.FileObject.__name__
        'FileObjectThread'

    .. versionadded:: 1.3a2

    """
    settings: Incomplete
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def set(self, name, value) -> None: ...
    def __dir__(self): ...
    def print_help(self) -> None: ...

class ImportableSetting:
    shortname_map: Incomplete
    def validate(self, value): ...
    def get_options(self): ...

class BoolSettingMixin:
    validate: Incomplete

class IntSettingMixin:
    validate: Incomplete

class _PositiveValueMixin:
    def validate(self, value): ...

class FloatSettingMixin(_PositiveValueMixin): ...
class ByteCountSettingMixin(_PositiveValueMixin): ...

class Resolver(ImportableSetting, Setting):
    desc: str
    default: Incomplete
    shortname_map: Incomplete

class Threadpool(ImportableSetting, Setting):
    desc: str
    default: str

class ThreadpoolIdleTaskTimeout(FloatSettingMixin, Setting):
    document: bool
    name: str
    environment_key: str
    desc: str
    default: float

class Loop(ImportableSetting, Setting):
    desc: str
    default: Incomplete
    shortname_map: Incomplete

class FormatContext(ImportableSetting, Setting):
    name: str
    default: str

class LibevBackend(Setting):
    name: str
    environment_key: str
    desc: str
    default: Incomplete
    validate: Incomplete

class FileObject(ImportableSetting, Setting):
    desc: str
    environment_key: str
    default: Incomplete
    shortname_map: Incomplete

class WatchChildren(BoolSettingMixin, Setting):
    desc: str
    name: str
    environment_key: str
    default: bool

class TraceMalloc(IntSettingMixin, Setting):
    name: str
    environment_key: str
    default: bool
    desc: str

class TrackGreenletTree(BoolSettingMixin, Setting):
    name: str
    environment_key: str
    default: bool
    desc: str

class MonitorThread(BoolSettingMixin, Setting):
    name: str
    environment_key: str
    default: bool
    desc: str

class MaxBlockingTime(FloatSettingMixin, Setting):
    name: str
    environment_key: str
    default: float
    desc: str

class MonitorMemoryPeriod(FloatSettingMixin, Setting):
    name: str
    environment_key: str
    default: int
    desc: str

class MonitorMemoryMaxUsage(ByteCountSettingMixin, Setting):
    name: str
    environment_key: str
    default: Incomplete
    desc: str

class AresSettingMixin:
    document: bool
    @property
    def kwarg_name(self): ...
    validate: Incomplete

class AresFlags(AresSettingMixin, Setting):
    name: str
    default: Incomplete
    environment_key: str

class AresTimeout(AresSettingMixin, Setting):
    document: bool
    name: str
    default: Incomplete
    environment_key: str
    desc: str

class AresTries(AresSettingMixin, Setting):
    name: str
    default: Incomplete
    environment_key: str

class AresNdots(AresSettingMixin, Setting):
    name: str
    default: Incomplete
    environment_key: str

class AresUDPPort(AresSettingMixin, Setting):
    name: str
    default: Incomplete
    environment_key: str

class AresTCPPort(AresSettingMixin, Setting):
    name: str
    default: Incomplete
    environment_key: str

class AresServers(AresSettingMixin, Setting):
    document: bool
    name: str
    default: Incomplete
    environment_key: str
    desc: str

class ResolverNameservers(AresSettingMixin, Setting):
    document: bool
    name: str
    default: Incomplete
    environment_key: str
    desc: str
    @property
    def kwarg_name(self): ...

class ResolverTimeout(FloatSettingMixin, AresSettingMixin, Setting):
    document: bool
    name: str
    environment_key: str
    desc: str
    @property
    def kwarg_name(self): ...

config: Incomplete
