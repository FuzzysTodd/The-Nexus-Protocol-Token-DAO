from _typeshed import Incomplete

class Reduce:
    """
    Reduce objects are wrappers used for compatibility enforcement during
    unpickle-time. They should only be used in calls to pickler.save and
    other Reduce objects. They are only evaluated within unpickler.load.

    Pickling a Reduce object makes the two implementations equivalent:

    pickler.save(Reduce(*reduction))

    pickler.save_reduce(*reduction, obj=reduction)
    """
    reduction: Incomplete
    def __new__(cls, *reduction, **kwargs):
        """
        Args:
            *reduction: a tuple that matches the format given here:
              https://docs.python.org/3/library/pickle.html#object.__reduce__
            is_callable: a bool to indicate that the object created by
              unpickling `reduction` is callable. If true, the current Reduce
              is allowed to be used as the function in further save_reduce calls
              or Reduce objects.
        """
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __reduce__(self): ...
    def __reduce_ex__(self, protocol): ...

class _CallableReduce(Reduce):
    def __call__(self, *args, **kwargs): ...

def Getattr(object, name, default=...):
    """
    A Reduce object that represents the getattr operation. When unpickled, the
    Getattr will access an attribute 'name' of 'object' and return the value
    stored there. If the attribute doesn't exist, the default value will be
    returned if present.

    The following statements are equivalent:

    Getattr(collections, 'OrderedDict')
    Getattr(collections, 'spam', None)
    Getattr(*args)

    Reduce(getattr, (collections, 'OrderedDict'))
    Reduce(getattr, (collections, 'spam', None))
    Reduce(getattr, args)

    During unpickling, the first two will result in collections.OrderedDict and
    None respectively because the first attribute exists and the second one does
    not, forcing it to use the default value given in the third argument.
    """
def move_to(module, name: Incomplete | None = None): ...
def register_shim(name, default):
    '''
    A easier to understand and more compact way of "softly" defining a function.
    These two pieces of code are equivalent:

    if _dill.OLD3X:
        def _create_class():
            ...
    _create_class = register_shim(\'_create_class\', types.new_class)

    if _dill.OLD3X:
        @move_to(_dill)
        def _create_class():
            ...
    _create_class = Getattr(_dill, \'_create_class\', types.new_class)

    Intuitively, it creates a function or object in the versions of dill/python
    that require special reimplementations, and use a core library or default
    implementation if that function or object does not exist.
    '''
