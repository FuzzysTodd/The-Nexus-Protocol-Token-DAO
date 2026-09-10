class TrioRunner:
    """A trio loop runner."""
    def __init__(self) -> None:
        """Initialize the runner."""
    def initialize(self, kernel, io_loop):
        """Initialize the runner."""
    def interrupt(self, signum, frame) -> None:
        """Interuppt the runner."""
    def run(self) -> None:
        """Run the loop."""
    def __call__(self, async_fn):
        """Handle a function call."""
