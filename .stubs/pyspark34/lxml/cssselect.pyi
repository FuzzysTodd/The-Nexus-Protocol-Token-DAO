import cssselect as external_cssselect
from . import etree
from _typeshed import Incomplete

__all__ = ['SelectorSyntaxError', 'ExpressionError', 'SelectorError', 'CSSSelector']

SelectorSyntaxError: Incomplete
ExpressionError: Incomplete
SelectorError: Incomplete

class LxmlTranslator(external_cssselect.GenericTranslator):
    """
    A custom CSS selector to XPath translator with lxml-specific extensions.
    """
    def xpath_contains_function(self, xpath, function): ...

class LxmlHTMLTranslator(LxmlTranslator, external_cssselect.HTMLTranslator):
    """
    lxml extensions + HTML support.
    """

class CSSSelector(etree.XPath):
    '''A CSS selector.

    Usage::

        >>> from lxml import etree, cssselect
        >>> select = cssselect.CSSSelector("a tag > child")

        >>> root = etree.XML("<a><b><c/><tag><child>TEXT</child></tag></b></a>")
        >>> [ el.tag for el in select(root) ]
        [\'child\']

    To use CSS namespaces, you need to pass a prefix-to-namespace
    mapping as ``namespaces`` keyword argument::

        >>> rdfns = \'http://www.w3.org/1999/02/22-rdf-syntax-ns#\'
        >>> select_ns = cssselect.CSSSelector(\'root > rdf|Description\',
        ...                                   namespaces={\'rdf\': rdfns})

        >>> rdf = etree.XML((
        ...     \'<root xmlns:rdf="%s">\'
        ...       \'<rdf:Description>blah</rdf:Description>\'
        ...     \'</root>\') % rdfns)
        >>> [(el.tag, el.text) for el in select_ns(rdf)]
        [(\'{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description\', \'blah\')]

    '''
    css: Incomplete
    def __init__(self, css, namespaces: Incomplete | None = None, translator: str = 'xml') -> None: ...
