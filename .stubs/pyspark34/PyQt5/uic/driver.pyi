from . import compileUi as compileUi, loadUi as loadUi

class Driver:
    """ This encapsulates access to the pyuic functionality so that it can be
    called by code that is Python v2/v3 specific.
    """
    LOGGER_NAME: str
    def __init__(self, opts, ui_file) -> None:
        """ Initialise the object.  opts is the parsed options.  ui_file is the
        name of the .ui file.
        """
    def invoke(self):
        """ Invoke the action as specified by the parsed options.  Returns 0 if
        there was no error.
        """
    def on_IOError(self, e) -> None:
        """ Handle an IOError exception. """
    def on_SyntaxError(self, e) -> None:
        """ Handle a SyntaxError exception. """
    def on_NoSuchClassError(self, e) -> None:
        """ Handle a NoSuchClassError exception. """
    def on_NoSuchWidgetError(self, e) -> None:
        """ Handle a NoSuchWidgetError exception. """
    def on_Exception(self, e) -> None:
        """ Handle a generic exception. """
