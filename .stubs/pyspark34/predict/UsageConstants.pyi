from enum import Enum

EMIT_USAGE: str

class UsageFeatureNames(Enum):
    """Enum for the feature names of the usage data"""
    SynapseML: int

class FeatureActivityName(Enum):
    """Enum for the feature names of the activity data"""
    predict: int
