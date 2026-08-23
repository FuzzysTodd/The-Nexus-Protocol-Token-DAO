class AsyncThread:
    def __init__(self) -> None: ...
    def terminate(self) -> None: ...
    def __del__(self) -> None: ...
    def submit(self, func, *args, **kwargs):
        """
        Run async func with args/kwargs in separate thread, returns Future object.
        """
    def wrap(self, func): ...
    def call_soon(self, func, *args):
        """
        Call normal (non-async) function with arguments in the processing thread
        it's just a wrapper over `loop.call_soon_threadsafe()`

        Returns a handle with `.cancel`, not a full on Future
        """
    @property
    def loop(self): ...
