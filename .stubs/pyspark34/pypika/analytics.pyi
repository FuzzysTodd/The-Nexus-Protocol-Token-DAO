from pypika.terms import AnalyticFunction as AnalyticFunction, IgnoreNullsAnalyticFunction as IgnoreNullsAnalyticFunction, WindowFrameAnalyticFunction as WindowFrameAnalyticFunction

class Preceding(WindowFrameAnalyticFunction.Edge):
    modifier: str

class Following(WindowFrameAnalyticFunction.Edge):
    modifier: str

CURRENT_ROW: str

class Rank(AnalyticFunction):
    def __init__(self, **kwargs) -> None: ...

class DenseRank(AnalyticFunction):
    def __init__(self, **kwargs) -> None: ...

class RowNumber(AnalyticFunction):
    def __init__(self, **kwargs) -> None: ...

class NTile(AnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class FirstValue(WindowFrameAnalyticFunction, IgnoreNullsAnalyticFunction):
    def __init__(self, *terms, **kwargs) -> None: ...

class LastValue(WindowFrameAnalyticFunction, IgnoreNullsAnalyticFunction):
    def __init__(self, *terms, **kwargs) -> None: ...

class Median(AnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Avg(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class StdDev(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class StdDevPop(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class StdDevSamp(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Variance(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class VarPop(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class VarSamp(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Count(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Sum(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Max(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Min(WindowFrameAnalyticFunction):
    def __init__(self, term, **kwargs) -> None: ...

class Lag(AnalyticFunction):
    def __init__(self, *args, **kwargs) -> None: ...

class Lead(AnalyticFunction):
    def __init__(self, *args, **kwargs) -> None: ...
