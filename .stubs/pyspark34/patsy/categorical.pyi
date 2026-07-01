from _typeshed import Incomplete

__all__ = ['C', 'guess_categorical', 'CategoricalSniffer', 'categorical_to_int']

class _CategoricalBox:
    data: Incomplete
    contrast: Incomplete
    levels: Incomplete
    def __init__(self, data, contrast, levels) -> None: ...

def C(data, contrast: Incomplete | None = None, levels: Incomplete | None = None):
    '''
    Marks some `data` as being categorical, and specifies how to interpret
    it.

    This is used for three reasons:

    * To explicitly mark some data as categorical. For instance, integer data
      is by default treated as numerical. If you have data that is stored
      using an integer type, but where you want patsy to treat each different
      value as a different level of a categorical factor, you can wrap it in a
      call to `C` to accomplish this. E.g., compare::

        dmatrix("a", {"a": [1, 2, 3]})
        dmatrix("C(a)", {"a": [1, 2, 3]})

    * To explicitly set the levels or override the default level ordering for
      categorical data, e.g.::

        dmatrix("C(a, levels=["a2", "a1"])", balanced(a=2))
    * To override the default coding scheme for categorical data. The
      `contrast` argument can be any of:

      * A :class:`ContrastMatrix` object
      * A simple 2d ndarray (which is treated the same as a ContrastMatrix
        object except that you can\'t specify column names)
      * An object with methods called `code_with_intercept` and
        `code_without_intercept`, like the built-in contrasts
        (:class:`Treatment`, :class:`Diff`, :class:`Poly`, etc.). See
        :ref:`categorical-coding` for more details.
      * A callable that returns one of the above.
    '''
def guess_categorical(data): ...

class CategoricalSniffer:
    def __init__(self, NA_action, origin: Incomplete | None = None) -> None: ...
    def levels_contrast(self): ...
    def sniff(self, data): ...

def categorical_to_int(data, levels, NA_action, origin: Incomplete | None = None): ...
