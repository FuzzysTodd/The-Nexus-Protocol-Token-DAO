from prompt_toolkit.contrib.regular_languages.completion import GrammarCompleter

__all__ = ['SystemCompleter']

class SystemCompleter(GrammarCompleter):
    """
    Completer for system commands.
    """
    def __init__(self) -> None: ...
