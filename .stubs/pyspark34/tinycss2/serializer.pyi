from _typeshed import Incomplete

def serialize(nodes):
    """Serialize nodes to CSS syntax.

    This should be used for :term:`component values`
    instead of just :meth:`tinycss2.ast.Node.serialize` on each node
    as it takes care of corner cases such as ``;`` between declarations,
    and consecutive identifiers
    that would otherwise parse back as the same token.

    :type nodes: :term:`iterable`
    :param nodes: An iterable of :class:`tinycss2.ast.Node` objects.
    :returns: A :obj:`string <str>` representing the nodes.

    """
def serialize_identifier(value):
    """Serialize any string as a CSS identifier

    :type value: :obj:`str`
    :param value: A string representing a CSS value.
    :returns:
        A :obj:`string <str>` that would parse as an
        :class:`tinycss2.ast.IdentToken` whose
        :attr:`tinycss2.ast.IdentToken.value` attribute equals the passed
        ``value`` argument.

    """
def serialize_name(value): ...
def serialize_string_value(value): ...
def serialize_url(value): ...

BAD_PAIRS: Incomplete
