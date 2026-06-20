from .base import StyleAndTextTuples
from _typeshed import Incomplete
from string import Formatter

__all__ = ['HTML']

class HTML:
    '''
    HTML formatted text.
    Take something HTML-like, for use as a formatted string.

    ::

        # Turn something into red.
        HTML(\'<style fg="ansired" bg="#00ff44">...</style>\')

        # Italic, bold, underline and strike.
        HTML(\'<i>...</i>\')
        HTML(\'<b>...</b>\')
        HTML(\'<u>...</u>\')
        HTML(\'<s>...</s>\')

    All HTML elements become available as a "class" in the style sheet.
    E.g. ``<username>...</username>`` can be styled, by setting a style for
    ``username``.
    '''
    value: Incomplete
    formatted_text: Incomplete
    def __init__(self, value: str) -> None: ...
    def __pt_formatted_text__(self) -> StyleAndTextTuples: ...
    def format(self, *args: object, **kwargs: object) -> HTML:
        """
        Like `str.format`, but make sure that the arguments are properly
        escaped.
        """
    def __mod__(self, value: object) -> HTML:
        """
        HTML('<b>%s</b>') % value
        """

class HTMLFormatter(Formatter):
    def format_field(self, value: object, format_spec: str) -> str: ...
