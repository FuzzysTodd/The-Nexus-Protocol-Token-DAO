from _typeshed import Incomplete

VERSION: str
PYTHON_NAMES: Incomplete
CACHE: Incomplete

def ascii_lower(string):
    """Transform (only) ASCII letters to lower case: A-Z is mapped to a-z.

    :param string: An Unicode string.
    :returns: A new Unicode string.

    This is used for `ASCII case-insensitive
    <http://encoding.spec.whatwg.org/#ascii-case-insensitive>`_
    matching of encoding labels.
    The same matching is also used, among other things,
    for `CSS keywords <http://dev.w3.org/csswg/css-values/#keywords>`_.

    This is different from the :meth:`~py:str.lower` method of Unicode strings
    which also affect non-ASCII characters,
    sometimes mapping them into the ASCII range:

        >>> keyword = u'Bac\\N{KELVIN SIGN}ground'
        >>> assert keyword.lower() == u'background'
        >>> assert ascii_lower(keyword) != keyword.lower()
        >>> assert ascii_lower(keyword) == u'bac\\N{KELVIN SIGN}ground'

    """
def lookup(label):
    """
    Look for an encoding by its label.
    This is the spec’s `get an encoding
    <http://encoding.spec.whatwg.org/#concept-encoding-get>`_ algorithm.
    Supported labels are listed there.

    :param label: A string.
    :returns:
        An :class:`Encoding` object, or :obj:`None` for an unknown label.

    """

class Encoding:
    """Reresents a character encoding such as UTF-8,
    that can be used for decoding or encoding.

    .. attribute:: name

        Canonical name of the encoding

    .. attribute:: codec_info

        The actual implementation of the encoding,
        a stdlib :class:`~codecs.CodecInfo` object.
        See :func:`codecs.register`.

    """
    name: Incomplete
    codec_info: Incomplete
    def __init__(self, name, codec_info) -> None: ...

UTF8: Incomplete

def decode(input, fallback_encoding, errors: str = 'replace'):
    """
    Decode a single string.

    :param input: A byte string
    :param fallback_encoding:
        An :class:`Encoding` object or a label string.
        The encoding to use if :obj:`input` does note have a BOM.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.
    :return:
        A ``(output, encoding)`` tuple of an Unicode string
        and an :obj:`Encoding`.

    """
def encode(input, encoding=..., errors: str = 'strict'):
    """
    Encode a single string.

    :param input: An Unicode string.
    :param encoding: An :class:`Encoding` object or a label string.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.
    :return: A byte string.

    """
def iter_decode(input, fallback_encoding, errors: str = 'replace'):
    '''
    "Pull"-based decoder.

    :param input:
        An iterable of byte strings.

        The input is first consumed just enough to determine the encoding
        based on the precense of a BOM,
        then consumed on demand when the return value is.
    :param fallback_encoding:
        An :class:`Encoding` object or a label string.
        The encoding to use if :obj:`input` does note have a BOM.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.
    :returns:
        An ``(output, encoding)`` tuple.
        :obj:`output` is an iterable of Unicode strings,
        :obj:`encoding` is the :obj:`Encoding` that is being used.

    '''
def iter_encode(input, encoding=..., errors: str = 'strict'):
    """
    “Pull”-based encoder.

    :param input: An iterable of Unicode strings.
    :param encoding: An :class:`Encoding` object or a label string.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.
    :returns: An iterable of byte strings.

    """

class IncrementalDecoder:
    """
    “Push”-based decoder.

    :param fallback_encoding:
        An :class:`Encoding` object or a label string.
        The encoding to use if :obj:`input` does note have a BOM.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.

    """
    encoding: Incomplete
    def __init__(self, fallback_encoding, errors: str = 'replace') -> None: ...
    def decode(self, input, final: bool = False):
        """Decode one chunk of the input.

        :param input: A byte string.
        :param final:
            Indicate that no more input is available.
            Must be :obj:`True` if this is the last call.
        :returns: An Unicode string.

        """

class IncrementalEncoder:
    """
    “Push”-based encoder.

    :param encoding: An :class:`Encoding` object or a label string.
    :param errors: Type of error handling. See :func:`codecs.register`.
    :raises: :exc:`~exceptions.LookupError` for an unknown encoding label.

    .. method:: encode(input, final=False)

        :param input: An Unicode string.
        :param final:
            Indicate that no more input is available.
            Must be :obj:`True` if this is the last call.
        :returns: A byte string.

    """
    encode: Incomplete
    def __init__(self, encoding=..., errors: str = 'strict') -> None: ...
