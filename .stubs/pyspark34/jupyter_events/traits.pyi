import typing as t
from traitlets import TraitType

baseclass = TraitType

class Handlers(baseclass):
    """A trait that takes a list of logging handlers and converts
    it to a callable that returns that list (thus, making this
    trait pickleable).
    """
    info_text: str
    def validate_elements(self, obj: t.Any, value: t.Any) -> None:
        """Validate the elements of an object."""
    def element_error(self, obj: t.Any) -> None:
        """Raise an error for bad elements."""
    def validate(self, obj: t.Any, value: t.Any) -> t.Any:
        """Validate an object."""
