__all__ = ['math', 'math_in_quote', 'math_in_list']

def math(md) -> None:
    """A mistune plugin to support math. The syntax is used
    by many markdown extensions:

    .. code-block:: text

        Block math is surrounded by $$:

        $$
        f(a)=f(b)
        $$

        Inline math is surrounded by `$`, such as $f(a)=f(b)$

    :param md: Markdown instance
    """
def math_in_quote(md) -> None:
    """Enable block math plugin in block quote."""
def math_in_list(md) -> None:
    """Enable block math plugin in list."""
