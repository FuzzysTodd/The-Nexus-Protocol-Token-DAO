from _typeshed import Incomplete

class GeneratedServiceType(type):
    """Metaclass for service classes created at runtime from ServiceDescriptors.

  Implementations for all methods described in the Service class are added here
  by this class. We also create properties to allow getting/setting all fields
  in the protocol message.

  The protocol compiler currently uses this metaclass to create protocol service
  classes at runtime. Clients can also manually create their own classes at
  runtime, as in this example::

    mydescriptor = ServiceDescriptor(.....)
    class MyProtoService(service.Service):
      __metaclass__ = GeneratedServiceType
      DESCRIPTOR = mydescriptor
    myservice_instance = MyProtoService()
    # ...
  """
    def __init__(cls, name, bases, dictionary) -> None:
        """Creates a message service class.

    Args:
      name: Name of the class (ignored, but required by the metaclass
        protocol).
      bases: Base classes of the class being constructed.
      dictionary: The class dictionary of the class being constructed.
        dictionary[_DESCRIPTOR_KEY] must contain a ServiceDescriptor object
        describing this protocol service type.
    """

class GeneratedServiceStubType(GeneratedServiceType):
    """Metaclass for service stubs created at runtime from ServiceDescriptors.

  This class has similar responsibilities as GeneratedServiceType, except that
  it creates the service stub classes.
  """
    def __init__(cls, name, bases, dictionary) -> None:
        """Creates a message service stub class.

    Args:
      name: Name of the class (ignored, here).
      bases: Base classes of the class being constructed.
      dictionary: The class dictionary of the class being constructed.
        dictionary[_DESCRIPTOR_KEY] must contain a ServiceDescriptor object
        describing this protocol service type.
    """

class _ServiceBuilder:
    """This class constructs a protocol service class using a service descriptor.

  Given a service descriptor, this class constructs a class that represents
  the specified service descriptor. One service builder instance constructs
  exactly one service class. That means all instances of that class share the
  same builder.
  """
    descriptor: Incomplete
    def __init__(self, service_descriptor) -> None:
        """Initializes an instance of the service class builder.

    Args:
      service_descriptor: ServiceDescriptor to use when constructing the
        service class.
    """
    def BuildService(builder, cls):
        """Constructs the service class.

    Args:
      cls: The class that will be constructed.
    """

class _ServiceStubBuilder:
    """Constructs a protocol service stub class using a service descriptor.

  Given a service descriptor, this class constructs a suitable stub class.
  A stub is just a type-safe wrapper around an RpcChannel which emulates a
  local implementation of the service.

  One service stub builder instance constructs exactly one class. It means all
  instances of that class share the same service stub builder.
  """
    descriptor: Incomplete
    def __init__(self, service_descriptor) -> None:
        """Initializes an instance of the service stub class builder.

    Args:
      service_descriptor: ServiceDescriptor to use when constructing the
        stub class.
    """
    cls: Incomplete
    def BuildServiceStub(self, cls) -> None:
        """Constructs the stub class.

    Args:
      cls: The class that will be constructed.
    """
