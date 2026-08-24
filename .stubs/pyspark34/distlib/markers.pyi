from _typeshed import Incomplete

__all__ = ['interpret']

class Evaluator:
    """
    This class is used to evaluate marker expressions.
    """
    operations: Incomplete
    def evaluate(self, expr, context):
        """
        Evaluate a marker expression returned by the :func:`parse_requirement`
        function in the specified context.
        """

def interpret(marker, execution_context: Incomplete | None = None):
    """
    Interpret a marker and return a result depending on environment.

    :param marker: The marker to interpret.
    :type marker: str
    :param execution_context: The context used for name lookup.
    :type execution_context: mapping
    """
