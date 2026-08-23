from .nbbase import new_code_cell as new_code_cell, new_notebook as new_notebook, new_text_cell as new_text_cell, new_worksheet as new_worksheet

def upgrade(nb, from_version: int = 1):
    """Convert a notebook to the v2 format.

    Parameters
    ----------
    nb : NotebookNode
        The Python representation of the notebook to convert.
    from_version : int
        The version of the notebook to convert from.
    """
def downgrade(nb) -> None:
    """Convert a v2 notebook to v1.

    Parameters
    ----------
    nb : NotebookNode
        The Python representation of the notebook to convert.
    """
