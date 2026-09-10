from _typeshed import Incomplete

class DottedName(str):
    """ Encapsulate a dotted name.  A dedicated type is used (rather than a
    str) because we need to be able to distinguish it from a quoted string when
    used as the value of an annotation.
    """

class InvalidAnnotation(Exception):
    """ An invalid annotation. """
    use: Incomplete
    def __init__(self, name, message, use) -> None:
        """ Initialise the exception. """

class RequiredAnnotation(InvalidAnnotation):
    """ A required annotation. """
    def __init__(name, use) -> None:
        """ Initialise the exception. """

def validate_annotation_value(pm, p, symbol, name, value):
    """ Return a valid value for the annotation or raise an InvalidAnnotation
    exception.
    """
def bind(validator, **proto_kw):
    """ Return a function that when called with a validator function and
    prototype keyword arguments will itself return a function that will create
    an annotation-specific validator.
    """
def validate_boolean(pm, p, symbol, name, value):
    """ Return a valid boolean value. """

boolean: Incomplete

def validate_integer(pm, p, symbol, name, value, *, optional):
    """ Return a valid, possibly optional, integer. """

integer: Incomplete

def validate_name(pm, p, symbol, name, value, *, allow_dots, optional):
    """ Return a valid, possibly optional, possibly dotted name. """

name: Incomplete

def validate_string(pm, p, symbol, name, value):
    """ Return a valid string value. """

string: Incomplete

def validate_string_list(pm, p, symbol, name, value):
    """ Return a valid string list value. """

string_list: Incomplete
