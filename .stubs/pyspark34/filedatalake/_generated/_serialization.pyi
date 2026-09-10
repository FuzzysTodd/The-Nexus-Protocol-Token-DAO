import datetime
from _typeshed import Incomplete
from typing import Any, AnyStr, Callable, Dict, IO, Mapping, MutableMapping, Type, TypeVar

ModelType = TypeVar('ModelType', bound='Model')
JSON = MutableMapping[str, Any]

class RawDeserializer:
    JSON_REGEXP: Incomplete
    CONTEXT_NAME: str
    @classmethod
    def deserialize_from_text(cls, data: AnyStr | IO | None, content_type: str | None = None) -> Any:
        """Decode data according to content-type.

        Accept a stream of data as well, but will be load at once in memory for now.

        If no content-type, will return the string version (not bytes, not stream)

        :param data: Input, could be bytes or stream (will be decoded with UTF8) or text
        :type data: str or bytes or IO
        :param str content_type: The content type.
        """
    @classmethod
    def deserialize_from_http_generics(cls, body_bytes: AnyStr | IO | None, headers: Mapping) -> Any:
        '''Deserialize from HTTP response.

        Use bytes and headers to NOT use any requests/aiohttp or whatever
        specific implementation.
        Headers will tested for "content-type"
        '''
unicode_str = unicode
basestring = str
unicode_str = str

class UTC(datetime.tzinfo):
    """Time Zone info for handling UTC"""
    def utcoffset(self, dt):
        """UTF offset for UTC is 0."""
    def tzname(self, dt):
        """Timestamp representation."""
    def dst(self, dt):
        """No daylight saving for UTC."""

class _FixedOffset(datetime.tzinfo):
    """Fixed offset in minutes east from UTC.
        Copy/pasted from Python doc
        :param datetime.timedelta offset: offset in timedelta format
        """
    def __init__(self, offset) -> None: ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...
    def __getinitargs__(self): ...

TZ_UTC: Incomplete

def attribute_transformer(key, attr_desc, value):
    """A key transformer that returns the Python attribute.

    :param str key: The attribute name
    :param dict attr_desc: The attribute metadata
    :param object value: The value
    :returns: A key using attribute name
    """
def full_restapi_key_transformer(key, attr_desc, value):
    """A key transformer that returns the full RestAPI key path.

    :param str _: The attribute name
    :param dict attr_desc: The attribute metadata
    :param object value: The value
    :returns: A list of keys using RestAPI syntax.
    """
def last_restapi_key_transformer(key, attr_desc, value):
    """A key transformer that returns the last RestAPI key.

    :param str key: The attribute name
    :param dict attr_desc: The attribute metadata
    :param object value: The value
    :returns: The last RestAPI key.
    """

class Model:
    """Mixin for all client request body/response body models to support
    serialization and deserialization.
    """
    additional_properties: Incomplete
    def __init__(self, **kwargs: Any) -> None: ...
    def __eq__(self, other: Any) -> bool:
        """Compare objects by comparing all attributes."""
    def __ne__(self, other: Any) -> bool:
        """Compare objects by comparing all attributes."""
    @classmethod
    def enable_additional_properties_sending(cls) -> None: ...
    @classmethod
    def is_xml_model(cls) -> bool: ...
    def serialize(self, keep_readonly: bool = False, **kwargs: Any) -> JSON:
        """Return the JSON that would be sent to azure from this model.

        This is an alias to `as_dict(full_restapi_key_transformer, keep_readonly=False)`.

        If you want XML serialization, you can pass the kwargs is_xml=True.

        :param bool keep_readonly: If you want to serialize the readonly attributes
        :returns: A dict JSON compatible object
        :rtype: dict
        """
    def as_dict(self, keep_readonly: bool = True, key_transformer: Callable[[str, Dict[str, Any], Any], Any] = ..., **kwargs: Any) -> JSON:
        """Return a dict that can be serialized using json.dump.

        Advanced usage might optionally use a callback as parameter:

        .. code::python

            def my_key_transformer(key, attr_desc, value):
                return key

        Key is the attribute name used in Python. Attr_desc
        is a dict of metadata. Currently contains 'type' with the
        msrest type and 'key' with the RestAPI encoded key.
        Value is the current value in this object.

        The string returned will be used to serialize the key.
        If the return type is a list, this is considered hierarchical
        result dict.

        See the three examples in this file:

        - attribute_transformer
        - full_restapi_key_transformer
        - last_restapi_key_transformer

        If you want XML serialization, you can pass the kwargs is_xml=True.

        :param function key_transformer: A key transformer function.
        :returns: A dict JSON compatible object
        :rtype: dict
        """
    @classmethod
    def deserialize(cls, data: Any, content_type: str | None = None) -> ModelType:
        """Parse a str using the RestAPI syntax and return a model.

        :param str data: A str using RestAPI structure. JSON by default.
        :param str content_type: JSON by default, set application/xml if XML.
        :returns: An instance of this model
        :raises: DeserializationError if something went wrong
        """
    @classmethod
    def from_dict(cls, data: Any, key_extractors: Callable[[str, Dict[str, Any], Any], Any] | None = None, content_type: str | None = None) -> ModelType:
        """Parse a dict using given key extractor return a model.

        By default consider key
        extractors (rest_key_case_insensitive_extractor, attribute_key_case_insensitive_extractor
        and last_rest_key_case_insensitive_extractor)

        :param dict data: A dict using RestAPI structure
        :param str content_type: JSON by default, set application/xml if XML.
        :returns: An instance of this model
        :raises: DeserializationError if something went wrong
        """

class Serializer:
    """Request object model serializer."""
    basic_types: Incomplete
    days: Incomplete
    months: Incomplete
    validation: Incomplete
    serialize_type: Incomplete
    dependencies: Incomplete
    key_transformer: Incomplete
    client_side_validation: bool
    def __init__(self, classes: Mapping[str, Type[ModelType]] | None = None) -> None: ...
    def body(self, data, data_type, **kwargs):
        """Serialize data intended for a request body.

        :param data: The data to be serialized.
        :param str data_type: The type to be serialized from.
        :rtype: dict
        :raises: SerializationError if serialization fails.
        :raises: ValueError if data is None
        """
    def url(self, name, data, data_type, **kwargs):
        """Serialize data intended for a URL path.

        :param data: The data to be serialized.
        :param str data_type: The type to be serialized from.
        :rtype: str
        :raises: TypeError if serialization fails.
        :raises: ValueError if data is None
        """
    def query(self, name, data, data_type, **kwargs):
        """Serialize data intended for a URL query.

        :param data: The data to be serialized.
        :param str data_type: The type to be serialized from.
        :rtype: str
        :raises: TypeError if serialization fails.
        :raises: ValueError if data is None
        """
    def header(self, name, data, data_type, **kwargs):
        """Serialize data intended for a request header.

        :param data: The data to be serialized.
        :param str data_type: The type to be serialized from.
        :rtype: str
        :raises: TypeError if serialization fails.
        :raises: ValueError if data is None
        """
    def serialize_data(self, data, data_type, **kwargs):
        """Serialize generic data according to supplied data type.

        :param data: The data to be serialized.
        :param str data_type: The type to be serialized from.
        :param bool required: Whether it's essential that the data not be
         empty or None
        :raises: AttributeError if required data is None.
        :raises: ValueError if data is None
        :raises: SerializationError if serialization fails.
        """
    @classmethod
    def serialize_basic(cls, data, data_type, **kwargs):
        """Serialize basic builting data type.
        Serializes objects to str, int, float or bool.

        Possible kwargs:
        - basic_types_serializers dict[str, callable] : If set, use the callable as serializer
        - is_xml bool : If set, use xml_basic_types_serializers

        :param data: Object to be serialized.
        :param str data_type: Type of object in the iterable.
        """
    @classmethod
    def serialize_unicode(cls, data):
        """Special handling for serializing unicode strings in Py2.
        Encode to UTF-8 if unicode, otherwise handle as a str.

        :param data: Object to be serialized.
        :rtype: str
        """
    def serialize_iter(self, data, iter_type, div: Incomplete | None = None, **kwargs):
        """Serialize iterable.

        Supported kwargs:
        - serialization_ctxt dict : The current entry of _attribute_map, or same format.
          serialization_ctxt['type'] should be same as data_type.
        - is_xml bool : If set, serialize as XML

        :param list attr: Object to be serialized.
        :param str iter_type: Type of object in the iterable.
        :param bool required: Whether the objects in the iterable must
         not be None or empty.
        :param str div: If set, this str will be used to combine the elements
         in the iterable into a combined string. Default is 'None'.
        :rtype: list, str
        """
    def serialize_dict(self, attr, dict_type, **kwargs):
        """Serialize a dictionary of objects.

        :param dict attr: Object to be serialized.
        :param str dict_type: Type of object in the dictionary.
        :param bool required: Whether the objects in the dictionary must
         not be None or empty.
        :rtype: dict
        """
    def serialize_object(self, attr, **kwargs):
        """Serialize a generic object.
        This will be handled as a dictionary. If object passed in is not
        a basic type (str, int, float, dict, list) it will simply be
        cast to str.

        :param dict attr: Object to be serialized.
        :rtype: dict or str
        """
    @staticmethod
    def serialize_enum(attr, enum_obj: Incomplete | None = None): ...
    @staticmethod
    def serialize_bytearray(attr, **kwargs):
        """Serialize bytearray into base-64 string.

        :param attr: Object to be serialized.
        :rtype: str
        """
    @staticmethod
    def serialize_base64(attr, **kwargs):
        """Serialize str into base-64 string.

        :param attr: Object to be serialized.
        :rtype: str
        """
    @staticmethod
    def serialize_decimal(attr, **kwargs):
        """Serialize Decimal object to float.

        :param attr: Object to be serialized.
        :rtype: float
        """
    @staticmethod
    def serialize_long(attr, **kwargs):
        """Serialize long (Py2) or int (Py3).

        :param attr: Object to be serialized.
        :rtype: int/long
        """
    @staticmethod
    def serialize_date(attr, **kwargs):
        """Serialize Date object into ISO-8601 formatted string.

        :param Date attr: Object to be serialized.
        :rtype: str
        """
    @staticmethod
    def serialize_time(attr, **kwargs):
        """Serialize Time object into ISO-8601 formatted string.

        :param datetime.time attr: Object to be serialized.
        :rtype: str
        """
    @staticmethod
    def serialize_duration(attr, **kwargs):
        """Serialize TimeDelta object into ISO-8601 formatted string.

        :param TimeDelta attr: Object to be serialized.
        :rtype: str
        """
    @staticmethod
    def serialize_rfc(attr, **kwargs):
        """Serialize Datetime object into RFC-1123 formatted string.

        :param Datetime attr: Object to be serialized.
        :rtype: str
        :raises: TypeError if format invalid.
        """
    @staticmethod
    def serialize_iso(attr, **kwargs):
        """Serialize Datetime object into ISO-8601 formatted string.

        :param Datetime attr: Object to be serialized.
        :rtype: str
        :raises: SerializationError if format invalid.
        """
    @staticmethod
    def serialize_unix(attr, **kwargs):
        """Serialize Datetime object into IntTime format.
        This is represented as seconds.

        :param Datetime attr: Object to be serialized.
        :rtype: int
        :raises: SerializationError if format invalid
        """

def rest_key_extractor(attr, attr_desc, data): ...
def rest_key_case_insensitive_extractor(attr, attr_desc, data): ...
def last_rest_key_extractor(attr, attr_desc, data):
    '''Extract the attribute in "data" based on the last part of the JSON path key.'''
def last_rest_key_case_insensitive_extractor(attr, attr_desc, data):
    '''Extract the attribute in "data" based on the last part of the JSON path key.

    This is the case insensitive version of "last_rest_key_extractor"
    '''
def attribute_key_extractor(attr, _, data): ...
def attribute_key_case_insensitive_extractor(attr, _, data): ...
def xml_key_extractor(attr, attr_desc, data): ...

class Deserializer:
    """Response object model deserializer.

    :param dict classes: Class type dictionary for deserializing complex types.
    :ivar list key_extractors: Ordered list of extractors to be used by this deserializer.
    """
    basic_types: Incomplete
    valid_date: Incomplete
    deserialize_type: Incomplete
    deserialize_expected_types: Incomplete
    dependencies: Incomplete
    key_extractors: Incomplete
    additional_properties_detection: bool
    def __init__(self, classes: Mapping[str, Type[ModelType]] | None = None) -> None: ...
    def __call__(self, target_obj, response_data, content_type: Incomplete | None = None):
        '''Call the deserializer to process a REST response.

        :param str target_obj: Target data type to deserialize to.
        :param requests.Response response_data: REST response object.
        :param str content_type: Swagger "produces" if available.
        :raises: DeserializationError if deserialization fails.
        :return: Deserialized object.
        '''
    def failsafe_deserialize(self, target_obj, data, content_type: Incomplete | None = None):
        '''Ignores any errors encountered in deserialization,
        and falls back to not deserializing the object. Recommended
        for use in error deserialization, as we want to return the
        HttpResponseError to users, and not have them deal with
        a deserialization error.

        :param str target_obj: The target object type to deserialize to.
        :param str/dict data: The response data to deserialize.
        :param str content_type: Swagger "produces" if available.
        '''
    def deserialize_data(self, data, data_type):
        """Process data for deserialization according to data type.

        :param str data: The response string to be deserialized.
        :param str data_type: The type to deserialize to.
        :raises: DeserializationError if deserialization fails.
        :return: Deserialized object.
        """
    def deserialize_iter(self, attr, iter_type):
        """Deserialize an iterable.

        :param list attr: Iterable to be deserialized.
        :param str iter_type: The type of object in the iterable.
        :rtype: list
        """
    def deserialize_dict(self, attr, dict_type):
        """Deserialize a dictionary.

        :param dict/list attr: Dictionary to be deserialized. Also accepts
         a list of key, value pairs.
        :param str dict_type: The object type of the items in the dictionary.
        :rtype: dict
        """
    def deserialize_object(self, attr, **kwargs):
        """Deserialize a generic object.
        This will be handled as a dictionary.

        :param dict attr: Dictionary to be deserialized.
        :rtype: dict
        :raises: TypeError if non-builtin datatype encountered.
        """
    def deserialize_basic(self, attr, data_type):
        """Deserialize basic builtin data type from string.
        Will attempt to convert to str, int, float and bool.
        This function will also accept '1', '0', 'true' and 'false' as
        valid bool values.

        :param str attr: response string to be deserialized.
        :param str data_type: deserialization data type.
        :rtype: str, int, float or bool
        :raises: TypeError if string format is not valid.
        """
    @staticmethod
    def deserialize_unicode(data):
        """Preserve unicode objects in Python 2, otherwise return data
        as a string.

        :param str data: response string to be deserialized.
        :rtype: str or unicode
        """
    @staticmethod
    def deserialize_enum(data, enum_obj):
        """Deserialize string into enum object.

        If the string is not a valid enum value it will be returned as-is
        and a warning will be logged.

        :param str data: Response string to be deserialized. If this value is
         None or invalid it will be returned as-is.
        :param Enum enum_obj: Enum object to deserialize to.
        :rtype: Enum
        """
    @staticmethod
    def deserialize_bytearray(attr):
        """Deserialize string into bytearray.

        :param str attr: response string to be deserialized.
        :rtype: bytearray
        :raises: TypeError if string format invalid.
        """
    @staticmethod
    def deserialize_base64(attr):
        """Deserialize base64 encoded string into string.

        :param str attr: response string to be deserialized.
        :rtype: bytearray
        :raises: TypeError if string format invalid.
        """
    @staticmethod
    def deserialize_decimal(attr):
        """Deserialize string into Decimal object.

        :param str attr: response string to be deserialized.
        :rtype: Decimal
        :raises: DeserializationError if string format invalid.
        """
    @staticmethod
    def deserialize_long(attr):
        """Deserialize string into long (Py2) or int (Py3).

        :param str attr: response string to be deserialized.
        :rtype: long or int
        :raises: ValueError if string format invalid.
        """
    @staticmethod
    def deserialize_duration(attr):
        """Deserialize ISO-8601 formatted string into TimeDelta object.

        :param str attr: response string to be deserialized.
        :rtype: TimeDelta
        :raises: DeserializationError if string format invalid.
        """
    @staticmethod
    def deserialize_date(attr):
        """Deserialize ISO-8601 formatted string into Date object.

        :param str attr: response string to be deserialized.
        :rtype: Date
        :raises: DeserializationError if string format invalid.
        """
    @staticmethod
    def deserialize_time(attr):
        """Deserialize ISO-8601 formatted string into time object.

        :param str attr: response string to be deserialized.
        :rtype: datetime.time
        :raises: DeserializationError if string format invalid.
        """
    @staticmethod
    def deserialize_rfc(attr):
        """Deserialize RFC-1123 formatted string into Datetime object.

        :param str attr: response string to be deserialized.
        :rtype: Datetime
        :raises: DeserializationError if string format invalid.
        """
    @staticmethod
    def deserialize_iso(attr):
        """Deserialize ISO-8601 formatted string into Datetime object.

        :param str attr: response string to be deserialized.
        :rtype: Datetime
        :raises: DeserializationError if string format invalid.
        """
    @staticmethod
    def deserialize_unix(attr):
        """Serialize Datetime object into IntTime format.
        This is represented as seconds.

        :param int attr: Object to be serialized.
        :rtype: Datetime
        :raises: DeserializationError if format invalid
        """
