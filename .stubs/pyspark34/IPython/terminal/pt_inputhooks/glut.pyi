from _typeshed import Incomplete

glut_fps: int
glut_display_mode: Incomplete
glutMainLoopEvent: Incomplete

def glut_display() -> None: ...
def glut_idle() -> None: ...
def glut_close() -> None: ...
def glut_int_handler(signum, frame) -> None: ...
def inputhook(context):
    """Run the pyglet event loop by processing pending events only.

    This keeps processing pending events until stdin is ready.  After
    processing all pending events, a call to time.sleep is inserted.  This is
    needed, otherwise, CPU usage is at 100%.  This sleep time should be tuned
    though for best performance.
    """
