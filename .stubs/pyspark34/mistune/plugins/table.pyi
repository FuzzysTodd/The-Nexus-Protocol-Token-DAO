__all__ = ['table', 'table_in_quote', 'table_in_list']

def table(md) -> None:
    """A mistune plugin to support table, spec defined at
    https://michelf.ca/projects/php-markdown/extra/#table

    Here is an example:

    .. code-block:: text

        First Header  | Second Header
        ------------- | -------------
        Content Cell  | Content Cell
        Content Cell  | Content Cell

    :param md: Markdown instance
    """
def table_in_quote(md) -> None:
    """Enable table plugin in block quotes."""
def table_in_list(md) -> None:
    """Enable table plugin in list."""
