from _typeshed import Incomplete
from pyglet.window import Window

gl_lock: Incomplete

class ManagedWindow(Window):
    """
    A pyglet window with an event loop which executes automatically
    in a separate thread. Behavior is added by creating a subclass
    which overrides setup, update, and/or draw.
    """
    fps_limit: int
    default_win_args: Incomplete
    win_args: Incomplete
    Thread: Incomplete
    def __init__(self, **win_args) -> None:
        """
        It is best not to override this function in the child
        class, unless you need to take additional arguments.
        Do any OpenGL initialization calls in setup().
        """
    has_exit: bool
    def __event_loop__(self, **win_args) -> None:
        """
        The event loop thread function. Do not override or call
        directly (it is called by __init__).
        """
    def close(self) -> None:
        """
        Closes the window.
        """
    def setup(self) -> None:
        """
        Called once before the event loop begins.
        Override this method in a child class. This
        is the best place to put things like OpenGL
        initialization calls.
        """
    def update(self, dt) -> None:
        """
        Called before draw during each iteration of
        the event loop. dt is the elapsed time in
        seconds since the last update. OpenGL rendering
        calls are best put in draw() rather than here.
        """
    def draw(self) -> None:
        """
        Called after update during each iteration of
        the event loop. Put OpenGL rendering calls
        here.
        """
