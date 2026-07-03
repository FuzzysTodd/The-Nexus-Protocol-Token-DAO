from . import attributes as attributes, instrumentation as instrumentation, loading as loading, properties as properties
from .. import event as event, inspection as inspection, log as log, schema as schema, sql as sql, util as util
from ..engine import Row as Row, RowMapping as RowMapping
from ..event import EventTarget as EventTarget, dispatcher as dispatcher
from ..sql import TableClause as TableClause, coercions as coercions, expression as expression, operators as operators, roles as roles, visitors as visitors
from ..sql._typing import _ColumnExpressionArgument
from ..sql.base import ReadOnlyColumnCollection as ReadOnlyColumnCollection
from ..sql.cache_key import MemoizedHasCacheKey as MemoizedHasCacheKey
from ..sql.elements import ColumnClause as ColumnClause, ColumnElement as ColumnElement, KeyedColumnElement as KeyedColumnElement
from ..sql.schema import Column as Column, Table as Table
from ..sql.selectable import FromClause as FromClause, LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL
from ..util import HasMemoized as HasMemoized, HasMemoized_ro_memoized_attribute as HasMemoized_ro_memoized_attribute, OrderedSet as OrderedSet
from ..util.typing import Literal as Literal
from ._typing import _IdentityKeyType, _InstanceDict, _O, _ORMColumnExprArgument, _RegistryType
from .base import PassiveFlag as PassiveFlag, state_str as state_str
from .decl_api import registry as registry
from .dependency import DependencyProcessor as DependencyProcessor
from .descriptor_props import CompositeProperty as CompositeProperty, SynonymProperty as SynonymProperty
from .events import MapperEvents as MapperEvents
from .instrumentation import ClassManager as ClassManager
from .interfaces import EXT_SKIP as EXT_SKIP, InspectionAttr as InspectionAttr, MapperProperty as MapperProperty, ORMEntityColumnsClauseRole as ORMEntityColumnsClauseRole, ORMFromClauseRole as ORMFromClauseRole, StrategizedProperty as StrategizedProperty
from .path_registry import CachingEntityRegistry as CachingEntityRegistry, PathRegistry as PathRegistry
from .properties import ColumnProperty as ColumnProperty
from .relationships import RelationshipProperty as RelationshipProperty
from .state import InstanceState as InstanceState
from .util import ORMAdapter as ORMAdapter
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generic, Iterable, Iterator, Mapping, Sequence, Tuple, Type

NO_ATTRIBUTE: Incomplete

class Mapper(ORMFromClauseRole, ORMEntityColumnsClauseRole[_O], MemoizedHasCacheKey, InspectionAttr, log.Identified, inspection.Inspectable['Mapper[_O]'], EventTarget, Generic[_O]):
    """Defines an association between a Python class and a database table or
    other relational structure, so that ORM operations against the class may
    proceed.

    The :class:`_orm.Mapper` object is instantiated using mapping methods
    present on the :class:`_orm.registry` object.  For information
    about instantiating new :class:`_orm.Mapper` objects, see
    :ref:`orm_mapping_classes_toplevel`.

    """
    dispatch: dispatcher[Mapper[_O]]
    class_: Incomplete
    non_primary: Incomplete
    always_refresh: Incomplete
    version_id_prop: Incomplete
    version_id_col: Incomplete
    version_id_generator: bool
    concrete: Incomplete
    single: bool
    inherits: Incomplete
    local_table: Incomplete
    inherit_condition: Incomplete
    inherit_foreign_keys: Incomplete
    batch: Incomplete
    eager_defaults: Incomplete
    column_prefix: Incomplete
    polymorphic_on: Incomplete
    polymorphic_abstract: Incomplete
    validators: Incomplete
    passive_updates: Incomplete
    passive_deletes: Incomplete
    legacy_is_orphan: Incomplete
    allow_partial_pks: Incomplete
    confirm_deleted_rows: bool
    polymorphic_load: Incomplete
    polymorphic_identity: Incomplete
    polymorphic_map: Incomplete
    include_properties: Incomplete
    exclude_properties: Incomplete
    def __init__(self, class_: Type[_O], local_table: FromClause | None = None, properties: Mapping[str, MapperProperty[Any]] | None = None, primary_key: Iterable[_ORMColumnExprArgument[Any]] | None = None, non_primary: bool = False, inherits: Mapper[Any] | Type[Any] | None = None, inherit_condition: _ColumnExpressionArgument[bool] | None = None, inherit_foreign_keys: Sequence[_ORMColumnExprArgument[Any]] | None = None, always_refresh: bool = False, version_id_col: _ORMColumnExprArgument[Any] | None = None, version_id_generator: Literal[False] | Callable[[Any], Any] | None = None, polymorphic_on: _ORMColumnExprArgument[Any] | str | MapperProperty[Any] | None = None, _polymorphic_map: Dict[Any, Mapper[Any]] | None = None, polymorphic_identity: Any | None = None, concrete: bool = False, with_polymorphic: _WithPolymorphicArg | None = None, polymorphic_abstract: bool = False, polymorphic_load: Literal['selectin', 'inline'] | None = None, allow_partial_pks: bool = True, batch: bool = True, column_prefix: str | None = None, include_properties: Sequence[str] | None = None, exclude_properties: Sequence[str] | None = None, passive_updates: bool = True, passive_deletes: bool = False, confirm_deleted_rows: bool = True, eager_defaults: Literal[True, False, 'auto'] = 'auto', legacy_is_orphan: bool = False, _compiled_cache_size: int = 100) -> None:
        '''Direct constructor for a new :class:`_orm.Mapper` object.

        The :class:`_orm.Mapper` constructor is not called directly, and
        is normally invoked through the
        use of the :class:`_orm.registry` object through either the
        :ref:`Declarative <orm_declarative_mapping>` or
        :ref:`Imperative <orm_imperative_mapping>` mapping styles.

        .. versionchanged:: 2.0 The public facing ``mapper()`` function is
           removed; for a classical mapping configuration, use the
           :meth:`_orm.registry.map_imperatively` method.

        Parameters documented below may be passed to either the
        :meth:`_orm.registry.map_imperatively` method, or may be passed in the
        ``__mapper_args__`` declarative class attribute described at
        :ref:`orm_declarative_mapper_options`.

        :param class\\_: The class to be mapped.  When using Declarative,
          this argument is automatically passed as the declared class
          itself.

        :param local_table: The :class:`_schema.Table` or other
           :class:`_sql.FromClause` (i.e. selectable) to which the class is
           mapped. May be ``None`` if this mapper inherits from another mapper
           using single-table inheritance. When using Declarative, this
           argument is automatically passed by the extension, based on what is
           configured via the :attr:`_orm.DeclarativeBase.__table__` attribute
           or via the :class:`_schema.Table` produced as a result of
           the :attr:`_orm.DeclarativeBase.__tablename__` attribute being
           present.

        :param polymorphic_abstract: Indicates this class will be mapped in a
            polymorphic hierarchy, but not directly instantiated. The class is
            mapped normally, except that it has no requirement for a
            :paramref:`_orm.Mapper.polymorphic_identity` within an inheritance
            hierarchy. The class however must be part of a polymorphic
            inheritance scheme which uses
            :paramref:`_orm.Mapper.polymorphic_on` at the base.

            .. versionadded:: 2.0

            .. seealso::

                :ref:`orm_inheritance_abstract_poly`

        :param always_refresh: If True, all query operations for this mapped
           class will overwrite all data within object instances that already
           exist within the session, erasing any in-memory changes with
           whatever information was loaded from the database. Usage of this
           flag is highly discouraged; as an alternative, see the method
           :meth:`_query.Query.populate_existing`.

        :param allow_partial_pks: Defaults to True.  Indicates that a
           composite primary key with some NULL values should be considered as
           possibly existing within the database. This affects whether a
           mapper will assign an incoming row to an existing identity, as well
           as if :meth:`.Session.merge` will check the database first for a
           particular primary key value. A "partial primary key" can occur if
           one has mapped to an OUTER JOIN, for example.

        :param batch: Defaults to ``True``, indicating that save operations
           of multiple entities can be batched together for efficiency.
           Setting to False indicates
           that an instance will be fully saved before saving the next
           instance.  This is used in the extremely rare case that a
           :class:`.MapperEvents` listener requires being called
           in between individual row persistence operations.

        :param column_prefix: A string which will be prepended
           to the mapped attribute name when :class:`_schema.Column`
           objects are automatically assigned as attributes to the
           mapped class.  Does not affect :class:`.Column` objects that
           are mapped explicitly in the :paramref:`.Mapper.properties`
           dictionary.

           This parameter is typically useful with imperative mappings
           that keep the :class:`.Table` object separate.  Below, assuming
           the ``user_table`` :class:`.Table` object has columns named
           ``user_id``, ``user_name``, and ``password``::

                class User(Base):
                    __table__ = user_table
                    __mapper_args__ = {\'column_prefix\':\'_\'}

           The above mapping will assign the ``user_id``, ``user_name``, and
           ``password`` columns to attributes named ``_user_id``,
           ``_user_name``, and ``_password`` on the mapped ``User`` class.

           The :paramref:`.Mapper.column_prefix` parameter is uncommon in
           modern use. For dealing with reflected tables, a more flexible
           approach to automating a naming scheme is to intercept the
           :class:`.Column` objects as they are reflected; see the section
           :ref:`mapper_automated_reflection_schemes` for notes on this usage
           pattern.

        :param concrete: If True, indicates this mapper should use concrete
           table inheritance with its parent mapper.

           See the section :ref:`concrete_inheritance` for an example.

        :param confirm_deleted_rows: defaults to True; when a DELETE occurs
          of one more rows based on specific primary keys, a warning is
          emitted when the number of rows matched does not equal the number
          of rows expected.  This parameter may be set to False to handle the
          case where database ON DELETE CASCADE rules may be deleting some of
          those rows automatically.  The warning may be changed to an
          exception in a future release.

        :param eager_defaults: if True, the ORM will immediately fetch the
          value of server-generated default values after an INSERT or UPDATE,
          rather than leaving them as expired to be fetched on next access.
          This can be used for event schemes where the server-generated values
          are needed immediately before the flush completes.

          The fetch of values occurs either by using ``RETURNING`` inline
          with the ``INSERT`` or ``UPDATE`` statement, or by adding an
          additional ``SELECT`` statement subsequent to the ``INSERT`` or
          ``UPDATE``, if the backend does not support ``RETURNING``.

          The use of ``RETURNING`` is extremely performant in particular for
          ``INSERT`` statements where SQLAlchemy can take advantage of
          :ref:`insertmanyvalues <engine_insertmanyvalues>`, whereas the use of
          an additional ``SELECT`` is relatively poor performing, adding
          additional SQL round trips which would be unnecessary if these new
          attributes are not to be accessed in any case.

          For this reason, :paramref:`.Mapper.eager_defaults` defaults to the
          string value ``"auto"``, which indicates that server defaults for
          INSERT should be fetched using ``RETURNING`` if the backing database
          supports it and if the dialect in use supports "insertmanyreturning"
          for an INSERT statement. If the backing database does not support
          ``RETURNING`` or "insertmanyreturning" is not available, server
          defaults will not be fetched.

          .. versionchanged:: 2.0.0rc1 added the "auto" option for
             :paramref:`.Mapper.eager_defaults`

          .. seealso::

                :ref:`orm_server_defaults`

          .. versionchanged:: 2.0.0  RETURNING now works with multiple rows
             INSERTed at once using the
             :ref:`insertmanyvalues <engine_insertmanyvalues>` feature, which
             among other things allows the :paramref:`.Mapper.eager_defaults`
             feature to be very performant on supporting backends.

        :param exclude_properties: A list or set of string column names to
          be excluded from mapping.

          .. seealso::

            :ref:`include_exclude_cols`

        :param include_properties: An inclusive list or set of string column
          names to map.

          .. seealso::

            :ref:`include_exclude_cols`

        :param inherits: A mapped class or the corresponding
          :class:`_orm.Mapper`
          of one indicating a superclass to which this :class:`_orm.Mapper`
          should *inherit* from.   The mapped class here must be a subclass
          of the other mapper\'s class.   When using Declarative, this argument
          is passed automatically as a result of the natural class
          hierarchy of the declared classes.

          .. seealso::

            :ref:`inheritance_toplevel`

        :param inherit_condition: For joined table inheritance, a SQL
           expression which will
           define how the two tables are joined; defaults to a natural join
           between the two tables.

        :param inherit_foreign_keys: When ``inherit_condition`` is used and
           the columns present are missing a :class:`_schema.ForeignKey`
           configuration, this parameter can be used to specify which columns
           are "foreign".  In most cases can be left as ``None``.

        :param legacy_is_orphan: Boolean, defaults to ``False``.
          When ``True``, specifies that "legacy" orphan consideration
          is to be applied to objects mapped by this mapper, which means
          that a pending (that is, not persistent) object is auto-expunged
          from an owning :class:`.Session` only when it is de-associated
          from *all* parents that specify a ``delete-orphan`` cascade towards
          this mapper.  The new default behavior is that the object is
          auto-expunged when it is de-associated with *any* of its parents
          that specify ``delete-orphan`` cascade.  This behavior is more
          consistent with that of a persistent object, and allows behavior to
          be consistent in more scenarios independently of whether or not an
          orphan object has been flushed yet or not.

          See the change note and example at :ref:`legacy_is_orphan_addition`
          for more detail on this change.

        :param non_primary: Specify that this :class:`_orm.Mapper`
          is in addition
          to the "primary" mapper, that is, the one used for persistence.
          The :class:`_orm.Mapper` created here may be used for ad-hoc
          mapping of the class to an alternate selectable, for loading
          only.

         .. seealso::

            :ref:`relationship_aliased_class` - the new pattern that removes
            the need for the :paramref:`_orm.Mapper.non_primary` flag.

        :param passive_deletes: Indicates DELETE behavior of foreign key
           columns when a joined-table inheritance entity is being deleted.
           Defaults to ``False`` for a base mapper; for an inheriting mapper,
           defaults to ``False`` unless the value is set to ``True``
           on the superclass mapper.

           When ``True``, it is assumed that ON DELETE CASCADE is configured
           on the foreign key relationships that link this mapper\'s table
           to its superclass table, so that when the unit of work attempts
           to delete the entity, it need only emit a DELETE statement for the
           superclass table, and not this table.

           When ``False``, a DELETE statement is emitted for this mapper\'s
           table individually.  If the primary key attributes local to this
           table are unloaded, then a SELECT must be emitted in order to
           validate these attributes; note that the primary key columns
           of a joined-table subclass are not part of the "primary key" of
           the object as a whole.

           Note that a value of ``True`` is **always** forced onto the
           subclass mappers; that is, it\'s not possible for a superclass
           to specify passive_deletes without this taking effect for
           all subclass mappers.

           .. seealso::

               :ref:`passive_deletes` - description of similar feature as
               used with :func:`_orm.relationship`

               :paramref:`.mapper.passive_updates` - supporting ON UPDATE
               CASCADE for joined-table inheritance mappers

        :param passive_updates: Indicates UPDATE behavior of foreign key
           columns when a primary key column changes on a joined-table
           inheritance mapping.   Defaults to ``True``.

           When True, it is assumed that ON UPDATE CASCADE is configured on
           the foreign key in the database, and that the database will handle
           propagation of an UPDATE from a source column to dependent columns
           on joined-table rows.

           When False, it is assumed that the database does not enforce
           referential integrity and will not be issuing its own CASCADE
           operation for an update.  The unit of work process will
           emit an UPDATE statement for the dependent columns during a
           primary key change.

           .. seealso::

               :ref:`passive_updates` - description of a similar feature as
               used with :func:`_orm.relationship`

               :paramref:`.mapper.passive_deletes` - supporting ON DELETE
               CASCADE for joined-table inheritance mappers

        :param polymorphic_load: Specifies "polymorphic loading" behavior
         for a subclass in an inheritance hierarchy (joined and single
         table inheritance only).   Valid values are:

          * "\'inline\'" - specifies this class should be part of
            the "with_polymorphic" mappers, e.g. its columns will be included
            in a SELECT query against the base.

          * "\'selectin\'" - specifies that when instances of this class
            are loaded, an additional SELECT will be emitted to retrieve
            the columns specific to this subclass.  The SELECT uses
            IN to fetch multiple subclasses at once.

         .. versionadded:: 1.2

         .. seealso::

            :ref:`with_polymorphic_mapper_config`

            :ref:`polymorphic_selectin`

        :param polymorphic_on: Specifies the column, attribute, or
          SQL expression used to determine the target class for an
          incoming row, when inheriting classes are present.

          May be specified as a string attribute name, or as a SQL
          expression such as a :class:`_schema.Column` or in a Declarative
          mapping a :func:`_orm.mapped_column` object.  It is typically
          expected that the SQL expression corresponds to a column in the
          base-most mapped :class:`.Table`::

            class Employee(Base):
                __tablename__ = \'employee\'

                id: Mapped[int] = mapped_column(primary_key=True)
                discriminator: Mapped[str] = mapped_column(String(50))

                __mapper_args__ = {
                    "polymorphic_on":discriminator,
                    "polymorphic_identity":"employee"
                }

          It may also be specified
          as a SQL expression, as in this example where we
          use the :func:`.case` construct to provide a conditional
          approach::

            class Employee(Base):
                __tablename__ = \'employee\'

                id: Mapped[int] = mapped_column(primary_key=True)
                discriminator: Mapped[str] = mapped_column(String(50))

                __mapper_args__ = {
                    "polymorphic_on":case(
                        (discriminator == "EN", "engineer"),
                        (discriminator == "MA", "manager"),
                        else_="employee"),
                    "polymorphic_identity":"employee"
                }

          It may also refer to any attribute using its string name,
          which is of particular use when using annotated column
          configurations::

                class Employee(Base):
                    __tablename__ = \'employee\'

                    id: Mapped[int] = mapped_column(primary_key=True)
                    discriminator: Mapped[str]

                    __mapper_args__ = {
                        "polymorphic_on": "discriminator",
                        "polymorphic_identity": "employee"
                    }

          When setting ``polymorphic_on`` to reference an
          attribute or expression that\'s not present in the
          locally mapped :class:`_schema.Table`, yet the value
          of the discriminator should be persisted to the database,
          the value of the
          discriminator is not automatically set on new
          instances; this must be handled by the user,
          either through manual means or via event listeners.
          A typical approach to establishing such a listener
          looks like::

                from sqlalchemy import event
                from sqlalchemy.orm import object_mapper

                @event.listens_for(Employee, "init", propagate=True)
                def set_identity(instance, *arg, **kw):
                    mapper = object_mapper(instance)
                    instance.discriminator = mapper.polymorphic_identity

          Where above, we assign the value of ``polymorphic_identity``
          for the mapped class to the ``discriminator`` attribute,
          thus persisting the value to the ``discriminator`` column
          in the database.

          .. warning::

             Currently, **only one discriminator column may be set**, typically
             on the base-most class in the hierarchy. "Cascading" polymorphic
             columns are not yet supported.

          .. seealso::

            :ref:`inheritance_toplevel`

        :param polymorphic_identity: Specifies the value which
          identifies this particular class as returned by the column expression
          referred to by the :paramref:`_orm.Mapper.polymorphic_on` setting. As
          rows are received, the value corresponding to the
          :paramref:`_orm.Mapper.polymorphic_on` column expression is compared
          to this value, indicating which subclass should be used for the newly
          reconstructed object.

          .. seealso::

            :ref:`inheritance_toplevel`

        :param properties: A dictionary mapping the string names of object
           attributes to :class:`.MapperProperty` instances, which define the
           persistence behavior of that attribute.  Note that
           :class:`_schema.Column`
           objects present in
           the mapped :class:`_schema.Table` are automatically placed into
           ``ColumnProperty`` instances upon mapping, unless overridden.
           When using Declarative, this argument is passed automatically,
           based on all those :class:`.MapperProperty` instances declared
           in the declared class body.

           .. seealso::

               :ref:`orm_mapping_properties` - in the
               :ref:`orm_mapping_classes_toplevel`

        :param primary_key: A list of :class:`_schema.Column`
           objects, or alternatively string names of attribute names which
           refer to :class:`_schema.Column`, which define
           the primary key to be used against this mapper\'s selectable unit.
           This is normally simply the primary key of the ``local_table``, but
           can be overridden here.

           .. versionchanged:: 2.0.2 :paramref:`_orm.Mapper.primary_key`
              arguments may be indicated as string attribute names as well.

           .. seealso::

                :ref:`mapper_primary_key` - background and example use

        :param version_id_col: A :class:`_schema.Column`
           that will be used to keep a running version id of rows
           in the table.  This is used to detect concurrent updates or
           the presence of stale data in a flush.  The methodology is to
           detect if an UPDATE statement does not match the last known
           version id, a
           :class:`~sqlalchemy.orm.exc.StaleDataError` exception is
           thrown.
           By default, the column must be of :class:`.Integer` type,
           unless ``version_id_generator`` specifies an alternative version
           generator.

           .. seealso::

              :ref:`mapper_version_counter` - discussion of version counting
              and rationale.

        :param version_id_generator: Define how new version ids should
          be generated.  Defaults to ``None``, which indicates that
          a simple integer counting scheme be employed.  To provide a custom
          versioning scheme, provide a callable function of the form::

              def generate_version(version):
                  return next_version

          Alternatively, server-side versioning functions such as triggers,
          or programmatic versioning schemes outside of the version id
          generator may be used, by specifying the value ``False``.
          Please see :ref:`server_side_version_counter` for a discussion
          of important points when using this option.

          .. seealso::

             :ref:`custom_version_counter`

             :ref:`server_side_version_counter`


        :param with_polymorphic: A tuple in the form ``(<classes>,
            <selectable>)`` indicating the default style of "polymorphic"
            loading, that is, which tables are queried at once. <classes> is
            any single or list of mappers and/or classes indicating the
            inherited classes that should be loaded at once. The special value
            ``\'*\'`` may be used to indicate all descending classes should be
            loaded immediately. The second tuple argument <selectable>
            indicates a selectable that will be used to query for multiple
            classes.

            The :paramref:`_orm.Mapper.polymorphic_load` parameter may be
            preferable over the use of :paramref:`_orm.Mapper.with_polymorphic`
            in modern mappings to indicate a per-subclass technique of
            indicating polymorphic loading styles.

            .. seealso::

                :ref:`with_polymorphic_mapper_config`

        '''
    is_mapper: bool
    represents_outer_join: bool
    registry: _RegistryType
    @property
    def mapper(self) -> Mapper[_O]:
        """Part of the inspection API.

        Returns self.

        """
    @property
    def entity(self):
        """Part of the inspection API.

        Returns self.class\\_.

        """
    tables: Sequence[TableClause]
    with_polymorphic: Tuple[Literal['*'] | Sequence[Mapper[Any] | Type[Any]], FromClause | None] | None
    persist_selectable: FromClause
    configured: bool
    primary_key: Tuple[Column[Any], ...]
    class_manager: ClassManager[_O]
    base_mapper: Mapper[Any]
    columns: ReadOnlyColumnCollection[str, Column[Any]]
    c: ReadOnlyColumnCollection[str, Column[Any]]
    def mapped_table(self): ...
    def add_properties(self, dict_of_properties) -> None:
        """Add the given dictionary of properties to this mapper,
        using `add_property`.

        """
    def add_property(self, key: str, prop: Column[Any] | MapperProperty[Any]) -> None:
        """Add an individual MapperProperty to this mapper.

        If the mapper has not been configured yet, just adds the
        property to the initial properties dictionary sent to the
        constructor.  If this Mapper has already been configured, then
        the given MapperProperty is configured immediately.

        """
    def has_property(self, key: str) -> bool: ...
    def get_property(self, key: str, _configure_mappers: bool = False) -> MapperProperty[Any]:
        """return a MapperProperty associated with the given key."""
    def get_property_by_column(self, column: ColumnElement[_T]) -> MapperProperty[_T]:
        """Given a :class:`_schema.Column` object, return the
        :class:`.MapperProperty` which maps this column."""
    @property
    def iterate_properties(self):
        """return an iterator of all MapperProperty objects."""
    with_polymorphic_mappers: Incomplete
    def __clause_element__(self): ...
    def select_identity_token(self): ...
    @property
    def selectable(self) -> FromClause:
        '''The :class:`_schema.FromClause` construct this
        :class:`_orm.Mapper` selects from by default.

        Normally, this is equivalent to :attr:`.persist_selectable`, unless
        the ``with_polymorphic`` feature is in use, in which case the
        full "polymorphic" selectable is returned.

        '''
    def attrs(self) -> util.ReadOnlyProperties[MapperProperty[Any]]:
        """A namespace of all :class:`.MapperProperty` objects
        associated this mapper.

        This is an object that provides each property based on
        its key name.  For instance, the mapper for a
        ``User`` class which has ``User.name`` attribute would
        provide ``mapper.attrs.name``, which would be the
        :class:`.ColumnProperty` representing the ``name``
        column.   The namespace object can also be iterated,
        which would yield each :class:`.MapperProperty`.

        :class:`_orm.Mapper` has several pre-filtered views
        of this attribute which limit the types of properties
        returned, including :attr:`.synonyms`, :attr:`.column_attrs`,
        :attr:`.relationships`, and :attr:`.composites`.

        .. warning::

            The :attr:`_orm.Mapper.attrs` accessor namespace is an
            instance of :class:`.OrderedProperties`.  This is
            a dictionary-like object which includes a small number of
            named methods such as :meth:`.OrderedProperties.items`
            and :meth:`.OrderedProperties.values`.  When
            accessing attributes dynamically, favor using the dict-access
            scheme, e.g. ``mapper.attrs[somename]`` over
            ``getattr(mapper.attrs, somename)`` to avoid name collisions.

        .. seealso::

            :attr:`_orm.Mapper.all_orm_descriptors`

        """
    def all_orm_descriptors(self) -> util.ReadOnlyProperties[InspectionAttr]:
        """A namespace of all :class:`.InspectionAttr` attributes associated
        with the mapped class.

        These attributes are in all cases Python :term:`descriptors`
        associated with the mapped class or its superclasses.

        This namespace includes attributes that are mapped to the class
        as well as attributes declared by extension modules.
        It includes any Python descriptor type that inherits from
        :class:`.InspectionAttr`.  This includes
        :class:`.QueryableAttribute`, as well as extension types such as
        :class:`.hybrid_property`, :class:`.hybrid_method` and
        :class:`.AssociationProxy`.

        To distinguish between mapped attributes and extension attributes,
        the attribute :attr:`.InspectionAttr.extension_type` will refer
        to a constant that distinguishes between different extension types.

        The sorting of the attributes is based on the following rules:

        1. Iterate through the class and its superclasses in order from
           subclass to superclass (i.e. iterate through ``cls.__mro__``)

        2. For each class, yield the attributes in the order in which they
           appear in ``__dict__``, with the exception of those in step
           3 below.  In Python 3.6 and above this ordering will be the
           same as that of the class' construction, with the exception
           of attributes that were added after the fact by the application
           or the mapper.

        3. If a certain attribute key is also in the superclass ``__dict__``,
           then it's included in the iteration for that class, and not the
           class in which it first appeared.

        The above process produces an ordering that is deterministic in terms
        of the order in which attributes were assigned to the class.

        .. versionchanged:: 1.3.19 ensured deterministic ordering for
           :meth:`_orm.Mapper.all_orm_descriptors`.

        When dealing with a :class:`.QueryableAttribute`, the
        :attr:`.QueryableAttribute.property` attribute refers to the
        :class:`.MapperProperty` property, which is what you get when
        referring to the collection of mapped properties via
        :attr:`_orm.Mapper.attrs`.

        .. warning::

            The :attr:`_orm.Mapper.all_orm_descriptors`
            accessor namespace is an
            instance of :class:`.OrderedProperties`.  This is
            a dictionary-like object which includes a small number of
            named methods such as :meth:`.OrderedProperties.items`
            and :meth:`.OrderedProperties.values`.  When
            accessing attributes dynamically, favor using the dict-access
            scheme, e.g. ``mapper.all_orm_descriptors[somename]`` over
            ``getattr(mapper.all_orm_descriptors, somename)`` to avoid name
            collisions.

        .. seealso::

            :attr:`_orm.Mapper.attrs`

        """
    def synonyms(self) -> util.ReadOnlyProperties[SynonymProperty[Any]]:
        """Return a namespace of all :class:`.Synonym`
        properties maintained by this :class:`_orm.Mapper`.

        .. seealso::

            :attr:`_orm.Mapper.attrs` - namespace of all
            :class:`.MapperProperty`
            objects.

        """
    @property
    def entity_namespace(self): ...
    def column_attrs(self) -> util.ReadOnlyProperties[ColumnProperty[Any]]:
        """Return a namespace of all :class:`.ColumnProperty`
        properties maintained by this :class:`_orm.Mapper`.

        .. seealso::

            :attr:`_orm.Mapper.attrs` - namespace of all
            :class:`.MapperProperty`
            objects.

        """
    def relationships(self) -> util.ReadOnlyProperties[RelationshipProperty[Any]]:
        """A namespace of all :class:`.Relationship` properties
        maintained by this :class:`_orm.Mapper`.

        .. warning::

            the :attr:`_orm.Mapper.relationships` accessor namespace is an
            instance of :class:`.OrderedProperties`.  This is
            a dictionary-like object which includes a small number of
            named methods such as :meth:`.OrderedProperties.items`
            and :meth:`.OrderedProperties.values`.  When
            accessing attributes dynamically, favor using the dict-access
            scheme, e.g. ``mapper.relationships[somename]`` over
            ``getattr(mapper.relationships, somename)`` to avoid name
            collisions.

        .. seealso::

            :attr:`_orm.Mapper.attrs` - namespace of all
            :class:`.MapperProperty`
            objects.

        """
    def composites(self) -> util.ReadOnlyProperties[CompositeProperty[Any]]:
        """Return a namespace of all :class:`.Composite`
        properties maintained by this :class:`_orm.Mapper`.

        .. seealso::

            :attr:`_orm.Mapper.attrs` - namespace of all
            :class:`.MapperProperty`
            objects.

        """
    def common_parent(self, other: Mapper[Any]) -> bool:
        """Return true if the given mapper shares a
        common inherited parent as this mapper."""
    def is_sibling(self, other: Mapper[Any]) -> bool:
        """return true if the other mapper is an inheriting sibling to this
        one.  common parent but different branch

        """
    def isa(self, other: Mapper[Any]) -> bool:
        """Return True if the this mapper inherits from the given mapper."""
    def iterate_to_root(self) -> Iterator[Mapper[Any]]: ...
    def self_and_descendants(self) -> Sequence[Mapper[Any]]:
        """The collection including this mapper and all descendant mappers.

        This includes not just the immediately inheriting mappers but
        all their inheriting mappers as well.

        """
    def polymorphic_iterator(self) -> Iterator[Mapper[Any]]:
        """Iterate through the collection including this mapper and
        all descendant mappers.

        This includes not just the immediately inheriting mappers but
        all their inheriting mappers as well.

        To iterate through an entire hierarchy, use
        ``mapper.base_mapper.polymorphic_iterator()``.

        """
    def primary_mapper(self) -> Mapper[Any]:
        """Return the primary mapper corresponding to this mapper's class key
        (class)."""
    @property
    def primary_base_mapper(self) -> Mapper[Any]: ...
    def identity_key_from_row(self, row: Row[Any] | RowMapping | None, identity_token: Any | None = None, adapter: ORMAdapter | None = None) -> _IdentityKeyType[_O]:
        '''Return an identity-map key for use in storing/retrieving an
        item from the identity map.

        :param row: A :class:`.Row` or :class:`.RowMapping` produced from a
         result set that selected from the ORM mapped primary key columns.

         .. versionchanged:: 2.0
            :class:`.Row` or :class:`.RowMapping` are accepted
            for the "row" argument

        '''
    def identity_key_from_primary_key(self, primary_key: Tuple[Any, ...], identity_token: Any | None = None) -> _IdentityKeyType[_O]:
        """Return an identity-map key for use in storing/retrieving an
        item from an identity map.

        :param primary_key: A list of values indicating the identifier.

        """
    def identity_key_from_instance(self, instance: _O) -> _IdentityKeyType[_O]:
        """Return the identity key for the given instance, based on
        its primary key attributes.

        If the instance's state is expired, calling this method
        will result in a database check to see if the object has been deleted.
        If the row no longer exists,
        :class:`~sqlalchemy.orm.exc.ObjectDeletedError` is raised.

        This value is typically also found on the instance state under the
        attribute name `key`.

        """
    def primary_key_from_instance(self, instance: _O) -> Tuple[Any, ...]:
        """Return the list of primary key values for the given
        instance.

        If the instance's state is expired, calling this method
        will result in a database check to see if the object has been deleted.
        If the row no longer exists,
        :class:`~sqlalchemy.orm.exc.ObjectDeletedError` is raised.

        """
    def cascade_iterator(self, type_: str, state: InstanceState[_O], halt_on: Callable[[InstanceState[Any]], bool] | None = None) -> Iterator[Tuple[object, Mapper[Any], InstanceState[Any], _InstanceDict]]:
        '''Iterate each element and its mapper in an object graph,
        for all relationships that meet the given cascade rule.

        :param type\\_:
          The name of the cascade rule (i.e. ``"save-update"``, ``"delete"``,
          etc.).

          .. note::  the ``"all"`` cascade is not accepted here.  For a generic
             object traversal function, see :ref:`faq_walk_objects`.

        :param state:
          The lead InstanceState.  child items will be processed per
          the relationships defined for this object\'s mapper.

        :return: the method yields individual object instances.

        .. seealso::

            :ref:`unitofwork_cascades`

            :ref:`faq_walk_objects` - illustrates a generic function to
            traverse all objects without relying on cascades.

        '''

class _OptGetColumnsNotAvailable(Exception): ...

def configure_mappers() -> None:
    """Initialize the inter-mapper relationships of all mappers that
    have been constructed thus far across all :class:`_orm.registry`
    collections.

    The configure step is used to reconcile and initialize the
    :func:`_orm.relationship` linkages between mapped classes, as well as to
    invoke configuration events such as the
    :meth:`_orm.MapperEvents.before_configured` and
    :meth:`_orm.MapperEvents.after_configured`, which may be used by ORM
    extensions or user-defined extension hooks.

    Mapper configuration is normally invoked automatically, the first time
    mappings from a particular :class:`_orm.registry` are used, as well as
    whenever mappings are used and additional not-yet-configured mappers have
    been constructed. The automatic configuration process however is local only
    to the :class:`_orm.registry` involving the target mapper and any related
    :class:`_orm.registry` objects which it may depend on; this is
    equivalent to invoking the :meth:`_orm.registry.configure` method
    on a particular :class:`_orm.registry`.

    By contrast, the :func:`_orm.configure_mappers` function will invoke the
    configuration process on all :class:`_orm.registry` objects that
    exist in memory, and may be useful for scenarios where many individual
    :class:`_orm.registry` objects that are nonetheless interrelated are
    in use.

    .. versionchanged:: 1.4

        As of SQLAlchemy 1.4.0b2, this function works on a
        per-:class:`_orm.registry` basis, locating all :class:`_orm.registry`
        objects present and invoking the :meth:`_orm.registry.configure` method
        on each. The :meth:`_orm.registry.configure` method may be preferred to
        limit the configuration of mappers to those local to a particular
        :class:`_orm.registry` and/or declarative base class.

    Points at which automatic configuration is invoked include when a mapped
    class is instantiated into an instance, as well as when ORM queries
    are emitted using :meth:`.Session.query` or :meth:`_orm.Session.execute`
    with an ORM-enabled statement.

    The mapper configure process, whether invoked by
    :func:`_orm.configure_mappers` or from :meth:`_orm.registry.configure`,
    provides several event hooks that can be used to augment the mapper
    configuration step. These hooks include:

    * :meth:`.MapperEvents.before_configured` - called once before
      :func:`.configure_mappers` or :meth:`_orm.registry.configure` does any
      work; this can be used to establish additional options, properties, or
      related mappings before the operation proceeds.

    * :meth:`.MapperEvents.mapper_configured` - called as each individual
      :class:`_orm.Mapper` is configured within the process; will include all
      mapper state except for backrefs set up by other mappers that are still
      to be configured.

    * :meth:`.MapperEvents.after_configured` - called once after
      :func:`.configure_mappers` or :meth:`_orm.registry.configure` is
      complete; at this stage, all :class:`_orm.Mapper` objects that fall
      within the scope of the configuration operation will be fully configured.
      Note that the calling application may still have other mappings that
      haven't been produced yet, such as if they are in modules as yet
      unimported, and may also have mappings that are still to be configured,
      if they are in other :class:`_orm.registry` collections not part of the
      current scope of configuration.

    """
def reconstructor(fn):
    '''Decorate a method as the \'reconstructor\' hook.

    Designates a single method as the "reconstructor", an ``__init__``-like
    method that will be called by the ORM after the instance has been
    loaded from the database or otherwise reconstituted.

    .. tip::

        The :func:`_orm.reconstructor` decorator makes use of the
        :meth:`_orm.InstanceEvents.load` event hook, which can be
        used directly.

    The reconstructor will be invoked with no arguments.  Scalar
    (non-collection) database-mapped attributes of the instance will
    be available for use within the function.  Eagerly-loaded
    collections are generally not yet available and will usually only
    contain the first element.  ORM state changes made to objects at
    this stage will not be recorded for the next flush() operation, so
    the activity within a reconstructor should be conservative.

    .. seealso::

        :meth:`.InstanceEvents.load`

    '''
def validates(*names: str, include_removes: bool = False, include_backrefs: bool = True) -> Callable[[_Fn], _Fn]:
    '''Decorate a method as a \'validator\' for one or more named properties.

    Designates a method as a validator, a method which receives the
    name of the attribute as well as a value to be assigned, or in the
    case of a collection, the value to be added to the collection.
    The function can then raise validation exceptions to halt the
    process from continuing (where Python\'s built-in ``ValueError``
    and ``AssertionError`` exceptions are reasonable choices), or can
    modify or replace the value before proceeding. The function should
    otherwise return the given value.

    Note that a validator for a collection **cannot** issue a load of that
    collection within the validation routine - this usage raises
    an assertion to avoid recursion overflows.  This is a reentrant
    condition which is not supported.

    :param \\*names: list of attribute names to be validated.
    :param include_removes: if True, "remove" events will be
     sent as well - the validation function must accept an additional
     argument "is_remove" which will be a boolean.

    :param include_backrefs: defaults to ``True``; if ``False``, the
     validation function will not emit if the originator is an attribute
     event related via a backref.  This can be used for bi-directional
     :func:`.validates` usage where only one validator should emit per
     attribute operation.

     .. versionchanged:: 2.0.16 This paramter inadvertently defaulted to
        ``False`` for releases 2.0.0 through 2.0.15.  Its correct default
        of ``True`` is restored in 2.0.16.

    .. seealso::

      :ref:`simple_validators` - usage examples for :func:`.validates`

    '''

class _ColumnMapping(Dict['ColumnElement[Any]', 'MapperProperty[Any]']):
    """Error reporting helper for mapper._columntoproperty."""
    mapper: Incomplete
    def __init__(self, mapper) -> None: ...
    def __missing__(self, column) -> None: ...
