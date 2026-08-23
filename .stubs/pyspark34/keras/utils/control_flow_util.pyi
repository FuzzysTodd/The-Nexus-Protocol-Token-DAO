from _typeshed import Incomplete

def InXlaContext(graph): ...
def GraphOrParentsInXlaContext(graph): ...
def IsInWhileLoop(op): ...
def GetContainingWhileContext(ctxt, stop_ctxt: Incomplete | None = None):
    """Returns the first ancestor WhileContext of `ctxt`.

    Returns `ctxt` if `ctxt` is a WhileContext, or None if `ctxt` is not in a
    while loop.

    Args:
      ctxt: ControlFlowContext
      stop_ctxt: ControlFlowContext, optional. If provided, the search will end
        if it sees stop_ctxt.

    Returns:
      `ctxt` if `ctxt` is a WhileContext, the most nested WhileContext
      containing `ctxt`, or None if `ctxt` is not in a while loop.  If
      `stop_ctxt` is not `None`, this returns `ctxt` if it matches `stop_ctxt`
      in its traversal.
    """
def GetContainingXLAContext(ctxt):
    """Returns the first ancestor XLAContext of `ctxt`.

    Returns `ctxt` if `ctxt` is a XLAContext, or None if `ctxt` is not in a
    while loop.

    Args:
      ctxt: ControlFlowContext

    Returns:
      `ctxt` if `ctxt` is a XLAContext, the most nested XLAContext containing
      `ctxt`, or None if `ctxt` is not in a while loop.
    """
def smart_cond(pred, true_fn: Incomplete | None = None, false_fn: Incomplete | None = None, name: Incomplete | None = None):
    """Return either `true_fn()` if predicate `pred` is true else `false_fn()`.

    If `pred` is a bool or has a constant value, we return either `true_fn()`
    or `false_fn()`, otherwise we use `tf.cond` to dynamically route to both.

    Args:
      pred: A scalar determining whether to return the result of `true_fn` or
        `false_fn`.
      true_fn: The callable to be performed if pred is true.
      false_fn: The callable to be performed if pred is false.
      name: Optional name prefix when using `tf.cond`.

    Returns:
      Tensors returned by the call to either `true_fn` or `false_fn`.

    Raises:
      TypeError: If `true_fn` or `false_fn` is not callable.
    """
def constant_value(pred):
    """Return the bool value for `pred`, or None if `pred` had a dynamic value.

    Args:
      pred: A scalar, either a Python bool or a TensorFlow boolean variable
        or tensor, or the Python integer 1 or 0.

    Returns:
      True or False if `pred` has a constant boolean value, None otherwise.

    Raises:
      TypeError: If `pred` is not a Variable, Tensor or bool, or Python
        integer 1 or 0.
    """
