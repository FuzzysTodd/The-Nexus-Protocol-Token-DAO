import abc
from ..features import Features as Features
from dataclasses import dataclass
from typing import ClassVar, Dict, TypeVar

T = TypeVar('T', bound='TaskTemplate')

@dataclass(frozen=True)
class TaskTemplate(abc.ABC, metaclass=abc.ABCMeta):
    task: str
    input_schema: ClassVar[Features]
    label_schema: ClassVar[Features]
    def align_with_features(self, features: Features) -> T:
        """
        Align features with the task template.
        """
    @property
    def features(self) -> Features: ...
    @property
    @abc.abstractmethod
    def column_mapping(self) -> Dict[str, str]: ...
    @classmethod
    def from_dict(cls, template_dict: dict) -> T: ...
    def __init__(self, task) -> None: ...
