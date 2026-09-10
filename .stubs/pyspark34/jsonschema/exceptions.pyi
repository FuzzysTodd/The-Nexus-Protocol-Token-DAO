from _typeshed import Incomplete
from referencing.exceptions import Unresolvable as _Unresolvable

WEAK_MATCHES: frozenset[str]
STRONG_MATCHES: frozenset[str]

def __getattr__(name): ...

class _Error(Exception):
    message: Incomplete
    path: Incomplete
    schema_path: Incomplete
    context: Incomplete
    cause: Incomplete
    validator: Incomplete
    validator_value: Incomplete
    instance: Incomplete
    schema: Incomplete
    parent: Incomplete
    def __init__(self, message: str, validator=..., path=(), cause: Incomplete | None = None, context=(), validator_value=..., instance=..., schema=..., schema_path=(), parent: Incomplete | None = None, type_checker=...) -> None: ...
    @classmethod
    def create_from(cls, other): ...
    @property
    def absolute_path(self): ...
    @property
    def absolute_schema_path(self): ...
    @property
    def json_path(self): ...

class ValidationError(_Error):
    """
    An instance was invalid under a provided schema.
    """
class SchemaError(_Error):
    """
    A schema was invalid under its corresponding metaschema.
    """

class _RefResolutionError(Exception):
    """
    A ref could not be resolved.
    """
    def __eq__(self, other): ...
    def __init__(self, cause) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class _WrappedReferencingError(_RefResolutionError, _Unresolvable):
    def __init__(self, cause: _Unresolvable) -> None: ...
    def __eq__(self, other): ...
    def __getattr__(self, attr): ...
    def __hash__(self): ...

class UndefinedTypeCheck(Exception):
    """
    A type checker was asked to check a type it did not have registered.
    """
    type: Incomplete
    def __init__(self, type) -> None: ...

class UnknownType(Exception):
    """
    A validator was asked to validate an instance against an unknown type.
    """
    type: Incomplete
    instance: Incomplete
    schema: Incomplete
    def __init__(self, type, instance, schema) -> None: ...

class FormatError(Exception):
    """
    Validating a format failed.
    """
    message: Incomplete
    cause: Incomplete
    def __init__(self, message, cause: Incomplete | None = None) -> None: ...

class ErrorTree:
    """
    ErrorTrees make it easier to check which validations failed.
    """
    errors: Incomplete
    def __init__(self, errors=()) -> None: ...
    def __contains__(self, index) -> bool:
        """
        Check whether ``instance[index]`` has any errors.
        """
    def __getitem__(self, index):
        """
        Retrieve the child tree one level down at the given ``index``.

        If the index is not in the instance that this tree corresponds
        to and is not known by this tree, whatever error would be raised
        by ``instance.__getitem__`` will be propagated (usually this is
        some subclass of `LookupError`.
        """
    def __setitem__(self, index, value) -> None:
        """
        Add an error to the tree at the given ``index``.
        """
    def __iter__(self):
        """
        Iterate (non-recursively) over the indices in the instance with errors.
        """
    def __len__(self) -> int:
        """
        Return the `total_errors`.
        """
    @property
    def total_errors(self):
        """
        The total number of errors in the entire tree, including children.
        """

def by_relevance(weak=..., strong=...):
    '''
    Create a key function that can be used to sort errors by relevance.

    Arguments:
        weak (set):
            a collection of validation keywords to consider to be
            "weak".  If there are two errors at the same level of the
            instance and one is in the set of weak validation keywords,
            the other error will take priority. By default, :kw:`anyOf`
            and :kw:`oneOf` are considered weak keywords and will be
            superseded by other same-level validation errors.

        strong (set):
            a collection of validation keywords to consider to be
            "strong"
    '''

relevance: Incomplete

def best_match(errors, key=...):
    '''
    Try to find an error that appears to be the best match among given errors.

    In general, errors that are higher up in the instance (i.e. for which
    `ValidationError.path` is shorter) are considered better matches,
    since they indicate "more" is wrong with the instance.

    If the resulting match is either :kw:`oneOf` or :kw:`anyOf`, the
    *opposite* assumption is made -- i.e. the deepest error is picked,
    since these keywords only need to match once, and any other errors
    may not be relevant.

    Arguments:
        errors (collections.abc.Iterable):

            the errors to select from. Do not provide a mixture of
            errors from different validation attempts (i.e. from
            different instances or schemas), since it won\'t produce
            sensical output.

        key (collections.abc.Callable):

            the key to use when sorting errors. See `relevance` and
            transitively `by_relevance` for more details (the default is
            to sort with the defaults of that function). Changing the
            default is only useful if you want to change the function
            that rates errors but still want the error context descent
            done by this function.

    Returns:
        the best matching error, or ``None`` if the iterable was empty

    .. note::

        This function is a heuristic. Its return value may change for a given
        set of inputs from version to version if better heuristics are added.
    '''
