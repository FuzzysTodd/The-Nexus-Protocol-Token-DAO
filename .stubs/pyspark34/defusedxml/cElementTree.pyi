from .ElementTree import DefusedXMLParser, ParseError as ParseError, XML as XML, XMLParse as XMLParse, XMLParser as XMLParser, XMLTreeBuilder as XMLTreeBuilder, fromstring as fromstring, iterparse as iterparse, parse as parse, tostring as tostring

__all__ = ['ParseError', 'XML', 'XMLParse', 'XMLParser', 'XMLTreeBuilder', 'fromstring', 'iterparse', 'parse', 'tostring']

XMLTreeBuilder = DefusedXMLParser
XMLParse = DefusedXMLParser
XMLParser = DefusedXMLParser
XML = fromstring
