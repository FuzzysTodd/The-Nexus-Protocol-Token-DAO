def translate(pattern):
    """
    Given a glob pattern, produce a regex that matches it.

    >>> translate('*.txt')
    '[^/]*\\\\.txt'
    >>> translate('a?txt')
    'a[^/]txt'
    >>> translate('**/*')
    '.*/[^/]*'
    """
def separate(pattern):
    """
    Separate out character sets to avoid translating their contents.

    >>> [m.group(0) for m in separate('*.txt')]
    ['*.txt']
    >>> [m.group(0) for m in separate('a[?]txt')]
    ['a', '[?]', 'txt']
    """
def replace(match):
    """
    Perform the replacements for a match from :func:`separate`.
    """
