from typing import NamedTuple

class FeatureLibLocation(NamedTuple):
    """A location in a feature file"""
    file: str
    line: int
    column: int
