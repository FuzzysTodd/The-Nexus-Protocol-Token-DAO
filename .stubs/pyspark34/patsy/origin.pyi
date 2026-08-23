from _typeshed import Incomplete

__all__ = ['Origin']

class Origin:
    '''This represents the origin of some object in some string.

    For example, if we have an object ``x1_obj`` that was produced by parsing
    the ``x1`` in the formula ``"y ~ x1:x2"``, then we conventionally keep
    track of that relationship by doing::

      x1_obj.origin = Origin("y ~ x1:x2", 4, 6)

    Then later if we run into a problem, we can do::

      raise PatsyError("invalid factor", x1_obj)

    and we\'ll produce a nice error message like::

      PatsyError: invalid factor
          y ~ x1:x2
              ^^

    Origins are compared by value, and hashable.
    '''
    code: Incomplete
    start: Incomplete
    end: Incomplete
    def __init__(self, code, start, end) -> None: ...
    @classmethod
    def combine(cls, origin_objs):
        '''Class method for combining a set of Origins into one large Origin
        that spans them.

        Example usage: if we wanted to represent the origin of the "x1:x2"
        term, we could do ``Origin.combine([x1_obj, x2_obj])``.

        Single argument is an iterable, and each element in the iterable
        should be either:

        * An Origin object
        * ``None``
        * An object that has a ``.origin`` attribute which fulfills the above
          criteria.
          
        Returns either an Origin object, or None.
        '''
    def relevant_code(self):
        """Extracts and returns the span of the original code represented by
        this Origin. Example: ``x1``."""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def caretize(self, indent: int = 0):
        """Produces a user-readable two line string indicating the origin of
        some code. Example::

          y ~ x1:x2
              ^^

        If optional argument 'indent' is given, then both lines will be
        indented by this much. The returned string does not have a trailing
        newline.
        """
