class Stopwatch:
    """Deprecated zmq.Stopwatch implementation

    You can use Python's builtin timers (time.monotonic, etc.).
    """
    def __init__(self) -> None: ...
    def start(self) -> None:
        """Start the counter"""
    def stop(self):
        """Return time since start in microseconds"""
