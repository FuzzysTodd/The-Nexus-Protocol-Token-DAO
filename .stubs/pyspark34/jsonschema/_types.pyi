from _typeshed import Incomplete
from jsonschema.exceptions import UndefinedTypeCheck as UndefinedTypeCheck

def is_array(checker, instance): ...
def is_bool(checker, instance): ...
def is_integer(checker, instance): ...
def is_null(checker, instance): ...
def is_number(checker, instance): ...
def is_object(checker, instance): ...
def is_string(checker, instance): ...
def is_any(checker, instance): ...

class TypeChecker:
    """
    A :kw:`type` property checker.

    A `TypeChecker` performs type checking for a `Validator`, converting
    between the defined JSON Schema types and some associated Python types or
    objects.

    Modifying the behavior just mentioned by redefining which Python objects
    are considered to be of which JSON Schema types can be done using
    `TypeChecker.redefine` or `TypeChecker.redefine_many`, and types can be
    removed via `TypeChecker.remove`. Each of these return a new `TypeChecker`.

    Arguments:

        type_checkers:

            The initial mapping of types to their checking functions.
    """
    def is_type(self, instance, type: str) -> bool:
        """
        Check if the instance is of the appropriate type.

        Arguments:

            instance:

                The instance to check

            type:

                The name of the type that is expected.

        Raises:

            `jsonschema.exceptions.UndefinedTypeCheck`:

                if ``type`` is unknown to this object.
        """
    def redefine(self, type: str, fn) -> TypeChecker:
        """
        Produce a new checker with the given type redefined.

        Arguments:

            type:

                The name of the type to check.

            fn (collections.abc.Callable):

                A callable taking exactly two parameters - the type
                checker calling the function and the instance to check.
                The function should return true if instance is of this
                type and false otherwise.
        """
    def redefine_many(self, definitions=()) -> TypeChecker:
        """
        Produce a new checker with the given types redefined.

        Arguments:

            definitions (dict):

                A dictionary mapping types to their checking functions.
        """
    def remove(self, *types) -> TypeChecker:
        """
        Produce a new checker with the given types forgotten.

        Arguments:

            types:

                the names of the types to remove.

        Raises:

            `jsonschema.exceptions.UndefinedTypeCheck`:

                if any given type is unknown to this object
        """
    def __init__(self, type_checkers) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

draft3_type_checker: Incomplete
draft4_type_checker: Incomplete
draft6_type_checker: Incomplete
draft7_type_checker = draft6_type_checker
draft201909_type_checker = draft7_type_checker
draft202012_type_checker = draft201909_type_checker
