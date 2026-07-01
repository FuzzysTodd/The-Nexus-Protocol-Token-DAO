from _typeshed import Incomplete

__all__ = ['editor', 'synchronize_with_editor', 'show_in_pager', 'pre_prompt_hook', 'clipboard_get']

def editor(self, filename, linenum: Incomplete | None = None, wait: bool = True) -> None:
    """Open the default editor at the given filename and linenumber.

    This is IPython's default editor hook, you can use it as an example to
    write your own modified one.  To set your own editor function as the
    new editor hook, call ip.set_hook('editor',yourfunc)."""
def synchronize_with_editor(self, filename, linenum, column) -> None: ...

class CommandChainDispatcher:
    ''' Dispatch calls to a chain of commands until some func can handle it

    Usage: instantiate, execute "add" to add commands (with optional
    priority), execute normally via f() calling mechanism.

    '''
    chain: Incomplete
    def __init__(self, commands: Incomplete | None = None) -> None: ...
    def __call__(self, *args, **kw):
        """ Command chain is called just like normal func.

        This will call all funcs in chain with the same args as were given to
        this function, and return the result of first func that didn't raise
        TryNext"""
    def add(self, func, priority: int = 0):
        """ Add a func to the cmd chain with given priority """
    def __iter__(self):
        """ Return all objects in chain.

        Handy if the objects are not callable.
        """

def show_in_pager(self, data, start, screen_lines) -> None:
    """ Run a string through pager """
def pre_prompt_hook(self) -> None:
    """ Run before displaying the next prompt

    Use this e.g. to display output from asynchronous operations (in order
    to not mess up text entry)
    """
def clipboard_get(self):
    """ Get text from the clipboard.
    """
