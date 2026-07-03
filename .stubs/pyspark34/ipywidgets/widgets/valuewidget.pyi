from .widget import Widget as Widget
from _typeshed import Incomplete

class ValueWidget(Widget):
    """Widget that can be used for the input of an interactive function"""
    value: Incomplete
    def get_interact_value(self):
        """Return the value for this widget which should be passed to
        interactive functions. Custom widgets can change this method
        to process the raw value ``self.value``.
        """
