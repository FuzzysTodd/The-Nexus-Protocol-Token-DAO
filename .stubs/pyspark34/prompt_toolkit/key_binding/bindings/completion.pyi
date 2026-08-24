from prompt_toolkit.key_binding.key_processor import KeyPressEvent

__all__ = ['generate_completions', 'display_completions_like_readline']

E = KeyPressEvent

def generate_completions(event: E) -> None:
    """
    Tab-completion: where the first tab completes the common suffix and the
    second tab lists all the completions.
    """
def display_completions_like_readline(event: E) -> None:
    """
    Key binding handler for readline-style tab completion.
    This is meant to be as similar as possible to the way how readline displays
    completions.

    Generate the completions immediately (blocking) and display them above the
    prompt in columns.

    Usage::

        # Call this handler when 'Tab' has been pressed.
        key_bindings.add(Keys.ControlI)(display_completions_like_readline)
    """
