from _typeshed import Incomplete
from docutils.parsers import rst
from stevedore import extension as extension

LOG: Incomplete

class ListPluginsDirective(rst.Directive):
    """Present a simple list of the plugins in a namespace."""
    option_spec: Incomplete
    has_content: bool
    def run(self): ...

def setup(app): ...
