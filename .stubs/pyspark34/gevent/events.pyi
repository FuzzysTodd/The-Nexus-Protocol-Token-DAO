from _typeshed import Incomplete
from zope.event import subscribers as subscribers
from zope.interface import Interface

__all__ = ['subscribers', 'IEventLoopBlocked', 'EventLoopBlocked', 'IMemoryUsageThresholdExceeded', 'MemoryUsageThresholdExceeded', 'IMemoryUsageUnderThreshold', 'MemoryUsageUnderThreshold', 'IPeriodicMonitorThread', 'IPeriodicMonitorThreadStartedEvent', 'PeriodicMonitorThreadStartedEvent', 'IGeventPatchEvent', 'GeventPatchEvent', 'IGeventWillPatchEvent', 'DoNotPatch', 'GeventWillPatchEvent', 'IGeventDidPatchEvent', 'IGeventWillPatchModuleEvent', 'GeventWillPatchModuleEvent', 'IGeventDidPatchModuleEvent', 'GeventDidPatchModuleEvent', 'IGeventWillPatchAllEvent', 'GeventWillPatchAllEvent', 'IGeventDidPatchBuiltinModulesEvent', 'GeventDidPatchBuiltinModulesEvent', 'IGeventDidPatchAllEvent', 'GeventDidPatchAllEvent']

subscribers = subscribers

class IPeriodicMonitorThread(Interface):
    """
    The contract for the periodic monitoring thread that is started
    by the hub.
    """
    def add_monitoring_function(function, period) -> None:
        """
        Schedule the *function* to be called approximately every *period* fractional seconds.

        The *function* receives one argument, the hub being monitored. It is called
        in the monitoring thread, *not* the hub thread. It **must not** attempt to
        use the gevent asynchronous API.

        If the *function* is already a monitoring function, then its *period*
        will be updated for future runs.

        If the *period* is ``None``, then the function will be removed.

        A *period* less than or equal to zero is not allowed.
        """

class IPeriodicMonitorThreadStartedEvent(Interface):
    """
    The event emitted when a hub starts a periodic monitoring thread.

    You can use this event to add additional monitoring functions.
    """
    monitor: Incomplete

class PeriodicMonitorThreadStartedEvent:
    """
    The implementation of :class:`IPeriodicMonitorThreadStartedEvent`.
    """
    ENTRY_POINT_NAME: str
    monitor: Incomplete
    def __init__(self, monitor) -> None: ...

class IEventLoopBlocked(Interface):
    """
    The event emitted when the event loop is blocked.

    This event is emitted in the monitor thread.
    """
    greenlet: Incomplete
    blocking_time: Incomplete
    info: Incomplete

class EventLoopBlocked:
    """
    The event emitted when the event loop is blocked.

    Implements `IEventLoopBlocked`.
    """
    greenlet: Incomplete
    blocking_time: Incomplete
    info: Incomplete
    def __init__(self, greenlet, blocking_time, info) -> None: ...

class IMemoryUsageThresholdExceeded(Interface):
    """
    The event emitted when the memory usage threshold is exceeded.

    This event is emitted only while memory continues to grow
    above the threshold. Only if the condition or stabilized is corrected (memory
    usage drops) will the event be emitted in the future.

    This event is emitted in the monitor thread.
    """
    mem_usage: Incomplete
    max_allowed: Incomplete
    memory_info: Incomplete

class _AbstractMemoryEvent:
    mem_usage: Incomplete
    max_allowed: Incomplete
    memory_info: Incomplete
    def __init__(self, mem_usage, max_allowed, memory_info) -> None: ...

class MemoryUsageThresholdExceeded(_AbstractMemoryEvent):
    """
    Implementation of `IMemoryUsageThresholdExceeded`.
    """

class IMemoryUsageUnderThreshold(Interface):
    """
    The event emitted when the memory usage drops below the
    threshold after having previously been above it.

    This event is emitted only the first time memory usage is detected
    to be below the threshold after having previously been above it.
    If memory usage climbs again, a `IMemoryUsageThresholdExceeded`
    event will be broadcast, and then this event could be broadcast again.

    This event is emitted in the monitor thread.
    """
    mem_usage: Incomplete
    max_allowed: Incomplete
    max_memory_usage: Incomplete
    memory_info: Incomplete

class MemoryUsageUnderThreshold(_AbstractMemoryEvent):
    """
    Implementation of `IMemoryUsageUnderThreshold`.
    """
    max_memory_usage: Incomplete
    def __init__(self, mem_usage, max_allowed, memory_info, max_usage) -> None: ...

class IGeventPatchEvent(Interface):
    """
    The root for all monkey-patch events gevent emits.
    """
    source: Incomplete
    target: Incomplete

class GeventPatchEvent:
    """
    Implementation of `IGeventPatchEvent`.
    """
    source: Incomplete
    target: Incomplete
    def __init__(self, source, target) -> None: ...

class IGeventWillPatchEvent(IGeventPatchEvent):
    """
    An event emitted *before* gevent monkey-patches something.

    If a subscriber raises `DoNotPatch`, then patching this particular
    item will not take place.
    """
class DoNotPatch(BaseException):
    """
    Subscribers to will-patch events can raise instances
    of this class to tell gevent not to patch that particular item.
    """
class GeventWillPatchEvent(GeventPatchEvent):
    """
    Implementation of `IGeventWillPatchEvent`.
    """
class IGeventDidPatchEvent(IGeventPatchEvent):
    """
    An event emitted *after* gevent has patched something.
    """
class GeventDidPatchEvent(GeventPatchEvent):
    """
    Implementation of `IGeventDidPatchEvent`.
    """

class IGeventWillPatchModuleEvent(IGeventWillPatchEvent):
    """
    An event emitted *before* gevent begins patching a specific module.

    Both *source* and *target* attributes are module objects.
    """
    module_name: Incomplete
    target_item_names: Incomplete

class GeventWillPatchModuleEvent(GeventWillPatchEvent):
    """
    Implementation of `IGeventWillPatchModuleEvent`.
    """
    ENTRY_POINT_NAME: str
    module_name: Incomplete
    target_item_names: Incomplete
    def __init__(self, module_name, source, target, items) -> None: ...

class IGeventDidPatchModuleEvent(IGeventDidPatchEvent):
    """
    An event emitted *after* gevent has completed patching a specific
    module.
    """
    module_name: Incomplete

class GeventDidPatchModuleEvent(GeventDidPatchEvent):
    """
    Implementation of `IGeventDidPatchModuleEvent`.
    """
    ENTRY_POINT_NAME: str
    module_name: Incomplete
    def __init__(self, module_name, source, target) -> None: ...

class IGeventWillPatchAllEvent(IGeventWillPatchEvent):
    """
    An event emitted *before* gevent begins patching the system.

    Following this event will be a series of
    `IGeventWillPatchModuleEvent` and `IGeventDidPatchModuleEvent` for
    each patched module.

    Once the gevent builtin modules have been processed,
    `IGeventDidPatchBuiltinModulesEvent` will be emitted. Processing
    this event is an ideal time for third-party modules to be imported
    and patched (which may trigger its own will/did patch module
    events).

    Finally, a `IGeventDidPatchAllEvent` will be sent.

    If a subscriber to this event raises `DoNotPatch`, no patching
    will be done.

    The *source* and *target* attributes have undefined values.
    """
    patch_all_arguments: Incomplete
    patch_all_kwargs: Incomplete
    def will_patch_module(module_name) -> None:
        """
        Return whether the module named *module_name* will be patched.
        """

class _PatchAllMixin:
    def __init__(self, patch_all_arguments, patch_all_kwargs) -> None: ...
    @property
    def patch_all_arguments(self): ...
    @property
    def patch_all_kwargs(self): ...

class GeventWillPatchAllEvent(_PatchAllMixin, GeventWillPatchEvent):
    """
    Implementation of `IGeventWillPatchAllEvent`.
    """
    ENTRY_POINT_NAME: str
    def will_patch_module(self, module_name): ...

class IGeventDidPatchBuiltinModulesEvent(IGeventDidPatchEvent):
    """
    Event emitted *after* the builtin modules have been patched.

    If you're going to monkey-patch a third-party library, this is
    usually the event to listen for.

    The values of the *source* and *target* attributes are undefined.
    """
    patch_all_arguments: Incomplete
    patch_all_kwargs: Incomplete

class GeventDidPatchBuiltinModulesEvent(_PatchAllMixin, GeventDidPatchEvent):
    """
    Implementation of `IGeventDidPatchBuiltinModulesEvent`.
    """
    ENTRY_POINT_NAME: str

class IGeventDidPatchAllEvent(IGeventDidPatchEvent):
    """
    Event emitted after gevent has patched all modules, both builtin
    and those provided by plugins/subscribers.

    The values of the *source* and *target* attributes are undefined.
    """

class GeventDidPatchAllEvent(_PatchAllMixin, GeventDidPatchEvent):
    """
    Implementation of `IGeventDidPatchAllEvent`.
    """
    ENTRY_POINT_NAME: str
