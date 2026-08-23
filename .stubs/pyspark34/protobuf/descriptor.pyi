from _typeshed import Incomplete

class Error(Exception):
    """Base error for this module."""
class TypeTransformationError(Error):
    """Error transforming between python proto type and corresponding C++ type."""

class DescriptorMetaclass(type):
    def __instancecheck__(cls, obj): ...
DescriptorMetaclass = type

class _Lock:
    """Wrapper class of threading.Lock(), which is allowed by 'with'."""
    def __new__(cls): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class DescriptorBase(metaclass=DescriptorMetaclass):
    """Descriptors base class.

  This class is the base of all descriptor classes. It provides common options
  related functionality.

  Attributes:
    has_options:  True if the descriptor has non-default options.  Usually it
        is not necessary to read this -- just call GetOptions() which will
        happily return the default instance.  However, it's sometimes useful
        for efficiency, and also useful inside the protobuf implementation to
        avoid some bootstrapping issues.
  """
    has_options: Incomplete
    def __init__(self, options, serialized_options, options_class_name) -> None:
        """Initialize the descriptor given its options message and the name of the
    class of the options message. The name of the class is required in case
    the options message is None and has to be created.
    """
    def GetOptions(self):
        """Retrieves descriptor options.

    This method returns the options set or creates the default options for the
    descriptor.
    """

class _NestedDescriptorBase(DescriptorBase):
    """Common class for descriptors that can be nested."""
    name: Incomplete
    full_name: Incomplete
    file: Incomplete
    containing_type: Incomplete
    def __init__(self, options, options_class_name, name, full_name, file, containing_type, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, serialized_options: Incomplete | None = None) -> None:
        '''Constructor.

    Args:
      options: Protocol message options or None
        to use default message options.
      options_class_name (str): The class name of the above options.
      name (str): Name of this protocol message type.
      full_name (str): Fully-qualified name of this protocol message type,
        which will include protocol "package" name and the name of any
        enclosing types.
      file (FileDescriptor): Reference to file info.
      containing_type: if provided, this is a nested descriptor, with this
        descriptor as parent, otherwise None.
      serialized_start: The start index (inclusive) in block in the
        file.serialized_pb that describes this descriptor.
      serialized_end: The end index (exclusive) in block in the
        file.serialized_pb that describes this descriptor.
      serialized_options: Protocol message serialized options or None.
    '''
    def CopyToProto(self, proto) -> None:
        """Copies this to the matching proto in descriptor_pb2.

    Args:
      proto: An empty proto instance from descriptor_pb2.

    Raises:
      Error: If self couldn't be serialized, due to to few constructor
        arguments.
    """

class Descriptor(_NestedDescriptorBase):
    '''Descriptor for a protocol message type.

  Attributes:
      name (str): Name of this protocol message type.
      full_name (str): Fully-qualified name of this protocol message type,
          which will include protocol "package" name and the name of any
          enclosing types.
      containing_type (Descriptor): Reference to the descriptor of the type
          containing us, or None if this is top-level.
      fields (list[FieldDescriptor]): Field descriptors for all fields in
          this type.
      fields_by_number (dict(int, FieldDescriptor)): Same
          :class:`FieldDescriptor` objects as in :attr:`fields`, but indexed
          by "number" attribute in each FieldDescriptor.
      fields_by_name (dict(str, FieldDescriptor)): Same
          :class:`FieldDescriptor` objects as in :attr:`fields`, but indexed by
          "name" attribute in each :class:`FieldDescriptor`.
      nested_types (list[Descriptor]): Descriptor references
          for all protocol message types nested within this one.
      nested_types_by_name (dict(str, Descriptor)): Same Descriptor
          objects as in :attr:`nested_types`, but indexed by "name" attribute
          in each Descriptor.
      enum_types (list[EnumDescriptor]): :class:`EnumDescriptor` references
          for all enums contained within this type.
      enum_types_by_name (dict(str, EnumDescriptor)): Same
          :class:`EnumDescriptor` objects as in :attr:`enum_types`, but
          indexed by "name" attribute in each EnumDescriptor.
      enum_values_by_name (dict(str, EnumValueDescriptor)): Dict mapping
          from enum value name to :class:`EnumValueDescriptor` for that value.
      extensions (list[FieldDescriptor]): All extensions defined directly
          within this message type (NOT within a nested type).
      extensions_by_name (dict(str, FieldDescriptor)): Same FieldDescriptor
          objects as :attr:`extensions`, but indexed by "name" attribute of each
          FieldDescriptor.
      is_extendable (bool):  Does this type define any extension ranges?
      oneofs (list[OneofDescriptor]): The list of descriptors for oneof fields
          in this message.
      oneofs_by_name (dict(str, OneofDescriptor)): Same objects as in
          :attr:`oneofs`, but indexed by "name" attribute.
      file (FileDescriptor): Reference to file descriptor.

  '''
    def __new__(cls, name: Incomplete | None = None, full_name: Incomplete | None = None, filename: Incomplete | None = None, containing_type: Incomplete | None = None, fields: Incomplete | None = None, nested_types: Incomplete | None = None, enum_types: Incomplete | None = None, extensions: Incomplete | None = None, options: Incomplete | None = None, serialized_options: Incomplete | None = None, is_extendable: bool = True, extension_ranges: Incomplete | None = None, oneofs: Incomplete | None = None, file: Incomplete | None = None, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, syntax: Incomplete | None = None, create_key: Incomplete | None = None): ...
    fields: Incomplete
    fields_by_number: Incomplete
    fields_by_name: Incomplete
    nested_types: Incomplete
    nested_types_by_name: Incomplete
    enum_types: Incomplete
    enum_types_by_name: Incomplete
    enum_values_by_name: Incomplete
    extensions: Incomplete
    extensions_by_name: Incomplete
    is_extendable: Incomplete
    extension_ranges: Incomplete
    oneofs: Incomplete
    oneofs_by_name: Incomplete
    syntax: Incomplete
    def __init__(self, name, full_name, filename, containing_type, fields, nested_types, enum_types, extensions, options: Incomplete | None = None, serialized_options: Incomplete | None = None, is_extendable: bool = True, extension_ranges: Incomplete | None = None, oneofs: Incomplete | None = None, file: Incomplete | None = None, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, syntax: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """Arguments to __init__() are as described in the description
    of Descriptor fields above.

    Note that filename is an obsolete argument, that is not used anymore.
    Please use file.name to access this as an attribute.
    """
    @property
    def fields_by_camelcase_name(self):
        """Same FieldDescriptor objects as in :attr:`fields`, but indexed by
    :attr:`FieldDescriptor.camelcase_name`.
    """
    def EnumValueName(self, enum, value):
        """Returns the string name of an enum value.

    This is just a small helper method to simplify a common operation.

    Args:
      enum: string name of the Enum.
      value: int, value of the enum.

    Returns:
      string name of the enum value.

    Raises:
      KeyError if either the Enum doesn't exist or the value is not a valid
        value for the enum.
    """
    def CopyToProto(self, proto) -> None:
        """Copies this to a descriptor_pb2.DescriptorProto.

    Args:
      proto: An empty descriptor_pb2.DescriptorProto.
    """

class FieldDescriptor(DescriptorBase):
    """Descriptor for a single field in a .proto file.

  Attributes:
    name (str): Name of this field, exactly as it appears in .proto.
    full_name (str): Name of this field, including containing scope.  This is
      particularly relevant for extensions.
    index (int): Dense, 0-indexed index giving the order that this
      field textually appears within its message in the .proto file.
    number (int): Tag number declared for this field in the .proto file.

    type (int): (One of the TYPE_* constants below) Declared type.
    cpp_type (int): (One of the CPPTYPE_* constants below) C++ type used to
      represent this field.

    label (int): (One of the LABEL_* constants below) Tells whether this
      field is optional, required, or repeated.
    has_default_value (bool): True if this field has a default value defined,
      otherwise false.
    default_value (Varies): Default value of this field.  Only
      meaningful for non-repeated scalar fields.  Repeated fields
      should always set this to [], and non-repeated composite
      fields should always set this to None.

    containing_type (Descriptor): Descriptor of the protocol message
      type that contains this field.  Set by the Descriptor constructor
      if we're passed into one.
      Somewhat confusingly, for extension fields, this is the
      descriptor of the EXTENDED message, not the descriptor
      of the message containing this field.  (See is_extension and
      extension_scope below).
    message_type (Descriptor): If a composite field, a descriptor
      of the message type contained in this field.  Otherwise, this is None.
    enum_type (EnumDescriptor): If this field contains an enum, a
      descriptor of that enum.  Otherwise, this is None.

    is_extension: True iff this describes an extension field.
    extension_scope (Descriptor): Only meaningful if is_extension is True.
      Gives the message that immediately contains this extension field.
      Will be None iff we're a top-level (file-level) extension field.

    options (descriptor_pb2.FieldOptions): Protocol message field options or
      None to use default field options.

    containing_oneof (OneofDescriptor): If the field is a member of a oneof
      union, contains its descriptor. Otherwise, None.

    file (FileDescriptor): Reference to file descriptor.
  """
    TYPE_DOUBLE: int
    TYPE_FLOAT: int
    TYPE_INT64: int
    TYPE_UINT64: int
    TYPE_INT32: int
    TYPE_FIXED64: int
    TYPE_FIXED32: int
    TYPE_BOOL: int
    TYPE_STRING: int
    TYPE_GROUP: int
    TYPE_MESSAGE: int
    TYPE_BYTES: int
    TYPE_UINT32: int
    TYPE_ENUM: int
    TYPE_SFIXED32: int
    TYPE_SFIXED64: int
    TYPE_SINT32: int
    TYPE_SINT64: int
    MAX_TYPE: int
    CPPTYPE_INT32: int
    CPPTYPE_INT64: int
    CPPTYPE_UINT32: int
    CPPTYPE_UINT64: int
    CPPTYPE_DOUBLE: int
    CPPTYPE_FLOAT: int
    CPPTYPE_BOOL: int
    CPPTYPE_ENUM: int
    CPPTYPE_STRING: int
    CPPTYPE_MESSAGE: int
    MAX_CPPTYPE: int
    LABEL_OPTIONAL: int
    LABEL_REQUIRED: int
    LABEL_REPEATED: int
    MAX_LABEL: int
    MAX_FIELD_NUMBER: Incomplete
    FIRST_RESERVED_FIELD_NUMBER: int
    LAST_RESERVED_FIELD_NUMBER: int
    def __new__(cls, name, full_name, index, number, type, cpp_type, label, default_value, message_type, enum_type, containing_type, is_extension, extension_scope, options: Incomplete | None = None, serialized_options: Incomplete | None = None, has_default_value: bool = True, containing_oneof: Incomplete | None = None, json_name: Incomplete | None = None, file: Incomplete | None = None, create_key: Incomplete | None = None): ...
    name: Incomplete
    full_name: Incomplete
    file: Incomplete
    json_name: Incomplete
    index: Incomplete
    number: Incomplete
    type: Incomplete
    cpp_type: Incomplete
    label: Incomplete
    has_default_value: Incomplete
    default_value: Incomplete
    containing_type: Incomplete
    message_type: Incomplete
    enum_type: Incomplete
    is_extension: Incomplete
    extension_scope: Incomplete
    containing_oneof: Incomplete
    def __init__(self, name, full_name, index, number, type, cpp_type, label, default_value, message_type, enum_type, containing_type, is_extension, extension_scope, options: Incomplete | None = None, serialized_options: Incomplete | None = None, has_default_value: bool = True, containing_oneof: Incomplete | None = None, json_name: Incomplete | None = None, file: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """The arguments are as described in the description of FieldDescriptor
    attributes above.

    Note that containing_type may be None, and may be set later if necessary
    (to deal with circular references between message types, for example).
    Likewise for extension_scope.
    """
    @property
    def camelcase_name(self):
        """Camelcase name of this field.

    Returns:
      str: the name in CamelCase.
    """
    @property
    def has_presence(self):
        """Whether the field distinguishes between unpopulated and default values.

    Raises:
      RuntimeError: singular field that is not linked with message nor file.
    """
    @staticmethod
    def ProtoTypeToCppProtoType(proto_type):
        """Converts from a Python proto type to a C++ Proto Type.

    The Python ProtocolBuffer classes specify both the 'Python' datatype and the
    'C++' datatype - and they're not the same. This helper method should
    translate from one to another.

    Args:
      proto_type: the Python proto type (descriptor.FieldDescriptor.TYPE_*)
    Returns:
      int: descriptor.FieldDescriptor.CPPTYPE_*, the C++ type.
    Raises:
      TypeTransformationError: when the Python proto type isn't known.
    """

class EnumDescriptor(_NestedDescriptorBase):
    '''Descriptor for an enum defined in a .proto file.

  Attributes:
    name (str): Name of the enum type.
    full_name (str): Full name of the type, including package name
      and any enclosing type(s).

    values (list[EnumValueDescriptor]): List of the values
      in this enum.
    values_by_name (dict(str, EnumValueDescriptor)): Same as :attr:`values`,
      but indexed by the "name" field of each EnumValueDescriptor.
    values_by_number (dict(int, EnumValueDescriptor)): Same as :attr:`values`,
      but indexed by the "number" field of each EnumValueDescriptor.
    containing_type (Descriptor): Descriptor of the immediate containing
      type of this enum, or None if this is an enum defined at the
      top level in a .proto file.  Set by Descriptor\'s constructor
      if we\'re passed into one.
    file (FileDescriptor): Reference to file descriptor.
    options (descriptor_pb2.EnumOptions): Enum options message or
      None to use default enum options.
  '''
    def __new__(cls, name, full_name, filename, values, containing_type: Incomplete | None = None, options: Incomplete | None = None, serialized_options: Incomplete | None = None, file: Incomplete | None = None, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, create_key: Incomplete | None = None): ...
    values: Incomplete
    values_by_name: Incomplete
    values_by_number: Incomplete
    def __init__(self, name, full_name, filename, values, containing_type: Incomplete | None = None, options: Incomplete | None = None, serialized_options: Incomplete | None = None, file: Incomplete | None = None, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """Arguments are as described in the attribute description above.

    Note that filename is an obsolete argument, that is not used anymore.
    Please use file.name to access this as an attribute.
    """
    def CopyToProto(self, proto) -> None:
        """Copies this to a descriptor_pb2.EnumDescriptorProto.

    Args:
      proto (descriptor_pb2.EnumDescriptorProto): An empty descriptor proto.
    """

class EnumValueDescriptor(DescriptorBase):
    """Descriptor for a single value within an enum.

  Attributes:
    name (str): Name of this value.
    index (int): Dense, 0-indexed index giving the order that this
      value appears textually within its enum in the .proto file.
    number (int): Actual number assigned to this enum value.
    type (EnumDescriptor): :class:`EnumDescriptor` to which this value
      belongs.  Set by :class:`EnumDescriptor`'s constructor if we're
      passed into one.
    options (descriptor_pb2.EnumValueOptions): Enum value options message or
      None to use default enum value options options.
  """
    def __new__(cls, name, index, number, type: Incomplete | None = None, options: Incomplete | None = None, serialized_options: Incomplete | None = None, create_key: Incomplete | None = None) -> None: ...
    name: Incomplete
    index: Incomplete
    number: Incomplete
    type: Incomplete
    def __init__(self, name, index, number, type: Incomplete | None = None, options: Incomplete | None = None, serialized_options: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """Arguments are as described in the attribute description above."""

class OneofDescriptor(DescriptorBase):
    """Descriptor for a oneof field.

  Attributes:
    name (str): Name of the oneof field.
    full_name (str): Full name of the oneof field, including package name.
    index (int): 0-based index giving the order of the oneof field inside
      its containing type.
    containing_type (Descriptor): :class:`Descriptor` of the protocol message
      type that contains this field.  Set by the :class:`Descriptor` constructor
      if we're passed into one.
    fields (list[FieldDescriptor]): The list of field descriptors this
      oneof can contain.
  """
    def __new__(cls, name, full_name, index, containing_type, fields, options: Incomplete | None = None, serialized_options: Incomplete | None = None, create_key: Incomplete | None = None): ...
    name: Incomplete
    full_name: Incomplete
    index: Incomplete
    containing_type: Incomplete
    fields: Incomplete
    def __init__(self, name, full_name, index, containing_type, fields, options: Incomplete | None = None, serialized_options: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """Arguments are as described in the attribute description above."""

class ServiceDescriptor(_NestedDescriptorBase):
    '''Descriptor for a service.

  Attributes:
    name (str): Name of the service.
    full_name (str): Full name of the service, including package name.
    index (int): 0-indexed index giving the order that this services
      definition appears within the .proto file.
    methods (list[MethodDescriptor]): List of methods provided by this
      service.
    methods_by_name (dict(str, MethodDescriptor)): Same
      :class:`MethodDescriptor` objects as in :attr:`methods_by_name`, but
      indexed by "name" attribute in each :class:`MethodDescriptor`.
    options (descriptor_pb2.ServiceOptions): Service options message or
      None to use default service options.
    file (FileDescriptor): Reference to file info.
  '''
    def __new__(cls, name: Incomplete | None = None, full_name: Incomplete | None = None, index: Incomplete | None = None, methods: Incomplete | None = None, options: Incomplete | None = None, serialized_options: Incomplete | None = None, file: Incomplete | None = None, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, create_key: Incomplete | None = None): ...
    index: Incomplete
    methods: Incomplete
    methods_by_name: Incomplete
    def __init__(self, name, full_name, index, methods, options: Incomplete | None = None, serialized_options: Incomplete | None = None, file: Incomplete | None = None, serialized_start: Incomplete | None = None, serialized_end: Incomplete | None = None, create_key: Incomplete | None = None) -> None: ...
    def FindMethodByName(self, name):
        """Searches for the specified method, and returns its descriptor.

    Args:
      name (str): Name of the method.
    Returns:
      MethodDescriptor or None: the descriptor for the requested method, if
      found.
    """
    def CopyToProto(self, proto) -> None:
        """Copies this to a descriptor_pb2.ServiceDescriptorProto.

    Args:
      proto (descriptor_pb2.ServiceDescriptorProto): An empty descriptor proto.
    """

class MethodDescriptor(DescriptorBase):
    """Descriptor for a method in a service.

  Attributes:
    name (str): Name of the method within the service.
    full_name (str): Full name of method.
    index (int): 0-indexed index of the method inside the service.
    containing_service (ServiceDescriptor): The service that contains this
      method.
    input_type (Descriptor): The descriptor of the message that this method
      accepts.
    output_type (Descriptor): The descriptor of the message that this method
      returns.
    client_streaming (bool): Whether this method uses client streaming.
    server_streaming (bool): Whether this method uses server streaming.
    options (descriptor_pb2.MethodOptions or None): Method options message, or
      None to use default method options.
  """
    def __new__(cls, name, full_name, index, containing_service, input_type, output_type, client_streaming: bool = False, server_streaming: bool = False, options: Incomplete | None = None, serialized_options: Incomplete | None = None, create_key: Incomplete | None = None): ...
    name: Incomplete
    full_name: Incomplete
    index: Incomplete
    containing_service: Incomplete
    input_type: Incomplete
    output_type: Incomplete
    client_streaming: Incomplete
    server_streaming: Incomplete
    def __init__(self, name, full_name, index, containing_service, input_type, output_type, client_streaming: bool = False, server_streaming: bool = False, options: Incomplete | None = None, serialized_options: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """The arguments are as described in the description of MethodDescriptor
    attributes above.

    Note that containing_service may be None, and may be set later if necessary.
    """
    def CopyToProto(self, proto) -> None:
        """Copies this to a descriptor_pb2.MethodDescriptorProto.

    Args:
      proto (descriptor_pb2.MethodDescriptorProto): An empty descriptor proto.

    Raises:
      Error: If self couldn't be serialized, due to too few constructor
        arguments.
    """

class FileDescriptor(DescriptorBase):
    '''Descriptor for a file. Mimics the descriptor_pb2.FileDescriptorProto.

  Note that :attr:`enum_types_by_name`, :attr:`extensions_by_name`, and
  :attr:`dependencies` fields are only set by the
  :py:mod:`google.protobuf.message_factory` module, and not by the generated
  proto code.

  Attributes:
    name (str): Name of file, relative to root of source tree.
    package (str): Name of the package
    syntax (str): string indicating syntax of the file (can be "proto2" or
      "proto3")
    serialized_pb (bytes): Byte string of serialized
      :class:`descriptor_pb2.FileDescriptorProto`.
    dependencies (list[FileDescriptor]): List of other :class:`FileDescriptor`
      objects this :class:`FileDescriptor` depends on.
    public_dependencies (list[FileDescriptor]): A subset of
      :attr:`dependencies`, which were declared as "public".
    message_types_by_name (dict(str, Descriptor)): Mapping from message names
      to their :class:`Descriptor`.
    enum_types_by_name (dict(str, EnumDescriptor)): Mapping from enum names to
      their :class:`EnumDescriptor`.
    extensions_by_name (dict(str, FieldDescriptor)): Mapping from extension
      names declared at file scope to their :class:`FieldDescriptor`.
    services_by_name (dict(str, ServiceDescriptor)): Mapping from services\'
      names to their :class:`ServiceDescriptor`.
    pool (DescriptorPool): The pool this descriptor belongs to.  When not
      passed to the constructor, the global default pool is used.
  '''
    def __new__(cls, name, package, options: Incomplete | None = None, serialized_options: Incomplete | None = None, serialized_pb: Incomplete | None = None, dependencies: Incomplete | None = None, public_dependencies: Incomplete | None = None, syntax: Incomplete | None = None, pool: Incomplete | None = None, create_key: Incomplete | None = None): ...
    pool: Incomplete
    message_types_by_name: Incomplete
    name: Incomplete
    package: Incomplete
    syntax: Incomplete
    serialized_pb: Incomplete
    enum_types_by_name: Incomplete
    extensions_by_name: Incomplete
    services_by_name: Incomplete
    dependencies: Incomplete
    public_dependencies: Incomplete
    def __init__(self, name, package, options: Incomplete | None = None, serialized_options: Incomplete | None = None, serialized_pb: Incomplete | None = None, dependencies: Incomplete | None = None, public_dependencies: Incomplete | None = None, syntax: Incomplete | None = None, pool: Incomplete | None = None, create_key: Incomplete | None = None) -> None:
        """Constructor."""
    def CopyToProto(self, proto) -> None:
        """Copies this to a descriptor_pb2.FileDescriptorProto.

    Args:
      proto: An empty descriptor_pb2.FileDescriptorProto.
    """

def MakeDescriptor(desc_proto, package: str = '', build_file_if_cpp: bool = True, syntax: Incomplete | None = None):
    '''Make a protobuf Descriptor given a DescriptorProto protobuf.

  Handles nested descriptors. Note that this is limited to the scope of defining
  a message inside of another message. Composite fields can currently only be
  resolved if the message is defined in the same scope as the field.

  Args:
    desc_proto: The descriptor_pb2.DescriptorProto protobuf message.
    package: Optional package name for the new message Descriptor (string).
    build_file_if_cpp: Update the C++ descriptor pool if api matches.
                       Set to False on recursion, so no duplicates are created.
    syntax: The syntax/semantics that should be used.  Set to "proto3" to get
            proto3 field presence semantics.
  Returns:
    A Descriptor for protobuf messages.
  '''
