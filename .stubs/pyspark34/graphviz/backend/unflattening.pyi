from _typeshed import Incomplete

__all__ = ['UNFLATTEN_BINARY', 'unflatten']

UNFLATTEN_BINARY: Incomplete

def unflatten(source: str, stagger: int | None = None, fanout: bool = False, chain: int | None = None, encoding: str = ...) -> str:
    """Return DOT ``source`` piped through ``unflatten`` preprocessor as string.

    Args:
        source: DOT source to process
            (improve layout aspect ratio).
        stagger: Stagger the minimum length of leaf edges
            between 1 and this small integer.
        fanout: Fanout nodes with indegree = outdegree = 1
            when staggering (requires ``stagger``).
        chain: Form disconnected nodes into chains of up to this many nodes.
        encoding: Encoding to encode unflatten stdin and decode its stdout.

    Returns:
        Decoded stdout of the Graphviz unflatten command.

    Raises:
        graphviz.RequiredArgumentError: If ``fanout`` is given
            but no ``stagger``.
        graphviz.ExecutableNotFound: If the Graphviz 'unflatten' executable
            is not found.
        graphviz.CalledProcessError: If the returncode (exit status)
            of the unflattening 'unflatten' subprocess is non-zero.

    See also:
        Upstream documentation:
        https://www.graphviz.org/pdf/unflatten.1.pdf
    """
