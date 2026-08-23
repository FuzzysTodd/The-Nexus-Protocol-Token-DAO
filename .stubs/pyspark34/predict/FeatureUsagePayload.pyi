from .UsageConstants import FeatureActivityName as FeatureActivityName, UsageFeatureNames as UsageFeatureNames
from _typeshed import Incomplete
from typing import Dict

class FeatureUsagePayload:
    feature_name: Incomplete
    activity_name: Incomplete
    attributes: Incomplete
    def __init__(self, feature_name: UsageFeatureNames, activity_name: FeatureActivityName, attributes: Dict[str, str] = {}) -> None: ...
