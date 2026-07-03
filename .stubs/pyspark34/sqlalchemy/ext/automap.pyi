import dataclasses
from .. import util as util
from ..engine.base import Engine as Engine
from ..orm import backref as backref, interfaces as interfaces, relationship as relationship
from ..orm.base import RelationshipDirection as RelationshipDirection
from ..orm.relationships import ORMBackrefArgument as ORMBackrefArgument, Relationship as Relationship
from ..schema import ForeignKeyConstraint as ForeignKeyConstraint
from ..sql import and_ as and_
from ..sql.schema import Column as Column, MetaData as MetaData, Table as Table
from ..util import Properties as Properties, immutabledict as immutabledict
from ..util.typing import Protocol as Protocol
from _typeshed import Incomplete
from typing import Any, Callable, ClassVar, Dict, Set, Type, overload

class PythonNameForTableType(Protocol):
    def __call__(self, base: Type[Any], tablename: str, table: Table) -> str: ...

def classname_for_table(base: Type[Any], tablename: str, table: Table) -> str:
    """Return the class name that should be used, given the name
    of a table.

    The default implementation is::

        return str(tablename)

    Alternate implementations can be specified using the
    :paramref:`.AutomapBase.prepare.classname_for_table`
    parameter.

    :param base: the :class:`.AutomapBase` class doing the prepare.

    :param tablename: string name of the :class:`_schema.Table`.

    :param table: the :class:`_schema.Table` object itself.

    :return: a string class name.

     .. note::

        In Python 2, the string used for the class name **must** be a
        non-Unicode object, e.g. a ``str()`` object.  The ``.name`` attribute
        of :class:`_schema.Table` is typically a Python unicode subclass,
        so the
        ``str()`` function should be applied to this name, after accounting for
        any non-ASCII characters.

    """

class NameForScalarRelationshipType(Protocol):
    def __call__(self, base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str: ...

def name_for_scalar_relationship(base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str:
    """Return the attribute name that should be used to refer from one
    class to another, for a scalar object reference.

    The default implementation is::

        return referred_cls.__name__.lower()

    Alternate implementations can be specified using the
    :paramref:`.AutomapBase.prepare.name_for_scalar_relationship`
    parameter.

    :param base: the :class:`.AutomapBase` class doing the prepare.

    :param local_cls: the class to be mapped on the local side.

    :param referred_cls: the class to be mapped on the referring side.

    :param constraint: the :class:`_schema.ForeignKeyConstraint` that is being
     inspected to produce this relationship.

    """

class NameForCollectionRelationshipType(Protocol):
    def __call__(self, base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str: ...

def name_for_collection_relationship(base: Type[Any], local_cls: Type[Any], referred_cls: Type[Any], constraint: ForeignKeyConstraint) -> str:
    '''Return the attribute name that should be used to refer from one
    class to another, for a collection reference.

    The default implementation is::

        return referred_cls.__name__.lower() + "_collection"

    Alternate implementations
    can be specified using the
    :paramref:`.AutomapBase.prepare.name_for_collection_relationship`
    parameter.

    :param base: the :class:`.AutomapBase` class doing the prepare.

    :param local_cls: the class to be mapped on the local side.

    :param referred_cls: the class to be mapped on the referring side.

    :param constraint: the :class:`_schema.ForeignKeyConstraint` that is being
     inspected to produce this relationship.

    '''

class GenerateRelationshipType(Protocol):
    @overload
    def __call__(self, base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., Relationship[Any]], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> Relationship[Any]: ...
    @overload
    def __call__(self, base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., ORMBackrefArgument], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> ORMBackrefArgument: ...

@overload
def generate_relationship(base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., Relationship[Any]], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> Relationship[Any]: ...
@overload
def generate_relationship(base: Type[Any], direction: RelationshipDirection, return_fn: Callable[..., ORMBackrefArgument], attrname: str, local_cls: Type[Any], referred_cls: Type[Any], **kw: Any) -> ORMBackrefArgument: ...

ByModuleProperties: Incomplete

class AutomapBase:
    '''Base class for an "automap" schema.

    The :class:`.AutomapBase` class can be compared to the "declarative base"
    class that is produced by the :func:`.declarative.declarative_base`
    function.  In practice, the :class:`.AutomapBase` class is always used
    as a mixin along with an actual declarative base.

    A new subclassable :class:`.AutomapBase` is typically instantiated
    using the :func:`.automap_base` function.

    .. seealso::

        :ref:`automap_toplevel`

    '''
    __abstract__: bool
    classes: ClassVar[Properties[Type[Any]]]
    by_module: ClassVar[ByModuleProperties]
    metadata: ClassVar[MetaData]
    @classmethod
    def prepare(cls, autoload_with: Engine | None = None, engine: Any | None = None, reflect: bool = False, schema: str | None = None, classname_for_table: PythonNameForTableType | None = None, modulename_for_table: PythonNameForTableType | None = None, collection_class: Any | None = None, name_for_scalar_relationship: NameForScalarRelationshipType | None = None, name_for_collection_relationship: NameForCollectionRelationshipType | None = None, generate_relationship: GenerateRelationshipType | None = None, reflection_options: Dict[_KT, _VT] | immutabledict[_KT, _VT] = ...) -> None:
        '''Extract mapped classes and relationships from the
        :class:`_schema.MetaData` and perform mappings.

        For full documentation and examples see
        :ref:`automap_basic_use`.

        :param autoload_with: an :class:`_engine.Engine` or
         :class:`_engine.Connection` with which
         to perform schema reflection; when specified, the
         :meth:`_schema.MetaData.reflect` method will be invoked within
         the scope of this method.

        :param engine: legacy; use :paramref:`.AutomapBase.autoload_with`.
         Used to indicate the :class:`_engine.Engine` or
         :class:`_engine.Connection` with which to reflect tables with,
         if :paramref:`.AutomapBase.reflect` is True.

        :param reflect: legacy; use :paramref:`.AutomapBase.autoload_with`.
         Indicates that :meth:`_schema.MetaData.reflect` should be invoked.

        :param classname_for_table: callable function which will be used to
         produce new class names, given a table name.  Defaults to
         :func:`.classname_for_table`.

        :param modulename_for_table: callable function which will be used to
         produce the effective ``__module__`` for an internally generated
         class, to allow for multiple classes of the same name in a single
         automap base which would be in different "modules".

         Defaults to ``None``, which will indicate that ``__module__`` will not
         be set explicitly; the Python runtime will use the value
         ``sqlalchemy.ext.automap`` for these classes.

         When assigning ``__module__`` to generated classes, they can be
         accessed based on dot-separated module names using the
         :attr:`.AutomapBase.by_module` collection.   Classes that have
         an explicit ``__module_`` assigned using this hook do **not** get
         placed into the :attr:`.AutomapBase.classes` collection, only
         into :attr:`.AutomapBase.by_module`.

         .. versionadded:: 2.0

         .. seealso::

            :ref:`automap_by_module`

        :param name_for_scalar_relationship: callable function which will be
         used to produce relationship names for scalar relationships.  Defaults
         to :func:`.name_for_scalar_relationship`.

        :param name_for_collection_relationship: callable function which will
         be used to produce relationship names for collection-oriented
         relationships.  Defaults to :func:`.name_for_collection_relationship`.

        :param generate_relationship: callable function which will be used to
         actually generate :func:`_orm.relationship` and :func:`.backref`
         constructs.  Defaults to :func:`.generate_relationship`.

        :param collection_class: the Python collection class that will be used
         when a new :func:`_orm.relationship`
         object is created that represents a
         collection.  Defaults to ``list``.

        :param schema: Schema name to reflect when reflecting tables using
         the :paramref:`.AutomapBase.prepare.autoload_with` parameter. The name
         is passed to the :paramref:`_schema.MetaData.reflect.schema` parameter
         of :meth:`_schema.MetaData.reflect`. When omitted, the default schema
         in use by the database connection is used.

         .. note:: The :paramref:`.AutomapBase.prepare.schema`
            parameter supports reflection of a single schema at a time.
            In order to include tables from many schemas, use
            multiple calls to :meth:`.AutomapBase.prepare`.

            For an overview of multiple-schema automap including the use
            of additional naming conventions to resolve table name
            conflicts, see the section :ref:`automap_by_module`.

            .. versionadded:: 2.0 :meth:`.AutomapBase.prepare` supports being
               directly invoked any number of times, keeping track of tables
               that have already been processed to avoid processing them
               a second time.

        :param reflection_options: When present, this dictionary of options
         will be passed to :meth:`_schema.MetaData.reflect`
         to supply general reflection-specific options like ``only`` and/or
         dialect-specific options like ``oracle_resolve_synonyms``.

         .. versionadded:: 1.4

        '''

@dataclasses.dataclass
class _Bookkeeping:
    table_keys: Set[str]
    def __init__(self, table_keys) -> None: ...

def automap_base(declarative_base: Type[Any] | None = None, **kw: Any) -> Any:
    """Produce a declarative automap base.

    This function produces a new base class that is a product of the
    :class:`.AutomapBase` class as well a declarative base produced by
    :func:`.declarative.declarative_base`.

    All parameters other than ``declarative_base`` are keyword arguments
    that are passed directly to the :func:`.declarative.declarative_base`
    function.

    :param declarative_base: an existing class produced by
     :func:`.declarative.declarative_base`.  When this is passed, the function
     no longer invokes :func:`.declarative.declarative_base` itself, and all
     other keyword arguments are ignored.

    :param \\**kw: keyword arguments are passed along to
     :func:`.declarative.declarative_base`.

    """
