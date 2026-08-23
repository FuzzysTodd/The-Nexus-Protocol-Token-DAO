from . import resources as resources
from .deprecation_utils import deprecated as deprecated
from _typeshed import Incomplete
from pathlib import Path
from typing import Any, List, Tuple

BASE_REF_URL: str
this_url: Incomplete
logger: Incomplete

def load_yaml_resource(resource: str) -> Tuple[Any, str]: ...

readme_structure: Incomplete
known_readme_structure_url: Incomplete
FILLER_TEXT: Incomplete
ReadmeValidatorOutput = Tuple[dict, List[str], List[str]]

class Section:
    name: Incomplete
    level: Incomplete
    lines: Incomplete
    text: str
    is_empty_text: bool
    content: Incomplete
    parsing_error_list: Incomplete
    parsing_warning_list: Incomplete
    def __init__(self, name: str, level: str, lines: List[str] = None, suppress_parsing_errors: bool = False) -> None: ...
    def parse(self, suppress_parsing_errors: bool = False): ...
    def validate(self, structure: dict) -> ReadmeValidatorOutput:
        """Validates a Section class object recursively using the structure provided as a dictionary.

        Args:
            structute (:obj: `dict`): The dictionary representing expected structure.

        Returns:
            :obj: `ReadmeValidatorOutput`: The dictionary representation of the section, and the errors.
        """
    def to_dict(self) -> dict:
        """Returns the dictionary representation of a section."""

class ReadMe(Section):
    structure: Incomplete
    yaml_tags_line_count: int
    tag_count: int
    lines: Incomplete
    def __init__(self, name: str, lines: List[str], structure: dict = None, suppress_parsing_errors: bool = False) -> None: ...
    def validate(self) -> None: ...
    @classmethod
    def from_readme(cls, path: Path, structure: dict = None, suppress_parsing_errors: bool = False): ...
    @classmethod
    def from_string(cls, string: str, structure: dict = None, root_name: str = 'root', suppress_parsing_errors: bool = False): ...
    def parse(self, suppress_parsing_errors: bool = False): ...
