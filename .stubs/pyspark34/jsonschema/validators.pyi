import referencing.jsonschema
from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Mapping
from jsonschema import _format, _types, _typing, exceptions as exceptions
from jsonschema.protocols import Validator as Validator

def __getattr__(name): ...
def validates(version):
    """
    Register the decorated validator for a ``version`` of the specification.

    Registered validators and their meta schemas will be considered when
    parsing :kw:`$schema` keywords' URIs.

    Arguments:

        version (str):

            An identifier to use as the version's name

    Returns:

        collections.abc.Callable:

            a class decorator to decorate the validator with the version
    """
def create(meta_schema: referencing.jsonschema.ObjectSchema, validators: Mapping[str, _typing.SchemaKeywordValidator] | Iterable[tuple[str, _typing.SchemaKeywordValidator]] = (), version: str | None = None, type_checker: _types.TypeChecker = ..., format_checker: _format.FormatChecker = ..., id_of: _typing.id_of = ..., applicable_validators: _typing.ApplicableValidators = ...):
    """
    Create a new validator class.

    Arguments:

        meta_schema:

            the meta schema for the new validator class

        validators:

            a mapping from names to callables, where each callable will
            validate the schema property with the given name.

            Each callable should take 4 arguments:

                1. a validator instance,
                2. the value of the property being validated within the
                   instance
                3. the instance
                4. the schema

        version:

            an identifier for the version that this validator class will
            validate. If provided, the returned validator class will
            have its ``__name__`` set to include the version, and also
            will have `jsonschema.validators.validates` automatically
            called for the given version.

        type_checker:

            a type checker, used when applying the :kw:`type` keyword.

            If unprovided, a `jsonschema.TypeChecker` will be created
            with a set of default types typical of JSON Schema drafts.

        format_checker:

            a format checker, used when applying the :kw:`format` keyword.

            If unprovided, a `jsonschema.FormatChecker` will be created
            with a set of default formats typical of JSON Schema drafts.

        id_of:

            A function that given a schema, returns its ID.

        applicable_validators:

            A function that, given a schema, returns the list of
            applicable schema keywords and associated values
            which will be used to validate the instance.
            This is mostly used to support pre-draft 7 versions of JSON Schema
            which specified behavior around ignoring keywords if they were
            siblings of a ``$ref`` keyword. If you're not attempting to
            implement similar behavior, you can typically ignore this argument
            and leave it at its default.

    Returns:

        a new `jsonschema.protocols.Validator` class
    """
def extend(validator, validators=(), version: Incomplete | None = None, type_checker: Incomplete | None = None, format_checker: Incomplete | None = None):
    '''
    Create a new validator class by extending an existing one.

    Arguments:

        validator (jsonschema.protocols.Validator):

            an existing validator class

        validators (collections.abc.Mapping):

            a mapping of new validator callables to extend with, whose
            structure is as in `create`.

            .. note::

                Any validator callables with the same name as an
                existing one will (silently) replace the old validator
                callable entirely, effectively overriding any validation
                done in the "parent" validator class.

                If you wish to instead extend the behavior of a parent\'s
                validator callable, delegate and call it directly in
                the new validator function by retrieving it using
                ``OldValidator.VALIDATORS["validation_keyword_name"]``.

        version (str):

            a version for the new validator class

        type_checker (jsonschema.TypeChecker):

            a type checker, used when applying the :kw:`type` keyword.

            If unprovided, the type checker of the extended
            `jsonschema.protocols.Validator` will be carried along.

        format_checker (jsonschema.FormatChecker):

            a format checker, used when applying the :kw:`format` keyword.

            If unprovided, the format checker of the extended
            `jsonschema.protocols.Validator` will be carried along.

    Returns:

        a new `jsonschema.protocols.Validator` class extending the one
        provided

    .. note:: Meta Schemas

        The new validator class will have its parent\'s meta schema.

        If you wish to change or extend the meta schema in the new
        validator class, modify ``META_SCHEMA`` directly on the returned
        class. Note that no implicit copying is done, so a copy should
        likely be made before modifying it, in order to not affect the
        old validator.
    '''

Draft3Validator: Incomplete
Draft4Validator: Incomplete
Draft6Validator: Incomplete
Draft7Validator: Incomplete
Draft201909Validator: Incomplete
Draft202012Validator: Incomplete

class _RefResolver:
    """
    Resolve JSON References.

    Arguments:

        base_uri (str):

            The URI of the referring document

        referrer:

            The actual referring document

        store (dict):

            A mapping from URIs to documents to cache

        cache_remote (bool):

            Whether remote refs should be cached after first resolution

        handlers (dict):

            A mapping from URI schemes to functions that should be used
            to retrieve them

        urljoin_cache (:func:`functools.lru_cache`):

            A cache that will be used for caching the results of joining
            the resolution scope to subscopes.

        remote_cache (:func:`functools.lru_cache`):

            A cache that will be used for caching the results of
            resolved remote URLs.

    Attributes:

        cache_remote (bool):

            Whether remote refs should be cached after first resolution

    .. deprecated:: v4.18.0

        ``RefResolver`` has been deprecated in favor of `referencing`.
    """
    referrer: Incomplete
    cache_remote: Incomplete
    handlers: Incomplete
    store: Incomplete
    def __init__(self, base_uri, referrer, store=..., cache_remote: bool = True, handlers=(), urljoin_cache: Incomplete | None = None, remote_cache: Incomplete | None = None) -> None: ...
    @classmethod
    def from_schema(cls, schema, id_of=..., *args, **kwargs):
        """
        Construct a resolver from a JSON schema object.

        Arguments:

            schema:

                the referring schema

        Returns:

            `_RefResolver`
        """
    def push_scope(self, scope) -> None:
        """
        Enter a given sub-scope.

        Treats further dereferences as being performed underneath the
        given scope.
        """
    def pop_scope(self) -> None:
        """
        Exit the most recent entered scope.

        Treats further dereferences as being performed underneath the
        original scope.

        Don't call this method more times than `push_scope` has been
        called.
        """
    @property
    def resolution_scope(self):
        """
        Retrieve the current resolution scope.
        """
    @property
    def base_uri(self):
        """
        Retrieve the current base URI, not including any fragment.
        """
    def in_scope(self, scope) -> Generator[None, None, None]:
        """
        Temporarily enter the given scope for the duration of the context.

        .. deprecated:: v4.0.0
        """
    def resolving(self, ref) -> Generator[Incomplete, None, None]:
        """
        Resolve the given ``ref`` and enter its resolution scope.

        Exits the scope on exit of this context manager.

        Arguments:

            ref (str):

                The reference to resolve
        """
    def resolve(self, ref):
        """
        Resolve the given reference.
        """
    def resolve_from_url(self, url):
        """
        Resolve the given URL.
        """
    def resolve_fragment(self, document, fragment):
        """
        Resolve a ``fragment`` within the referenced ``document``.

        Arguments:

            document:

                The referent document

            fragment (str):

                a URI fragment to resolve within it
        """
    def resolve_remote(self, uri):
        """
        Resolve a remote ``uri``.

        If called directly, does not check the store first, but after
        retrieving the document at the specified URI it will be saved in
        the store if :attr:`cache_remote` is True.

        .. note::

            If the requests_ library is present, ``jsonschema`` will use it to
            request the remote ``uri``, so that the correct encoding is
            detected and used.

            If it isn't, or if the scheme of the ``uri`` is not ``http`` or
            ``https``, UTF-8 is assumed.

        Arguments:

            uri (str):

                The URI to resolve

        Returns:

            The retrieved document

        .. _requests: https://pypi.org/project/requests/
        """

def validate(instance, schema, cls: Incomplete | None = None, *args, **kwargs) -> None:
    '''
    Validate an instance under the given schema.

        >>> validate([2, 3, 4], {"maxItems": 2})
        Traceback (most recent call last):
            ...
        ValidationError: [2, 3, 4] is too long

    :func:`~jsonschema.validators.validate` will first verify that the
    provided schema is itself valid, since not doing so can lead to less
    obvious error messages and fail in less obvious or consistent ways.

    If you know you have a valid schema already, especially
    if you intend to validate multiple instances with
    the same schema, you likely would prefer using the
    `jsonschema.protocols.Validator.validate` method directly on a
    specific validator (e.g. ``Draft202012Validator.validate``).


    Arguments:

        instance:

            The instance to validate

        schema:

            The schema to validate with

        cls (jsonschema.protocols.Validator):

            The class that will be used to validate the instance.

    If the ``cls`` argument is not provided, two things will happen
    in accordance with the specification. First, if the schema has a
    :kw:`$schema` keyword containing a known meta-schema [#]_ then the
    proper validator will be used. The specification recommends that
    all schemas contain :kw:`$schema` properties for this reason. If no
    :kw:`$schema` property is found, the default validator class is the
    latest released draft.

    Any other provided positional and keyword arguments will be passed
    on when instantiating the ``cls``.

    Raises:

        `jsonschema.exceptions.ValidationError`:

            if the instance is invalid

        `jsonschema.exceptions.SchemaError`:

            if the schema itself is invalid

    .. rubric:: Footnotes
    .. [#] known by a validator registered with
        `jsonschema.validators.validates`
    '''
def validator_for(schema, default=...):
    '''
    Retrieve the validator class appropriate for validating the given schema.

    Uses the :kw:`$schema` keyword that should be present in the given
    schema to look up the appropriate validator class.

    Arguments:

        schema (collections.abc.Mapping or bool):

            the schema to look at

        default:

            the default to return if the appropriate validator class
            cannot be determined.

            If unprovided, the default is to return the latest supported
            draft.

    Examples:

        The :kw:`$schema` JSON Schema keyword will control which validator
        class is returned:

        >>> schema = {
        ...     "$schema": "https://json-schema.org/draft/2020-12/schema",
        ...     "type": "integer",
        ... }
        >>> jsonschema.validators.validator_for(schema)
        <class \'jsonschema.validators.Draft202012Validator\'>


        Here, a draft 7 schema instead will return the draft 7 validator:

        >>> schema = {
        ...     "$schema": "http://json-schema.org/draft-07/schema#",
        ...     "type": "integer",
        ... }
        >>> jsonschema.validators.validator_for(schema)
        <class \'jsonschema.validators.Draft7Validator\'>


        Schemas with no ``$schema`` keyword will fallback to the default
        argument:

        >>> schema = {"type": "integer"}
        >>> jsonschema.validators.validator_for(
        ...     schema, default=Draft7Validator,
        ... )
        <class \'jsonschema.validators.Draft7Validator\'>

        or if none is provided, to the latest version supported.
        Always including the keyword when authoring schemas is highly
        recommended.

    '''
