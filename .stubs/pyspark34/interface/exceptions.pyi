__all__ = ['Invalid', 'DoesNotImplement', 'BrokenImplementation', 'BrokenMethodImplementation', 'MultipleInvalid', 'BadImplements', 'InvalidInterface']

class Invalid(Exception):
    """A specification is violated
    """

class _TargetInvalid(Invalid):
    @property
    def interface(self): ...
    @property
    def target(self): ...

class DoesNotImplement(_TargetInvalid):
    """
    DoesNotImplement(interface[, target])

    The *target* (optional) does not implement the *interface*.

    .. versionchanged:: 5.0.0
       Add the *target* argument and attribute, and change the resulting
       string value of this object accordingly.
    """

class BrokenImplementation(_TargetInvalid):
    """
    BrokenImplementation(interface, name[, target])

    The *target* (optional) is missing the attribute *name*.

    .. versionchanged:: 5.0.0
       Add the *target* argument and attribute, and change the resulting
       string value of this object accordingly.

       The *name* can either be a simple string or a ``Attribute`` object.
    """
    @property
    def name(self): ...

class BrokenMethodImplementation(_TargetInvalid):
    '''
    BrokenMethodImplementation(method, message[, implementation, interface, target])

    The *target* (optional) has a *method* in *implementation* that violates
    its contract in a way described by *mess*.

    .. versionchanged:: 5.0.0
       Add the *interface* and *target* argument and attribute,
       and change the resulting string value of this object accordingly.

       The *method* can either be a simple string or a ``Method`` object.

    .. versionchanged:: 5.0.0
       If *implementation* is given, then the *message* will have the
       string "implementation" replaced with an short but informative
       representation of *implementation*.

    '''
    @property
    def method(self): ...
    @property
    def mess(self): ...

class MultipleInvalid(_TargetInvalid):
    """
    The *target* has failed to implement the *interface* in
    multiple ways.

    The failures are described by *exceptions*, a collection of
    other `Invalid` instances.

    .. versionadded:: 5.0
    """
    def __init__(self, interface, target, exceptions) -> None: ...
    @property
    def exceptions(self): ...

class InvalidInterface(Exception):
    """The interface has invalid contents
    """
class BadImplements(TypeError):
    """An implementation assertion is invalid

    because it doesn't contain an interface or a sequence of valid
    implementation assertions.
    """
