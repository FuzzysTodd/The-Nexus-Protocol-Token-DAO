from .widget import Widget as Widget, register as register, widget_serialization as widget_serialization
from .widget_core import CoreWidget as CoreWidget
from _typeshed import Incomplete
from traitlets import TraitError as TraitError, Tuple

class WidgetTraitTuple(Tuple):
    """Traitlet for validating a single (Widget, 'trait_name') pair"""
    info_text: str
    default_args: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def validate_elements(self, obj, value): ...

class Link(CoreWidget):
    """Link Widget

    source: a (Widget, 'trait_name') tuple for the source trait
    target: a (Widget, 'trait_name') tuple that should be updated
    """
    target: Incomplete
    source: Incomplete
    def __init__(self, source, target, **kwargs) -> None: ...
    def unlink(self) -> None: ...

def jslink(attr1, attr2):
    """Link two widget attributes on the frontend so they remain in sync.

    The link is created in the front-end and does not rely on a roundtrip
    to the backend.

    Parameters
    ----------
    source : a (Widget, 'trait_name') tuple for the first trait
    target : a (Widget, 'trait_name') tuple for the second trait

    Examples
    --------

    >>> c = link((widget1, 'value'), (widget2, 'value'))
    """

class DirectionalLink(Link):
    """A directional link

    source: a (Widget, 'trait_name') tuple for the source trait
    target: a (Widget, 'trait_name') tuple that should be updated
    when the source trait changes.
    """

def jsdlink(source, target):
    """Link a source widget attribute with a target widget attribute.

    The link is created in the front-end and does not rely on a roundtrip
    to the backend.

    Parameters
    ----------
    source : a (Widget, 'trait_name') tuple for the source trait
    target : a (Widget, 'trait_name') tuple for the target trait

    Examples
    --------

    >>> c = dlink((src_widget, 'value'), (tgt_widget, 'value'))
    """
