from _typeshed import Incomplete
from py4j.java_gateway import JavaGateway as JavaGateway, JavaObject as JavaObject
from pyspark import SparkContext as SparkContext, since as since
from pyspark.ml._typing import PipelineStage as PipelineStage
from pyspark.ml.base import Params as Params
from pyspark.ml.common import inherit_doc as inherit_doc
from pyspark.ml.wrapper import JavaWrapper as JavaWrapper
from pyspark.sql import SparkSession as SparkSession
from pyspark.util import VersionUtils as VersionUtils
from typing import Any, Dict, Generic, List, Sequence, Type, TypeVar

T = TypeVar('T')
RW = TypeVar('RW', bound='BaseReadWrite')
W = TypeVar('W', bound='MLWriter')
JW = TypeVar('JW', bound='JavaMLWriter')
RL = TypeVar('RL', bound='MLReadable')
JR = TypeVar('JR', bound='JavaMLReader')

class Identifiable:
    """
    Object with a unique ID.
    """
    uid: Incomplete
    def __init__(self) -> None: ...

class BaseReadWrite:
    """
    Base class for MLWriter and MLReader. Stores information about the SparkContext
    and SparkSession.

    .. versionadded:: 2.3.0
    """
    def __init__(self) -> None: ...
    def session(self, sparkSession: SparkSession) -> RW:
        """
        Sets the Spark Session to use for saving/loading.
        """
    @property
    def sparkSession(self) -> SparkSession:
        """
        Returns the user-specified Spark Session or the default.
        """
    @property
    def sc(self) -> SparkContext:
        """
        Returns the underlying `SparkContext`.
        """

class MLWriter(BaseReadWrite):
    """
    Utility class that can save ML instances.

    .. versionadded:: 2.0.0
    """
    shouldOverwrite: bool
    optionMap: Incomplete
    def __init__(self) -> None: ...
    def save(self, path: str) -> None:
        """Save the ML instance to the input path."""
    def saveImpl(self, path: str) -> None:
        """
        save() handles overwriting and then calls this method.  Subclasses should override this
        method to implement the actual saving of the instance.
        """
    def overwrite(self) -> MLWriter:
        """Overwrites if the output path already exists."""
    def option(self, key: str, value: Any) -> MLWriter:
        """
        Adds an option to the underlying MLWriter. See the documentation for the specific model's
        writer for possible options. The option name (key) is case-insensitive.
        """

class GeneralMLWriter(MLWriter):
    """
    Utility class that can save ML instances in different formats.

    .. versionadded:: 2.4.0
    """
    source: Incomplete
    def format(self, source: str) -> GeneralMLWriter:
        '''
        Specifies the format of ML export ("pmml", "internal", or the fully qualified class
        name for export).
        '''

class JavaMLWriter(MLWriter):
    """
    (Private) Specialization of :py:class:`MLWriter` for :py:class:`JavaParams` types
    """
    def __init__(self, instance: JavaMLWritable) -> None: ...
    def save(self, path: str) -> None:
        """Save the ML instance to the input path."""
    def overwrite(self) -> JavaMLWriter:
        """Overwrites if the output path already exists."""
    def option(self, key: str, value: str) -> JavaMLWriter: ...
    def session(self, sparkSession: SparkSession) -> JavaMLWriter:
        """Sets the Spark Session to use for saving."""

class GeneralJavaMLWriter(JavaMLWriter):
    """
    (Private) Specialization of :py:class:`GeneralMLWriter` for :py:class:`JavaParams` types
    """
    def __init__(self, instance: JavaMLWritable) -> None: ...
    def format(self, source: str) -> GeneralJavaMLWriter:
        '''
        Specifies the format of ML export ("pmml", "internal", or the fully qualified class
        name for export).
        '''

class MLWritable:
    """
    Mixin for ML instances that provide :py:class:`MLWriter`.

    .. versionadded:: 2.0.0
    """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    def save(self, path: str) -> None:
        """Save this ML instance to the given path, a shortcut of 'write().save(path)'."""

class JavaMLWritable(MLWritable):
    """
    (Private) Mixin for ML instances that provide :py:class:`JavaMLWriter`.
    """
    def write(self) -> JavaMLWriter:
        """Returns an MLWriter instance for this ML instance."""

class GeneralJavaMLWritable(JavaMLWritable):
    """
    (Private) Mixin for ML instances that provide :py:class:`GeneralJavaMLWriter`.
    """
    def write(self) -> GeneralJavaMLWriter:
        """Returns an GeneralMLWriter instance for this ML instance."""

class MLReader(BaseReadWrite, Generic[RL]):
    """
    Utility class that can load ML instances.

    .. versionadded:: 2.0.0
    """
    def __init__(self) -> None: ...
    def load(self, path: str) -> RL:
        """Load the ML instance from the input path."""

class JavaMLReader(MLReader[RL]):
    """
    (Private) Specialization of :py:class:`MLReader` for :py:class:`JavaParams` types
    """
    def __init__(self, clazz: Type['JavaMLReadable[RL]']) -> None: ...
    def load(self, path: str) -> RL:
        """Load the ML instance from the input path."""
    def session(self, sparkSession: SparkSession) -> JR:
        """Sets the Spark Session to use for loading."""

class MLReadable(Generic[RL]):
    """
    Mixin for instances that provide :py:class:`MLReader`.

    .. versionadded:: 2.0.0
    """
    @classmethod
    def read(cls) -> MLReader[RL]:
        """Returns an MLReader instance for this class."""
    @classmethod
    def load(cls, path: str) -> RL:
        """Reads an ML instance from the input path, a shortcut of `read().load(path)`."""

class JavaMLReadable(MLReadable[RL]):
    """
    (Private) Mixin for instances that provide JavaMLReader.
    """
    @classmethod
    def read(cls) -> JavaMLReader[RL]:
        """Returns an MLReader instance for this class."""

class DefaultParamsWritable(MLWritable):
    """
    Helper trait for making simple :py:class:`Params` types writable.  If a :py:class:`Params`
    class stores all data as :py:class:`Param` values, then extending this trait will provide
    a default implementation of writing saved instances of the class.
    This only handles simple :py:class:`Param` types; e.g., it will not handle
    :py:class:`pyspark.sql.DataFrame`. See :py:class:`DefaultParamsReadable`, the counterpart
    to this class.

    .. versionadded:: 2.3.0
    """
    def write(self) -> MLWriter:
        """Returns a DefaultParamsWriter instance for this class."""

class DefaultParamsWriter(MLWriter):
    """
    Specialization of :py:class:`MLWriter` for :py:class:`Params` types

    Class for writing Estimators and Transformers whose parameters are JSON-serializable.

    .. versionadded:: 2.3.0
    """
    instance: Incomplete
    def __init__(self, instance: Params) -> None: ...
    def saveImpl(self, path: str) -> None: ...
    @staticmethod
    def extractJsonParams(instance: Params, skipParams: Sequence[str]) -> Dict[str, Any]: ...
    @staticmethod
    def saveMetadata(instance: Params, path: str, sc: SparkContext, extraMetadata: Dict[str, Any] | None = None, paramMap: Dict[str, Any] | None = None) -> None:
        '''
        Saves metadata + Params to: path + "/metadata"

        - class
        - timestamp
        - sparkVersion
        - uid
        - paramMap
        - defaultParamMap (since 2.4.0)
        - (optionally, extra metadata)

        Parameters
        ----------
        extraMetadata : dict, optional
            Extra metadata to be saved at same level as uid, paramMap, etc.
        paramMap : dict, optional
            If given, this is saved in the "paramMap" field.
        '''

class DefaultParamsReadable(MLReadable[RL]):
    """
    Helper trait for making simple :py:class:`Params` types readable.
    If a :py:class:`Params` class stores all data as :py:class:`Param` values,
    then extending this trait will provide a default implementation of reading saved
    instances of the class. This only handles simple :py:class:`Param` types;
    e.g., it will not handle :py:class:`pyspark.sql.DataFrame`. See
    :py:class:`DefaultParamsWritable`, the counterpart to this class.

    .. versionadded:: 2.3.0
    """
    @classmethod
    def read(cls) -> DefaultParamsReader[RL]:
        """Returns a DefaultParamsReader instance for this class."""

class DefaultParamsReader(MLReader[RL]):
    """
    Specialization of :py:class:`MLReader` for :py:class:`Params` types

    Default :py:class:`MLReader` implementation for transformers and estimators that
    contain basic (json-serializable) params and no data. This will not handle
    more complex params or types with data (e.g., models with coefficients).

    .. versionadded:: 2.3.0
    """
    cls: Incomplete
    def __init__(self, cls: Type[DefaultParamsReadable[RL]]) -> None: ...
    def load(self, path: str) -> RL: ...
    @staticmethod
    def loadMetadata(path: str, sc: SparkContext, expectedClassName: str = '') -> Dict[str, Any]:
        """
        Load metadata saved using :py:meth:`DefaultParamsWriter.saveMetadata`

        Parameters
        ----------
        path : str
        sc : :py:class:`pyspark.SparkContext`
        expectedClassName : str, optional
            If non empty, this is checked against the loaded metadata.
        """
    @staticmethod
    def getAndSetParams(instance: RL, metadata: Dict[str, Any], skipParams: List[str] | None = None) -> None:
        """
        Extract Params from metadata, and set them in the instance.
        """
    @staticmethod
    def isPythonParamsInstance(metadata: Dict[str, Any]) -> bool: ...
    @staticmethod
    def loadParamsInstance(path: str, sc: SparkContext) -> RL:
        """
        Load a :py:class:`Params` instance from the given path, and return it.
        This assumes the instance inherits from :py:class:`MLReadable`.
        """

class HasTrainingSummary(Generic[T]):
    """
    Base class for models that provides Training summary.

    .. versionadded:: 3.0.0
    """
    @property
    def hasSummary(self) -> bool:
        """
        Indicates whether a training summary exists for this model
        instance.
        """
    @property
    def summary(self) -> T:
        """
        Gets summary of the model trained on the training set. An exception is thrown if
        no summary exists.
        """

class MetaAlgorithmReadWrite:
    @staticmethod
    def isMetaEstimator(pyInstance: Any) -> bool: ...
    @staticmethod
    def getAllNestedStages(pyInstance: Any) -> List['Params']: ...
    @staticmethod
    def getUidMap(instance: Any) -> Dict[str, 'Params']: ...
