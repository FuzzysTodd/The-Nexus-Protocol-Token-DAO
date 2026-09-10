import typing
from . import exceptions as exceptions, utils as utils
from _typeshed import Incomplete
from redis import client

logger: Incomplete
DEFAULT_UNAVAILABLE_TIMEOUT: int
DEFAULT_THREAD_SLEEP_TIME: float

class PubSubWorkerThread(client.PubSubWorkerThread):
    def run(self) -> None: ...

class RedisLock(utils.LockBase):
    """
    An extremely reliable Redis lock based on pubsub with a keep-alive thread

    As opposed to most Redis locking systems based on key/value pairs,
    this locking method is based on the pubsub system. The big advantage is
    that if the connection gets killed due to network issues, crashing
    processes or otherwise, it will still immediately unlock instead of
    waiting for a lock timeout.

    To make sure both sides of the lock know about the connection state it is
    recommended to set the `health_check_interval` when creating the redis
    connection..

    Args:
        channel: the redis channel to use as locking key.
        connection: an optional redis connection if you already have one
        or if you need to specify the redis connection
        timeout: timeout when trying to acquire a lock
        check_interval: check interval while waiting
        fail_when_locked: after the initial lock failed, return an error
            or lock the file. This does not wait for the timeout.
        thread_sleep_time: sleep time between fetching messages from redis to
            prevent a busy/wait loop. In the case of lock conflicts this
            increases the time it takes to resolve the conflict. This should
            be smaller than the `check_interval` to be useful.
        unavailable_timeout: If the conflicting lock is properly connected
            this should never exceed twice your redis latency. Note that this
            will increase the wait time possibly beyond your `timeout` and is
            always executed if a conflict arises.
        redis_kwargs: The redis connection arguments if no connection is
            given. The `DEFAULT_REDIS_KWARGS` are used as default, if you want
            to override these you need to explicitly specify a value (e.g.
            `health_check_interval=0`)

    """
    redis_kwargs: typing.Dict[str, typing.Any]
    thread: PubSubWorkerThread | None
    channel: str
    timeout: float
    connection: client.Redis | None
    pubsub: client.PubSub | None
    close_connection: bool
    DEFAULT_REDIS_KWARGS: typing.ClassVar[typing.Dict[str, typing.Any]]
    thread_sleep_time: Incomplete
    unavailable_timeout: Incomplete
    def __init__(self, channel: str, connection: client.Redis | None = None, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = False, thread_sleep_time: float = ..., unavailable_timeout: float = ..., redis_kwargs: typing.Dict | None = None) -> None: ...
    def get_connection(self) -> client.Redis: ...
    def channel_handler(self, message) -> None: ...
    @property
    def client_name(self): ...
    def acquire(self, timeout: float | None = None, check_interval: float | None = None, fail_when_locked: bool | None = None): ...
    def check_or_kill_lock(self, connection, timeout): ...
    def release(self) -> None: ...
    def __del__(self) -> None: ...
