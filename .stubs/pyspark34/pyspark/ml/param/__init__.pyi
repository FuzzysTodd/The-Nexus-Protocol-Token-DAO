from _typeshed import Incomplete
from abc import ABCMeta
from pyspark.ml._typing import ParamMap
from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.util import Identifiable
from typing import Any, Callable, Generic, List, TypeVar, overload

__all__ = ['Param', 'Params', 'TypeConverters']

T = TypeVar('T')
P = TypeVar('P', bound='Params')

class Param(Generic[T]):
    """
    A param with self-contained documentation.

    .. versionadded:: 1.3.0
    """
    parent: Incomplete
    name: Incomplete
    doc: Incomplete
    typeConverter: Incomplete
    def __init__(self, parent: Identifiable, name: str, doc: str, typeConverter: Callable[[Any], T] | None = None) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...

class TypeConverters:
    """
    Factory methods for common type conversion functions for `Param.typeConverter`.

    .. versionadded:: 2.0.0
    """
    @staticmethod
    def identity(value: T) -> T:
        """
        Dummy converter that just returns value.
        """
    @staticmethod
    def toList(value: Any) -> List:
        """
        Convert a value to a list, if possible.
        """
    @staticmethod
    def toListFloat(value: Any) -> List[float]:
        """
        Convert a value to list of floats, if possible.
        """
    @staticmethod
    def toListListFloat(value: Any) -> List[List[float]]:
        """
        Convert a value to list of list of floats, if possible.
        """
    @staticmethod
    def toListInt(value: Any) -> List[int]:
        """
        Convert a value to list of ints, if possible.
        """
    @staticmethod
    def toListString(value: Any) -> List[str]:
        """
        Convert a value to list of strings, if possible.
        """
    @staticmethod
    def toVector(value: Any) -> Vector:
        """
        Convert a value to a MLlib Vector, if possible.
        """
    @staticmethod
    def toMatrix(value: Any) -> Matrix:
        """
        Convert a value to a MLlib Matrix, if possible.
        """
    @staticmethod
    def toFloat(value: Any) -> float:
        """
        Convert a value to a float, if possible.
        """
    @staticmethod
    def toInt(value: Any) -> int:
        """
        Convert a value to an int, if possible.
        """
    @staticmethod
    def toString(value: Any) -> str:
        """
        Convert a value to a string, if possible.
        """
    @staticmethod
    def toBoolean(value: Any) -> bool:
        """
        Convert a value to a boolean, if possible.
        """

class Params(Identifiable, metaclass=ABCMeta):
    """
    Components that take parameters. This also provides an internal
    param map to store parameter values attached to the instance.

    .. versionadded:: 1.3.0
    """
    def __init__(self) -> None: ...
    @property
    def params(self) -> List[Param]:
        """
        Returns all params ordered by name. The default implementation
        uses :py:func:`dir` to get all attributes of type
        :py:class:`Param`.
        """
    def explainParam(self, param: str | Param) -> str:
        """
        Explains a single param and returns its name, doc, and optional
        default value and user-supplied value in a string.
        """
    def explainParams(self) -> str:
        """
        Returns the documentation of all params with their optionally
        default values and user-supplied values.
        """
    def getParam(self, paramName: str) -> Param:
        """
        Gets a param by its name.
        """
    def isSet(self, param: str | Param[Any]) -> bool:
        """
        Checks whether a param is explicitly set by user.
        """
    def hasDefault(self, param: str | Param[Any]) -> bool:
        """
        Checks whether a param has a default value.
        """
    def isDefined(self, param: str | Param[Any]) -> bool:
        """
        Checks whether a param is explicitly set by user or has
        a default value.
        """
    def hasParam(self, paramName: str) -> bool:
        """
        Tests whether this instance contains a param with a given
        (string) name.
        """
    @overload
    def getOrDefault(self, param: str) -> Any: ...
    @overload
    def getOrDefault(self, param: Param[T]) -> T: ...
    def extractParamMap(self, extra: ParamMap | None = None) -> ParamMap:
        """
        Extracts the embedded default param values and user-supplied
        values, and then merges them with extra values from input into
        a flat param map, where the latter value is used if there exist
        conflicts, i.e., with ordering: default param values <
        user-supplied values < extra.

        Parameters
        ----------
        extra : dict, optional
            extra param values

        Returns
        -------
        dict
            merged param map
        """
    def copy(self, extra: ParamMap | None = None) -> P:
        """
        Creates a copy of this instance with the same uid and some
        extra params. The default implementation creates a
        shallow copy using :py:func:`copy.copy`, and then copies the
        embedded and extra parameters over and returns the copy.
        Subclasses should override this method if the default approach
        is not sufficient.

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`Params`
            Copy of this instance
        """
    def set(self, param: Param, value: Any) -> None:
        """
        Sets a parameter in the embedded param map.
        """
    def clear(self, param: Param) -> None:
        """
        Clears a param from the param map if it has been explicitly set.
        """
