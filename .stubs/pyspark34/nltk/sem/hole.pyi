from _typeshed import Incomplete
from nltk.parse import load_parser as load_parser
from nltk.sem.logic import AllExpression as AllExpression, AndExpression as AndExpression, ApplicationExpression as ApplicationExpression, ExistsExpression as ExistsExpression, IffExpression as IffExpression, ImpExpression as ImpExpression, LambdaExpression as LambdaExpression, NegatedExpression as NegatedExpression, OrExpression as OrExpression
from nltk.sem.skolemize import skolemize as skolemize

class Constants:
    ALL: str
    EXISTS: str
    NOT: str
    AND: str
    OR: str
    IMP: str
    IFF: str
    PRED: str
    LEQ: str
    HOLE: str
    LABEL: str
    MAP: Incomplete

class HoleSemantics:
    """
    This class holds the broken-down components of a hole semantics, i.e. it
    extracts the holes, labels, logic formula fragments and constraints out of
    a big conjunction of such as produced by the hole semantics grammar.  It
    then provides some operations on the semantics dealing with holes, labels
    and finding legal ways to plug holes with labels.
    """
    holes: Incomplete
    labels: Incomplete
    fragments: Incomplete
    constraints: Incomplete
    top_most_labels: Incomplete
    top_hole: Incomplete
    def __init__(self, usr) -> None:
        """
        Constructor.  `usr' is a ``sem.Expression`` representing an
        Underspecified Representation Structure (USR).  A USR has the following
        special predicates:
        ALL(l,v,n),
        EXISTS(l,v,n),
        AND(l,n,n),
        OR(l,n,n),
        IMP(l,n,n),
        IFF(l,n,n),
        PRED(l,v,n,v[,v]*) where the brackets and star indicate zero or more repetitions,
        LEQ(n,n),
        HOLE(n),
        LABEL(n)
        where l is the label of the node described by the predicate, n is either
        a label or a hole, and v is a variable.
        """
    def is_node(self, x):
        """
        Return true if x is a node (label or hole) in this semantic
        representation.
        """
    def pluggings(self):
        """
        Calculate and return all the legal pluggings (mappings of labels to
        holes) of this semantics given the constraints.
        """
    def formula_tree(self, plugging):
        """
        Return the first-order logic formula tree for this underspecified
        representation using the plugging given.
        """

class Constraint:
    """
    This class represents a constraint of the form (L =< N),
    where L is a label and N is a node (a label or a hole).
    """
    lhs: Incomplete
    rhs: Incomplete
    def __init__(self, lhs, rhs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

def hole_readings(sentence, grammar_filename: Incomplete | None = None, verbose: bool = False): ...
