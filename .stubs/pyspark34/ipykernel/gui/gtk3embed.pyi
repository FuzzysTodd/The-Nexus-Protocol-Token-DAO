from _typeshed import Incomplete

class GTKEmbed:
    """A class to embed a kernel into the GTK main event loop."""
    kernel: Incomplete
    gtk_main: Incomplete
    gtk_main_quit: Incomplete
    def __init__(self, kernel) -> None:
        """Initialize the embed."""
    def start(self) -> None:
        """Starts the GTK main event loop and sets our kernel startup routine."""
    def iterate_kernel(self):
        """Run one iteration of the kernel and return True.

        GTK timer functions must return True to be called again, so we make the
        call to :meth:`do_one_iteration` and then return True for GTK.
        """
    def stop(self) -> None:
        """Stop the embed."""
