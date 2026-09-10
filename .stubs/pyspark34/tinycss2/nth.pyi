from _typeshed import Incomplete

def parse_nth(input):
    """Parse `<An+B> <https://drafts.csswg.org/css-syntax-3/#anb>`_,
    as found in `:nth-child()
    <https://drafts.csswg.org/selectors/#nth-child-pseudo>`_
    and related Selector pseudo-classes.

    Although tinycss2 does not include a full Selector parser,
    this bit of syntax is included as it is particularly tricky to define
    on top of a CSS tokenizer.

    :type input: :obj:`str` or :term:`iterable`
    :param input: A string or an iterable of :term:`component values`.
    :returns:
        A ``(a, b)`` tuple of integers, or :obj:`None` if the input is invalid.

    """
def parse_b(tokens, a): ...
def parse_signless_b(tokens, a, b_sign): ...
def parse_end(tokens, a, b): ...

N_DASH_DIGITS_RE: Incomplete
