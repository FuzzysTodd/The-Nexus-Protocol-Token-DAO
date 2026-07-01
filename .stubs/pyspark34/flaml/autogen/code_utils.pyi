from _typeshed import Incomplete
from flaml.autogen import oai as oai
from typing import Callable, Dict, List, Tuple

DEFAULT_MODEL: str
FAST_MODEL: str
CODE_BLOCK_PATTERN: str
WORKING_DIR: Incomplete
UNKNOWN: str
TIMEOUT_MSG: str
DEFAULT_TIMEOUT: int

def infer_lang(code):
    """infer the language for the code.
    TODO: make it robust.
    """
def extract_code(text: str, pattern: str = ...) -> List[Tuple[str, str]]:
    """Extract code from a text.

    Args:
        text (str): The text to extract code from.
        pattern (Optional, str): The regular expression pattern for finding the code block.

    Returns:
        list: A list of tuples, each containing the language and the code.
    """
def generate_code(pattern: str = ..., **config) -> Tuple[str, float]:
    """Generate code.

    Args:
        pattern (Optional, str): The regular expression pattern for finding the code block.
            The default pattern is for finding a code block in a markdown file.
        config (Optional, dict): The configuration for the API call.

    Returns:
        str: The generated code.
        float: The cost of the generation.
    """
def improve_function(file_name, func_name, objective, **config):
    """(work in progress) Improve the function to achieve the objective."""
def improve_code(files, objective, suggest_only: bool = True, **config):
    """Improve the code to achieve a given objective.

    Args:
        files (list): A list of file names containing the source code.
        objective (str): The objective to achieve.
        suggest_only (bool): Whether to return only the suggestions or the improved code.
        config (Optional, dict): The configuration for the API call.

    Returns:
        str: The improved code if suggest_only=False; a list of suggestions if suggest_only=True (default).
        float: The cost of the generation.
    """
def timeout_handler(signum, frame) -> None: ...
def execute_code(code: str | None = None, timeout: int | None = None, filename: str | None = None, work_dir: str | None = None, use_docker: List[str] | str | bool | None = ..., lang: str | None = 'python') -> Tuple[int, str, str]:
    '''Execute code in a docker container.
    This function is not tested on MacOS.

    Args:
        code (Optional, str): The code to execute.
            If None, the code from the file specified by filename will be executed.
            Either code or filename must be provided.
        timeout (Optional, int): The maximum execution time in seconds.
            If None, a default timeout will be used. The default timeout is 600 seconds. On Windows, the timeout is not enforced when use_docker=False.
        filename (Optional, str): The file name to save the code or where the code is stored when `code` is None.
            If None, a file with a randomly generated name will be created.
            The randomly generated file will be deleted after execution.
            The file name must be a relative path. Relative paths are relative to the working directory.
        work_dir (Optional, str): The working directory for the code execution.
            If None, a default working directory will be used.
            The default working directory is the "extensions" directory under
            "path_to_flaml/autogen".
        use_docker (Optional, list, str or bool): The docker image to use for code execution.
            If a list or a str of image name(s) is provided, the code will be executed in a docker container
            with the first image successfully pulled.
            If None, False or empty, the code will be executed in the current environment.
            Default is True, which will be converted into a list.
            If the code is executed in the current environment,
            the code must be trusted.
        lang (Optional, str): The language of the code. Default is "python".

    Returns:
        int: 0 if the code executes successfully.
        str: The error message if the code fails to execute; the stdout otherwise.
        image: The docker image name after container run when docker is used.
    '''
def generate_assertions(definition: str, **config) -> Tuple[str, float]:
    """Generate assertions for a function.

    Args:
        definition (str): The function definition, including the signature and docstr.
        config (Optional, dict): The configuration for the API call.

    Returns:
        str: The generated assertions.
        float: The cost of the generation.
    """
def eval_function_completions(responses: List[str], definition: str, test: str | None = None, entry_point: str | None = None, assertions: str | Callable[[str], Tuple[str, float]] | None = None, timeout: float | None = 3, use_docker: bool | None = True) -> Dict:
    """Select a response from a list of responses for the function completion task (using generated assertions), and/or evaluate if the task is successful using a gold test.

    Args:
        responses (list): The list of responses.
        definition (str): The input definition.
        test (Optional, str): The test code.
        entry_point (Optional, str): The name of the function.
        assertions (Optional, str or Callable): The assertion code which serves as a filter of the responses, or an assertion generator.
            When provided, only the responses that pass the assertions will be considered for the actual test (if provided).
        timeout (Optional, float): The timeout for executing the code.

    Returns:
        dict: The success metrics.
    """

class PassAssertionFilter:
    cost: int
    metrics: Incomplete
    def __init__(self, assertions) -> None: ...
    responses: Incomplete
    def pass_assertions(self, context, response, **_):
        """Check if the response passes the assertions."""

def implement(definition: str, configs: List[Dict] | None = None, assertions: str | Callable[[str], Tuple[str, float]] | None = ...) -> Tuple[str, float]:
    """Implement a function from a definition.

    Args:
        definition (str): The function definition, including the signature and docstr.
        configs (list): The list of configurations for completion.
        assertions (Optional, str or Callable): The assertion code which serves as a filter of the responses, or an assertion generator.

    Returns:
        str: The implementation.
        float: The cost of the implementation.
        int: The index of the configuration which generates the implementation.
    """
