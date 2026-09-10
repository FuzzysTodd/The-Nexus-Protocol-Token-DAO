from _typeshed import Incomplete
from dash.testing.browser import Browser as Browser

class DashComposite(Browser):
    server: Incomplete
    def __init__(self, server, **kwargs) -> None: ...
    server_url: Incomplete
    def start_server(self, app, navigate: bool = True, **kwargs) -> None:
        """Start the local server with app."""

class DashRComposite(Browser):
    server: Incomplete
    def __init__(self, server, **kwargs) -> None: ...
    server_url: Incomplete
    def start_server(self, app, cwd: Incomplete | None = None) -> None: ...

class DashJuliaComposite(Browser):
    server: Incomplete
    def __init__(self, server, **kwargs) -> None: ...
    server_url: Incomplete
    def start_server(self, app, cwd: Incomplete | None = None) -> None: ...
