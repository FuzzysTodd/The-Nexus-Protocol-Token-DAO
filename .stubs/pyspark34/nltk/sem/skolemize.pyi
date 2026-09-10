from _typeshed import Incomplete
from nltk.sem.logic import AllExpression as AllExpression, AndExpression as AndExpression, ApplicationExpression as ApplicationExpression, EqualityExpression as EqualityExpression, ExistsExpression as ExistsExpression, IffExpression as IffExpression, ImpExpression as ImpExpression, NegatedExpression as NegatedExpression, OrExpression as OrExpression, VariableExpression as VariableExpression, skolem_function as skolem_function, unique_variable as unique_variable

def skolemize(expression, univ_scope: Incomplete | None = None, used_variables: Incomplete | None = None):
    """
    Skolemize the expression and convert to conjunctive normal form (CNF)
    """
def to_cnf(first, second):
    """
    Convert this split disjunction to conjunctive normal form (CNF)
    """
