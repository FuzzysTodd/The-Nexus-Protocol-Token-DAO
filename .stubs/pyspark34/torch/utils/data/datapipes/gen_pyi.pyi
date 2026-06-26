from typing import Any, Dict, List, Set, Tuple

def materialize_lines(lines: List[str], indentation: int) -> str: ...
def gen_from_template(dir: str, template_name: str, output_name: str, replacements: List[Tuple[str, Any, int]]): ...
def find_file_paths(dir_paths: List[str], files_to_exclude: Set[str]) -> Set[str]:
    """
    When given a path to a directory, returns the paths to the relevant files within it.
    This function does NOT recursive traverse to subdirectories.
    """
def extract_method_name(line: str) -> str:
    '''
    Extracts method name from decorator in the form of "@functional_datapipe({method_name})"
    '''
def extract_class_name(line: str) -> str:
    '''
    Extracts class name from class definition in the form of "class {CLASS_NAME}({Type}):"
    '''
def parse_datapipe_file(file_path: str) -> Tuple[Dict[str, str], Dict[str, str], Set[str]]:
    """
    Given a path to file, parses the file and returns a dictionary of method names to function signatures.
    """
def parse_datapipe_files(file_paths: Set[str]) -> Tuple[Dict[str, str], Dict[str, str], Set[str]]: ...
def split_outside_bracket(line: str, delimiter: str = ',') -> List[str]:
    """
    Given a line of text, split it on comma unless the comma is within a bracket '[]'.
    """
def process_signature(line: str) -> str:
    """
    Given a raw function signature, clean it up by removing the self-referential datapipe argument,
    default arguments of input functions, newlines, and spaces.
    """
def get_method_definitions(file_path: str | List[str], files_to_exclude: Set[str], deprecated_files: Set[str], default_output_type: str, method_to_special_output_type: Dict[str, str], root: str = '') -> List[str]:
    '''
    .pyi generation for functional DataPipes Process
    # 1. Find files that we want to process (exclude the ones who don\'t)
    # 2. Parse method name and signature
    # 3. Remove first argument after self (unless it is "*datapipes"), default args, and spaces
    '''

iterDP_file_path: str
iterDP_files_to_exclude: Set[str]
iterDP_deprecated_files: Set[str]
iterDP_method_to_special_output_type: Dict[str, str]
mapDP_file_path: str
mapDP_files_to_exclude: Set[str]
mapDP_deprecated_files: Set[str]
mapDP_method_to_special_output_type: Dict[str, str]

def main() -> None:
    """
    # Inject file into template datapipe.pyi.in
    TODO: The current implementation of this script only generates interfaces for built-in methods. To generate
          interface for user-defined DataPipes, consider changing `IterDataPipe.register_datapipe_as_function`.
    """
