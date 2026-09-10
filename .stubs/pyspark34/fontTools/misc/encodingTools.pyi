from _typeshed import Incomplete

def getEncoding(platformID, platEncID, langID, default: Incomplete | None = None):
    """Returns the Python encoding name for OpenType platformID/encodingID/langID
    triplet.  If encoding for these values is not known, by default None is
    returned.  That can be overriden by passing a value to the default argument.
    """
