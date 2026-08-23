from _typeshed import Incomplete

HAS_NUMPY: bool
getrefcount: Incomplete
memo: Incomplete
id_to_obj: Incomplete
builtins_types: Incomplete
dont_memo: Incomplete

def get_attrs(obj):
    """
    Gets all the attributes of an object though its __dict__ or return None
    """
def get_seq(obj, cache=...):
    """
    Gets all the items in a sequence or return None
    """
def memorise(obj, force: bool = False) -> None:
    """
    Adds an object to the memo, and recursively adds all the objects
    attributes, and if it is a container, its items. Use force=True to update
    an object already in the memo. Updating is not recursively done.
    """
def release_gone() -> None: ...
def whats_changed(obj, seen: Incomplete | None = None, simple: bool = False, first: bool = True):
    """
    Check an object against the memo. Returns a list in the form
    (attribute changes, container changed). Attribute changes is a dict of
    attribute name to attribute value. container changed is a boolean.
    If simple is true, just returns a boolean. None for either item means
    that it has not been checked yet
    """
def has_changed(*args, **kwds): ...
__import__ = __import__
