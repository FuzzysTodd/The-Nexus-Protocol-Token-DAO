from . import attributes as attributes, clsregistry as clsregistry, instrumentation as instrumentation, interfaces as interfaces, mapperlib as mapperlib
from .. import exc as exc, inspection as inspection, util as util
from ..sql import sqltypes as sqltypes
from ..sql.base import _NoArg
from ..sql.elements import SQLCoreOperations as SQLCoreOperations
from ..sql.schema import MetaData as MetaData
from ..sql.selectable import FromClause as FromClause
from ..util import hybridmethod as hybridmethod, hybridproperty as hybridproperty
from ..util.typing import CallableReference as CallableReference, Literal as Literal, Self as Self, flatten_newtype as flatten_newtype, is_generic as is_generic, is_literal as is_literal, is_newtype as is_newtype
from ._orm_constructors import composite as composite, deferred as deferred, mapped_column as mapped_column, relationship as relationship, synonym as synonym
from ._typing import _O, _RegistryType
from .attributes import InstrumentedAttribute as InstrumentedAttribute
from .base import Mapped as Mapped, ORMDescriptor as ORMDescriptor
from .descriptor_props import Composite as Composite, Synonym as Synonym
from .instrumentation import ClassManager as ClassManager
from .interfaces import MapperProperty as MapperProperty
from .mapper import Mapper as Mapper
from .properties import MappedColumn as MappedColumn
from .relationships import RelationshipProperty as RelationshipProperty
from .state import InstanceState as InstanceState
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, Dict, FrozenSet, Generic, Type, overload

def has_inherited_table(cls) -> bool:
    """Given a class, return True if any of the classes it inherits from has a
    mapped table, otherwise return False.

    This is used in declarative mixins to build attributes that behave
    differently for the base class vs. a subclass in an inheritance
    hierarchy.

    .. seealso::

        :ref:`decl_mixin_inheritance`

    """

class _DynamicAttributesType(type):
    def __setattr__(cls, key: str, value: Any) -> None: ...
    def __delattr__(cls, key: str) -> None: ...

class DeclarativeAttributeIntercept(_DynamicAttributesType, inspection.Inspectable[Mapper[Any]]):
    """Metaclass that may be used in conjunction with the
    :class:`_orm.DeclarativeBase` class to support addition of class
    attributes dynamically.

    """
class DCTransformDeclarative(DeclarativeAttributeIntercept):
    """metaclass that includes @dataclass_transforms"""

class DeclarativeMeta(DeclarativeAttributeIntercept):
    metadata: MetaData
    registry: RegistryType
    def __init__(cls, classname: Any, bases: Any, dict_: Any, **kw: Any) -> None: ...

def synonym_for(name: str, map_column: bool = False) -> Callable[[Callable[..., Any]], Synonym[Any]]:
    '''Decorator that produces an :func:`_orm.synonym`
    attribute in conjunction with a Python descriptor.

    The function being decorated is passed to :func:`_orm.synonym` as the
    :paramref:`.orm.synonym.descriptor` parameter::

        class MyClass(Base):
            __tablename__ = \'my_table\'

            id = Column(Integer, primary_key=True)
            _job_status = Column("job_status", String(50))

            @synonym_for("job_status")
            @property
            def job_status(self):
                return "Status: %s" % self._job_status

    The :ref:`hybrid properties <mapper_hybrids>` feature of SQLAlchemy
    is typically preferred instead of synonyms, which is a more legacy
    feature.

    .. seealso::

        :ref:`synonyms` - Overview of synonyms

        :func:`_orm.synonym` - the mapper-level function

        :ref:`mapper_hybrids` - The Hybrid Attribute extension provides an
        updated approach to augmenting attribute behavior more flexibly than
        can be achieved with synonyms.

    '''

class _declared_attr_common:
    fget: Incomplete
    __doc__: Incomplete
    def __init__(self, fn: Callable[..., Any], cascading: bool = False, quiet: bool = False) -> None: ...
    def __get__(self, instance: object | None, owner: Any) -> Any: ...

class _declared_directive(_declared_attr_common, Generic[_T]):
    def __init__(self, fn: Callable[..., _T], cascading: bool = False) -> None: ...
    def __get__(self, instance: object | None, owner: Any) -> _T: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...
    def __call__(self, fn: Callable[..., _TT]) -> _declared_directive[_TT]: ...

class declared_attr(interfaces._MappedAttribute[_T], _declared_attr_common):
    '''Mark a class-level method as representing the definition of
    a mapped property or Declarative directive.

    :class:`_orm.declared_attr` is typically applied as a decorator to a class
    level method, turning the attribute into a scalar-like property that can be
    invoked from the uninstantiated class. The Declarative mapping process
    looks for these :class:`_orm.declared_attr` callables as it scans classes,
    and assumes any attribute marked with :class:`_orm.declared_attr` will be a
    callable that will produce an object specific to the Declarative mapping or
    table configuration.

    :class:`_orm.declared_attr` is usually applicable to
    :ref:`mixins <orm_mixins_toplevel>`, to define relationships that are to be
    applied to different implementors of the class. It may also be used to
    define dynamically generated column expressions and other Declarative
    attributes.

    Example::

        class ProvidesUserMixin:
            "A mixin that adds a \'user\' relationship to classes."

            user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

            @declared_attr
            def user(cls) -> Mapped["User"]:
                return relationship("User")

    When used with Declarative directives such as ``__tablename__``, the
    :meth:`_orm.declared_attr.directive` modifier may be used which indicates
    to :pep:`484` typing tools that the given method is not dealing with
    :class:`_orm.Mapped` attributes::

        class CreateTableName:
            @declared_attr.directive
            def __tablename__(cls) -> str:
                return cls.__name__.lower()

    :class:`_orm.declared_attr` can also be applied directly to mapped
    classes, to allow for attributes that dynamically configure themselves
    on subclasses when using mapped inheritance schemes.   Below
    illustrates :class:`_orm.declared_attr` to create a dynamic scheme
    for generating the :paramref:`_orm.Mapper.polymorphic_identity` parameter
    for subclasses::

        class Employee(Base):
            __tablename__ = \'employee\'

            id: Mapped[int] = mapped_column(primary_key=True)
            type: Mapped[str] = mapped_column(String(50))

            @declared_attr.directive
            def __mapper_args__(cls) -> Dict[str, Any]:
                if cls.__name__ == \'Employee\':
                    return {
                            "polymorphic_on":cls.type,
                            "polymorphic_identity":"Employee"
                    }
                else:
                    return {"polymorphic_identity":cls.__name__}

        class Engineer(Employee):
            pass

    :class:`_orm.declared_attr` supports decorating functions that are
    explicitly decorated with ``@classmethod``. This is never necessary from a
    runtime perspective, however may be needed in order to support :pep:`484`
    typing tools that don\'t otherwise recognize the decorated function as
    having class-level behaviors for the ``cls`` parameter::

        class SomethingMixin:
            x: Mapped[int]
            y: Mapped[int]

            @declared_attr
            @classmethod
            def x_plus_y(cls) -> Mapped[int]:
                return column_property(cls.x + cls.y)

    .. versionadded:: 2.0 - :class:`_orm.declared_attr` can accommodate a
       function decorated with ``@classmethod`` to help with :pep:`484`
       integration where needed.


    .. seealso::

        :ref:`orm_mixins_toplevel` - Declarative Mixin documentation with
        background on use patterns for :class:`_orm.declared_attr`.

    '''
    def __init__(self, fn: _DeclaredAttrDecorated[_T], cascading: bool = False) -> None: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T: ...
    def directive(cls) -> _declared_directive[Any]: ...
    def cascading(cls) -> _stateful_declared_attr[_T]: ...

class _stateful_declared_attr(declared_attr[_T]):
    kw: Dict[str, Any]
    def __init__(self, **kw: Any) -> None: ...
    def __call__(self, fn: _DeclaredAttrDecorated[_T]) -> declared_attr[_T]: ...

def declarative_mixin(cls) -> Type[_T]:
    '''Mark a class as providing the feature of "declarative mixin".

    E.g.::

        from sqlalchemy.orm import declared_attr
        from sqlalchemy.orm import declarative_mixin

        @declarative_mixin
        class MyMixin:

            @declared_attr
            def __tablename__(cls):
                return cls.__name__.lower()

            __table_args__ = {\'mysql_engine\': \'InnoDB\'}
            __mapper_args__= {\'always_refresh\': True}

            id =  Column(Integer, primary_key=True)

        class MyModel(MyMixin, Base):
            name = Column(String(1000))

    The :func:`_orm.declarative_mixin` decorator currently does not modify
    the given class in any way; it\'s current purpose is strictly to assist
    the :ref:`Mypy plugin <mypy_toplevel>` in being able to identify
    SQLAlchemy declarative mixin classes when no other context is present.

    .. versionadded:: 1.4.6

    .. seealso::

        :ref:`orm_mixins_toplevel`

        :ref:`mypy_declarative_mixins` - in the
        :ref:`Mypy plugin documentation <mypy_toplevel>`

    '''

class MappedAsDataclass(metaclass=DCTransformDeclarative):
    """Mixin class to indicate when mapping this class, also convert it to be
    a dataclass.

    .. seealso::

        :ref:`orm_declarative_native_dataclasses` - complete background
        on SQLAlchemy native dataclass mapping

    .. versionadded:: 2.0

    """
    def __init_subclass__(cls, init: _NoArg | bool = ..., repr: _NoArg | bool = ..., eq: _NoArg | bool = ..., order: _NoArg | bool = ..., unsafe_hash: _NoArg | bool = ..., match_args: _NoArg | bool = ..., kw_only: _NoArg | bool = ..., dataclass_callable: _NoArg | Callable[..., Type[Any]] = ...) -> None: ...

class DeclarativeBase(inspection.Inspectable[InstanceState[Any]], metaclass=DeclarativeAttributeIntercept):
    '''Base class used for declarative class definitions.

    The :class:`_orm.DeclarativeBase` allows for the creation of new
    declarative bases in such a way that is compatible with type checkers::


        from sqlalchemy.orm import DeclarativeBase

        class Base(DeclarativeBase):
            pass


    The above ``Base`` class is now usable as the base for new declarative
    mappings.  The superclass makes use of the ``__init_subclass__()``
    method to set up new classes and metaclasses aren\'t used.

    When first used, the :class:`_orm.DeclarativeBase` class instantiates a new
    :class:`_orm.registry` to be used with the base, assuming one was not
    provided explicitly. The :class:`_orm.DeclarativeBase` class supports
    class-level attributes which act as parameters for the construction of this
    registry; such as to indicate a specific :class:`_schema.MetaData`
    collection as well as a specific value for
    :paramref:`_orm.registry.type_annotation_map`::

        from typing_extensions import Annotated

        from sqlalchemy import BigInteger
        from sqlalchemy import MetaData
        from sqlalchemy import String
        from sqlalchemy.orm import DeclarativeBase

        bigint = Annotated[int, "bigint"]
        my_metadata = MetaData()

        class Base(DeclarativeBase):
            metadata = my_metadata
            type_annotation_map = {
                str: String().with_variant(String(255), "mysql", "mariadb"),
                bigint: BigInteger()
            }

    Class-level attributes which may be specified include:

    :param metadata: optional :class:`_schema.MetaData` collection.
     If a :class:`_orm.registry` is constructed automatically, this
     :class:`_schema.MetaData` collection will be used to construct it.
     Otherwise, the local :class:`_schema.MetaData` collection will supercede
     that used by an existing :class:`_orm.registry` passed using the
     :paramref:`_orm.DeclarativeBase.registry` parameter.
    :param type_annotation_map: optional type annotation map that will be
     passed to the :class:`_orm.registry` as
     :paramref:`_orm.registry.type_annotation_map`.
    :param registry: supply a pre-existing :class:`_orm.registry` directly.

    .. versionadded:: 2.0  Added :class:`.DeclarativeBase`, so that declarative
       base classes may be constructed in such a way that is also recognized
       by :pep:`484` type checkers.   As a result, :class:`.DeclarativeBase`
       and other subclassing-oriented APIs should be seen as
       superseding previous "class returned by a function" APIs, namely
       :func:`_orm.declarative_base` and :meth:`_orm.registry.generate_base`,
       where the base class returned cannot be recognized by type checkers
       without using plugins.

    **__init__ behavior**

    In a plain Python class, the base-most ``__init__()`` method in the class
    hierarchy is ``object.__init__()``, which accepts no arguments. However,
    when the :class:`_orm.DeclarativeBase` subclass is first declared, the
    class is given an ``__init__()`` method that links to the
    :paramref:`_orm.registry.constructor` constructor function, if no
    ``__init__()`` method is already present; this is the usual declarative
    constructor that will assign keyword arguments as attributes on the
    instance, assuming those attributes are established at the class level
    (i.e. are mapped, or are linked to a descriptor). This constructor is
    **never accessed by a mapped class without being called explicitly via
    super()**, as mapped classes are themselves given an ``__init__()`` method
    directly which calls :paramref:`_orm.registry.constructor`, so in the
    default case works independently of what the base-most ``__init__()``
    method does.

    .. versionchanged:: 2.0.1  :class:`_orm.DeclarativeBase` has a default
       constructor that links to :paramref:`_orm.registry.constructor` by
       default, so that calls to ``super().__init__()`` can access this
       constructor. Previously, due to an implementation mistake, this default
       constructor was missing, and calling ``super().__init__()`` would invoke
       ``object.__init__()``.

    The :class:`_orm.DeclarativeBase` subclass may also declare an explicit
    ``__init__()`` method which will replace the use of the
    :paramref:`_orm.registry.constructor` function at this level::

        class Base(DeclarativeBase):
            def __init__(self, id=None):
                self.id = id

    Mapped classes still will not invoke this constructor implicitly; it
    remains only accessible by calling ``super().__init__()``::

        class MyClass(Base):
            def __init__(self, id=None, name=None):
                self.name = name
                super().__init__(id=id)

    Note that this is a different behavior from what functions like the legacy
    :func:`_orm.declarative_base` would do; the base created by those functions
    would always install :paramref:`_orm.registry.constructor` for
    ``__init__()``.


    '''
    registry: ClassVar[_RegistryType]
    metadata: ClassVar[MetaData]
    __mapper__: ClassVar[Mapper[Any]]
    __table__: ClassVar[FromClause]
    __tablename__: Any
    __mapper_args__: Any
    __table_args__: Any
    def __init__(self, **kw: Any) -> None: ...
    def __init_subclass__(cls) -> None: ...

class DeclarativeBaseNoMeta(inspection.Inspectable[InstanceState[Any]]):
    """Same as :class:`_orm.DeclarativeBase`, but does not use a metaclass
    to intercept new attributes.

    The :class:`_orm.DeclarativeBaseNoMeta` base may be used when use of
    custom metaclasses is desirable.

    .. versionadded:: 2.0


    """
    registry: ClassVar[_RegistryType]
    metadata: ClassVar[MetaData]
    __mapper__: ClassVar[Mapper[Any]]
    __table__: FromClause | None
    __tablename__: Any
    __mapper_args__: Any
    __table_args__: Any
    def __init__(self, **kw: Any) -> None: ...
    def __init_subclass__(cls) -> None: ...

def add_mapped_attribute(target: Type[_O], key: str, attr: MapperProperty[Any]) -> None:
    '''Add a new mapped attribute to an ORM mapped class.

    E.g.::

        add_mapped_attribute(User, "addresses", relationship(Address))

    This may be used for ORM mappings that aren\'t using a declarative
    metaclass that intercepts attribute set operations.

    .. versionadded:: 2.0


    '''
def declarative_base(*, metadata: MetaData | None = None, mapper: Callable[..., Mapper[Any]] | None = None, cls: Type[Any] = ..., name: str = 'Base', class_registry: clsregistry._ClsRegistryType | None = None, type_annotation_map: _TypeAnnotationMapType | None = None, constructor: Callable[..., None] = ..., metaclass: Type[Any] = ...) -> Any:
    '''Construct a base class for declarative class definitions.

    The new base class will be given a metaclass that produces
    appropriate :class:`~sqlalchemy.schema.Table` objects and makes
    the appropriate :class:`_orm.Mapper` calls based on the
    information provided declaratively in the class and any subclasses
    of the class.

    .. versionchanged:: 2.0 Note that the :func:`_orm.declarative_base`
       function is superseded by the new :class:`_orm.DeclarativeBase` class,
       which generates a new "base" class using subclassing, rather than
       return value of a function.  This allows an approach that is compatible
       with :pep:`484` typing tools.

    The :func:`_orm.declarative_base` function is a shorthand version
    of using the :meth:`_orm.registry.generate_base`
    method.  That is, the following::

        from sqlalchemy.orm import declarative_base

        Base = declarative_base()

    Is equivalent to::

        from sqlalchemy.orm import registry

        mapper_registry = registry()
        Base = mapper_registry.generate_base()

    See the docstring for :class:`_orm.registry`
    and :meth:`_orm.registry.generate_base`
    for more details.

    .. versionchanged:: 1.4  The :func:`_orm.declarative_base`
       function is now a specialization of the more generic
       :class:`_orm.registry` class.  The function also moves to the
       ``sqlalchemy.orm`` package from the ``declarative.ext`` package.


    :param metadata:
      An optional :class:`~sqlalchemy.schema.MetaData` instance.  All
      :class:`~sqlalchemy.schema.Table` objects implicitly declared by
      subclasses of the base will share this MetaData.  A MetaData instance
      will be created if none is provided.  The
      :class:`~sqlalchemy.schema.MetaData` instance will be available via the
      ``metadata`` attribute of the generated declarative base class.

    :param mapper:
      An optional callable, defaults to :class:`_orm.Mapper`. Will
      be used to map subclasses to their Tables.

    :param cls:
      Defaults to :class:`object`. A type to use as the base for the generated
      declarative base class. May be a class or tuple of classes.

    :param name:
      Defaults to ``Base``.  The display name for the generated
      class.  Customizing this is not required, but can improve clarity in
      tracebacks and debugging.

    :param constructor:
      Specify the implementation for the ``__init__`` function on a mapped
      class that has no ``__init__`` of its own.  Defaults to an
      implementation that assigns \\**kwargs for declared
      fields and relationships to an instance.  If ``None`` is supplied,
      no __init__ will be provided and construction will fall back to
      cls.__init__ by way of the normal Python semantics.

    :param class_registry: optional dictionary that will serve as the
      registry of class names-> mapped classes when string names
      are used to identify classes inside of :func:`_orm.relationship`
      and others.  Allows two or more declarative base classes
      to share the same registry of class names for simplified
      inter-base relationships.

    :param type_annotation_map: optional dictionary of Python types to
        SQLAlchemy :class:`_types.TypeEngine` classes or instances.  This
        is used exclusively by the :class:`_orm.MappedColumn` construct
        to produce column types based on annotations within the
        :class:`_orm.Mapped` type.


        .. versionadded:: 2.0

        .. seealso::

            :ref:`orm_declarative_mapped_column_type_map`

    :param metaclass:
      Defaults to :class:`.DeclarativeMeta`.  A metaclass or __metaclass__
      compatible callable to use as the meta type of the generated
      declarative base class.

    .. seealso::

        :class:`_orm.registry`

    '''

class registry:
    """Generalized registry for mapping classes.

    The :class:`_orm.registry` serves as the basis for maintaining a collection
    of mappings, and provides configurational hooks used to map classes.

    The three general kinds of mappings supported are Declarative Base,
    Declarative Decorator, and Imperative Mapping.   All of these mapping
    styles may be used interchangeably:

    * :meth:`_orm.registry.generate_base` returns a new declarative base
      class, and is the underlying implementation of the
      :func:`_orm.declarative_base` function.

    * :meth:`_orm.registry.mapped` provides a class decorator that will
      apply declarative mapping to a class without the use of a declarative
      base class.

    * :meth:`_orm.registry.map_imperatively` will produce a
      :class:`_orm.Mapper` for a class without scanning the class for
      declarative class attributes. This method suits the use case historically
      provided by the ``sqlalchemy.orm.mapper()`` classical mapping function,
      which is removed as of SQLAlchemy 2.0.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`orm_mapping_classes_toplevel` - overview of class mapping
        styles.

    """
    metadata: MetaData
    constructor: CallableReference[Callable[..., None]]
    type_annotation_map: _MutableTypeAnnotationMapType
    def __init__(self, *, metadata: MetaData | None = None, class_registry: clsregistry._ClsRegistryType | None = None, type_annotation_map: _TypeAnnotationMapType | None = None, constructor: Callable[..., None] = ...) -> None:
        """Construct a new :class:`_orm.registry`

        :param metadata:
          An optional :class:`_schema.MetaData` instance.  All
          :class:`_schema.Table` objects generated using declarative
          table mapping will make use of this :class:`_schema.MetaData`
          collection.  If this argument is left at its default of ``None``,
          a blank :class:`_schema.MetaData` collection is created.

        :param constructor:
          Specify the implementation for the ``__init__`` function on a mapped
          class that has no ``__init__`` of its own.  Defaults to an
          implementation that assigns \\**kwargs for declared
          fields and relationships to an instance.  If ``None`` is supplied,
          no __init__ will be provided and construction will fall back to
          cls.__init__ by way of the normal Python semantics.

        :param class_registry: optional dictionary that will serve as the
          registry of class names-> mapped classes when string names
          are used to identify classes inside of :func:`_orm.relationship`
          and others.  Allows two or more declarative base classes
          to share the same registry of class names for simplified
          inter-base relationships.

        :param type_annotation_map: optional dictionary of Python types to
          SQLAlchemy :class:`_types.TypeEngine` classes or instances.
          The provided dict will update the default type mapping.  This
          is used exclusively by the :class:`_orm.MappedColumn` construct
          to produce column types based on annotations within the
          :class:`_orm.Mapped` type.

          .. versionadded:: 2.0

          .. seealso::

              :ref:`orm_declarative_mapped_column_type_map`


        """
    def update_type_annotation_map(self, type_annotation_map: _TypeAnnotationMapType) -> None:
        """update the :paramref:`_orm.registry.type_annotation_map` with new
        values."""
    @property
    def mappers(self) -> FrozenSet[Mapper[Any]]:
        """read only collection of all :class:`_orm.Mapper` objects."""
    def configure(self, cascade: bool = False) -> None:
        """Configure all as-yet unconfigured mappers in this
        :class:`_orm.registry`.

        The configure step is used to reconcile and initialize the
        :func:`_orm.relationship` linkages between mapped classes, as well as
        to invoke configuration events such as the
        :meth:`_orm.MapperEvents.before_configured` and
        :meth:`_orm.MapperEvents.after_configured`, which may be used by ORM
        extensions or user-defined extension hooks.

        If one or more mappers in this registry contain
        :func:`_orm.relationship` constructs that refer to mapped classes in
        other registries, this registry is said to be *dependent* on those
        registries. In order to configure those dependent registries
        automatically, the :paramref:`_orm.registry.configure.cascade` flag
        should be set to ``True``. Otherwise, if they are not configured, an
        exception will be raised.  The rationale behind this behavior is to
        allow an application to programmatically invoke configuration of
        registries while controlling whether or not the process implicitly
        reaches other registries.

        As an alternative to invoking :meth:`_orm.registry.configure`, the ORM
        function :func:`_orm.configure_mappers` function may be used to ensure
        configuration is complete for all :class:`_orm.registry` objects in
        memory. This is generally simpler to use and also predates the usage of
        :class:`_orm.registry` objects overall. However, this function will
        impact all mappings throughout the running Python process and may be
        more memory/time consuming for an application that has many registries
        in use for different purposes that may not be needed immediately.

        .. seealso::

            :func:`_orm.configure_mappers`


        .. versionadded:: 1.4.0b2

        """
    def dispose(self, cascade: bool = False) -> None:
        """Dispose of all mappers in this :class:`_orm.registry`.

        After invocation, all the classes that were mapped within this registry
        will no longer have class instrumentation associated with them. This
        method is the per-:class:`_orm.registry` analogue to the
        application-wide :func:`_orm.clear_mappers` function.

        If this registry contains mappers that are dependencies of other
        registries, typically via :func:`_orm.relationship` links, then those
        registries must be disposed as well. When such registries exist in
        relation to this one, their :meth:`_orm.registry.dispose` method will
        also be called, if the :paramref:`_orm.registry.dispose.cascade` flag
        is set to ``True``; otherwise, an error is raised if those registries
        were not already disposed.

        .. versionadded:: 1.4.0b2

        .. seealso::

            :func:`_orm.clear_mappers`

        """
    def generate_base(self, mapper: Callable[..., Mapper[Any]] | None = None, cls: Type[Any] = ..., name: str = 'Base', metaclass: Type[Any] = ...) -> Any:
        '''Generate a declarative base class.

        Classes that inherit from the returned class object will be
        automatically mapped using declarative mapping.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            Base = mapper_registry.generate_base()

            class MyClass(Base):
                __tablename__ = "my_table"
                id = Column(Integer, primary_key=True)

        The above dynamically generated class is equivalent to the
        non-dynamic example below::

            from sqlalchemy.orm import registry
            from sqlalchemy.orm.decl_api import DeclarativeMeta

            mapper_registry = registry()

            class Base(metaclass=DeclarativeMeta):
                __abstract__ = True
                registry = mapper_registry
                metadata = mapper_registry.metadata

                __init__ = mapper_registry.constructor

        .. versionchanged:: 2.0 Note that the
           :meth:`_orm.registry.generate_base` method is superseded by the new
           :class:`_orm.DeclarativeBase` class, which generates a new "base"
           class using subclassing, rather than return value of a function.
           This allows an approach that is compatible with :pep:`484` typing
           tools.

        The :meth:`_orm.registry.generate_base` method provides the
        implementation for the :func:`_orm.declarative_base` function, which
        creates the :class:`_orm.registry` and base class all at once.

        See the section :ref:`orm_declarative_mapping` for background and
        examples.

        :param mapper:
          An optional callable, defaults to :class:`_orm.Mapper`.
          This function is used to generate new :class:`_orm.Mapper` objects.

        :param cls:
          Defaults to :class:`object`. A type to use as the base for the
          generated declarative base class. May be a class or tuple of classes.

        :param name:
          Defaults to ``Base``.  The display name for the generated
          class.  Customizing this is not required, but can improve clarity in
          tracebacks and debugging.

        :param metaclass:
          Defaults to :class:`.DeclarativeMeta`.  A metaclass or __metaclass__
          compatible callable to use as the meta type of the generated
          declarative base class.

        .. seealso::

            :ref:`orm_declarative_mapping`

            :func:`_orm.declarative_base`

        '''
    @overload
    def mapped_as_dataclass(self, __cls: Type[_O]) -> Type[_O]: ...
    @overload
    def mapped_as_dataclass(self, __cls: Literal[None] = ..., *, init: _NoArg | bool = ..., repr: _NoArg | bool = ..., eq: _NoArg | bool = ..., order: _NoArg | bool = ..., unsafe_hash: _NoArg | bool = ..., match_args: _NoArg | bool = ..., kw_only: _NoArg | bool = ..., dataclass_callable: _NoArg | Callable[..., Type[Any]] = ...) -> Callable[[Type[_O]], Type[_O]]: ...
    def mapped(self, cls: Type[_O]) -> Type[_O]:
        """Class decorator that will apply the Declarative mapping process
        to a given class.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            @mapper_registry.mapped
            class Foo:
                __tablename__ = 'some_table'

                id = Column(Integer, primary_key=True)
                name = Column(String)

        See the section :ref:`orm_declarative_mapping` for complete
        details and examples.

        :param cls: class to be mapped.

        :return: the class that was passed.

        .. seealso::

            :ref:`orm_declarative_mapping`

            :meth:`_orm.registry.generate_base` - generates a base class
            that will apply Declarative mapping to subclasses automatically
            using a Python metaclass.

        .. seealso::

            :meth:`_orm.registry.mapped_as_dataclass`

        """
    def as_declarative_base(self, **kw: Any) -> Callable[[Type[_T]], Type[_T]]:
        """
        Class decorator which will invoke
        :meth:`_orm.registry.generate_base`
        for a given base class.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            @mapper_registry.as_declarative_base()
            class Base:
                @declared_attr
                def __tablename__(cls):
                    return cls.__name__.lower()
                id = Column(Integer, primary_key=True)

            class MyMappedClass(Base):
                # ...

        All keyword arguments passed to
        :meth:`_orm.registry.as_declarative_base` are passed
        along to :meth:`_orm.registry.generate_base`.

        """
    def map_declaratively(self, cls: Type[_O]) -> Mapper[_O]:
        """Map a class declaratively.

        In this form of mapping, the class is scanned for mapping information,
        including for columns to be associated with a table, and/or an
        actual table object.

        Returns the :class:`_orm.Mapper` object.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            class Foo:
                __tablename__ = 'some_table'

                id = Column(Integer, primary_key=True)
                name = Column(String)

            mapper = mapper_registry.map_declaratively(Foo)

        This function is more conveniently invoked indirectly via either the
        :meth:`_orm.registry.mapped` class decorator or by subclassing a
        declarative metaclass generated from
        :meth:`_orm.registry.generate_base`.

        See the section :ref:`orm_declarative_mapping` for complete
        details and examples.

        :param cls: class to be mapped.

        :return: a :class:`_orm.Mapper` object.

        .. seealso::

            :ref:`orm_declarative_mapping`

            :meth:`_orm.registry.mapped` - more common decorator interface
            to this function.

            :meth:`_orm.registry.map_imperatively`

        """
    def map_imperatively(self, class_: Type[_O], local_table: FromClause | None = None, **kw: Any) -> Mapper[_O]:
        '''Map a class imperatively.

        In this form of mapping, the class is not scanned for any mapping
        information.  Instead, all mapping constructs are passed as
        arguments.

        This method is intended to be fully equivalent to the now-removed
        SQLAlchemy ``mapper()`` function, except that it\'s in terms of
        a particular registry.

        E.g.::

            from sqlalchemy.orm import registry

            mapper_registry = registry()

            my_table = Table(
                "my_table",
                mapper_registry.metadata,
                Column(\'id\', Integer, primary_key=True)
            )

            class MyClass:
                pass

            mapper_registry.map_imperatively(MyClass, my_table)

        See the section :ref:`orm_imperative_mapping` for complete background
        and usage examples.

        :param class\\_: The class to be mapped.  Corresponds to the
         :paramref:`_orm.Mapper.class_` parameter.

        :param local_table: the :class:`_schema.Table` or other
         :class:`_sql.FromClause` object that is the subject of the mapping.
         Corresponds to the
         :paramref:`_orm.Mapper.local_table` parameter.

        :param \\**kw: all other keyword arguments are passed to the
         :class:`_orm.Mapper` constructor directly.

        .. seealso::

            :ref:`orm_imperative_mapping`

            :ref:`orm_declarative_mapping`

        '''
RegistryType = registry

def as_declarative(**kw: Any) -> Callable[[Type[_T]], Type[_T]]:
    """
    Class decorator which will adapt a given class into a
    :func:`_orm.declarative_base`.

    This function makes use of the :meth:`_orm.registry.as_declarative_base`
    method, by first creating a :class:`_orm.registry` automatically
    and then invoking the decorator.

    E.g.::

        from sqlalchemy.orm import as_declarative

        @as_declarative()
        class Base:
            @declared_attr
            def __tablename__(cls):
                return cls.__name__.lower()
            id = Column(Integer, primary_key=True)

        class MyMappedClass(Base):
            # ...

    .. seealso::

        :meth:`_orm.registry.as_declarative_base`

    """
