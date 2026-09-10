__all__ = ['CopyBase']

class CopyBase:
    """Create new instance copies with cooperative ``super()`` calls."""
    def copy(self):
        """Return a copied instance of the object.

        Returns:
            An independent copy of the current object.
        """
