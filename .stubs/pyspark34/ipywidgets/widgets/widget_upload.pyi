from .trait_types import InstanceDict as InstanceDict, TypedTuple as TypedTuple
from .valuewidget import ValueWidget as ValueWidget
from .widget import register as register, widget_serialization as widget_serialization
from .widget_button import ButtonStyle as ButtonStyle
from .widget_core import CoreWidget as CoreWidget
from .widget_description import DescriptionWidget as DescriptionWidget
from _typeshed import Incomplete
from traitlets import Bytes as Bytes, Int as Int, observe as observe

class FileUpload(DescriptionWidget, ValueWidget, CoreWidget):
    """File upload widget

    This creates a file upload input that allows the user to select
    one or more files to upload. The file metadata and content
    can be retrieved in the kernel.

    Examples
    --------

    >>> import ipywidgets as widgets
    >>> uploader = widgets.FileUpload()

    # After displaying `uploader` and uploading a file:

    >>> uploader.value
    [
      {
        'name': 'example.txt',
        'type': 'text/plain',
        'size': 36,
        'last_modified': datetime.datetime(2020, 1, 9, 15, 58, 43, 321000, tzinfo=datetime.timezone.utc),
        'content': <memory at 0x10c1b37c8>
      }
    ]
    >>> uploader.value[0].content.tobytes()
    b'This is the content of example.txt.
'

    Parameters
    ----------

    accept: str, optional
        Which file types to accept, e.g. '.doc,.docx'. For a full
        description of how to specify this, see
        https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file#attr-accept
        Defaults to accepting all file types.

    multiple: bool, optional
        Whether to accept multiple files at the same time. Defaults to False.

    disabled: bool, optional
        Whether user interaction is enabled.

    icon: str, optional
        The icon to use for the button displayed on the screen.
        Can be any Font-awesome icon without the fa- prefix.
        Defaults to 'upload'. If missing, no icon is shown.

    description: str, optional
        The text to show on the label. Defaults to 'Upload'.

    button_style: str, optional
        One of 'primary', 'success', 'info', 'warning', 'danger' or ''.

    style: widgets.widget_button.ButtonStyle, optional
        Style configuration for the button.

    value: Tuple[Dict], optional
        The value of the last uploaded file or set of files. See the
        documentation for details of how to use this to retrieve file
        content and metadata:
        https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#File-Upload

    error: str, optional
        Whether the last upload triggered an error.
    """
    accept: Incomplete
    multiple: Incomplete
    disabled: Incomplete
    icon: Incomplete
    button_style: Incomplete
    style: Incomplete
    error: Incomplete
    value: Incomplete
