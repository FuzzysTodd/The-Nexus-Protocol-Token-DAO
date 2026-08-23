from tensorflow.python.trackable import base as base, converter as converter
from tensorflow.python.util import object_identity as object_identity
from tensorflow.python.util.tf_export import tf_export as tf_export

class TrackableView:
    '''Gathers and serializes a trackable view.

  Example usage:

  >>> class SimpleModule(tf.Module):
  ...   def __init__(self, name=None):
  ...     super().__init__(name=name)
  ...     self.a_var = tf.Variable(5.0)
  ...     self.b_var = tf.Variable(4.0)
  ...     self.vars = [tf.Variable(1.0), tf.Variable(2.0)]

  >>> root = SimpleModule(name="root")
  >>> root.leaf = SimpleModule(name="leaf")
  >>> trackable_view = tf.train.TrackableView(root)

  Pass root to tf.train.TrackableView.children() to get the dictionary of all
  children directly linked to root by name.
  >>> trackable_view_children = trackable_view.children(root)
  >>> for item in trackable_view_children.items():
  ...   print(item)
  (\'a_var\', <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=5.0>)
  (\'b_var\', <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=4.0>)
  (\'vars\', ListWrapper([<tf.Variable \'Variable:0\' shape=() dtype=float32,
  numpy=1.0>, <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=2.0>]))
  (\'leaf\', ...)

  '''
    def __init__(self, root) -> None:
        """Configure the trackable view.

    Args:
      root: A `Trackable` object whose variables (including the variables of
        dependencies, recursively) should be saved. May be a weak reference.
    """
    @classmethod
    def children(cls, obj, save_type=..., **kwargs):
        """Returns all child trackables attached to obj.

    Args:
      obj: A `Trackable` object.
      save_type: A string, can be 'savedmodel' or 'checkpoint'.
      **kwargs: kwargs to use when retrieving the object's children.

    Returns:
      Dictionary of all children attached to the object with name to trackable.
    """
    @property
    def root(self): ...
    def descendants(self):
        """Returns a list of all nodes from self.root using a breadth first traversal."""
