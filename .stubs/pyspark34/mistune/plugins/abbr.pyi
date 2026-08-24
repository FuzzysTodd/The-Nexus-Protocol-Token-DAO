__all__ = ['abbr']

def abbr(md) -> None:
    '''A mistune plugin to support abbreviations, spec defined at
    https://michelf.ca/projects/php-markdown/extra/#abbr

    Here is an example:

    .. code-block:: text

        The HTML specification
        is maintained by the W3C.

        *[HTML]: Hyper Text Markup Language
        *[W3C]:  World Wide Web Consortium

    It will be converted into HTML:

    .. code-block:: html

        The <abbr title="Hyper Text Markup Language">HTML</abbr> specification
        is maintained by the <abbr title="World Wide Web Consortium">W3C</abbr>.

    :param md: Markdown instance
    '''
