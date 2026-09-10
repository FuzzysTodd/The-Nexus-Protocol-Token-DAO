from _typeshed import Incomplete
from collections import MutableMapping

class _ExpiringMapping(MutableMapping):
    def __init__(self, mapping: Incomplete | None = None, capacity: Incomplete | None = None, expires_in: Incomplete | None = None, lock: Incomplete | None = None, *args, **kwargs) -> None:
        """Items in this mapping can have individual shelf life,
        just like food items in your refrigerator have their different shelf life
        determined by each food, not by the refrigerator.

        Expired items will be automatically evicted.
        The clean-up will be done at each time when adding a new item,
        or when looping or counting the entire mapping.
        (This is better than being done indecisively by a background thread,
        which might not always happen before your accessing the mapping.)

        This implementation uses no dependency other than Python standard library.

        :param MutableMapping mapping:
            A dict-like key-value mapping, which needs to support __setitem__(),
            __getitem__(), __delitem__(), get(), pop().

            The default mapping is an in-memory dict.

            You could potentially supply a file-based dict-like object, too.
            This implementation deliberately avoid mapping.__iter__(),
            which could be slow on a file-based mapping.

        :param int capacity:
            How many items this mapping will hold.
            When you attempt to add new item into a full mapping,
            it will automatically delete the item that is expiring soonest.

            The default value is None, which means there is no capacity limit.

        :param int expires_in:
            How many seconds an item would expire and be purged from this mapping.
            Also known as time-to-live (TTL).
            You can also use :func:`~set()` to provide per-item expires_in value.

        :param Lock lock:
            A locking mechanism with context manager interface.
            If no lock is provided, a threading.Lock will be used.
            But you may want to supply a different lock,
            if your customized mapping is being shared differently.
        """
    def set(self, key, value, expires_in) -> None:
        """It sets the key-value pair into this mapping, with its per-item expires_in.

        It will take O(logN) time, because it will run some maintenance.
        This worse-than-constant time is acceptable, because in a cache scenario,
        __setitem__() would only be called during a cache miss,
        which would already incur an expensive target function call anyway.

        By the way, most other methods of this mapping still have O(1) constant time.
        """
    def __setitem__(self, key, value) -> None:
        """Implements the __setitem__().

        Same characteristic as :func:`~set()`,
        but use class-wide expires_in which was specified by :func:`~__init__()`.
        """
    def __getitem__(self, key):
        """If the item you requested already expires, KeyError will be raised."""
    def __delitem__(self, key) -> None:
        """If the item you requested already expires, KeyError will be raised."""
    def __len__(self) -> int:
        """Drop all expired items and return the remaining length"""
    def __iter__(self):
        """Drop all expired items and return an iterator of the remaining items"""

class _IndividualCache:
    def __init__(self, mapping: Incomplete | None = None, key_maker: Incomplete | None = None, expires_in: Incomplete | None = None) -> None:
        '''Constructs a cache decorator that allows item-by-item control on
        how to cache the return value of the decorated function.

        :param MutableMapping mapping:
            The cached items will be stored inside.
            You\'d want to use a ExpiringMapping
            if you plan to utilize the ``expires_in`` behavior.

            If nothing is provided, an in-memory dict will be used,
            but it will provide no expiry functionality.

            .. note::

                When using this class as a decorator,
                your mapping needs to be available at "compile" time,
                so it would typically be a global-, module- or class-level mapping::

                    module_mapping = {}

                    @IndividualCache(mapping=module_mapping, ...)
                    def foo():
                        ...

                If you want to use a mapping available only at run-time,
                you have to manually decorate your function at run-time, too::

                    def foo():
                        ...

                    def bar(runtime_mapping):
                        foo = IndividualCache(mapping=runtime_mapping...)(foo)

        :param callable key_maker:
            A callable which should have signature as
            ``lambda function, args, kwargs: "return a string as key"``.

            If key_maker happens to return ``None``, the cache will be bypassed,
            the underlying function will be invoked directly,
            and the invoke result will not be cached either.

        :param callable expires_in:
            The default value is ``None``,
            which means the content being cached has no per-item expiry,
            and will subject to the underlying mapping\'s global expiry time.

            It can be an integer indicating
            how many seconds the result will be cached.
            In particular, if the value is 0,
            it means the result expires after zero second (i.e. immediately),
            therefore the result will *not* be cached.
            (Mind the difference between ``expires_in=0`` and ``expires_in=None``.)

            Or it can be a callable with the signature as
            ``lambda function=function, args=args, kwargs=kwargs, result=result: 123``
            to calculate the expiry on the fly.
            Its return value will be interpreted in the same way as above.
        '''
    def __call__(self, function): ...
