from .. import util as util
from ..orm.query import Query as Query
from ..orm.session import Session as Session
from ..sql import func as func, literal_column as literal_column
from _typeshed import Incomplete

log: Incomplete

class Bakery:
    '''Callable which returns a :class:`.BakedQuery`.

    This object is returned by the class method
    :meth:`.BakedQuery.bakery`.  It exists as an object
    so that the "cache" can be easily inspected.

    .. versionadded:: 1.2


    '''
    cls: Incomplete
    cache: Incomplete
    def __init__(self, cls_, cache) -> None: ...
    def __call__(self, initial_fn, *args): ...

class BakedQuery:
    """A builder object for :class:`.query.Query` objects."""
    steps: Incomplete
    def __init__(self, bakery, initial_fn, args=()) -> None: ...
    @classmethod
    def bakery(cls, size: int = 200, _size_alert: Incomplete | None = None):
        """Construct a new bakery.

        :return: an instance of :class:`.Bakery`

        """
    def __iadd__(self, other): ...
    def __add__(self, other): ...
    def add_criteria(self, fn, *args):
        """Add a criteria function to this :class:`.BakedQuery`.

        This is equivalent to using the ``+=`` operator to
        modify a :class:`.BakedQuery` in-place.

        """
    def with_criteria(self, fn, *args):
        """Add a criteria function to a :class:`.BakedQuery` cloned from this
        one.

        This is equivalent to using the ``+`` operator to
        produce a new :class:`.BakedQuery` with modifications.

        """
    def for_session(self, session):
        """Return a :class:`_baked.Result` object for this
        :class:`.BakedQuery`.

        This is equivalent to calling the :class:`.BakedQuery` as a
        Python callable, e.g. ``result = my_baked_query(session)``.

        """
    def __call__(self, session): ...
    def spoil(self, full: bool = False):
        """Cancel any query caching that will occur on this BakedQuery object.

        The BakedQuery can continue to be used normally, however additional
        creational functions will not be cached; they will be called
        on every invocation.

        This is to support the case where a particular step in constructing
        a baked query disqualifies the query from being cacheable, such
        as a variant that relies upon some uncacheable value.

        :param full: if False, only functions added to this
         :class:`.BakedQuery` object subsequent to the spoil step will be
         non-cached; the state of the :class:`.BakedQuery` up until
         this point will be pulled from the cache.   If True, then the
         entire :class:`_query.Query` object is built from scratch each
         time, with all creational functions being called on each
         invocation.

        """
    def to_query(self, query_or_session):
        """Return the :class:`_query.Query` object for use as a subquery.

        This method should be used within the lambda callable being used
        to generate a step of an enclosing :class:`.BakedQuery`.   The
        parameter should normally be the :class:`_query.Query` object that
        is passed to the lambda::

            sub_bq = self.bakery(lambda s: s.query(User.name))
            sub_bq += lambda q: q.filter(
                User.id == Address.user_id).correlate(Address)

            main_bq = self.bakery(lambda s: s.query(Address))
            main_bq += lambda q: q.filter(
                sub_bq.to_query(q).exists())

        In the case where the subquery is used in the first callable against
        a :class:`.Session`, the :class:`.Session` is also accepted::

            sub_bq = self.bakery(lambda s: s.query(User.name))
            sub_bq += lambda q: q.filter(
                User.id == Address.user_id).correlate(Address)

            main_bq = self.bakery(
                lambda s: s.query(
                Address.id, sub_bq.to_query(q).scalar_subquery())
            )

        :param query_or_session: a :class:`_query.Query` object or a class
         :class:`.Session` object, that is assumed to be within the context
         of an enclosing :class:`.BakedQuery` callable.


         .. versionadded:: 1.3


        """

class Result:
    """Invokes a :class:`.BakedQuery` against a :class:`.Session`.

    The :class:`_baked.Result` object is where the actual :class:`.query.Query`
    object gets created, or retrieved from the cache,
    against a target :class:`.Session`, and is then invoked for results.

    """
    bq: Incomplete
    session: Incomplete
    def __init__(self, bq, session) -> None: ...
    def params(self, *args, **kw):
        """Specify parameters to be replaced into the string SQL statement."""
    def with_post_criteria(self, fn):
        """Add a criteria function that will be applied post-cache.

        This adds a function that will be run against the
        :class:`_query.Query` object after it is retrieved from the
        cache.    This currently includes **only** the
        :meth:`_query.Query.params` and :meth:`_query.Query.execution_options`
        methods.

        .. warning::  :meth:`_baked.Result.with_post_criteria`
           functions are applied
           to the :class:`_query.Query`
           object **after** the query's SQL statement
           object has been retrieved from the cache.   Only
           :meth:`_query.Query.params` and
           :meth:`_query.Query.execution_options`
           methods should be used.


        .. versionadded:: 1.2


        """
    def __iter__(self): ...
    def count(self):
        """return the 'count'.

        Equivalent to :meth:`_query.Query.count`.

        Note this uses a subquery to ensure an accurate count regardless
        of the structure of the original statement.

        """
    def scalar(self):
        """Return the first element of the first result or None
        if no rows present.  If multiple rows are returned,
        raises MultipleResultsFound.

        Equivalent to :meth:`_query.Query.scalar`.

        """
    def first(self):
        """Return the first row.

        Equivalent to :meth:`_query.Query.first`.

        """
    def one(self):
        """Return exactly one result or raise an exception.

        Equivalent to :meth:`_query.Query.one`.

        """
    def one_or_none(self):
        """Return one or zero results, or raise an exception for multiple
        rows.

        Equivalent to :meth:`_query.Query.one_or_none`.

        """
    def all(self):
        """Return all rows.

        Equivalent to :meth:`_query.Query.all`.

        """
    def get(self, ident):
        """Retrieve an object based on identity.

        Equivalent to :meth:`_query.Query.get`.

        """

bakery: Incomplete
