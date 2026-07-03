from _typeshed import Incomplete

HOOKS: Incomplete

def default_hooks(): ...
def dispatch_hook(key, hooks, hook_data, **kwargs):
    """Dispatches a hook dictionary on a given piece of data."""
