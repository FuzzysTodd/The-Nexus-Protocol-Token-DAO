from .base import PostProcessorBase as PostProcessorBase
from _typeshed import Incomplete
from collections.abc import Generator
from tornado import web

class ProxyHandler(web.RequestHandler):
    """handler the proxies requests from a local prefix to a CDN"""
    def get(self, prefix, url) -> Generator[Incomplete, Incomplete, None]:
        """proxy a request to a CDN"""

class ServePostProcessor(PostProcessorBase):
    """Post processor designed to serve files

    Proxies reveal.js requests to a CDN if no local reveal.js is present
    """
    open_in_browser: Incomplete
    browser: Incomplete
    reveal_cdn: Incomplete
    reveal_prefix: Incomplete
    ip: Incomplete
    port: Incomplete
    def postprocess(self, input):
        """Serve the build directory with a webserver."""

def main(path) -> None:
    """allow running this module to serve the slides"""
