from jupyter_server_terminals import api_handlers as api_handlers
from jupyter_server_terminals.handlers import TermSocket as TermSocket
from jupyter_server_terminals.terminalmanager import TerminalManager as TerminalManager

def initialize(webapp, root_dir, connection_url, settings) -> None:
    """Included for backward compat, but no-op."""
