from _typeshed import Incomplete
from flaml.autogen import DEFAULT_MODEL as DEFAULT_MODEL, oai as oai

def solve_problem(problem: str, **config) -> str:
    """(Experimental) Solve the math problem.

    Args:
        problem (str): The problem statement.
        config (Optional, dict): The configuration for the API call.

    Returns:
        str: The solution to the problem.
    """
def remove_boxed(string: str) -> str | None:
    '''Source: https://github.com/hendrycks/math
    Extract the text within a \\boxed{...} environment.
    Example:

    >> remove_boxed("\\boxed{\\frac{2}{3}}")

    \\frac{2}{3}
    '''
def last_boxed_only_string(string: str) -> str | None:
    """Source: https://github.com/hendrycks/math
    Extract the last \\boxed{...} or \\fbox{...} element from a string.
    """
def get_answer(solution: str | None) -> str | None: ...
def is_equiv(str1: str | None, str2: str | None) -> float:
    """Returns (as a float) whether two strings containing math are equivalent up to differences of formatting in
    - units
    - fractions
    - square roots
    - superfluous LaTeX.
    Source: https://github.com/hendrycks/math
    """
def is_equiv_chain_of_thought(str1: str, str2: str) -> float:
    """Strips the solution first before calling `is_equiv`."""
def voting_counts(responses): ...
def eval_math_responses(responses, solution: Incomplete | None = None, **args):
    """Select a response for a math problem using voting, and check if the response is correct if the solution is provided.

    Args:
        responses (list): The list of responses.
        solution (str): The canonical solution.

    Returns:
        dict: The success metrics.
    """
