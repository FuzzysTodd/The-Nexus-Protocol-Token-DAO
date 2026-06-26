from ..errors import StreamParseError as StreamParseError
from _typeshed import Incomplete
from collections.abc import Generator

json_decoder: Incomplete

def stream_as_text(stream) -> Generator[Incomplete, None, None]:
    """
    Given a stream of bytes or text, if any of the items in the stream
    are bytes convert them to text.
    This function can be removed once we return text streams
    instead of byte streams.
    """
def json_splitter(buffer):
    """Attempt to parse a json object from a buffer. If there is at least one
    object, return it and the rest of the buffer, otherwise return None.
    """
def json_stream(stream):
    """Given a stream of text, return a stream of json objects.
    This handles streams which are inconsistently buffered (some entries may
    be newline delimited, and others are not).
    """
def line_splitter(buffer, separator: str = '\n'): ...
def split_buffer(stream, splitter: Incomplete | None = None, decoder=...) -> Generator[Incomplete, None, Incomplete]:
    """Given a generator which yields strings and a splitter function,
    joins all input, splits on the separator and yields each chunk.
    Unlike string.split(), each chunk includes the trailing
    separator, except for the last one if none was found on the end
    of the input.
    """
