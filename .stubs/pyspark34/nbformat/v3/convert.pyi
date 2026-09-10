from .nbbase import nbformat as nbformat, nbformat_minor as nbformat_minor

def upgrade(nb, from_version: int = 2, from_minor: int = 0):
    """Convert a notebook to v3.

    Parameters
    ----------
    nb : NotebookNode
        The Python representation of the notebook to convert.
    from_version : int
        The original version of the notebook to convert.
    from_minor : int
        The original minor version of the notebook to convert (only relevant for v >= 3).
    """
def heading_to_md(cell) -> None:
    """turn heading cell into corresponding markdown"""
def raw_to_md(cell) -> None:
    """let raw passthrough as markdown"""
def downgrade(nb):
    """Convert a v3 notebook to v2.

    Parameters
    ----------
    nb : NotebookNode
        The Python representation of the notebook to convert.
    """
