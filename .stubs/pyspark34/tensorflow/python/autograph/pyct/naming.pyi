from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import qual_names as qual_names

class Namer:
    """Symbol name generator."""
    global_namespace: Incomplete
    generated_names: Incomplete
    def __init__(self, global_namespace) -> None: ...
    def new_symbol(self, name_root, reserved_locals):
        """See control_flow.SymbolNamer.new_symbol."""
