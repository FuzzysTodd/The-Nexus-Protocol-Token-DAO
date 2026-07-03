from tensorflow.python.util import tf_inspect as tf_inspect

class PublicAPIVisitor:
    """Visitor to use with `traverse` to visit exactly the public TF API."""
    def __init__(self, visitor) -> None:
        """Constructor.

    `visitor` should be a callable suitable as a visitor for `traverse`. It will
    be called only for members of the public TensorFlow API.

    Args:
      visitor: A visitor to call for the public API.
    """
    @property
    def private_map(self):
        """A map from parents to symbols that should not be included at all.

    This map can be edited, but it should not be edited once traversal has
    begun.

    Returns:
      The map marking symbols to not include.
    """
    @property
    def do_not_descend_map(self):
        """A map from parents to symbols that should not be descended into.

    This map can be edited, but it should not be edited once traversal has
    begun.

    Returns:
      The map marking symbols to not explore.
    """
    def set_root_name(self, root_name) -> None:
        """Override the default root name of 'tf'."""
    def __call__(self, path, parent, children) -> None:
        """Visitor interface, see `traverse` for details."""
