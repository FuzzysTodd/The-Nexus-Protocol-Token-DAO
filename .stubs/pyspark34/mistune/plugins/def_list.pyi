__all__ = ['def_list']

def def_list(md) -> None:
    """A mistune plugin to support def list, spec defined at
    https://michelf.ca/projects/php-markdown/extra/#def-list

    Here is an example:

    .. code-block:: text

        Apple
        :   Pomaceous fruit of plants of the genus Malus in
            the family Rosaceae.

        Orange
        :   The fruit of an evergreen tree of the genus Citrus.

    It will be converted into HTML:

    .. code-block:: html

        <dl>
        <dt>Apple</dt>
        <dd>Pomaceous fruit of plants of the genus Malus in
        the family Rosaceae.</dd>

        <dt>Orange</dt>
        <dd>The fruit of an evergreen tree of the genus Citrus.</dd>
        </dl>

    :param md: Markdown instance
    """
