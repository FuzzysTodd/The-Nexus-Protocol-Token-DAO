from _typeshed import Incomplete
from sempy._metadata._mseries import MSeries as MSeries
from sempy.fabric import DataCategory as DataCategory
from sempy.functions.matcher import TypeMatcher as TypeMatcher

class DataCategoryMatcher(TypeMatcher):
    data_category: Incomplete
    def __init__(self, data_category: str, dtype: type) -> None:
        """
        Base class for PowerBI data category matchers.

        Parameters
        ----------
        data_category : str
            The Power BI data category to match.
        dtype : type
            The data type required in the column.
        """
    def matches(self, series: MSeries) -> bool:
        """
        Match the data category with metadata in the series.

        Parameters
        ----------
        series : MSeries
            The series that is checked.

        Returns
        -------
        bool
            Returns true if data category matches the data category of the series.
        """

class LatitudeMatcher(DataCategoryMatcher):
    """
    Match a column containing latitude values.
    """
    def __init__(self) -> None: ...

class LongitudeMatcher(DataCategoryMatcher):
    """
    Match a column containing longitude values.
    """
    def __init__(self) -> None: ...

class AddressMatcher(DataCategoryMatcher):
    """
    Match a column containing address values.
    """
    def __init__(self) -> None: ...

class BarcodeMatcher(DataCategoryMatcher):
    """
    Match a column containing barcode values.
    """
    def __init__(self) -> None: ...

class CityMatcher(DataCategoryMatcher):
    """
    Match a column containing city values.
    """
    def __init__(self) -> None: ...

class ContinentMatcher(DataCategoryMatcher):
    """
    Match a column containing continent values.
    """
    def __init__(self) -> None: ...

class CountryMatcher(DataCategoryMatcher):
    """
    Match a column containing country values.
    """
    def __init__(self) -> None: ...

class PlaceMatcher(DataCategoryMatcher):
    """
    Match a column containing place values.
    """
    def __init__(self) -> None: ...

class PostalCodeMatcher(DataCategoryMatcher):
    """
    Match a column containing postal code values.
    """
    def __init__(self) -> None: ...

class StateOrProvinceMatcher(DataCategoryMatcher):
    """
    Match a column containing state or province values.
    """
    def __init__(self) -> None: ...
