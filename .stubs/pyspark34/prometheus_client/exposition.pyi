from .asgi import make_asgi_app as make_asgi_app
from .registry import CollectorRegistry
from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from typing import Any, Callable, Dict
from urllib.request import HTTPRedirectHandler
from wsgiref.simple_server import WSGIRequestHandler, WSGIServer

__all__ = ['CONTENT_TYPE_LATEST', 'delete_from_gateway', 'generate_latest', 'instance_ip_grouping_key', 'make_asgi_app', 'make_wsgi_app', 'MetricsHandler', 'push_to_gateway', 'pushadd_to_gateway', 'start_http_server', 'start_wsgi_server', 'write_to_textfile']

CONTENT_TYPE_LATEST: str

class _PrometheusRedirectHandler(HTTPRedirectHandler):
    """
    Allow additional methods (e.g. PUT) and data forwarding in redirects.

    Use of this class constitute a user's explicit agreement to the
    redirect responses the Prometheus client will receive when using it.
    You should only use this class if you control or otherwise trust the
    redirect behavior involved and are certain it is safe to full transfer
    the original request (method and data) to the redirected URL. For
    example, if you know there is a cosmetic URL redirect in front of a
    local deployment of a Prometheus server, and all redirects are safe,
    this is the class to use to handle redirects in that case.

    The standard HTTPRedirectHandler does not forward request data nor
    does it allow redirected PUT requests (which Prometheus uses for some
    operations, for example `push_to_gateway`) because these cannot
    generically guarantee no violations of HTTP RFC 2616 requirements for
    the user to explicitly confirm redirects that could have unexpected
    side effects (such as rendering a PUT request non-idempotent or
    creating multiple resources not named in the original request).
    """
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """
        Apply redirect logic to a request.

        See parent HTTPRedirectHandler.redirect_request for parameter info.

        If the redirect is disallowed, this raises the corresponding HTTP error.
        If the redirect can't be determined, return None to allow other handlers
        to try. If the redirect is allowed, return the new request.

        This method specialized for the case when (a) the user knows that the
        redirect will not cause unacceptable side effects for any request method,
        and (b) the user knows that any request data should be passed through to
        the redirect. If either condition is not met, this should not be used.
        """

def make_wsgi_app(registry: CollectorRegistry = ..., disable_compression: bool = False) -> Callable:
    """Create a WSGI app which serves the metrics from a registry."""

class _SilentHandler(WSGIRequestHandler):
    """WSGI handler that does not log requests."""
    def log_message(self, format, *args) -> None:
        """Log nothing."""

class ThreadingWSGIServer(ThreadingMixIn, WSGIServer):
    """Thread per request HTTP server."""
    daemon_threads: bool

def start_wsgi_server(port: int, addr: str = '0.0.0.0', registry: CollectorRegistry = ...) -> None:
    """Starts a WSGI server for prometheus metrics as a daemon thread."""
start_http_server = start_wsgi_server

def generate_latest(registry: CollectorRegistry = ...) -> bytes:
    """Returns the metrics from the registry in latest text format as a string."""

class MetricsHandler(BaseHTTPRequestHandler):
    """HTTP handler that gives metrics from ``REGISTRY``."""
    registry: CollectorRegistry
    def do_GET(self) -> None: ...
    def log_message(self, format: str, *args: Any) -> None:
        """Log nothing."""
    @classmethod
    def factory(cls, registry: CollectorRegistry) -> type:
        """Returns a dynamic MetricsHandler class tied
           to the passed registry.
        """

def write_to_textfile(path: str, registry: CollectorRegistry) -> None:
    """Write metrics to the given path.

    This is intended for use with the Node exporter textfile collector.
    The path must end in .prom for the textfile collector to process it."""
def push_to_gateway(gateway: str, job: str, registry: CollectorRegistry, grouping_key: Dict[str, Any] | None = None, timeout: float | None = 30, handler: Callable = ...) -> None:
    '''Push metrics to the given pushgateway.

    `gateway` the url for your push gateway. Either of the form
              \'http://pushgateway.local\', or \'pushgateway.local\'.
              Scheme defaults to \'http\' if none is provided
    `job` is the job label to be attached to all pushed metrics
    `registry` is an instance of CollectorRegistry
    `grouping_key` please see the pushgateway documentation for details.
                   Defaults to None
    `timeout` is how long push will attempt to connect before giving up.
              Defaults to 30s, can be set to None for no timeout.
    `handler` is an optional function which can be provided to perform
              requests to the \'gateway\'.
              Defaults to None, in which case an http or https request
              will be carried out by a default handler.
              If not None, the argument must be a function which accepts
              the following arguments:
              url, method, timeout, headers, and content
              May be used to implement additional functionality not
              supported by the built-in default handler (such as SSL
              client certicates, and HTTP authentication mechanisms).
              \'url\' is the URL for the request, the \'gateway\' argument
              described earlier will form the basis of this URL.
              \'method\' is the HTTP method which should be used when
              carrying out the request.
              \'timeout\' requests not successfully completed after this
              many seconds should be aborted.  If timeout is None, then
              the handler should not set a timeout.
              \'headers\' is a list of ("header-name","header-value") tuples
              which must be passed to the pushgateway in the form of HTTP
              request headers.
              The function should raise an exception (e.g. IOError) on
              failure.
              \'content\' is the data which should be used to form the HTTP
              Message Body.

    This overwrites all metrics with the same job and grouping_key.
    This uses the PUT HTTP method.'''
def pushadd_to_gateway(gateway: str, job: str, registry: CollectorRegistry | None, grouping_key: Dict[str, Any] | None = None, timeout: float | None = 30, handler: Callable = ...) -> None:
    """PushAdd metrics to the given pushgateway.

    `gateway` the url for your push gateway. Either of the form
              'http://pushgateway.local', or 'pushgateway.local'.
              Scheme defaults to 'http' if none is provided
    `job` is the job label to be attached to all pushed metrics
    `registry` is an instance of CollectorRegistry
    `grouping_key` please see the pushgateway documentation for details.
                   Defaults to None
    `timeout` is how long push will attempt to connect before giving up.
              Defaults to 30s, can be set to None for no timeout.
    `handler` is an optional function which can be provided to perform
              requests to the 'gateway'.
              Defaults to None, in which case an http or https request
              will be carried out by a default handler.
              See the 'prometheus_client.push_to_gateway' documentation
              for implementation requirements.

    This replaces metrics with the same name, job and grouping_key.
    This uses the POST HTTP method."""
def delete_from_gateway(gateway: str, job: str, grouping_key: Dict[str, Any] | None = None, timeout: float | None = 30, handler: Callable = ...) -> None:
    """Delete metrics from the given pushgateway.

    `gateway` the url for your push gateway. Either of the form
              'http://pushgateway.local', or 'pushgateway.local'.
              Scheme defaults to 'http' if none is provided
    `job` is the job label to be attached to all pushed metrics
    `grouping_key` please see the pushgateway documentation for details.
                   Defaults to None
    `timeout` is how long delete will attempt to connect before giving up.
              Defaults to 30s, can be set to None for no timeout.
    `handler` is an optional function which can be provided to perform
              requests to the 'gateway'.
              Defaults to None, in which case an http or https request
              will be carried out by a default handler.
              See the 'prometheus_client.push_to_gateway' documentation
              for implementation requirements.

    This deletes metrics with the given job and grouping_key.
    This uses the DELETE HTTP method."""
def instance_ip_grouping_key() -> Dict[str, Any]:
    """Grouping key with instance set to the IP Address of this host."""
