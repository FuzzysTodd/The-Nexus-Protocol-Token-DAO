from _typeshed import Incomplete
from nltk.parse import load_parser as load_parser
from nltk.parse.featurechart import InstantiateVarsChart as InstantiateVarsChart
from nltk.sem.logic import ApplicationExpression as ApplicationExpression, LambdaExpression as LambdaExpression, Variable as Variable

class CooperStore:
    """
    A container for handling quantifier ambiguity via Cooper storage.
    """
    featstruct: Incomplete
    readings: Incomplete
    core: Incomplete
    store: Incomplete
    def __init__(self, featstruct) -> None:
        """
        :param featstruct: The value of the ``sem`` node in a tree from
            ``parse_with_bindops()``
        :type featstruct: FeatStruct (with features ``core`` and ``store``)

        """
    def s_retrieve(self, trace: bool = False) -> None:
        """
        Carry out S-Retrieval of binding operators in store. If hack=True,
        serialize the bindop and core as strings and reparse. Ugh.

        Each permutation of the store (i.e. list of binding operators) is
        taken to be a possible scoping of quantifiers. We iterate through the
        binding operators in each permutation, and successively apply them to
        the current term, starting with the core semantic representation,
        working from the inside out.

        Binding operators are of the form::

             bo(\\P.all x.(man(x) -> P(x)),z1)
        """

def parse_with_bindops(sentence, grammar: Incomplete | None = None, trace: int = 0):
    """
    Use a grammar with Binding Operators to parse a sentence.
    """
def demo() -> None: ...
