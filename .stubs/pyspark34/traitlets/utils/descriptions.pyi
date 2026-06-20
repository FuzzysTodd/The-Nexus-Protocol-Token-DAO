from typing import Any

def describe(article: str | None, value: Any, name: str | None = None, verbose: bool = False, capital: bool = False) -> str:
    '''Return string that describes a value

    Parameters
    ----------
    article : str or None
        A definite or indefinite article. If the article is
        indefinite (i.e. "a" or "an") the appropriate one
        will be inferred. Thus, the arguments of ``describe``
        can themselves represent what the resulting string
        will actually look like. If None, then no article
        will be prepended to the result. For non-articled
        description, values that are instances are treated
        definitely, while classes are handled indefinitely.
    value : any
        The value which will be named.
    name : str or None (default: None)
        Only applies when ``article`` is "the" - this
        ``name`` is a definite reference to the value.
        By default one will be inferred from the value\'s
        type and repr methods.
    verbose : bool (default: False)
        Whether the name should be concise or verbose. When
        possible, verbose names include the module, and/or
        class name where an object was defined.
    capital : bool (default: False)
        Whether the first letter of the article should
        be capitalized or not. By default it is not.

    Examples
    --------
    Indefinite description:

    >>> describe("a", object())
    \'an object\'
    >>> describe("a", object)
    \'an object\'
    >>> describe("a", type(object))
    \'a type\'

    Definite description:

    >>> describe("the", object())
    "the object at \'...\'"
    >>> describe("the", object)
    \'the object object\'
    >>> describe("the", type(object))
    \'the type type\'

    Definitely named description:

    >>> describe("the", object(), "I made")
    \'the object I made\'
    >>> describe("the", object, "I will use")
    \'the object I will use\'
    '''
def class_of(value: Any) -> Any:
    """Returns a string of the value's type with an indefinite article.

    For example 'an Image' or 'a PlotValue'.
    """
def add_article(name: str, definite: bool = False, capital: bool = False) -> str:
    """Returns the string with a prepended article.

    The input does not need to begin with a character.

    Parameters
    ----------
    name : str
        Name to which to prepend an article
    definite : bool (default: False)
        Whether the article is definite or not.
        Indefinite articles being 'a' and 'an',
        while 'the' is definite.
    capital : bool (default: False)
        Whether the added article should have
        its first letter capitalized or not.
    """
def repr_type(obj: Any) -> str:
    """Return a string representation of a value and its type for readable

    error messages.
    """
