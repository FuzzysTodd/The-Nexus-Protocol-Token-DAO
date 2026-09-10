from networkx.utils import open_file as open_file

def write_p2g(G, path, encoding: str = 'utf-8') -> None:
    """Write NetworkX graph in p2g format.

    Notes
    -----
    This format is meant to be used with directed graphs with
    possible self loops.
    """
def read_p2g(path, encoding: str = 'utf-8'):
    """Read graph in p2g format from path.

    Returns
    -------
    MultiDiGraph

    Notes
    -----
    If you want a DiGraph (with no self loops allowed and no edge data)
    use D=nx.DiGraph(read_p2g(path))
    """
def parse_p2g(lines):
    """Parse p2g format graph from string or iterable.

    Returns
    -------
    MultiDiGraph
    """
