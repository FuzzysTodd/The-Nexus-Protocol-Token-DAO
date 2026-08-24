from _typeshed import Incomplete
from typing import List

class ReportBase:
    COLUMN_NAMES: List[str]
    COLUMN_WIDTHS: List[int]
    ITERATION_FORMATS: List[str]
    @classmethod
    def print_header(cls) -> None: ...
    @classmethod
    def print_iteration(cls, *args) -> None: ...
    @classmethod
    def print_footer(cls) -> None: ...

class BasicReport(ReportBase):
    COLUMN_NAMES: Incomplete
    COLUMN_WIDTHS: Incomplete
    ITERATION_FORMATS: Incomplete

class SQPReport(ReportBase):
    COLUMN_NAMES: Incomplete
    COLUMN_WIDTHS: Incomplete
    ITERATION_FORMATS: Incomplete

class IPReport(ReportBase):
    COLUMN_NAMES: Incomplete
    COLUMN_WIDTHS: Incomplete
    ITERATION_FORMATS: Incomplete
