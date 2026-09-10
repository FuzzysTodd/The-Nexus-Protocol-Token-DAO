from ..base import BaseEstimator
from ._available_if import available_if as available_if
from abc import ABCMeta, abstractmethod
from typing import Any, List

__all__ = ['available_if']

class _BaseComposition(BaseEstimator, metaclass=ABCMeta):
    """Handles parameter management for classifiers composed of named estimators."""
    steps: List[Any]
    @abstractmethod
    def __init__(self): ...
