from _typeshed import Incomplete
from nltk.inference.api import BaseModelBuilderCommand as BaseModelBuilderCommand, ModelBuilder as ModelBuilder
from nltk.inference.prover9 import Prover9CommandParent as Prover9CommandParent, Prover9Parent as Prover9Parent
from nltk.sem import Expression as Expression, Valuation as Valuation
from nltk.sem.logic import is_indvar as is_indvar

class MaceCommand(Prover9CommandParent, BaseModelBuilderCommand):
    """
    A ``MaceCommand`` specific to the ``Mace`` model builder.  It contains
    a print_assumptions() method that is used to print the list
    of assumptions in multiple formats.
    """
    def __init__(self, goal: Incomplete | None = None, assumptions: Incomplete | None = None, max_models: int = 500, model_builder: Incomplete | None = None) -> None:
        """
        :param goal: Input expression to prove
        :type goal: sem.Expression
        :param assumptions: Input expressions to use as assumptions in
            the proof.
        :type assumptions: list(sem.Expression)
        :param max_models: The maximum number of models that Mace will try before
            simply returning false. (Use 0 for no maximum.)
        :type max_models: int
        """
    @property
    def valuation(mbc): ...

class Mace(Prover9Parent, ModelBuilder):
    def __init__(self, end_size: int = 500) -> None: ...

def spacer(num: int = 30) -> None: ...
def decode_result(found):
    """
    Decode the result of model_found()

    :param found: The output of model_found()
    :type found: bool
    """
def test_model_found(arguments) -> None:
    """
    Try some proofs and exhibit the results.
    """
def test_build_model(arguments) -> None:
    """
    Try to build a ``nltk.sem.Valuation``.
    """
def test_transform_output(argument_pair) -> None:
    """
    Transform the model into various Mace4 ``interpformat`` formats.
    """
def test_make_relation_set() -> None: ...

arguments: Incomplete

def demo() -> None: ...
