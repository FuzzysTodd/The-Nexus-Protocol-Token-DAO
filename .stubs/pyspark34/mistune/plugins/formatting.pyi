__all__ = ['strikethrough', 'mark', 'insert', 'superscript', 'subscript']

def strikethrough(md) -> None:
    """A mistune plugin to support strikethrough. Spec defined by
    GitHub flavored Markdown and commonly used by many parsers:

    .. code-block:: text

        ~~This was mistaken text~~

    It will be converted into HTML:

    .. code-block:: html

        <del>This was mistaken text</del>

    :param md: Markdown instance
    """
def mark(md) -> None:
    """A mistune plugin to add ``<mark>`` tag. Spec defined at
    https://facelessuser.github.io/pymdown-extensions/extensions/mark/:

    .. code-block:: text

        ==mark me== ==mark \\=\\= equal==

    :param md: Markdown instance
    """
def insert(md) -> None:
    """A mistune plugin to add ``<ins>`` tag. Spec defined at
    https://facelessuser.github.io/pymdown-extensions/extensions/caret/#insert:

    .. code-block:: text

        ^^insert me^^

    :param md: Markdown instance
    """
def superscript(md) -> None:
    """A mistune plugin to add ``<sup>`` tag. Spec defined at
    https://pandoc.org/MANUAL.html#superscripts-and-subscripts:

    .. code-block:: text

        2^10^ is 1024.

    :param md: Markdown instance
    """
def subscript(md) -> None:
    """A mistune plugin to add ``<sub>`` tag. Spec defined at
    https://pandoc.org/MANUAL.html#superscripts-and-subscripts:

    .. code-block:: text

        H~2~O is a liquid.

    :param md: Markdown instance
    """
