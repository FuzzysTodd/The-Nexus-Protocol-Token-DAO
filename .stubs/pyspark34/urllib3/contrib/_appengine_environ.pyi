def is_appengine(): ...
def is_appengine_sandbox():
    """Reports if the app is running in the first generation sandbox.

    The second generation runtimes are technically still in a sandbox, but it
    is much less restrictive, so generally you shouldn't need to check for it.
    see https://cloud.google.com/appengine/docs/standard/runtimes
    """
def is_local_appengine(): ...
def is_prod_appengine(): ...
def is_prod_appengine_mvms():
    """Deprecated."""
