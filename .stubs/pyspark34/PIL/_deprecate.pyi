from . import __version__ as __version__

def deprecate(deprecated: str, when: int | None, replacement: str | None = None, *, action: str | None = None, plural: bool = False) -> None:
    '''
    Deprecations helper.

    :param deprecated: Name of thing to be deprecated.
    :param when: Pillow major version to be removed in.
    :param replacement: Name of replacement.
    :param action: Instead of "replacement", give a custom call to action
        e.g. "Upgrade to new thing".
    :param plural: if the deprecated thing is plural, needing "are" instead of "is".

    Usually of the form:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
        Use [replacement] instead."

    You can leave out the replacement sentence:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd)"

    Or with another call to action:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
        [action]."
    '''
