import typing as t
from .wrappers.request import Request as Request
from .wrappers.response import Response as Response

TEMPLATE: str

def iter_sys_path() -> t.Iterator[tuple[str, bool, bool]]: ...
def test_app(req: Request) -> Response:
    """Simple test application that dumps the environment.  You can use
    it to check if Werkzeug is working properly:

    .. sourcecode:: pycon

        >>> from werkzeug.serving import run_simple
        >>> from werkzeug.testapp import test_app
        >>> run_simple('localhost', 3000, test_app)
         * Running on http://localhost:3000/

    The application displays important information from the WSGI environment,
    the Python interpreter and the installed libraries.
    """
