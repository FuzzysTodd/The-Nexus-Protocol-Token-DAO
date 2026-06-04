import abc
from .key_processor import KeyPressEvent
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.keys import Keys
from typing import Callable, Sequence, Tuple, TypeVar

__all__ = ['NotImplementedOrNone', 'Binding', 'KeyBindingsBase', 'KeyBindings', 'ConditionalKeyBindings', 'merge_key_bindings', 'DynamicKeyBindings', 'GlobalOnlyKeyBindings']

NotImplementedOrNone = object

class Binding:
    """
    Key binding: (key sequence + handler + filter).
    (Immutable binding class.)

    :param record_in_macro: When True, don't record this key binding when a
        macro is recorded.
    """
    keys: Incomplete
    handler: Incomplete
    filter: Incomplete
    eager: Incomplete
    is_global: Incomplete
    save_before: Incomplete
    record_in_macro: Incomplete
    def __init__(self, keys: tuple[Keys | str, ...], handler: KeyHandlerCallable, filter: FilterOrBool = True, eager: FilterOrBool = False, is_global: FilterOrBool = False, save_before: Callable[[KeyPressEvent], bool] = ..., record_in_macro: FilterOrBool = True) -> None: ...
    def call(self, event: KeyPressEvent) -> None: ...
KeysTuple = Tuple[Keys | str, ...]

class KeyBindingsBase(metaclass=ABCMeta):
    """
    Interface for a KeyBindings.
    """
    @abstractmethod
    def get_bindings_for_keys(self, keys: KeysTuple) -> list[Binding]:
        """
        Return a list of key bindings that can handle these keys.
        (This return also inactive bindings, so the `filter` still has to be
        called, for checking it.)

        :param keys: tuple of keys.
        """
    @abstractmethod
    def get_bindings_starting_with_keys(self, keys: KeysTuple) -> list[Binding]:
        """
        Return a list of key bindings that handle a key sequence starting with
        `keys`. (It does only return bindings for which the sequences are
        longer than `keys`. And like `get_bindings_for_keys`, it also includes
        inactive bindings.)

        :param keys: tuple of keys.
        """
    @property
    @abc.abstractmethod
    def bindings(self) -> list[Binding]:
        """
        List of `Binding` objects.
        (These need to be exposed, so that `KeyBindings` objects can be merged
        together.)
        """
T = TypeVar('T', bound=KeyHandlerCallable | Binding)

class KeyBindings(KeyBindingsBase):
    """
    A container for a set of key bindings.

    Example usage::

        kb = KeyBindings()

        @kb.add('c-t')
        def _(event):
            print('Control-T pressed')

        @kb.add('c-a', 'c-b')
        def _(event):
            print('Control-A pressed, followed by Control-B')

        @kb.add('c-x', filter=is_searching)
        def _(event):
            print('Control-X pressed')  # Works only if we are searching.

    """
    def __init__(self) -> None: ...
    @property
    def bindings(self) -> list[Binding]: ...
    def add(self, *keys: Keys | str, filter: FilterOrBool = True, eager: FilterOrBool = False, is_global: FilterOrBool = False, save_before: Callable[[KeyPressEvent], bool] = ..., record_in_macro: FilterOrBool = True) -> Callable[[T], T]:
        """
        Decorator for adding a key bindings.

        :param filter: :class:`~prompt_toolkit.filters.Filter` to determine
            when this key binding is active.
        :param eager: :class:`~prompt_toolkit.filters.Filter` or `bool`.
            When True, ignore potential longer matches when this key binding is
            hit. E.g. when there is an active eager key binding for Ctrl-X,
            execute the handler immediately and ignore the key binding for
            Ctrl-X Ctrl-E of which it is a prefix.
        :param is_global: When this key bindings is added to a `Container` or
            `Control`, make it a global (always active) binding.
        :param save_before: Callable that takes an `Event` and returns True if
            we should save the current buffer, before handling the event.
            (That's the default.)
        :param record_in_macro: Record these key bindings when a macro is
            being recorded. (True by default.)
        """
    def remove(self, *args: Keys | str | KeyHandlerCallable) -> None:
        """
        Remove a key binding.

        This expects either a function that was given to `add` method as
        parameter or a sequence of key bindings.

        Raises `ValueError` when no bindings was found.

        Usage::

            remove(handler)  # Pass handler.
            remove('c-x', 'c-a')  # Or pass the key bindings.
        """
    add_binding = add
    remove_binding = remove
    def get_bindings_for_keys(self, keys: KeysTuple) -> list[Binding]:
        """
        Return a list of key bindings that can handle this key.
        (This return also inactive bindings, so the `filter` still has to be
        called, for checking it.)

        :param keys: tuple of keys.
        """
    def get_bindings_starting_with_keys(self, keys: KeysTuple) -> list[Binding]:
        """
        Return a list of key bindings that handle a key sequence starting with
        `keys`. (It does only return bindings for which the sequences are
        longer than `keys`. And like `get_bindings_for_keys`, it also includes
        inactive bindings.)

        :param keys: tuple of keys.
        """

class _Proxy(KeyBindingsBase):
    """
    Common part for ConditionalKeyBindings and _MergedKeyBindings.
    """
    def __init__(self) -> None: ...
    @property
    def bindings(self) -> list[Binding]: ...
    def get_bindings_for_keys(self, keys: KeysTuple) -> list[Binding]: ...
    def get_bindings_starting_with_keys(self, keys: KeysTuple) -> list[Binding]: ...

class ConditionalKeyBindings(_Proxy):
    """
    Wraps around a `KeyBindings`. Disable/enable all the key bindings according to
    the given (additional) filter.::

        @Condition
        def setting_is_true():
            return True  # or False

        registry = ConditionalKeyBindings(key_bindings, setting_is_true)

    When new key bindings are added to this object. They are also
    enable/disabled according to the given `filter`.

    :param registries: List of :class:`.KeyBindings` objects.
    :param filter: :class:`~prompt_toolkit.filters.Filter` object.
    """
    key_bindings: Incomplete
    filter: Incomplete
    def __init__(self, key_bindings: KeyBindingsBase, filter: FilterOrBool = True) -> None: ...

class _MergedKeyBindings(_Proxy):
    """
    Merge multiple registries of key bindings into one.

    This class acts as a proxy to multiple :class:`.KeyBindings` objects, but
    behaves as if this is just one bigger :class:`.KeyBindings`.

    :param registries: List of :class:`.KeyBindings` objects.
    """
    registries: Incomplete
    def __init__(self, registries: Sequence[KeyBindingsBase]) -> None: ...

def merge_key_bindings(bindings: Sequence[KeyBindingsBase]) -> _MergedKeyBindings:
    """
    Merge multiple :class:`.Keybinding` objects together.

    Usage::

        bindings = merge_key_bindings([bindings1, bindings2, ...])
    """

class DynamicKeyBindings(_Proxy):
    """
    KeyBindings class that can dynamically returns any KeyBindings.

    :param get_key_bindings: Callable that returns a :class:`.KeyBindings` instance.
    """
    get_key_bindings: Incomplete
    def __init__(self, get_key_bindings: Callable[[], KeyBindingsBase | None]) -> None: ...

class GlobalOnlyKeyBindings(_Proxy):
    """
    Wrapper around a :class:`.KeyBindings` object that only exposes the global
    key bindings.
    """
    key_bindings: Incomplete
    def __init__(self, key_bindings: KeyBindingsBase) -> None: ...
