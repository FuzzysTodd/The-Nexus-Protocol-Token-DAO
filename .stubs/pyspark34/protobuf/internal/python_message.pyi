from _typeshed import Incomplete

class GeneratedProtocolMessageType(type):
    '''Metaclass for protocol message classes created at runtime from Descriptors.

  We add implementations for all methods described in the Message class.  We
  also create properties to allow getting/setting all fields in the protocol
  message.  Finally, we create slots to prevent users from accidentally
  "setting" nonexistent fields in the protocol message, which then wouldn\'t get
  serialized / deserialized properly.

  The protocol compiler currently uses this metaclass to create protocol
  message classes at runtime.  Clients can also manually create their own
  classes at runtime, as in this example:

  mydescriptor = Descriptor(.....)
  factory = symbol_database.Default()
  factory.pool.AddDescriptor(mydescriptor)
  MyProtoClass = factory.GetPrototype(mydescriptor)
  myproto_instance = MyProtoClass()
  myproto.foo_field = 23
  ...
  '''
    def __new__(cls, name, bases, dictionary):
        """Custom allocation for runtime-generated class types.

    We override __new__ because this is apparently the only place
    where we can meaningfully set __slots__ on the class we're creating(?).
    (The interplay between metaclasses and slots is not very well-documented).

    Args:
      name: Name of the class (ignored, but required by the
        metaclass protocol).
      bases: Base classes of the class we're constructing.
        (Should be message.Message).  We ignore this field, but
        it's required by the metaclass protocol
      dictionary: The class dictionary of the class we're
        constructing.  dictionary[_DESCRIPTOR_KEY] must contain
        a Descriptor object describing this protocol message
        type.

    Returns:
      Newly-allocated class.

    Raises:
      RuntimeError: Generated code only work with python cpp extension.
    """
    def __init__(cls, name, bases, dictionary) -> None:
        """Here we perform the majority of our work on the class.
    We add enum getters, an __init__ method, implementations
    of all Message methods, and properties for all fields
    in the protocol type.

    Args:
      name: Name of the class (ignored, but required by the
        metaclass protocol).
      bases: Base classes of the class we're constructing.
        (Should be message.Message).  We ignore this field, but
        it's required by the metaclass protocol
      dictionary: The class dictionary of the class we're
        constructing.  dictionary[_DESCRIPTOR_KEY] must contain
        a Descriptor object describing this protocol message
        type.
    """

class _FieldProperty(property):
    DESCRIPTOR: Incomplete
    def __init__(self, descriptor, getter, setter, doc) -> None: ...

class _Listener:
    """MessageListener implementation that a parent message registers with its
  child message.

  In order to support semantics like:

    foo.bar.baz.moo = 23
    assert foo.HasField('bar')

  ...child objects must have back references to their parents.
  This helper class is at the heart of this support.
  """
    dirty: bool
    def __init__(self, parent_message) -> None:
        """Args:
      parent_message: The message whose _Modified() method we should call when
        we receive Modified() messages.
    """
    def Modified(self) -> None: ...

class _OneofListener(_Listener):
    """Special listener implementation for setting composite oneof fields."""
    def __init__(self, parent_message, field) -> None:
        """Args:
      parent_message: The message whose _Modified() method we should call when
        we receive Modified() messages.
      field: The descriptor of the field being set in the parent message.
    """
    def Modified(self) -> None:
        """Also updates the state of the containing oneof in the parent message."""
