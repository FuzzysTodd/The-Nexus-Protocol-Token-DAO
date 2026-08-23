from .data_source import AxDataSource as AxDataSource, NumDataSource as NumDataSource, NumRef as NumRef
from .reference import Reference as Reference
from .series import Series as Series, SeriesLabel as SeriesLabel, StrRef as StrRef, XYSeries as XYSeries
from _typeshed import Incomplete
from openpyxl.utils import quote_sheetname as quote_sheetname, rows_from_range as rows_from_range

def SeriesFactory(values, xvalues: Incomplete | None = None, zvalues: Incomplete | None = None, title: Incomplete | None = None, title_from_data: bool = False):
    """
    Convenience Factory for creating chart data series.
    """
