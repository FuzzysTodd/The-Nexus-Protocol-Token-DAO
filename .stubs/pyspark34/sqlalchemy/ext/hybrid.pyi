from .. import util as util
from ..orm import InspectionAttrExtensionType as InspectionAttrExtensionType, ORMDescriptor as ORMDescriptor, attributes as attributes, interfaces as interfaces
from ..orm.attributes import QueryableAttribute as QueryableAttribute
from ..orm.interfaces import MapperProperty as MapperProperty
from ..orm.util import AliasedInsp as AliasedInsp
from ..sql import SQLColumnExpression as SQLColumnExpression, roles as roles
from ..sql._typing import _ColumnExpressionArgument, _DMLColumnArgument, _HasClauseElement, _InfoType, is_has_clause_element as is_has_clause_element
from ..sql.elements import ColumnElement as ColumnElement, SQLCoreOperations as SQLCoreOperations
from ..sql.operators import OperatorType as OperatorType
from ..util.typing import Concatenate as Concatenate, Literal as Literal, ParamSpec as ParamSpec, Protocol as Protocol, Self as Self
from _typeshed import Incomplete
from typing import Any, Callable, Generic, List, Tuple, Type, overload

class HybridExtensionType(InspectionAttrExtensionType):
    HYBRID_METHOD: str
    HYBRID_PROPERTY: str

class _HybridGetterType(Protocol[_T_co]):
    def __call__(s, self: Any) -> _T_co: ...

class _HybridSetterType(Protocol[_T_con]):
    def __call__(s, self: Any, value: _T_con) -> None: ...

class _HybridUpdaterType(Protocol[_T_con]):
    def __call__(s, cls: Any, value: _T_con | _ColumnExpressionArgument[_T_con]) -> List[Tuple[_DMLColumnArgument, Any]]: ...

class _HybridDeleterType(Protocol[_T_co]):
    def __call__(s, self: Any) -> None: ...

class _HybridExprCallableType(Protocol[_T_co]):
    def __call__(s, cls: Any) -> _HasClauseElement | SQLColumnExpression[_T_co]: ...

class _HybridComparatorCallableType(Protocol[_T]):
    def __call__(self, cls: Any) -> Comparator[_T]: ...

class _HybridClassLevelAccessor(QueryableAttribute[_T]):
    """Describe the object returned by a hybrid_property() when
    called as a class-level descriptor.

    """
    def getter(self, fget: _HybridGetterType[_T]) -> hybrid_property[_T]: ...
    def setter(self, fset: _HybridSetterType[_T]) -> hybrid_property[_T]: ...
    def deleter(self, fdel: _HybridDeleterType[_T]) -> hybrid_property[_T]: ...
    @property
    def overrides(self) -> hybrid_property[_T]: ...
    def update_expression(self, meth: _HybridUpdaterType[_T]) -> hybrid_property[_T]: ...

class hybrid_method(interfaces.InspectionAttrInfo, Generic[_P, _R]):
    """A decorator which allows definition of a Python object method with both
    instance-level and class-level behavior.

    """
    is_attribute: bool
    extension_type: Incomplete
    func: Incomplete
    def __init__(self, func: Callable[Concatenate[Any, _P], _R], expr: Callable[Concatenate[Any, _P], SQLCoreOperations[_R]] | None = None) -> None:
        """Create a new :class:`.hybrid_method`.

        Usage is typically via decorator::

            from sqlalchemy.ext.hybrid import hybrid_method

            class SomeClass:
                @hybrid_method
                def value(self, x, y):
                    return self._value + x + y

                @value.expression
                @classmethod
                def value(cls, x, y):
                    return func.some_function(cls._value, x, y)

        """
    @property
    def inplace(self) -> Self:
        '''Return the inplace mutator for this :class:`.hybrid_method`.

        The :class:`.hybrid_method` class already performs "in place" mutation
        when the :meth:`.hybrid_method.expression` decorator is called,
        so this attribute returns Self.

        .. versionadded:: 2.0.4

        .. seealso::

            :ref:`hybrid_pep484_naming`

        '''
    @overload
    def __get__(self, instance: Literal[None], owner: Type[object]) -> Callable[_P, SQLCoreOperations[_R]]: ...
    @overload
    def __get__(self, instance: object, owner: Type[object]) -> Callable[_P, _R]: ...
    expr: Incomplete
    def expression(self, expr: Callable[Concatenate[Any, _P], SQLCoreOperations[_R]]) -> hybrid_method[_P, _R]:
        """Provide a modifying decorator that defines a
        SQL-expression producing method."""

class hybrid_property(interfaces.InspectionAttrInfo, ORMDescriptor[_T]):
    """A decorator which allows definition of a Python descriptor with both
    instance-level and class-level behavior.

    """
    is_attribute: bool
    extension_type: Incomplete
    fget: Incomplete
    fset: Incomplete
    fdel: Incomplete
    expr: Incomplete
    custom_comparator: Incomplete
    update_expr: Incomplete
    def __init__(self, fget: _HybridGetterType[_T], fset: _HybridSetterType[_T] | None = None, fdel: _HybridDeleterType[_T] | None = None, expr: _HybridExprCallableType[_T] | None = None, custom_comparator: Comparator[_T] | None = None, update_expr: _HybridUpdaterType[_T] | None = None) -> None:
        """Create a new :class:`.hybrid_property`.

        Usage is typically via decorator::

            from sqlalchemy.ext.hybrid import hybrid_property

            class SomeClass:
                @hybrid_property
                def value(self):
                    return self._value

                @value.setter
                def value(self, value):
                    self._value = value

        """
    @overload
    def __get__(self, instance: Any, owner: Literal[None]) -> Self: ...
    @overload
    def __get__(self, instance: Literal[None], owner: Type[object]) -> _HybridClassLevelAccessor[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Type[object]) -> _T: ...
    def __set__(self, instance: object, value: Any) -> None: ...
    def __delete__(self, instance: object) -> None: ...
    @property
    def overrides(self) -> Self:
        '''Prefix for a method that is overriding an existing attribute.

        The :attr:`.hybrid_property.overrides` accessor just returns
        this hybrid object, which when called at the class level from
        a parent class, will de-reference the "instrumented attribute"
        normally returned at this level, and allow modifying decorators
        like :meth:`.hybrid_property.expression` and
        :meth:`.hybrid_property.comparator`
        to be used without conflicting with the same-named attributes
        normally present on the :class:`.QueryableAttribute`::

            class SuperClass:
                # ...

                @hybrid_property
                def foobar(self):
                    return self._foobar

            class SubClass(SuperClass):
                # ...

                @SuperClass.foobar.overrides.expression
                def foobar(cls):
                    return func.subfoobar(self._foobar)

        .. versionadded:: 1.2

        .. seealso::

            :ref:`hybrid_reuse_subclass`

        '''
    class _InPlace(Generic[_TE]):
        """A builder helper for .hybrid_property.

        .. versionadded:: 2.0.4

        """
        attr: Incomplete
        def __init__(self, attr: hybrid_property[_TE]) -> None: ...
        def getter(self, fget: _HybridGetterType[_TE]) -> hybrid_property[_TE]: ...
        def setter(self, fset: _HybridSetterType[_TE]) -> hybrid_property[_TE]: ...
        def deleter(self, fdel: _HybridDeleterType[_TE]) -> hybrid_property[_TE]: ...
        def expression(self, expr: _HybridExprCallableType[_TE]) -> hybrid_property[_TE]: ...
        def comparator(self, comparator: _HybridComparatorCallableType[_TE]) -> hybrid_property[_TE]: ...
        def update_expression(self, meth: _HybridUpdaterType[_TE]) -> hybrid_property[_TE]: ...
    @property
    def inplace(self) -> _InPlace[_T]:
        """Return the inplace mutator for this :class:`.hybrid_property`.

        This is to allow in-place mutation of the hybrid, allowing the first
        hybrid method of a certain name to be re-used in order to add
        more methods without having to name those methods the same, e.g.::

            class Interval(Base):
                # ...

                @hybrid_property
                def radius(self) -> float:
                    return abs(self.length) / 2

                @radius.inplace.setter
                def _radius_setter(self, value: float) -> None:
                    self.length = value * 2

                @radius.inplace.expression
                def _radius_expression(cls) -> ColumnElement[float]:
                    return type_coerce(func.abs(cls.length) / 2, Float)

        .. versionadded:: 2.0.4

        .. seealso::

            :ref:`hybrid_pep484_naming`

        """
    def getter(self, fget: _HybridGetterType[_T]) -> hybrid_property[_T]:
        """Provide a modifying decorator that defines a getter method.

        .. versionadded:: 1.2

        """
    def setter(self, fset: _HybridSetterType[_T]) -> hybrid_property[_T]:
        """Provide a modifying decorator that defines a setter method."""
    def deleter(self, fdel: _HybridDeleterType[_T]) -> hybrid_property[_T]:
        """Provide a modifying decorator that defines a deletion method."""
    def expression(self, expr: _HybridExprCallableType[_T]) -> hybrid_property[_T]:
        """Provide a modifying decorator that defines a SQL-expression
        producing method.

        When a hybrid is invoked at the class level, the SQL expression given
        here is wrapped inside of a specialized :class:`.QueryableAttribute`,
        which is the same kind of object used by the ORM to represent other
        mapped attributes.   The reason for this is so that other class-level
        attributes such as docstrings and a reference to the hybrid itself may
        be maintained within the structure that's returned, without any
        modifications to the original SQL expression passed in.

        .. note::

           When referring to a hybrid property  from an owning class (e.g.
           ``SomeClass.some_hybrid``), an instance of
           :class:`.QueryableAttribute` is returned, representing the
           expression or comparator object as well as this  hybrid object.
           However, that object itself has accessors called ``expression`` and
           ``comparator``; so when attempting to override these decorators on a
           subclass, it may be necessary to qualify it using the
           :attr:`.hybrid_property.overrides` modifier first.  See that
           modifier for details.

        .. seealso::

            :ref:`hybrid_distinct_expression`

        """
    def comparator(self, comparator: _HybridComparatorCallableType[_T]) -> hybrid_property[_T]:
        """Provide a modifying decorator that defines a custom
        comparator producing method.

        The return value of the decorated method should be an instance of
        :class:`~.hybrid.Comparator`.

        .. note::  The :meth:`.hybrid_property.comparator` decorator
           **replaces** the use of the :meth:`.hybrid_property.expression`
           decorator.  They cannot be used together.

        When a hybrid is invoked at the class level, the
        :class:`~.hybrid.Comparator` object given here is wrapped inside of a
        specialized :class:`.QueryableAttribute`, which is the same kind of
        object used by the ORM to represent other mapped attributes.   The
        reason for this is so that other class-level attributes such as
        docstrings and a reference to the hybrid itself may be maintained
        within the structure that's returned, without any modifications to the
        original comparator object passed in.

        .. note::

           When referring to a hybrid property  from an owning class (e.g.
           ``SomeClass.some_hybrid``), an instance of
           :class:`.QueryableAttribute` is returned, representing the
           expression or comparator object as this  hybrid object.  However,
           that object itself has accessors called ``expression`` and
           ``comparator``; so when attempting to override these decorators on a
           subclass, it may be necessary to qualify it using the
           :attr:`.hybrid_property.overrides` modifier first.  See that
           modifier for details.

        """
    def update_expression(self, meth: _HybridUpdaterType[_T]) -> hybrid_property[_T]:
        '''Provide a modifying decorator that defines an UPDATE tuple
        producing method.

        The method accepts a single value, which is the value to be
        rendered into the SET clause of an UPDATE statement.  The method
        should then process this value into individual column expressions
        that fit into the ultimate SET clause, and return them as a
        sequence of 2-tuples.  Each tuple
        contains a column expression as the key and a value to be rendered.

        E.g.::

            class Person(Base):
                # ...

                first_name = Column(String)
                last_name = Column(String)

                @hybrid_property
                def fullname(self):
                    return first_name + " " + last_name

                @fullname.update_expression
                def fullname(cls, value):
                    fname, lname = value.split(" ", 1)
                    return [
                        (cls.first_name, fname),
                        (cls.last_name, lname)
                    ]

        .. versionadded:: 1.2

        '''

class Comparator(interfaces.PropComparator[_T]):
    """A helper class that allows easy construction of custom
    :class:`~.orm.interfaces.PropComparator`
    classes for usage with hybrids."""
    expression: Incomplete
    def __init__(self, expression: _HasClauseElement | SQLColumnExpression[_T]) -> None: ...
    def __clause_element__(self) -> roles.ColumnsClauseRole: ...
    def property(self) -> interfaces.MapperProperty[_T]: ...
    def adapt_to_entity(self, adapt_to_entity: AliasedInsp[Any]) -> Comparator[_T]: ...

class ExprComparator(Comparator[_T]):
    cls: Incomplete
    expression: Incomplete
    hybrid: Incomplete
    def __init__(self, cls: Type[Any], expression: _HasClauseElement | SQLColumnExpression[_T], hybrid: hybrid_property[_T]) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def info(self) -> _InfoType: ...
    def property(self) -> MapperProperty[_T]: ...
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[Any]: ...
