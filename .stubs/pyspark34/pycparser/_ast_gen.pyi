from _typeshed import Incomplete
from collections.abc import Generator

class ASTCodeGenerator:
    cfg_filename: Incomplete
    node_cfg: Incomplete
    def __init__(self, cfg_filename: str = '_c_ast.cfg') -> None:
        """ Initialize the code generator from a configuration
            file.
        """
    def generate(self, file: Incomplete | None = None) -> None:
        """ Generates the code into file, an open file buffer.
        """
    def parse_cfgfile(self, filename) -> Generator[Incomplete, None, None]:
        """ Parse the configuration file and yield pairs of
            (name, contents) for each node.
        """

class NodeCfg:
    """ Node configuration.

        name: node name
        contents: a list of contents - attributes and child nodes
        See comment at the top of the configuration file for details.
    """
    name: Incomplete
    all_entries: Incomplete
    attr: Incomplete
    child: Incomplete
    seq_child: Incomplete
    def __init__(self, name, contents) -> None: ...
    def generate_source(self): ...
