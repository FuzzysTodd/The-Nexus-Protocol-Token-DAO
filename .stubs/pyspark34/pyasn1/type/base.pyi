from _typeshed import Incomplete

__all__ = ['Asn1Item', 'Asn1Type', 'SimpleAsn1Type', 'ConstructedAsn1Type']

class Asn1Item:
    @classmethod
    def getTypeId(cls, increment: int = 1): ...

class Asn1Type(Asn1Item):
    """Base class for all classes representing ASN.1 types.

    In the user code, |ASN.1| class is normally used only for telling
    ASN.1 objects from others.

    Note
    ----
    For as long as ASN.1 is concerned, a way to compare ASN.1 types
    is to use :meth:`isSameTypeWith` and :meth:`isSuperTypeOf` methods.
    """
    tagSet: Incomplete
    subtypeSpec: Incomplete
    typeId: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    @property
    def readOnly(self): ...
    @property
    def effectiveTagSet(self):
        """For |ASN.1| type is equivalent to *tagSet*
        """
    @property
    def tagMap(self):
        """Return a :class:`~pyasn1.type.tagmap.TagMap` object mapping ASN.1 tags to ASN.1 objects within callee object.
        """
    def isSameTypeWith(self, other, matchTags: bool = True, matchConstraints: bool = True):
        """Examine |ASN.1| type for equality with other ASN.1 type.

        ASN.1 tags (:py:mod:`~pyasn1.type.tag`) and constraints
        (:py:mod:`~pyasn1.type.constraint`) are examined when carrying
        out ASN.1 types comparison.

        Python class inheritance relationship is NOT considered.

        Parameters
        ----------
        other: a pyasn1 type object
            Class instance representing ASN.1 type.

        Returns
        -------
        : :class:`bool`
            :obj:`True` if *other* is |ASN.1| type,
            :obj:`False` otherwise.
        """
    def isSuperTypeOf(self, other, matchTags: bool = True, matchConstraints: bool = True):
        """Examine |ASN.1| type for subtype relationship with other ASN.1 type.

        ASN.1 tags (:py:mod:`~pyasn1.type.tag`) and constraints
        (:py:mod:`~pyasn1.type.constraint`) are examined when carrying
        out ASN.1 types comparison.

        Python class inheritance relationship is NOT considered.

        Parameters
        ----------
            other: a pyasn1 type object
                Class instance representing ASN.1 type.

        Returns
        -------
            : :class:`bool`
                :obj:`True` if *other* is a subtype of |ASN.1| type,
                :obj:`False` otherwise.
        """
    @staticmethod
    def isNoValue(*values): ...
    def prettyPrint(self, scope: int = 0) -> None: ...
    def getTagSet(self): ...
    def getEffectiveTagSet(self): ...
    def getTagMap(self): ...
    def getSubtypeSpec(self): ...
    def hasValue(self): ...
Asn1ItemBase = Asn1Type

class NoValue:
    """Create a singleton instance of NoValue class.

    The *NoValue* sentinel object represents an instance of ASN.1 schema
    object as opposed to ASN.1 value object.

    Only ASN.1 schema-related operations can be performed on ASN.1
    schema objects.

    Warning
    -------
    Any operation attempted on the *noValue* object will raise the
    *PyAsn1Error* exception.
    """
    skipMethods: Incomplete
    def __new__(cls): ...
    def __getattr__(self, attr) -> None: ...

class SimpleAsn1Type(Asn1Type):
    """Base class for all simple classes representing ASN.1 types.

    ASN.1 distinguishes types by their ability to hold other objects.
    Scalar types are known as *simple* in ASN.1.

    In the user code, |ASN.1| class is normally used only for telling
    ASN.1 objects from others.

    Note
    ----
    For as long as ASN.1 is concerned, a way to compare ASN.1 types
    is to use :meth:`isSameTypeWith` and :meth:`isSuperTypeOf` methods.
    """
    defaultValue = noValue
    def __init__(self, value=..., **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __bool__(self) -> bool: ...
    def __hash__(self): ...
    @property
    def isValue(self):
        """Indicate that |ASN.1| object represents ASN.1 value.

        If *isValue* is :obj:`False` then this object represents just
        ASN.1 schema.

        If *isValue* is :obj:`True` then, in addition to its ASN.1 schema
        features, this object can also be used like a Python built-in object
        (e.g. :class:`int`, :class:`str`, :class:`dict` etc.).

        Returns
        -------
        : :class:`bool`
            :obj:`False` if object represents just ASN.1 schema.
            :obj:`True` if object represents ASN.1 schema and can be used as a normal value.

        Note
        ----
        There is an important distinction between PyASN1 schema and value objects.
        The PyASN1 schema objects can only participate in ASN.1 schema-related
        operations (e.g. defining or testing the structure of the data). Most
        obvious uses of ASN.1 schema is to guide serialisation codecs whilst
        encoding/decoding serialised ASN.1 contents.

        The PyASN1 value objects can **additionally** participate in many operations
        involving regular Python objects (e.g. arithmetic, comprehension etc).
        """
    def clone(self, value=..., **kwargs):
        """Create a modified version of |ASN.1| schema or value object.

        The `clone()` method accepts the same set arguments as |ASN.1|
        class takes on instantiation except that all arguments
        of the `clone()` method are optional.

        Whatever arguments are supplied, they are used to create a copy
        of `self` taking precedence over the ones used to instantiate `self`.

        Note
        ----
        Due to the immutable nature of the |ASN.1| object, if no arguments
        are supplied, no new |ASN.1| object will be created and `self` will
        be returned instead.
        """
    def subtype(self, value=..., **kwargs):
        """Create a specialization of |ASN.1| schema or value object.

        The subtype relationship between ASN.1 types has no correlation with
        subtype relationship between Python types. ASN.1 type is mainly identified
        by its tag(s) (:py:class:`~pyasn1.type.tag.TagSet`) and value range
        constraints (:py:class:`~pyasn1.type.constraint.ConstraintsIntersection`).
        These ASN.1 type properties are implemented as |ASN.1| attributes.  

        The `subtype()` method accepts the same set arguments as |ASN.1|
        class takes on instantiation except that all parameters
        of the `subtype()` method are optional.

        With the exception of the arguments described below, the rest of
        supplied arguments they are used to create a copy of `self` taking
        precedence over the ones used to instantiate `self`.

        The following arguments to `subtype()` create a ASN.1 subtype out of
        |ASN.1| type:

        Other Parameters
        ----------------
        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to `self`'s
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to `self`'s
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Add ASN.1 constraints object to one of the `self`'s, then
            use the result as new object's ASN.1 constraints.

        Returns
        -------
        :
            new instance of |ASN.1| schema or value object

        Note
        ----
        Due to the immutable nature of the |ASN.1| object, if no arguments
        are supplied, no new |ASN.1| object will be created and `self` will
        be returned instead.
        """
    def prettyIn(self, value): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = 0): ...
    def prettyPrintType(self, scope: int = 0): ...
AbstractSimpleAsn1Item = SimpleAsn1Type

class ConstructedAsn1Type(Asn1Type):
    '''Base class for all constructed classes representing ASN.1 types.

    ASN.1 distinguishes types by their ability to hold other objects.
    Those "nesting" types are known as *constructed* in ASN.1.

    In the user code, |ASN.1| class is normally used only for telling
    ASN.1 objects from others.

    Note
    ----
    For as long as ASN.1 is concerned, a way to compare ASN.1 types
    is to use :meth:`isSameTypeWith` and :meth:`isSuperTypeOf` methods.
    '''
    strictConstraints: bool
    componentType: Incomplete
    sizeSpec: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __bool__(self) -> bool: ...
    @property
    def components(self) -> None: ...
    def clone(self, **kwargs):
        """Create a modified version of |ASN.1| schema object.

        The `clone()` method accepts the same set arguments as |ASN.1|
        class takes on instantiation except that all arguments
        of the `clone()` method are optional.

        Whatever arguments are supplied, they are used to create a copy
        of `self` taking precedence over the ones used to instantiate `self`.

        Possible values of `self` are never copied over thus `clone()` can
        only create a new schema object.

        Returns
        -------
        :
            new instance of |ASN.1| type/value

        Note
        ----
        Due to the mutable nature of the |ASN.1| object, even if no arguments
        are supplied, a new |ASN.1| object will be created and returned.
        """
    def subtype(self, **kwargs):
        """Create a specialization of |ASN.1| schema object.

        The `subtype()` method accepts the same set arguments as |ASN.1|
        class takes on instantiation except that all parameters
        of the `subtype()` method are optional.

        With the exception of the arguments described below, the rest of
        supplied arguments they are used to create a copy of `self` taking
        precedence over the ones used to instantiate `self`.

        The following arguments to `subtype()` create a ASN.1 subtype out of
        |ASN.1| type.

        Other Parameters
        ----------------
        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to `self`'s
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to `self`'s
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Add ASN.1 constraints object to one of the `self`'s, then
            use the result as new object's ASN.1 constraints.


        Returns
        -------
        :
            new instance of |ASN.1| type/value

        Note
        ----
        Due to the mutable nature of the |ASN.1| object, even if no arguments
        are supplied, a new |ASN.1| object will be created and returned.
        """
    def getComponentByPosition(self, idx) -> None: ...
    def setComponentByPosition(self, idx, value, verifyConstraints: bool = True) -> None: ...
    def setComponents(self, *args, **kwargs): ...
    def setDefaultComponents(self) -> None: ...
    def getComponentType(self): ...
    def verifySizeSpec(self) -> None: ...
AbstractConstructedAsn1Item = ConstructedAsn1Type
