import logging
from .abc import AbstractAccessLogger as AbstractAccessLogger
from .web_request import BaseRequest as BaseRequest
from .web_response import StreamResponse as StreamResponse
from _typeshed import Incomplete
from typing import List, NamedTuple, Tuple

class KeyMethod(NamedTuple):
    key: Incomplete
    method: Incomplete

class AccessLogger(AbstractAccessLogger):
    '''Helper object to log access.

    Usage:
        log = logging.getLogger("spam")
        log_format = "%a %{User-Agent}i"
        access_logger = AccessLogger(log, log_format)
        access_logger.log(request, response, time)

    Format:
        %%  The percent sign
        %a  Remote IP-address (IP-address of proxy if using reverse proxy)
        %t  Time when the request was started to process
        %P  The process ID of the child that serviced the request
        %r  First line of request
        %s  Response status code
        %b  Size of response in bytes, including HTTP headers
        %T  Time taken to serve the request, in seconds
        %Tf Time taken to serve the request, in seconds with floating fraction
            in .06f format
        %D  Time taken to serve the request, in microseconds
        %{FOO}i  request.headers[\'FOO\']
        %{FOO}o  response.headers[\'FOO\']
        %{FOO}e  os.environ[\'FOO\']

    '''
    LOG_FORMAT_MAP: Incomplete
    LOG_FORMAT: str
    FORMAT_RE: Incomplete
    CLEANUP_RE: Incomplete
    def __init__(self, logger: logging.Logger, log_format: str = ...) -> None:
        """Initialise the logger.

        logger is a logger object to be used for logging.
        log_format is a string with apache compatible log format description.

        """
    def compile_format(self, log_format: str) -> Tuple[str, List[KeyMethod]]:
        '''Translate log_format into form usable by modulo formatting

        All known atoms will be replaced with %s
        Also methods for formatting of those atoms will be added to
        _methods in appropriate order

        For example we have log_format = "%a %t"
        This format will be translated to "%s %s"
        Also contents of _methods will be
        [self._format_a, self._format_t]
        These method will be called and results will be passed
        to translated string format.

        Each _format_* method receive \'args\' which is list of arguments
        given to self.log

        Exceptions are _format_e, _format_i and _format_o methods which
        also receive key name (by functools.partial)

        '''
    def log(self, request: BaseRequest, response: StreamResponse, time: float) -> None: ...
