import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from sempy._metadata._mseries import MSeries as MSeries

class SeriesMatcher(ABC, metaclass=abc.ABCMeta):
    """
    Define a column-level matcher for a semantic function.
    """
    @abstractmethod
    def matches(self, series: MSeries) -> bool:
        """
        Return true if the matcher is met.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The column the matcher is being tested against.

        Returns
        -------
        bool
            True if the matcher is met.
        """

class AlwaysTrueMatcher(SeriesMatcher):
    """
    Match any column.
    """
    def matches(self, series: MSeries) -> bool:
        """
        Match any column.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The series the matcher is being tested against.

        Returns
        -------
        bool
            True for all columns.
        """

class TypeMatcher(SeriesMatcher):
    """
    A column matcher that checks the data type of the column matches.

    Parameters
    ----------
    dtype : type
        The data type required in the column.
        Date/Time types like :class:`~pandas.Timestamp` and :class:`~numpy.datetime64` are normalized into datetime.datetime.
    """
    dtype: Incomplete
    def __init__(self, dtype: type) -> None: ...
    def matches(self, series: MSeries) -> bool:
        """
        Check if the column has the expected data type.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The series the matcher is being tested against.

        Returns
        -------
        bool
            True if the matcher is met.
        """

class NameMatcher(SeriesMatcher):
    """
    A column matcher that checks the name of the column matches.

    Parameters
    ----------
    name : str
        The name of the column.
    """
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def matches(self, series: MSeries) -> bool:
        """
        Check if the column has the expected name.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The series the matcher is being tested against.

        Returns
        -------
        bool
            True if the matcher is met.
        """

class AndMatcher(SeriesMatcher):
    """
    A column matcher that checks if a list of matchers are all met.

    Parameters
    ----------
    *matchers : list[sempy.functions.matcher.SeriesMatcher]
        The list of matchers to check.
    """
    matchers: Incomplete
    def __init__(self, *matchers: SeriesMatcher) -> None: ...
    def matches(self, series: MSeries) -> bool:
        """
        Check if the column has the expected name.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The series the matcher is being tested against.

        Returns
        -------
        bool
            True if the matcher is met.
        """

class OrMatcher(SeriesMatcher):
    """
    A column matcher that checks if at least one of a list of matchers is met.

    Parameters
    ----------
    *matchers : list[SeriesMatcher]
        The list of matchers to check.
    """
    matchers: Incomplete
    def __init__(self, *matchers: SeriesMatcher) -> None: ...
    def matches(self, series: MSeries) -> bool:
        """
        Check if the column has the expected name.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The series the matcher is being tested against.

        Returns
        -------
        bool
            True if the matcher is met.
        """

class NameTypeMatcher(SeriesMatcher):
    """
    A column matcher that checks if the column has the expected name and data type.

    Parameters
    ----------
    name : str
        The name of the column.
    dtype : Type
        The data type required in the column.
        Date/Time types like pd.TimeStamp and np.datetime64 are normalized into datetime.datetime.
    """
    matcher: Incomplete
    def __init__(self, name: str, dtype: type) -> None: ...
    def matches(self, series: MSeries) -> bool:
        """
        Check if the column has the expected name and data type.

        Parameters
        ----------
        series : sempy.fabric.FabricSeries
            The series the matcher is being tested against.

        Returns
        -------
        bool
            True if the matcher is met.
        """
