from _typeshed import Incomplete

class CSS:
    """A proxy object against the soupsieve library, to simplify its
    CSS selector API.

    Acquire this object through the .css attribute on the
    BeautifulSoup object, or on the Tag you want to use as the
    starting point for a CSS selector.

    The main advantage of doing this is that the tag to be selected
    against doesn't need to be explicitly specified in the function
    calls, since it's already scoped to a tag.
    """
    api: Incomplete
    tag: Incomplete
    def __init__(self, tag, api=...) -> None:
        """Constructor.

        You don't need to instantiate this class yourself; instead,
        access the .css attribute on the BeautifulSoup object, or on
        the Tag you want to use as the starting point for your CSS
        selector.

        :param tag: All CSS selectors will use this as their starting
        point.

        :param api: A plug-in replacement for the soupsieve module,
        designed mainly for use in tests.
        """
    def escape(self, ident):
        """Escape a CSS identifier.

        This is a simple wrapper around soupselect.escape(). See the
        documentation for that function for more information.
        """
    def compile(self, select, namespaces: Incomplete | None = None, flags: int = 0, **kwargs):
        """Pre-compile a selector and return the compiled object.

        :param selector: A CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
           used in the CSS selector to namespace URIs. By default,
           Beautiful Soup will use the prefixes it encountered while
           parsing the document.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.compile() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
           soupsieve.compile() method.

        :return: A precompiled selector object.
        :rtype: soupsieve.SoupSieve
        """
    def select_one(self, select, namespaces: Incomplete | None = None, flags: int = 0, **kwargs):
        """Perform a CSS selection operation on the current Tag and return the
        first result.

        This uses the Soup Sieve library. For more information, see
        that library's documentation for the soupsieve.select_one()
        method.

        :param selector: A CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
           used in the CSS selector to namespace URIs. By default,
           Beautiful Soup will use the prefixes it encountered while
           parsing the document.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.select_one() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
           soupsieve.select_one() method.

        :return: A Tag, or None if the selector has no match.
        :rtype: bs4.element.Tag

        """
    def select(self, select, namespaces: Incomplete | None = None, limit: int = 0, flags: int = 0, **kwargs):
        """Perform a CSS selection operation on the current Tag.

        This uses the Soup Sieve library. For more information, see
        that library's documentation for the soupsieve.select()
        method.

        :param selector: A string containing a CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
            used in the CSS selector to namespace URIs. By default,
            Beautiful Soup will pass in the prefixes it encountered while
            parsing the document.

        :param limit: After finding this number of results, stop looking.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.select() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
            soupsieve.select() method.

        :return: A ResultSet of Tag objects.
        :rtype: bs4.element.ResultSet

        """
    def iselect(self, select, namespaces: Incomplete | None = None, limit: int = 0, flags: int = 0, **kwargs):
        """Perform a CSS selection operation on the current Tag.

        This uses the Soup Sieve library. For more information, see
        that library's documentation for the soupsieve.iselect()
        method. It is the same as select(), but it returns a generator
        instead of a list.

        :param selector: A string containing a CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
            used in the CSS selector to namespace URIs. By default,
            Beautiful Soup will pass in the prefixes it encountered while
            parsing the document.

        :param limit: After finding this number of results, stop looking.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.iselect() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
            soupsieve.iselect() method.

        :return: A generator
        :rtype: types.GeneratorType
        """
    def closest(self, select, namespaces: Incomplete | None = None, flags: int = 0, **kwargs):
        """Find the Tag closest to this one that matches the given selector.

        This uses the Soup Sieve library. For more information, see
        that library's documentation for the soupsieve.closest()
        method.

        :param selector: A string containing a CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
            used in the CSS selector to namespace URIs. By default,
            Beautiful Soup will pass in the prefixes it encountered while
            parsing the document.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.closest() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
            soupsieve.closest() method.

        :return: A Tag, or None if there is no match.
        :rtype: bs4.Tag

        """
    def match(self, select, namespaces: Incomplete | None = None, flags: int = 0, **kwargs):
        """Check whether this Tag matches the given CSS selector.

        This uses the Soup Sieve library. For more information, see
        that library's documentation for the soupsieve.match()
        method.

        :param: a CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
            used in the CSS selector to namespace URIs. By default,
            Beautiful Soup will pass in the prefixes it encountered while
            parsing the document.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.match() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
            soupsieve.match() method.

        :return: True if this Tag matches the selector; False otherwise.
        :rtype: bool
        """
    def filter(self, select, namespaces: Incomplete | None = None, flags: int = 0, **kwargs):
        """Filter this Tag's direct children based on the given CSS selector.

        This uses the Soup Sieve library. It works the same way as
        passing this Tag into that library's soupsieve.filter()
        method. More information, for more information see the
        documentation for soupsieve.filter().

        :param namespaces: A dictionary mapping namespace prefixes
            used in the CSS selector to namespace URIs. By default,
            Beautiful Soup will pass in the prefixes it encountered while
            parsing the document.

        :param flags: Flags to be passed into Soup Sieve's
            soupsieve.filter() method.

        :param kwargs: Keyword arguments to be passed into SoupSieve's
            soupsieve.filter() method.

        :return: A ResultSet of Tag objects.
        :rtype: bs4.element.ResultSet

        """
