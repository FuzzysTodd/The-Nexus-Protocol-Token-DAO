def strip_comment_line_with_symbol(line, start): ...
def strip_comments(string, comment_symbols=...):
    """
\tStripping comments usually works, but there are a few edge cases that trip it up, like https://github.com/mverleg/pyjson_tricks/issues/57.

\t:param string: A string containing json with comments started by comment_symbols.
\t:param comment_symbols: Iterable of symbols that start a line comment (default # or //).
\t:return: The string with the comments removed.
\t"""
