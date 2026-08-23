from _typeshed import Incomplete

__all__ = ['EventLogAnalyzer', 'AnalyzeFunction']

class EventLogAnalyzer:
    def __init__(self, gw, analyzer) -> None:
        """
        Initializes EventLogAnalyzer object.
        :param analyzer: eventLogAnalyzer object

        >>> eventLogAnalyzer = EventLogAnalyzer(gw, analyzer)
        """
    def analyze(self, func) -> None: ...
    def analyzeString(self, func): ...
    def list(self): ...
    def addRule(self, rule) -> None: ...
    def removeRule(self, name) -> None: ...

class AnalyzeFunction:
    func: Incomplete
    def __init__(self, func) -> None: ...
    error: Incomplete
    def call(self) -> None: ...
    class Java:
        implements: Incomplete
