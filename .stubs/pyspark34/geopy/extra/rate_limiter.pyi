from _typeshed import Incomplete

__all__ = ['AsyncRateLimiter', 'RateLimiter']

class BaseRateLimiter:
    """Base Rate Limiter class for both sync and async versions."""
    min_delay_seconds: Incomplete
    max_retries: Incomplete
    swallow_exceptions: Incomplete
    return_value_on_exception: Incomplete
    def __init__(self, *, min_delay_seconds, max_retries, swallow_exceptions, return_value_on_exception) -> None: ...

class RateLimiter(BaseRateLimiter):
    '''This is a Rate Limiter implementation for synchronous functions
    (like geocoders with the default :class:`geopy.adapters.BaseSyncAdapter`).

    Examples::

        from geopy.extra.rate_limiter import RateLimiter
        from geopy.geocoders import Nominatim

        geolocator = Nominatim(user_agent="specify_your_app_name_here")

        search = ["moscow", "paris", "berlin", "tokyo", "beijing"]
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        locations = [geocode(s) for s in search]

        search = [
            (55.47, 37.32), (48.85, 2.35), (52.51, 13.38),
            (34.69, 139.40), (39.90, 116.39)
        ]
        reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)
        locations = [reverse(s) for s in search]

    RateLimiter class is thread-safe. If geocoding service\'s responses
    are slower than `min_delay_seconds`, then you can benefit from
    parallelizing the work::

        import concurrent.futures

        geolocator = OpenMapQuest(api_key="...")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1/20)

        with concurrent.futures.ThreadPoolExecutor() as e:
            locations = list(e.map(geocode, search))

    .. versionchanged:: 2.0
       Added thread-safety support.
    '''
    func: Incomplete
    error_wait_seconds: Incomplete
    def __init__(self, func, *, min_delay_seconds: float = 0.0, max_retries: int = 2, error_wait_seconds: float = 5.0, swallow_exceptions: bool = True, return_value_on_exception: Incomplete | None = None) -> None:
        """
        :param callable func:
            A function which should be wrapped by the rate limiter.

        :param float min_delay_seconds:
            Minimum delay in seconds between the wrapped ``func`` calls.
            To convert :abbr:`RPS (Requests Per Second)` rate to
            ``min_delay_seconds`` you need to divide 1 by RPS. For example,
            if you need to keep the rate at 20 RPS, you can use
            ``min_delay_seconds=1/20``.

        :param int max_retries:
            Number of retries on exceptions. Only
            :class:`geopy.exc.GeocoderServiceError` exceptions are
            retried -- others are always re-raised. ``max_retries + 1``
            requests would be performed at max per query. Set
            ``max_retries=0`` to disable retries.

        :param float error_wait_seconds:
            Time to wait between retries after errors. Must be
            greater or equal to ``min_delay_seconds``.

        :param bool swallow_exceptions:
            Should an exception be swallowed after retries? If not,
            it will be re-raised. If yes, the ``return_value_on_exception``
            will be returned.

        :param return_value_on_exception:
            Value to return on failure when ``swallow_exceptions=True``.

        """
    def __call__(self, *args, **kwargs): ...

class AsyncRateLimiter(BaseRateLimiter):
    '''This is a Rate Limiter implementation for asynchronous functions
    (like geocoders with :class:`geopy.adapters.BaseAsyncAdapter`).

    Examples::

        from geopy.adapters import AioHTTPAdapter
        from geopy.extra.rate_limiter import AsyncRateLimiter
        from geopy.geocoders import Nominatim

        async with Nominatim(
            user_agent="specify_your_app_name_here",
            adapter_factory=AioHTTPAdapter,
        ) as geolocator:

            search = ["moscow", "paris", "berlin", "tokyo", "beijing"]
            geocode = AsyncRateLimiter(geolocator.geocode, min_delay_seconds=1)
            locations = [await geocode(s) for s in search]

            search = [
                (55.47, 37.32), (48.85, 2.35), (52.51, 13.38),
                (34.69, 139.40), (39.90, 116.39)
            ]
            reverse = AsyncRateLimiter(geolocator.reverse, min_delay_seconds=1)
            locations = [await reverse(s) for s in search]

    AsyncRateLimiter class is safe to use across multiple concurrent tasks.
    If geocoding service\'s responses are slower than `min_delay_seconds`,
    then you can benefit from parallelizing the work::

        import asyncio

        async with OpenMapQuest(
            api_key="...", adapter_factory=AioHTTPAdapter
        ) as geolocator:

            geocode = AsyncRateLimiter(geolocator.geocode, min_delay_seconds=1/20)
            locations = await asyncio.gather(*(geocode(s) for s in search))

    .. versionadded:: 2.0
    '''
    func: Incomplete
    error_wait_seconds: Incomplete
    def __init__(self, func, *, min_delay_seconds: float = 0.0, max_retries: int = 2, error_wait_seconds: float = 5.0, swallow_exceptions: bool = True, return_value_on_exception: Incomplete | None = None) -> None:
        """
        :param callable func:
            A function which should be wrapped by the rate limiter.

        :param float min_delay_seconds:
            Minimum delay in seconds between the wrapped ``func`` calls.
            To convert :abbr:`RPS (Requests Per Second)` rate to
            ``min_delay_seconds`` you need to divide 1 by RPS. For example,
            if you need to keep the rate at 20 RPS, you can use
            ``min_delay_seconds=1/20``.

        :param int max_retries:
            Number of retries on exceptions. Only
            :class:`geopy.exc.GeocoderServiceError` exceptions are
            retried -- others are always re-raised. ``max_retries + 1``
            requests would be performed at max per query. Set
            ``max_retries=0`` to disable retries.

        :param float error_wait_seconds:
            Time to wait between retries after errors. Must be
            greater or equal to ``min_delay_seconds``.

        :param bool swallow_exceptions:
            Should an exception be swallowed after retries? If not,
            it will be re-raised. If yes, the ``return_value_on_exception``
            will be returned.

        :param return_value_on_exception:
            Value to return on failure when ``swallow_exceptions=True``.

        """
    async def __call__(self, *args, **kwargs): ...
