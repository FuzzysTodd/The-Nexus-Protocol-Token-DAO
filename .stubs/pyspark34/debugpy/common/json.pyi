import json
from _typeshed import Incomplete

JsonDecoder = json.JSONDecoder

class JsonEncoder(json.JSONEncoder):
    """Customizable JSON encoder.

    If the object implements __getstate__, then that method is invoked, and its
    result is serialized instead of the object itself.
    """
    def default(self, value): ...

class JsonObject:
    """A wrapped Python object that formats itself as JSON when asked for a string
    representation via str() or format().
    """
    json_encoder_factory = JsonEncoder
    json_encoder: Incomplete
    value: Incomplete
    def __init__(self, value) -> None: ...
    def __format__(self, format_spec) -> str:
        '''If format_spec is empty, uses self.json_encoder to serialize self.value
        as a string. Otherwise, format_spec is treated as an argument list to be
        passed to self.json_encoder_factory - which defaults to JSONEncoder - and
        then the resulting formatter is used to serialize self.value as a string.

        Example::

            format("{0} {0:indent=4,sort_keys=True}", json.repr(x))
        '''

def of_type(*classinfo, **kwargs):
    """Returns a validator for a JSON property that requires it to have a value of
    the specified type. If optional=True, () is also allowed.

    The meaning of classinfo is the same as for isinstance().
    """
def default(default):
    """Returns a validator for a JSON property with a default value.

    The validator will only allow property values that have the same type as the
    specified default value.
    """
def enum(*values, **kwargs):
    """Returns a validator for a JSON enum.

    The validator will only allow the property to have one of the specified values.

    If optional=True, and the property is missing, the first value specified is used
    as the default.
    """
def array(validate_item: bool = False, vectorize: bool = False, size: Incomplete | None = None):
    '''Returns a validator for a JSON array.

    If the property is missing, it is treated as if it were []. Otherwise, it must
    be a list.

    If validate_item=False, it\'s treated as if it were (lambda x: x) - i.e. any item
    is considered valid, and is unchanged. If validate_item is a type or a tuple,
    it\'s treated as if it were json.of_type(validate).

    Every item in the list is replaced with validate_item(item) in-place, propagating
    any exceptions raised by the latter. If validate_item is a type or a tuple, it is
    treated as if it were json.of_type(validate_item).

    If vectorize=True, and the value is neither a list nor a dict, it is treated as
    if it were a single-element list containing that single value - e.g. "foo" is
    then the same as ["foo"]; but {} is an error, and not [{}].

    If size is not None, it can be an int, a tuple of one int, a tuple of two ints,
    or a set. If it\'s an int, the array must have exactly that many elements. If it\'s
    a tuple of one int, it\'s the minimum length. If it\'s a tuple of two ints, they
    are the minimum and the maximum lengths. If it\'s a set, it\'s the set of sizes that
    are valid - e.g. for {2, 4}, the array can be either 2 or 4 elements long.
    '''
def object(validate_value: bool = False):
    """Returns a validator for a JSON object.

    If the property is missing, it is treated as if it were {}. Otherwise, it must
    be a dict.

    If validate_value=False, it's treated as if it were (lambda x: x) - i.e. any
    value is considered valid, and is unchanged. If validate_value is a type or a
    tuple, it's treated as if it were json.of_type(validate_value).

    Every value in the dict is replaced with validate_value(value) in-place, propagating
    any exceptions raised by the latter. If validate_value is a type or a tuple, it is
    treated as if it were json.of_type(validate_value). Keys are not affected.
    """
def repr(value): ...
dumps = json.dumps
loads = json.loads
