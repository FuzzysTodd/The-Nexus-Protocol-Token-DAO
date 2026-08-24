from _typeshed import Incomplete

def include_frame(fname): ...
def filter_traceback(fn):
    """Filter out Keras-internal stack trace frames in exceptions raised by
    fn."""
def inject_argument_info_in_traceback(fn, object_name: Incomplete | None = None):
    '''Add information about call argument values to an error message.

    Arguments:
      fn: Function to wrap. Exceptions raised by the this function will be
        re-raised with additional information added to the error message,
        displaying the values of the different arguments that the function
        was called with.
      object_name: String, display name of the class/function being called,
        e.g. `\'layer "layer_name" (LayerClass)\'`.

    Returns:
      A wrapped version of `fn`.
    '''
def format_argument_value(value): ...
