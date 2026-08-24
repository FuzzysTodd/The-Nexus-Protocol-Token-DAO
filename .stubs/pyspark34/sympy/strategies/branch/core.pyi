from _typeshed import Incomplete
from collections.abc import Generator

def identity(x) -> Generator[Incomplete, None, None]: ...
def exhaust(brule):
    """ Apply a branching rule repeatedly until it has no effect """
def onaction(brule, fn): ...
def debug(brule, file: Incomplete | None = None):
    """ Print the input and output expressions at each rule application """
def multiplex(*brules):
    """ Multiplex many branching rules into one """
def condition(cond, brule):
    """ Only apply branching rule if condition is true """
def sfilter(pred, brule):
    """ Yield only those results which satisfy the predicate """
def notempty(brule): ...
def do_one(*brules):
    """ Execute one of the branching rules """
def chain(*brules):
    """
    Compose a sequence of brules so that they apply to the expr sequentially
    """
def yieldify(rl):
    """ Turn a rule into a branching rule """
