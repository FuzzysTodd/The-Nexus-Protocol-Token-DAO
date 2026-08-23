import dataclasses
from _typeshed import Incomplete
from tensorboard.util import tb_logging as tb_logging
from typing import Collection

logger: Incomplete

@dataclasses.dataclass(frozen=True)
class Directive:
    """Content security policy directive.

    Loosely follow vocabulary from https://www.w3.org/TR/CSP/#framework-directives.

    Attributes:
      name: A non-empty string.
      value: A collection of non-empty strings.
    """
    name: str
    value: Collection[str]
    def __init__(self, name, value) -> None: ...

class SecurityValidatorMiddleware:
    '''WSGI middleware validating security on response.

    It validates:
    - responses have Content-Type
    - responses have X-Content-Type-Options: nosniff
    - text/html responses have CSP header. It also validates whether the CSP
      headers pass basic requirement. e.g., default-src should be present, cannot
      use "*" directive, and others. For more complete list, please refer to
      _validate_csp_policies.

    Instances of this class are WSGI applications (see PEP 3333).
    '''
    def __init__(self, application) -> None:
        """Initializes an `SecurityValidatorMiddleware`.

        Args:
          application: The WSGI application to wrap (see PEP 3333).
        """
    def __call__(self, environ, start_response): ...
