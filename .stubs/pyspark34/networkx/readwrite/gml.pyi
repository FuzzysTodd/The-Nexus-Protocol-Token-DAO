from _typeshed import Incomplete
from collections.abc import Generator
from enum import Enum
from typing import Any, NamedTuple

__all__ = ['read_gml', 'parse_gml', 'generate_gml', 'write_gml']

def read_gml(path, label: str = 'label', destringizer: Incomplete | None = None):
    '''Read graph in GML format from `path`.

    Parameters
    ----------
    path : filename or filehandle
        The filename or filehandle to read from.

    label : string, optional
        If not None, the parsed nodes will be renamed according to node
        attributes indicated by `label`. Default value: \'label\'.

    destringizer : callable, optional
        A `destringizer` that recovers values stored as strings in GML. If it
        cannot convert a string to a value, a `ValueError` is raised. Default
        value : None.

    Returns
    -------
    G : NetworkX graph
        The parsed graph.

    Raises
    ------
    NetworkXError
        If the input cannot be parsed.

    See Also
    --------
    write_gml, parse_gml
    literal_destringizer

    Notes
    -----
    GML files are stored using a 7-bit ASCII encoding with any extended
    ASCII characters (iso8859-1) appearing as HTML character entities.
    Without specifying a `stringizer`/`destringizer`, the code is capable of
    writing `int`/`float`/`str`/`dict`/`list` data as required by the GML
    specification.  For writing other data types, and for reading data other
    than `str` you need to explicitly supply a `stringizer`/`destringizer`.

    For additional documentation on the GML file format, please see the
    `GML url <https://web.archive.org/web/20190207140002/http://www.fim.uni-passau.de/index.php?id=17297&L=1>`_.

    See the module docstring :mod:`networkx.readwrite.gml` for more details.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_gml(G, "test.gml")

    GML values are interpreted as strings by default:

    >>> H = nx.read_gml("test.gml")
    >>> H.nodes
    NodeView((\'0\', \'1\', \'2\', \'3\'))

    When a `destringizer` is provided, GML values are converted to the provided type.
    For example, integer nodes can be recovered as shown below:

    >>> J = nx.read_gml("test.gml", destringizer=int)
    >>> J.nodes
    NodeView((0, 1, 2, 3))

    '''
def parse_gml(lines, label: str = 'label', destringizer: Incomplete | None = None):
    """Parse GML graph from a string or iterable.

    Parameters
    ----------
    lines : string or iterable of strings
       Data in GML format.

    label : string, optional
        If not None, the parsed nodes will be renamed according to node
        attributes indicated by `label`. Default value: 'label'.

    destringizer : callable, optional
        A `destringizer` that recovers values stored as strings in GML. If it
        cannot convert a string to a value, a `ValueError` is raised. Default
        value : None.

    Returns
    -------
    G : NetworkX graph
        The parsed graph.

    Raises
    ------
    NetworkXError
        If the input cannot be parsed.

    See Also
    --------
    write_gml, read_gml

    Notes
    -----
    This stores nested GML attributes as dictionaries in the NetworkX graph,
    node, and edge attribute structures.

    GML files are stored using a 7-bit ASCII encoding with any extended
    ASCII characters (iso8859-1) appearing as HTML character entities.
    Without specifying a `stringizer`/`destringizer`, the code is capable of
    writing `int`/`float`/`str`/`dict`/`list` data as required by the GML
    specification.  For writing other data types, and for reading data other
    than `str` you need to explicitly supply a `stringizer`/`destringizer`.

    For additional documentation on the GML file format, please see the
    `GML url <https://web.archive.org/web/20190207140002/http://www.fim.uni-passau.de/index.php?id=17297&L=1>`_.

    See the module docstring :mod:`networkx.readwrite.gml` for more details.
    """

class Pattern(Enum):
    """encodes the index of each token-matching pattern in `tokenize`."""
    KEYS: int
    REALS: int
    INTS: int
    STRINGS: int
    DICT_START: int
    DICT_END: int
    COMMENT_WHITESPACE: int

class Token(NamedTuple):
    category: Pattern
    value: Any
    line: int
    position: int

def generate_gml(G, stringizer: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]:
    '''Generate a single entry of the graph `G` in GML format.

    Parameters
    ----------
    G : NetworkX graph
        The graph to be converted to GML.

    stringizer : callable, optional
        A `stringizer` which converts non-int/non-float/non-dict values into
        strings. If it cannot convert a value into a string, it should raise a
        `ValueError` to indicate that. Default value: None.

    Returns
    -------
    lines: generator of strings
        Lines of GML data. Newlines are not appended.

    Raises
    ------
    NetworkXError
        If `stringizer` cannot convert a value into a string, or the value to
        convert is not a string while `stringizer` is None.

    See Also
    --------
    literal_stringizer

    Notes
    -----
    Graph attributes named \'directed\', \'multigraph\', \'node\' or
    \'edge\', node attributes named \'id\' or \'label\', edge attributes
    named \'source\' or \'target\' (or \'key\' if `G` is a multigraph)
    are ignored because these attribute names are used to encode the graph
    structure.

    GML files are stored using a 7-bit ASCII encoding with any extended
    ASCII characters (iso8859-1) appearing as HTML character entities.
    Without specifying a `stringizer`/`destringizer`, the code is capable of
    writing `int`/`float`/`str`/`dict`/`list` data as required by the GML
    specification.  For writing other data types, and for reading data other
    than `str` you need to explicitly supply a `stringizer`/`destringizer`.

    For additional documentation on the GML file format, please see the
    `GML url <https://web.archive.org/web/20190207140002/http://www.fim.uni-passau.de/index.php?id=17297&L=1>`_.

    See the module docstring :mod:`networkx.readwrite.gml` for more details.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_node("1")
    >>> print("\\n".join(nx.generate_gml(G)))
    graph [
      node [
        id 0
        label "1"
      ]
    ]
    >>> G = nx.MultiGraph([("a", "b"), ("a", "b")])
    >>> print("\\n".join(nx.generate_gml(G)))
    graph [
      multigraph 1
      node [
        id 0
        label "a"
      ]
      node [
        id 1
        label "b"
      ]
      edge [
        source 0
        target 1
        key 0
      ]
      edge [
        source 0
        target 1
        key 1
      ]
    ]
    '''
def write_gml(G, path, stringizer: Incomplete | None = None) -> None:
    '''Write a graph `G` in GML format to the file or file handle `path`.

    Parameters
    ----------
    G : NetworkX graph
        The graph to be converted to GML.

    path : filename or filehandle
        The filename or filehandle to write. Files whose names end with .gz or
        .bz2 will be compressed.

    stringizer : callable, optional
        A `stringizer` which converts non-int/non-float/non-dict values into
        strings. If it cannot convert a value into a string, it should raise a
        `ValueError` to indicate that. Default value: None.

    Raises
    ------
    NetworkXError
        If `stringizer` cannot convert a value into a string, or the value to
        convert is not a string while `stringizer` is None.

    See Also
    --------
    read_gml, generate_gml
    literal_stringizer

    Notes
    -----
    Graph attributes named \'directed\', \'multigraph\', \'node\' or
    \'edge\', node attributes named \'id\' or \'label\', edge attributes
    named \'source\' or \'target\' (or \'key\' if `G` is a multigraph)
    are ignored because these attribute names are used to encode the graph
    structure.

    GML files are stored using a 7-bit ASCII encoding with any extended
    ASCII characters (iso8859-1) appearing as HTML character entities.
    Without specifying a `stringizer`/`destringizer`, the code is capable of
    writing `int`/`float`/`str`/`dict`/`list` data as required by the GML
    specification.  For writing other data types, and for reading data other
    than `str` you need to explicitly supply a `stringizer`/`destringizer`.

    Note that while we allow non-standard GML to be read from a file, we make
    sure to write GML format. In particular, underscores are not allowed in
    attribute names.
    For additional documentation on the GML file format, please see the
    `GML url <https://web.archive.org/web/20190207140002/http://www.fim.uni-passau.de/index.php?id=17297&L=1>`_.

    See the module docstring :mod:`networkx.readwrite.gml` for more details.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_gml(G, "test.gml")

    Filenames ending in .gz or .bz2 will be compressed.

    >>> nx.write_gml(G, "test.gml.gz")
    '''
