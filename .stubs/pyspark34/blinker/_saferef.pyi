from _typeshed import Incomplete

get_self: Incomplete
get_func: Incomplete

def safe_ref(target, on_delete: Incomplete | None = None):
    """Return a *safe* weak reference to a callable target.

    - ``target``: The object to be weakly referenced, if it's a bound
      method reference, will create a BoundMethodWeakref, otherwise
      creates a simple weakref.

    - ``on_delete``: If provided, will have a hard reference stored to
      the callable to be called after the safe reference goes out of
      scope with the reference object, (either a weakref or a
      BoundMethodWeakref) as argument.
    """

class BoundMethodWeakref:
    """'Safe' and reusable weak references to instance methods.

    BoundMethodWeakref objects provide a mechanism for referencing a
    bound method without requiring that the method object itself
    (which is normally a transient object) is kept alive.  Instead,
    the BoundMethodWeakref object keeps weak references to both the
    object and the function which together define the instance method.

    Attributes:

    - ``key``: The identity key for the reference, calculated by the
      class's calculate_key method applied to the target instance method.

    - ``deletion_methods``: Sequence of callable objects taking single
      argument, a reference to this object which will be called when
      *either* the target object or target function is garbage
      collected (i.e. when this object becomes invalid).  These are
      specified as the on_delete parameters of safe_ref calls.

    - ``weak_self``: Weak reference to the target object.

    - ``weak_func``: Weak reference to the target function.

    Class Attributes:

    - ``_all_instances``: Class attribute pointing to all live
      BoundMethodWeakref objects indexed by the class's
      calculate_key(target) method applied to the target objects.
      This weak value dictionary is used to short-circuit creation so
      that multiple references to the same (object, function) pair
      produce the same BoundMethodWeakref instance.
    """
    def __new__(cls, target, on_delete: Incomplete | None = None, *arguments, **named):
        """Create new instance or return current instance.

        Basically this method of construction allows us to
        short-circuit creation of references to already-referenced
        instance methods.  The key corresponding to the target is
        calculated, and if there is already an existing reference,
        that is returned, with its deletion_methods attribute updated.
        Otherwise the new instance is created and registered in the
        table of already-referenced methods.
        """
    deletion_methods: Incomplete
    key: Incomplete
    weak_self: Incomplete
    weak_func: Incomplete
    self_name: Incomplete
    func_name: Incomplete
    def __init__(self, target, on_delete: Incomplete | None = None) -> None:
        """Return a weak-reference-like instance for a bound method.

        - ``target``: The instance-method target for the weak reference,
          must have im_self and im_func attributes and be
          reconstructable via the following, which is true of built-in
          instance methods::

            target.im_func.__get__( target.im_self )

        - ``on_delete``: Optional callback which will be called when
          this weak reference ceases to be valid (i.e. either the
          object or the function is garbage collected).  Should take a
          single argument, which will be passed a pointer to this
          object.
        """
    @classmethod
    def calculate_key(cls, target):
        """Calculate the reference key for this reference.

        Currently this is a two-tuple of the id()'s of the target
        object and the target function respectively.
        """
    def __hash__(self): ...
    def __nonzero__(self):
        """Whether we are still a valid reference."""
    def __eq__(self, other):
        """Compare with another reference."""
    def __call__(self):
        """Return a strong reference to the bound method.

        If the target cannot be retrieved, then will return None,
        otherwise returns a bound instance method for our object and
        function.

        Note: You may call this method any number of times, as it does
        not invalidate the reference.
        """
