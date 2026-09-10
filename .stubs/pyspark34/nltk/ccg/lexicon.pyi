from _typeshed import Incomplete
from nltk.ccg.api import CCGVar as CCGVar, Direction as Direction, FunctionalCategory as FunctionalCategory, PrimitiveCategory as PrimitiveCategory
from nltk.internals import deprecated as deprecated
from nltk.sem.logic import Expression as Expression

PRIM_RE: Incomplete
NEXTPRIM_RE: Incomplete
APP_RE: Incomplete
LEX_RE: Incomplete
RHS_RE: Incomplete
SEMANTICS_RE: Incomplete
COMMENTS_RE: Incomplete

class Token:
    """
    Class representing a token.

    token => category {semantics}
    e.g. eat => S\\var[pl]/var {\\x y.eat(x,y)}

    * `token` (string)
    * `categ` (string)
    * `semantics` (Expression)
    """
    def __init__(self, token, categ, semantics: Incomplete | None = None) -> None: ...
    def categ(self): ...
    def semantics(self): ...
    def __cmp__(self, other): ...

class CCGLexicon:
    """
    Class representing a lexicon for CCG grammars.

    * `primitives`: The list of primitive categories for the lexicon
    * `families`: Families of categories
    * `entries`: A mapping of words to possible categories
    """
    def __init__(self, start, primitives, families, entries) -> None: ...
    def categories(self, word):
        """
        Returns all the possible categories for a word
        """
    def start(self):
        """
        Return the target category for the parser
        """

def matchBrackets(string):
    """
    Separate the contents matching the first set of brackets from the rest of
    the input.
    """
def nextCategory(string):
    """
    Separate the string for the next portion of the category from the rest
    of the string
    """
def parseApplication(app):
    """
    Parse an application operator
    """
def parseSubscripts(subscr):
    """
    Parse the subscripts for a primitive category
    """
def parsePrimitiveCategory(chunks, primitives, families, var):
    """
    Parse a primitive category

    If the primitive is the special category 'var', replace it with the
    correct `CCGVar`.
    """
def augParseCategory(line, primitives, families, var: Incomplete | None = None):
    """
    Parse a string representing a category, and returns a tuple with
    (possibly) the CCG variable for the category
    """
def fromstring(lex_str, include_semantics: bool = False):
    """
    Convert string representation into a lexicon for CCGs.
    """
def parseLexicon(lex_str): ...

openccg_tinytiny: Incomplete
