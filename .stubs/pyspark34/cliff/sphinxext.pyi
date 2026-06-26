from _typeshed import Incomplete
from cliff import app as app, commandmanager as commandmanager
from docutils.parsers import rst

class AutoprogramCliffDirective(rst.Directive):
    """Auto-document a subclass of `cliff.command.Command`."""
    has_content: bool
    required_arguments: int
    option_spec: Incomplete
    env: Incomplete
    def run(self): ...

def setup(app) -> None: ...
