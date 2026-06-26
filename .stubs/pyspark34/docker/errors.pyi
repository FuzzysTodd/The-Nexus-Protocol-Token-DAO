import requests
from _typeshed import Incomplete

class DockerException(Exception):
    """
    A base class from which all other exceptions inherit.

    If you want to catch all errors that the Docker SDK might raise,
    catch this base exception.
    """

def create_api_error_from_http_exception(e) -> None:
    """
    Create a suitable APIError from requests.exceptions.HTTPError.
    """

class APIError(requests.exceptions.HTTPError, DockerException):
    """
    An HTTP error from the API.
    """
    response: Incomplete
    explanation: Incomplete
    def __init__(self, message, response: Incomplete | None = None, explanation: Incomplete | None = None) -> None: ...
    @property
    def status_code(self): ...
    def is_error(self): ...
    def is_client_error(self): ...
    def is_server_error(self): ...

class NotFound(APIError): ...
class ImageNotFound(NotFound): ...
class InvalidVersion(DockerException): ...
class InvalidRepository(DockerException): ...
class InvalidConfigFile(DockerException): ...
class InvalidArgument(DockerException): ...
class DeprecatedMethod(DockerException): ...

class TLSParameterError(DockerException):
    msg: Incomplete
    def __init__(self, msg) -> None: ...

class NullResource(DockerException, ValueError): ...

class ContainerError(DockerException):
    """
    Represents a container that has exited with a non-zero exit code.
    """
    container: Incomplete
    exit_status: Incomplete
    command: Incomplete
    image: Incomplete
    stderr: Incomplete
    def __init__(self, container, exit_status, command, image, stderr) -> None: ...

class StreamParseError(RuntimeError):
    msg: Incomplete
    def __init__(self, reason) -> None: ...

class BuildError(DockerException):
    msg: Incomplete
    build_log: Incomplete
    def __init__(self, reason, build_log) -> None: ...

class ImageLoadError(DockerException): ...

def create_unexpected_kwargs_error(name, kwargs): ...

class MissingContextParameter(DockerException):
    param: Incomplete
    def __init__(self, param) -> None: ...

class ContextAlreadyExists(DockerException):
    name: Incomplete
    def __init__(self, name) -> None: ...

class ContextException(DockerException):
    msg: Incomplete
    def __init__(self, msg) -> None: ...

class ContextNotFound(DockerException):
    name: Incomplete
    def __init__(self, name) -> None: ...
