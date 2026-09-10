def resolve_references(source):
    """
    This applies the resolve_one_reference to the text passed in via the source argument.

    This expects content in the form of a string encoded JSON object as represented
    internally in ``pandoc``.
    """
def resolve_one_reference(key, val, fmt, meta):
    """
    This takes a tuple of arguments that are compatible with ``pandocfilters.walk()`` that
    allows identifying hyperlinks in the document and transforms them into valid LaTeX
    \\hyperref{} calls so that linking to headers between cells is possible.

    See the documentation in ``pandocfilters.walk()`` for further information on the meaning
    and specification of ``key``, ``val``, ``fmt``, and ``meta``.
    """
