from _typeshed import Incomplete
from matplotlib.backends.qt_compat import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets

__version__: str
BLACKLIST: Incomplete

class ColorButton(QtWidgets.QPushButton):
    """
    Color choosing push button
    """
    colorChanged: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def choose_color(self) -> None: ...
    def get_color(self): ...
    def set_color(self, color) -> None: ...
    color: Incomplete

def to_qcolor(color):
    """Create a QColor from a matplotlib color"""

class ColorLayout(QtWidgets.QHBoxLayout):
    """Color-specialized QLineEdit layout"""
    lineedit: Incomplete
    colorbtn: Incomplete
    def __init__(self, color, parent: Incomplete | None = None) -> None: ...
    def update_color(self) -> None: ...
    def update_text(self, color) -> None: ...
    def text(self): ...

def font_is_installed(font):
    """Check if font is installed"""
def tuple_to_qfont(tup):
    """
    Create a QFont from tuple:
        (family [string], size [int], italic [bool], bold [bool])
    """
def qfont_to_tuple(font): ...

class FontLayout(QtWidgets.QGridLayout):
    """Font selection"""
    family: Incomplete
    size: Incomplete
    italic: Incomplete
    bold: Incomplete
    def __init__(self, value, parent: Incomplete | None = None) -> None: ...
    def get_font(self): ...

def is_edit_valid(edit): ...

class FormWidget(QtWidgets.QWidget):
    update_buttons: Incomplete
    data: Incomplete
    widgets: Incomplete
    formlayout: Incomplete
    def __init__(self, data, comment: str = '', with_margin: bool = False, parent: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        data : list of (label, value) pairs
            The data to be edited in the form.
        comment : str, optional
        with_margin : bool, default: False
            If False, the form elements reach to the border of the widget.
            This is the desired behavior if the FormWidget is used as a widget
            alongside with other widgets such as a QComboBox, which also do
            not have a margin around them.
            However, a margin can be desired if the FormWidget is the only
            widget within a container, e.g. a tab in a QTabWidget.
        parent : QWidget or None
            The parent widget.
        """
    def get_dialog(self):
        """Return FormDialog instance"""
    def setup(self): ...
    def get(self): ...

class FormComboWidget(QtWidgets.QWidget):
    update_buttons: Incomplete
    combobox: Incomplete
    stackwidget: Incomplete
    widgetlist: Incomplete
    def __init__(self, datalist, comment: str = '', parent: Incomplete | None = None) -> None: ...
    def setup(self) -> None: ...
    def get(self): ...

class FormTabWidget(QtWidgets.QWidget):
    update_buttons: Incomplete
    tabwidget: Incomplete
    widgetlist: Incomplete
    def __init__(self, datalist, comment: str = '', parent: Incomplete | None = None) -> None: ...
    def setup(self) -> None: ...
    def get(self): ...

class FormDialog(QtWidgets.QDialog):
    """Form Dialog"""
    apply_callback: Incomplete
    formwidget: Incomplete
    float_fields: Incomplete
    bbox: Incomplete
    def __init__(self, data, title: str = '', comment: str = '', icon: Incomplete | None = None, parent: Incomplete | None = None, apply: Incomplete | None = None) -> None: ...
    def register_float_field(self, field) -> None: ...
    def update_buttons(self) -> None: ...
    data: Incomplete
    def accept(self) -> None: ...
    def reject(self) -> None: ...
    def apply(self) -> None: ...
    def get(self):
        """Return form result"""

def fedit(data, title: str = '', comment: str = '', icon: Incomplete | None = None, parent: Incomplete | None = None, apply: Incomplete | None = None) -> None:
    """
    Create form dialog

    data: datalist, datagroup
    title: str
    comment: str
    icon: QIcon instance
    parent: parent QWidget
    apply: apply callback (function)

    datalist: list/tuple of (field_name, field_value)
    datagroup: list/tuple of (datalist *or* datagroup, title, comment)

    -> one field for each member of a datalist
    -> one tab for each member of a top-level datagroup
    -> one page (of a multipage widget, each page can be selected with a combo
       box) for each member of a datagroup inside a datagroup

    Supported types for field_value:
      - int, float, str, bool
      - colors: in Qt-compatible text form, i.e. in hex format or name
                (red, ...) (automatically detected from a string)
      - list/tuple:
          * the first element will be the selected index (or value)
          * the other elements can be couples (key, value) or only values
    """
