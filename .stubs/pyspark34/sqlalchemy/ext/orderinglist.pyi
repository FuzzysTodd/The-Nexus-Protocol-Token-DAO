from typing import Callable, List

__all__ = ['ordering_list']

def ordering_list(attr: str, count_from: int | None = None, ordering_func: OrderingFunc | None = None, reorder_on_append: bool = False) -> Callable[[], OrderingList]:
    '''Prepares an :class:`OrderingList` factory for use in mapper definitions.

    Returns an object suitable for use as an argument to a Mapper
    relationship\'s ``collection_class`` option.  e.g.::

        from sqlalchemy.ext.orderinglist import ordering_list

        class Slide(Base):
            __tablename__ = \'slide\'

            id = Column(Integer, primary_key=True)
            name = Column(String)

            bullets = relationship("Bullet", order_by="Bullet.position",
                                    collection_class=ordering_list(\'position\'))

    :param attr:
      Name of the mapped attribute to use for storage and retrieval of
      ordering information

    :param count_from:
      Set up an integer-based ordering, starting at ``count_from``.  For
      example, ``ordering_list(\'pos\', count_from=1)`` would create a 1-based
      list in SQL, storing the value in the \'pos\' column.  Ignored if
      ``ordering_func`` is supplied.

    Additional arguments are passed to the :class:`.OrderingList` constructor.

    '''

class OrderingList(List[_T]):
    """A custom list that manages position information for its children.

    The :class:`.OrderingList` object is normally set up using the
    :func:`.ordering_list` factory function, used in conjunction with
    the :func:`_orm.relationship` function.

    """
    ordering_attr: str
    ordering_func: OrderingFunc
    reorder_on_append: bool
    def __init__(self, ordering_attr: str | None = None, ordering_func: OrderingFunc | None = None, reorder_on_append: bool = False) -> None:
        '''A custom list that manages position information for its children.

        ``OrderingList`` is a ``collection_class`` list implementation that
        syncs position in a Python list with a position attribute on the
        mapped objects.

        This implementation relies on the list starting in the proper order,
        so be **sure** to put an ``order_by`` on your relationship.

        :param ordering_attr:
          Name of the attribute that stores the object\'s order in the
          relationship.

        :param ordering_func: Optional.  A function that maps the position in
          the Python list to a value to store in the
          ``ordering_attr``.  Values returned are usually (but need not be!)
          integers.

          An ``ordering_func`` is called with two positional parameters: the
          index of the element in the list, and the list itself.

          If omitted, Python list indexes are used for the attribute values.
          Two basic pre-built numbering functions are provided in this module:
          ``count_from_0`` and ``count_from_1``.  For more exotic examples
          like stepped numbering, alphabetical and Fibonacci numbering, see
          the unit tests.

        :param reorder_on_append:
          Default False.  When appending an object with an existing (non-None)
          ordering value, that value will be left untouched unless
          ``reorder_on_append`` is true.  This is an optimization to avoid a
          variety of dangerous unexpected database writes.

          SQLAlchemy will add instances to the list via append() when your
          object loads.  If for some reason the result set from the database
          skips a step in the ordering (say, row \'1\' is missing but you get
          \'2\', \'3\', and \'4\'), reorder_on_append=True would immediately
          renumber the items to \'1\', \'2\', \'3\'.  If you have multiple sessions
          making changes, any of whom happen to load this collection even in
          passing, all of the sessions would try to "clean up" the numbering
          in their commits, possibly causing all but one to fail with a
          concurrent modification error.

          Recommend leaving this with the default of False, and just call
          ``reorder()`` if you\'re doing ``append()`` operations with
          previously ordered instances or when doing some housekeeping after
          manual sql operations.

        '''
    def reorder(self) -> None:
        """Synchronize ordering for the entire collection.

        Sweeps through the list and ensures that each object has accurate
        ordering information set.

        """
    def append(self, entity) -> None: ...
    def insert(self, index, entity) -> None: ...
    def remove(self, entity) -> None: ...
    def pop(self, index: int = -1): ...
    def __setitem__(self, index, entity) -> None: ...
    def __delitem__(self, index) -> None: ...
    def __setslice__(self, start, end, values) -> None: ...
    def __delslice__(self, start, end) -> None: ...
    def __reduce__(self): ...
