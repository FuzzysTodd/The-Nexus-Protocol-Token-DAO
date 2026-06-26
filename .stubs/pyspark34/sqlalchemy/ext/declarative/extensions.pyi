from ...engine import Connection as Connection, Engine as Engine
from ...orm import relationships as relationships
from ...orm.util import polymorphic_union as polymorphic_union
from ...schema import Table as Table
from ...sql.schema import MetaData as MetaData
from ...util import OrderedDict as OrderedDict
from typing import Any

class ConcreteBase:
    """A helper class for 'concrete' declarative mappings.

    :class:`.ConcreteBase` will use the :func:`.polymorphic_union`
    function automatically, against all tables mapped as a subclass
    to this class.   The function is called via the
    ``__declare_last__()`` function, which is essentially
    a hook for the :meth:`.after_configured` event.

    :class:`.ConcreteBase` produces a mapped
    table for the class itself.  Compare to :class:`.AbstractConcreteBase`,
    which does not.

    Example::

        from sqlalchemy.ext.declarative import ConcreteBase

        class Employee(ConcreteBase, Base):
            __tablename__ = 'employee'
            employee_id = Column(Integer, primary_key=True)
            name = Column(String(50))
            __mapper_args__ = {
                            'polymorphic_identity':'employee',
                            'concrete':True}

        class Manager(Employee):
            __tablename__ = 'manager'
            employee_id = Column(Integer, primary_key=True)
            name = Column(String(50))
            manager_data = Column(String(40))
            __mapper_args__ = {
                            'polymorphic_identity':'manager',
                            'concrete':True}


    The name of the discriminator column used by :func:`.polymorphic_union`
    defaults to the name ``type``.  To suit the use case of a mapping where an
    actual column in a mapped table is already named ``type``, the
    discriminator name can be configured by setting the
    ``_concrete_discriminator_name`` attribute::

        class Employee(ConcreteBase, Base):
            _concrete_discriminator_name = '_concrete_discriminator'

    .. versionadded:: 1.3.19 Added the ``_concrete_discriminator_name``
       attribute to :class:`_declarative.ConcreteBase` so that the
       virtual discriminator column name can be customized.

    .. versionchanged:: 1.4.2 The ``_concrete_discriminator_name`` attribute
       need only be placed on the basemost class to take correct effect for
       all subclasses.   An explicit error message is now raised if the
       mapped column names conflict with the discriminator name, whereas
       in the 1.3.x series there would be some warnings and then a non-useful
       query would be generated.

    .. seealso::

        :class:`.AbstractConcreteBase`

        :ref:`concrete_inheritance`


    """
    @classmethod
    def __declare_first__(cls) -> None: ...

class AbstractConcreteBase(ConcreteBase):
    '''A helper class for \'concrete\' declarative mappings.

    :class:`.AbstractConcreteBase` will use the :func:`.polymorphic_union`
    function automatically, against all tables mapped as a subclass
    to this class.   The function is called via the
    ``__declare_first__()`` function, which is essentially
    a hook for the :meth:`.before_configured` event.

    :class:`.AbstractConcreteBase` applies :class:`_orm.Mapper` for its
    immediately inheriting class, as would occur for any other
    declarative mapped class. However, the :class:`_orm.Mapper` is not
    mapped to any particular :class:`.Table` object.  Instead, it\'s
    mapped directly to the "polymorphic" selectable produced by
    :func:`.polymorphic_union`, and performs no persistence operations on its
    own.  Compare to :class:`.ConcreteBase`, which maps its
    immediately inheriting class to an actual
    :class:`.Table` that stores rows directly.

    .. note::

        The :class:`.AbstractConcreteBase` delays the mapper creation of the
        base class until all the subclasses have been defined,
        as it needs to create a mapping against a selectable that will include
        all subclass tables.  In order to achieve this, it waits for the
        **mapper configuration event** to occur, at which point it scans
        through all the configured subclasses and sets up a mapping that will
        query against all subclasses at once.

        While this event is normally invoked automatically, in the case of
        :class:`.AbstractConcreteBase`, it may be necessary to invoke it
        explicitly after **all** subclass mappings are defined, if the first
        operation is to be a query against this base class. To do so, once all
        the desired classes have been configured, the
        :meth:`_orm.registry.configure` method on the :class:`_orm.registry`
        in use can be invoked, which is available in relation to a particular
        declarative base class::

            Base.registry.configure()

    Example::

        from sqlalchemy.orm import DeclarativeBase
        from sqlalchemy.ext.declarative import AbstractConcreteBase

        class Base(DeclarativeBase):
            pass

        class Employee(AbstractConcreteBase, Base):
            pass

        class Manager(Employee):
            __tablename__ = \'manager\'
            employee_id = Column(Integer, primary_key=True)
            name = Column(String(50))
            manager_data = Column(String(40))

            __mapper_args__ = {
                \'polymorphic_identity\':\'manager\',
                \'concrete\':True
            }

        Base.registry.configure()

    The abstract base class is handled by declarative in a special way;
    at class configuration time, it behaves like a declarative mixin
    or an ``__abstract__`` base class.   Once classes are configured
    and mappings are produced, it then gets mapped itself, but
    after all of its descendants.  This is a very unique system of mapping
    not found in any other SQLAlchemy API feature.

    Using this approach, we can specify columns and properties
    that will take place on mapped subclasses, in the way that
    we normally do as in :ref:`declarative_mixins`::

        from sqlalchemy.ext.declarative import AbstractConcreteBase

        class Company(Base):
            __tablename__ = \'company\'
            id = Column(Integer, primary_key=True)

        class Employee(AbstractConcreteBase, Base):
            strict_attrs = True

            employee_id = Column(Integer, primary_key=True)

            @declared_attr
            def company_id(cls):
                return Column(ForeignKey(\'company.id\'))

            @declared_attr
            def company(cls):
                return relationship("Company")

        class Manager(Employee):
            __tablename__ = \'manager\'

            name = Column(String(50))
            manager_data = Column(String(40))

            __mapper_args__ = {
                \'polymorphic_identity\':\'manager\',
                \'concrete\':True
            }

        Base.registry.configure()

    When we make use of our mappings however, both ``Manager`` and
    ``Employee`` will have an independently usable ``.company`` attribute::

        session.execute(
            select(Employee).filter(Employee.company.has(id=5))
        )

    :param strict_attrs: when specified on the base class, "strict" attribute
     mode is enabled which attempts to limit ORM mapped attributes on the
     base class to only those that are immediately present, while still
     preserving "polymorphic" loading behavior.

     .. versionadded:: 2.0

    .. seealso::

        :class:`.ConcreteBase`

        :ref:`concrete_inheritance`

        :ref:`abstract_concrete_base`

    '''
    __no_table__: bool
    @classmethod
    def __declare_first__(cls) -> None: ...

class DeferredReflection:
    '''A helper class for construction of mappings based on
    a deferred reflection step.

    Normally, declarative can be used with reflection by
    setting a :class:`_schema.Table` object using autoload_with=engine
    as the ``__table__`` attribute on a declarative class.
    The caveat is that the :class:`_schema.Table` must be fully
    reflected, or at the very least have a primary key column,
    at the point at which a normal declarative mapping is
    constructed, meaning the :class:`_engine.Engine` must be available
    at class declaration time.

    The :class:`.DeferredReflection` mixin moves the construction
    of mappers to be at a later point, after a specific
    method is called which first reflects all :class:`_schema.Table`
    objects created so far.   Classes can define it as such::

        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.ext.declarative import DeferredReflection
        Base = declarative_base()

        class MyClass(DeferredReflection, Base):
            __tablename__ = \'mytable\'

    Above, ``MyClass`` is not yet mapped.   After a series of
    classes have been defined in the above fashion, all tables
    can be reflected and mappings created using
    :meth:`.prepare`::

        engine = create_engine("someengine://...")
        DeferredReflection.prepare(engine)

    The :class:`.DeferredReflection` mixin can be applied to individual
    classes, used as the base for the declarative base itself,
    or used in a custom abstract class.   Using an abstract base
    allows that only a subset of classes to be prepared for a
    particular prepare step, which is necessary for applications
    that use more than one engine.  For example, if an application
    has two engines, you might use two bases, and prepare each
    separately, e.g.::

        class ReflectedOne(DeferredReflection, Base):
            __abstract__ = True

        class ReflectedTwo(DeferredReflection, Base):
            __abstract__ = True

        class MyClass(ReflectedOne):
            __tablename__ = \'mytable\'

        class MyOtherClass(ReflectedOne):
            __tablename__ = \'myothertable\'

        class YetAnotherClass(ReflectedTwo):
            __tablename__ = \'yetanothertable\'

        # ... etc.

    Above, the class hierarchies for ``ReflectedOne`` and
    ``ReflectedTwo`` can be configured separately::

        ReflectedOne.prepare(engine_one)
        ReflectedTwo.prepare(engine_two)

    .. seealso::

        :ref:`orm_declarative_reflected_deferred_reflection` - in the
        :ref:`orm_declarative_table_config_toplevel` section.

    '''
    @classmethod
    def prepare(cls, bind: Engine | Connection, **reflect_kw: Any) -> None:
        """Reflect all :class:`_schema.Table` objects for all current
        :class:`.DeferredReflection` subclasses

        :param bind: :class:`_engine.Engine` or :class:`_engine.Connection`
         instance

         ..versionchanged:: 2.0.16 a :class:`_engine.Connection` is also
         accepted.

        :param \\**reflect_kw: additional keyword arguments passed to
         :meth:`_schema.MetaData.reflect`, such as
         :paramref:`_schema.MetaData.reflect.views`.

         .. versionadded:: 2.0.16

        """
