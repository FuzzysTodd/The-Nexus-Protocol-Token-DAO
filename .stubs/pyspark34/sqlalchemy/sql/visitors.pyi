from .. import util
from ..util.typing import Literal, Protocol
from ._py_util import cache_anon_map as anon_map
from enum import Enum
from typing import Any, Callable, Dict, Iterable, Iterator, List, Mapping, Tuple, Type, overload

__all__ = ['iterate', 'traverse_using', 'traverse', 'cloned_traverse', 'replacement_traverse', 'Visitable', 'ExternalTraversal', 'InternalTraversal', 'anon_map']

class _CompilerDispatchType(Protocol):
    def __call__(_self, self: Visitable, visitor: Any, **kw: Any) -> Any: ...

class Visitable:
    """Base class for visitable objects.

    :class:`.Visitable` is used to implement the SQL compiler dispatch
    functions.    Other forms of traversal such as for cache key generation
    are implemented separately using the :class:`.HasTraverseInternals`
    interface.

    .. versionchanged:: 2.0  The :class:`.Visitable` class was named
       :class:`.Traversible` in the 1.4 series; the name is changed back
       to :class:`.Visitable` in 2.0 which is what it was prior to 1.4.

       Both names remain importable in both 1.4 and 2.0 versions.

    """
    __visit_name__: str
    def __init_subclass__(cls) -> None: ...
    def __class_getitem__(cls, key: Any) -> Any: ...

class InternalTraversal(Enum):
    '''Defines visitor symbols used for internal traversal.

    The :class:`.InternalTraversal` class is used in two ways.  One is that
    it can serve as the superclass for an object that implements the
    various visit methods of the class.   The other is that the symbols
    themselves of :class:`.InternalTraversal` are used within
    the ``_traverse_internals`` collection.   Such as, the :class:`.Case`
    object defines ``_traverse_internals`` as ::

        class Case(ColumnElement[_T]):
            _traverse_internals = [
                ("value", InternalTraversal.dp_clauseelement),
                ("whens", InternalTraversal.dp_clauseelement_tuples),
                ("else_", InternalTraversal.dp_clauseelement),
            ]

    Above, the :class:`.Case` class indicates its internal state as the
    attributes named ``value``, ``whens``, and ``else_``.    They each
    link to an :class:`.InternalTraversal` method which indicates the type
    of datastructure to which each attribute refers.

    Using the ``_traverse_internals`` structure, objects of type
    :class:`.InternalTraversible` will have the following methods automatically
    implemented:

    * :meth:`.HasTraverseInternals.get_children`

    * :meth:`.HasTraverseInternals._copy_internals`

    * :meth:`.HasCacheKey._gen_cache_key`

    Subclasses can also implement these methods directly, particularly for the
    :meth:`.HasTraverseInternals._copy_internals` method, when special steps
    are needed.

    .. versionadded:: 1.4

    '''
    dp_has_cache_key: str
    dp_has_cache_key_list: str
    dp_clauseelement: str
    dp_fromclause_canonical_column_collection: str
    dp_clauseelement_tuples: str
    dp_clauseelement_list: str
    dp_clauseelement_tuple: str
    dp_executable_options: str
    dp_with_context_options: str
    dp_fromclause_ordered_set: str
    dp_string: str
    dp_string_list: str
    dp_anon_name: str
    dp_boolean: str
    dp_operator: str
    dp_type: str
    dp_plain_dict: str
    dp_dialect_options: str
    dp_string_clauseelement_dict: str
    dp_string_multi_dict: str
    dp_annotations_key: str
    dp_plain_obj: str
    dp_named_ddl_element: str
    dp_prefix_sequence: str
    dp_table_hint_list: str
    dp_setup_join_tuple: str
    dp_memoized_select_entities: str
    dp_statement_hint_list: str
    dp_unknown_structure: str
    dp_dml_ordered_values: str
    dp_dml_values: str
    dp_dml_multi_values: str
    dp_propagate_attrs: str
    dp_ignore: str
    dp_inspectable: str
    dp_multi: str
    dp_multi_list: str
    dp_has_cache_key_tuples: str
    dp_inspectable_list: str

class HasTraverseInternals:
    '''base for classes that have a "traverse internals" element,
    which defines all kinds of ways of traversing the elements of an object.

    Compared to :class:`.Visitable`, which relies upon an external visitor to
    define how the object is travered (i.e. the :class:`.SQLCompiler`), the
    :class:`.HasTraverseInternals` interface allows classes to define their own
    traversal, that is, what attributes are accessed and in what order.

    '''
    def get_children(self, *, omit_attrs: Tuple[str, ...] = (), **kw: Any) -> Iterable[HasTraverseInternals]:
        """Return immediate child :class:`.visitors.HasTraverseInternals`
        elements of this :class:`.visitors.HasTraverseInternals`.

        This is used for visit traversal.

        \\**kw may contain flags that change the collection that is
        returned, for example to return a subset of items in order to
        cut down on larger traversals, or to return child items from a
        different context (such as schema-level collections instead of
        clause-level).

        """

class _InternalTraversalDispatchType(Protocol):
    def __call__(s, self: object, visitor: HasTraversalDispatch) -> Any: ...

class HasTraversalDispatch:
    """Define infrastructure for classes that perform internal traversals

    .. versionadded:: 2.0

    """
    def dispatch(self, visit_symbol: InternalTraversal) -> Callable[..., Any]:
        """Given a method from :class:`.HasTraversalDispatch`, return the
        corresponding method on a subclass.

        """
    def run_generated_dispatch(self, target: object, internal_dispatch: _TraverseInternalsType, generate_dispatcher_name: str) -> Any: ...
    def generate_dispatch(self, target_cls: Type[object], internal_dispatch: _TraverseInternalsType, generate_dispatcher_name: str) -> _InternalTraversalDispatchType: ...
ExtendedInternalTraversal = InternalTraversal

class ExternallyTraversible(HasTraverseInternals, Visitable):
    def get_children(self, *, omit_attrs: Tuple[str, ...] = (), **kw: Any) -> Iterable[ExternallyTraversible]: ...

class _CloneCallableType(Protocol):
    def __call__(self, element: _ET, **kw: Any) -> _ET: ...

class _TraverseTransformCallableType(Protocol[_ET]):
    def __call__(self, element: _ET, **kw: Any) -> _ET | None: ...

class ExternalTraversal(util.MemoizedSlots):
    """Base class for visitor objects which can traverse externally using
    the :func:`.visitors.traverse` function.

    Direct usage of the :func:`.visitors.traverse` function is usually
    preferred.

    """
    __traverse_options__: Dict[str, Any]
    def traverse_single(self, obj: Visitable, **kw: Any) -> Any: ...
    def iterate(self, obj: ExternallyTraversible | None) -> Iterator[ExternallyTraversible]:
        """Traverse the given expression structure, returning an iterator
        of all elements.

        """
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: ExternallyTraversible) -> ExternallyTraversible: ...
    @property
    def visitor_iterator(self) -> Iterator[ExternalTraversal]:
        """Iterate through this visitor and each 'chained' visitor."""
    def chain(self, visitor: ExternalTraversal) -> _ExtT:
        """'Chain' an additional ExternalTraversal onto this ExternalTraversal

        The chained visitor will receive all visit events after this one.

        """

class CloningExternalTraversal(ExternalTraversal):
    """Base class for visitor objects which can traverse using
    the :func:`.visitors.cloned_traverse` function.

    Direct usage of the :func:`.visitors.cloned_traverse` function is usually
    preferred.


    """
    def copy_and_process(self, list_: List[ExternallyTraversible]) -> List[ExternallyTraversible]:
        """Apply cloned traversal to the given list of elements, and return
        the new list.

        """
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: ExternallyTraversible) -> ExternallyTraversible: ...

class ReplacingExternalTraversal(CloningExternalTraversal):
    """Base class for visitor objects which can traverse using
    the :func:`.visitors.replacement_traverse` function.

    Direct usage of the :func:`.visitors.replacement_traverse` function is
    usually preferred.

    """
    def replace(self, elem: ExternallyTraversible) -> ExternallyTraversible | None:
        """Receive pre-copied elements during a cloning traversal.

        If the method returns a new element, the element is used
        instead of creating a simple copy of the element.  Traversal
        will halt on the newly returned element if it is re-encountered.
        """
    @overload
    def traverse(self, obj: Literal[None]) -> None: ...
    @overload
    def traverse(self, obj: ExternallyTraversible) -> ExternallyTraversible: ...
Traversible = Visitable
ClauseVisitor = ExternalTraversal
CloningVisitor = CloningExternalTraversal
ReplacingCloningVisitor = ReplacingExternalTraversal

def iterate(obj: ExternallyTraversible | None, opts: Mapping[str, Any] = ...) -> Iterator[ExternallyTraversible]:
    '''Traverse the given expression structure, returning an iterator.

    Traversal is configured to be breadth-first.

    The central API feature used by the :func:`.visitors.iterate`
    function is the
    :meth:`_expression.ClauseElement.get_children` method of
    :class:`_expression.ClauseElement` objects.  This method should return all
    the :class:`_expression.ClauseElement` objects which are associated with a
    particular :class:`_expression.ClauseElement` object. For example, a
    :class:`.Case` structure will refer to a series of
    :class:`_expression.ColumnElement` objects within its "whens" and "else\\_"
    member variables.

    :param obj: :class:`_expression.ClauseElement` structure to be traversed

    :param opts: dictionary of iteration options.   This dictionary is usually
     empty in modern usage.

    '''
@overload
def traverse_using(iterator: Iterable[ExternallyTraversible], obj: Literal[None], visitors: Mapping[str, _TraverseCallableType[Any]]) -> None: ...
@overload
def traverse_using(iterator: Iterable[ExternallyTraversible], obj: ExternallyTraversible, visitors: Mapping[str, _TraverseCallableType[Any]]) -> ExternallyTraversible: ...
@overload
def traverse(obj: Literal[None], opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> None: ...
@overload
def traverse(obj: ExternallyTraversible, opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> ExternallyTraversible: ...
@overload
def cloned_traverse(obj: Literal[None], opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> None: ...
@overload
def cloned_traverse(obj: _ET, opts: Mapping[str, Any], visitors: Mapping[str, _TraverseCallableType[Any]]) -> _ET: ...
@overload
def replacement_traverse(obj: Literal[None], opts: Mapping[str, Any], replace: _TraverseTransformCallableType[Any]) -> None: ...
@overload
def replacement_traverse(obj: _CE, opts: Mapping[str, Any], replace: _TraverseTransformCallableType[Any]) -> _CE: ...
@overload
def replacement_traverse(obj: ExternallyTraversible, opts: Mapping[str, Any], replace: _TraverseTransformCallableType[Any]) -> ExternallyTraversible: ...
