from _typeshed import Incomplete
from py4j.compat import basestring as basestring, bytearray2 as bytearray2, bytestr as bytestr, bytetoint as bytetoint, bytetostr as bytetostr, isbytearray as isbytearray, isbytestr as isbytestr, ispython3bytestr as ispython3bytestr, long as long, strtobyte as strtobyte, unicode as unicode

JAVA_MAX_INT: int
JAVA_MIN_INT: int
JAVA_INFINITY: str
JAVA_NEGATIVE_INFINITY: str
JAVA_NAN: str
ESCAPE_CHAR: str
ENTRY_POINT_OBJECT_ID: str
CONNECTION_PROPERTY_OBJECT_ID: str
GATEWAY_SERVER_OBJECT_ID: str
STATIC_PREFIX: str
DEFAULT_JVM_ID: str
DEFAULT_JVM_NAME: str
BYTES_TYPE: str
INTEGER_TYPE: str
LONG_TYPE: str
BOOLEAN_TYPE: str
DOUBLE_TYPE: str
DECIMAL_TYPE: str
STRING_TYPE: str
REFERENCE_TYPE: str
ARRAY_TYPE: str
SET_TYPE: str
LIST_TYPE: str
MAP_TYPE: str
NULL_TYPE: str
PACKAGE_TYPE: str
CLASS_TYPE: str
METHOD_TYPE: str
NO_MEMBER: str
VOID_TYPE: str
ITERATOR_TYPE: str
PYTHON_PROXY_TYPE: str
END: str
ERROR: str
FATAL_ERROR: str
SUCCESS: str
RETURN_MESSAGE: str
SUCCESS_PACKAGE: Incomplete
SUCCESS_CLASS: Incomplete
CLASS_FQN_START: int
END_COMMAND_PART: Incomplete
NO_MEMBER_COMMAND: Incomplete
CALL_COMMAND_NAME: str
FIELD_COMMAND_NAME: str
CONSTRUCTOR_COMMAND_NAME: str
SHUTDOWN_GATEWAY_COMMAND_NAME: str
LIST_COMMAND_NAME: str
REFLECTION_COMMAND_NAME: str
MEMORY_COMMAND_NAME: str
HELP_COMMAND_NAME: str
ARRAY_COMMAND_NAME: str
JVMVIEW_COMMAND_NAME: str
EXCEPTION_COMMAND_NAME: str
DIR_COMMAND_NAME: str
STREAM_COMMAND_NAME: str
ARRAY_GET_SUB_COMMAND_NAME: str
ARRAY_SET_SUB_COMMAND_NAME: str
ARRAY_SLICE_SUB_COMMAND_NAME: str
ARRAY_LEN_SUB_COMMAND_NAME: str
ARRAY_CREATE_SUB_COMMAND_NAME: str
REFL_GET_UNKNOWN_SUB_COMMAND_NAME: str
REFL_GET_MEMBER_SUB_COMMAND_NAME: str
REFL_GET_JAVA_LANG_CLASS_SUB_COMMAND_NAME: str
LIST_SORT_SUBCOMMAND_NAME: str
LIST_REVERSE_SUBCOMMAND_NAME: str
LIST_SLICE_SUBCOMMAND_NAME: str
LIST_CONCAT_SUBCOMMAND_NAME: str
LIST_MULT_SUBCOMMAND_NAME: str
LIST_IMULT_SUBCOMMAND_NAME: str
LIST_COUNT_SUBCOMMAND_NAME: str
FIELD_GET_SUBCOMMAND_NAME: str
FIELD_SET_SUBCOMMAND_NAME: str
MEMORY_DEL_SUBCOMMAND_NAME: str
MEMORY_ATTACH_SUBCOMMAND_NAME: str
HELP_OBJECT_SUBCOMMAND_NAME: str
HELP_CLASS_SUBCOMMAND_NAME: str
JVM_CREATE_VIEW_SUB_COMMAND_NAME: str
JVM_IMPORT_SUB_COMMAND_NAME: str
JVM_SEARCH_SUB_COMMAND_NAME: str
REMOVE_IMPORT_SUB_COMMAND_NAME: str
PYTHON_PROXY_PREFIX: str
ERROR_RETURN_MESSAGE: Incomplete
SUCCESS_RETURN_MESSAGE: Incomplete
OUTPUT_VOID_COMMAND: Incomplete
AUTH_COMMAND_NAME: str
CALL_PROXY_COMMAND_NAME: str
GARBAGE_COLLECT_PROXY_COMMAND_NAME: str
DIR_FIELDS_SUBCOMMAND_NAME: str
DIR_METHODS_SUBCOMMAND_NAME: str
DIR_STATIC_SUBCOMMAND_NAME: str
DIR_JVMVIEW_SUBCOMMAND_NAME: str
OUTPUT_CONVERTER: Incomplete
INPUT_CONVERTER: Incomplete
ERROR_ON_SEND: str
ERROR_ON_RECEIVE: str

def escape_new_line(original):
    """Replaces new line characters by a backslash followed by a n.

    Backslashes are also escaped by another backslash.

    :param original: the string to escape

    :rtype: an escaped string
    """
def unescape_new_line(escaped):
    """Replaces escaped characters by unescaped characters.

    For example, double backslashes are replaced by a single backslash.

    The behavior for improperly formatted strings is undefined and can change.

    :param escaped: the escaped string

    :rtype: the original string
    """
def smart_decode(s): ...
def encode_float(float_value): ...
def encode_bytearray(barray): ...
def decode_bytearray(encoded): ...
def is_python_proxy(parameter):
    """Determines whether parameter is a Python Proxy, i.e., it has a Java
    internal class with an `implements` member.

    :param parameter: the object to check.
    :rtype: True if the parameter is a Python Proxy
    """
def get_command_part(parameter, python_proxy_pool: Incomplete | None = None):
    '''Converts a Python object into a string representation respecting the
    Py4J protocol.

    For example, the integer `1` is converted to `u"i1"`

    :param parameter: the object to convert
    :rtype: the string representing the command part
    '''
def get_return_value(answer, gateway_client, target_id: Incomplete | None = None, name: Incomplete | None = None):
    """Converts an answer received from the Java gateway into a Python object.

    For example, string representation of integers are converted to Python
    integer, string representation of objects are converted to JavaObject
    instances, etc.

    :param answer: the string returned by the Java gateway
    :param gateway_client: the gateway client used to communicate with the Java
        Gateway. Only necessary if the answer is a reference (e.g., object,
        list, map)
    :param target_id: the name of the object from which the answer comes from
        (e.g., *object1* in `object1.hello()`). Optional.
    :param name: the name of the member from which the answer comes from
        (e.g., *hello* in `object1.hello()`). Optional.
    """
def get_error_message(answer, gateway_client: Incomplete | None = None):
    """Returns a tuple of:

    1. bool: if the answer is an error
    2. the error message if any (discards null and references)
    """
def compute_exception_message(default_message, extra_message: Incomplete | None = None):
    """Returns an error message with an extra error message if provided.

    Otherwise returns the default error message.
    """
def is_error(answer): ...
def is_fatal_error(answer): ...
def register_output_converter(output_type, converter) -> None:
    """Registers an output converter to the list of global output converters.

    An output converter transforms the output of the Java side to an instance
    on the Python side. For example, you could transform a java.util.ArrayList
    to a Python list. See ``py4j.java_collections`` for examples.

    :param output_type: A Py4J type of a return object (e.g., MAP_TYPE,
        BOOLEAN_TYPE).
    :param converter: A function that takes an object_id and a gateway_client
        as parameter and that returns a Python object (like a `bool` or a
        `JavaObject` instance).
    """
def register_input_converter(converter, prepend: bool = False) -> None:
    """Registers an input converter to the list of global input converters.

    An input converter transforms the input of the Python side to an instance
    on the Java side. For example, you could transform a Python list into a
    java.util.ArrayList on the Java side. See ``py4j.java_collections`` for
    examples.

    When initialized with `auto_convert=True`, a :class:`JavaGateway
    <py4j.java_gateway.JavaGateway>` will use the input converters on any
    parameter that is not a :class:`JavaObject <py4j.java_gateway.JavaObject>`
    or `basestring` instance.

    :param converter: A converter that declares the methods
        `can_convert(object)` and `convert(object,gateway_client)`.
    :param prepend: Put at the beginning of the input converters list

    """

class Py4JError(Exception):
    """Exception raised when a problem occurs with Py4J."""
    cause: Incomplete
    def __init__(self, args: Incomplete | None = None, cause: Incomplete | None = None) -> None: ...

class Py4JAuthenticationError(Py4JError):
    """Exception raised when Py4J cannot authenticate a connection."""
    cause: Incomplete
    def __init__(self, args: Incomplete | None = None, cause: Incomplete | None = None) -> None: ...

class Py4JNetworkError(Py4JError):
    """Exception raised when a network error occurs with Py4J."""
    cause: Incomplete
    when: Incomplete
    def __init__(self, args: Incomplete | None = None, cause: Incomplete | None = None, when: Incomplete | None = None) -> None: ...

class Py4JJavaError(Py4JError):
    """Exception raised when an exception occurs in the client code.

    The exception instance that was thrown on the Java side can be accessed
    with `Py4JJavaError.java_exception`.

    `str(py4j_java_error)` returns the error message and the stack trace
    available on the Java side (similar to printStackTrace()).

    Note that `str(py4j_java_error)` in Python 2 might not automatically handle
    a non-ascii unicode string but throw an error if the exception contains it.
    """
    args: Incomplete
    errmsg: Incomplete
    java_exception: Incomplete
    exception_cmd: Incomplete
    def __init__(self, msg, java_exception) -> None: ...
