import typing as t
import typing as te
from .datastructures import FileStorage as FileStorage, Headers as Headers, MultiDict as MultiDict
from .exceptions import RequestEntityTooLarge as RequestEntityTooLarge
from .http import parse_options_header as parse_options_header
from .sansio.multipart import Data as Data, Epilogue as Epilogue, Field as Field, File as File, MultipartDecoder as MultipartDecoder, NeedData as NeedData
from .wsgi import get_content_length as get_content_length, get_input_stream as get_input_stream
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIEnvironment as WSGIEnvironment

t_parse_result: Incomplete

class TStreamFactory(te.Protocol):
    def __call__(self, total_content_length: int | None, content_type: str | None, filename: str | None, content_length: int | None = None) -> t.IO[bytes]: ...
F = t.TypeVar('F', bound=t.Callable[..., t.Any])

def default_stream_factory(total_content_length: int | None, content_type: str | None, filename: str | None, content_length: int | None = None) -> t.IO[bytes]: ...
def parse_form_data(environ: WSGIEnvironment, stream_factory: TStreamFactory | None = None, max_form_memory_size: int | None = None, max_content_length: int | None = None, cls: type[MultiDict] | None = None, silent: bool = True, *, max_form_parts: int | None = None) -> t_parse_result:
    """Parse the form data in the environ and return it as tuple in the form
    ``(stream, form, files)``.  You should only call this method if the
    transport method is `POST`, `PUT`, or `PATCH`.

    If the mimetype of the data transmitted is `multipart/form-data` the
    files multidict will be filled with `FileStorage` objects.  If the
    mimetype is unknown the input stream is wrapped and returned as first
    argument, else the stream is empty.

    This is a shortcut for the common usage of :class:`FormDataParser`.

    :param environ: the WSGI environment to be used for parsing.
    :param stream_factory: An optional callable that returns a new read and
                           writeable file descriptor.  This callable works
                           the same as :meth:`Response._get_file_stream`.
    :param max_form_memory_size: the maximum number of bytes to be accepted for
                           in-memory stored form data.  If the data
                           exceeds the value specified an
                           :exc:`~exceptions.RequestEntityTooLarge`
                           exception is raised.
    :param max_content_length: If this is provided and the transmitted data
                               is longer than this value an
                               :exc:`~exceptions.RequestEntityTooLarge`
                               exception is raised.
    :param cls: an optional dict class to use.  If this is not specified
                       or `None` the default :class:`MultiDict` is used.
    :param silent: If set to False parsing errors will not be caught.
    :param max_form_parts: The maximum number of multipart parts to be parsed. If this
        is exceeded, a :exc:`~exceptions.RequestEntityTooLarge` exception is raised.
    :return: A tuple in the form ``(stream, form, files)``.

    .. versionchanged:: 3.0
        The ``charset`` and ``errors`` parameters were removed.

    .. versionchanged:: 2.3
        Added the ``max_form_parts`` parameter.

    .. versionadded:: 0.5.1
       Added the ``silent`` parameter.

    .. versionadded:: 0.5
       Added the ``max_form_memory_size``, ``max_content_length``, and ``cls``
       parameters.
    """

class FormDataParser:
    """This class implements parsing of form data for Werkzeug.  By itself
    it can parse multipart and url encoded form data.  It can be subclassed
    and extended but for most mimetypes it is a better idea to use the
    untouched stream and expose it as separate attributes on a request
    object.

    :param stream_factory: An optional callable that returns a new read and
                           writeable file descriptor.  This callable works
                           the same as :meth:`Response._get_file_stream`.
    :param max_form_memory_size: the maximum number of bytes to be accepted for
                           in-memory stored form data.  If the data
                           exceeds the value specified an
                           :exc:`~exceptions.RequestEntityTooLarge`
                           exception is raised.
    :param max_content_length: If this is provided and the transmitted data
                               is longer than this value an
                               :exc:`~exceptions.RequestEntityTooLarge`
                               exception is raised.
    :param cls: an optional dict class to use.  If this is not specified
                       or `None` the default :class:`MultiDict` is used.
    :param silent: If set to False parsing errors will not be caught.
    :param max_form_parts: The maximum number of multipart parts to be parsed. If this
        is exceeded, a :exc:`~exceptions.RequestEntityTooLarge` exception is raised.

    .. versionchanged:: 3.0
        The ``charset`` and ``errors`` parameters were removed.

    .. versionchanged:: 3.0
        The ``parse_functions`` attribute and ``get_parse_func`` methods were removed.

    .. versionchanged:: 2.2.3
        Added the ``max_form_parts`` parameter.

    .. versionadded:: 0.8
    """
    stream_factory: Incomplete
    max_form_memory_size: Incomplete
    max_content_length: Incomplete
    max_form_parts: Incomplete
    cls: Incomplete
    silent: Incomplete
    def __init__(self, stream_factory: TStreamFactory | None = None, max_form_memory_size: int | None = None, max_content_length: int | None = None, cls: type[MultiDict] | None = None, silent: bool = True, *, max_form_parts: int | None = None) -> None: ...
    def parse_from_environ(self, environ: WSGIEnvironment) -> t_parse_result:
        """Parses the information from the environment as form data.

        :param environ: the WSGI environment to be used for parsing.
        :return: A tuple in the form ``(stream, form, files)``.
        """
    def parse(self, stream: t.IO[bytes], mimetype: str, content_length: int | None, options: dict[str, str] | None = None) -> t_parse_result:
        """Parses the information from the given stream, mimetype,
        content length and mimetype parameters.

        :param stream: an input stream
        :param mimetype: the mimetype of the data
        :param content_length: the content length of the incoming data
        :param options: optional mimetype parameters (used for
                        the multipart boundary for instance)
        :return: A tuple in the form ``(stream, form, files)``.

        .. versionchanged:: 3.0
            The invalid ``application/x-url-encoded`` content type is not
            treated as ``application/x-www-form-urlencoded``.
        """

class MultiPartParser:
    max_form_memory_size: Incomplete
    max_form_parts: Incomplete
    stream_factory: Incomplete
    cls: Incomplete
    buffer_size: Incomplete
    def __init__(self, stream_factory: TStreamFactory | None = None, max_form_memory_size: int | None = None, cls: type[MultiDict] | None = None, buffer_size: int = ..., max_form_parts: int | None = None) -> None: ...
    def fail(self, message: str) -> te.NoReturn: ...
    def get_part_charset(self, headers: Headers) -> str: ...
    def start_file_streaming(self, event: File, total_content_length: int | None) -> t.IO[bytes]: ...
    def parse(self, stream: t.IO[bytes], boundary: bytes, content_length: int | None) -> tuple[MultiDict, MultiDict]: ...
