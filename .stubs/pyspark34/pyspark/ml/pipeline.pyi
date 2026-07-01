from _typeshed import Incomplete
from py4j.java_gateway import JavaObject as JavaObject
from pyspark import SparkContext as SparkContext, keyword_only as keyword_only, since as since
from pyspark.ml._typing import ParamMap as ParamMap, PipelineStage as PipelineStage
from pyspark.ml.base import Estimator as Estimator, Model as Model, Transformer as Transformer
from pyspark.ml.common import inherit_doc as inherit_doc
from pyspark.ml.param import Param as Param, Params as Params
from pyspark.ml.util import DefaultParamsReader as DefaultParamsReader, DefaultParamsWriter as DefaultParamsWriter, JavaMLReadable as JavaMLReadable, JavaMLReader as JavaMLReader, JavaMLWritable as JavaMLWritable, JavaMLWriter as JavaMLWriter, MLReadable as MLReadable, MLReader as MLReader, MLWritable as MLWritable, MLWriter as MLWriter
from pyspark.ml.wrapper import JavaParams as JavaParams
from pyspark.sql.dataframe import DataFrame as DataFrame
from typing import Any, Dict, List, Tuple, Type

class Pipeline(Estimator['PipelineModel'], MLReadable['Pipeline'], MLWritable):
    """
    A simple pipeline, which acts as an estimator. A Pipeline consists
    of a sequence of stages, each of which is either an
    :py:class:`Estimator` or a :py:class:`Transformer`. When
    :py:meth:`Pipeline.fit` is called, the stages are executed in
    order. If a stage is an :py:class:`Estimator`, its
    :py:meth:`Estimator.fit` method will be called on the input
    dataset to fit a model. Then the model, which is a transformer,
    will be used to transform the dataset as the input to the next
    stage. If a stage is a :py:class:`Transformer`, its
    :py:meth:`Transformer.transform` method will be called to produce
    the dataset for the next stage. The fitted model from a
    :py:class:`Pipeline` is a :py:class:`PipelineModel`, which
    consists of fitted models and transformers, corresponding to the
    pipeline stages. If stages is an empty list, the pipeline acts as an
    identity transformer.

    .. versionadded:: 1.3.0
    """
    stages: Param[List['PipelineStage']]
    def __init__(self, *, stages: List['PipelineStage'] | None = None) -> None:
        """
        __init__(self, \\*, stages=None)
        """
    def setStages(self, value: List['PipelineStage']) -> Pipeline:
        """
        Set pipeline stages.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        value : list
            of :py:class:`pyspark.ml.Transformer`
            or :py:class:`pyspark.ml.Estimator`

        Returns
        -------
        :py:class:`Pipeline`
            the pipeline instance
        """
    def getStages(self) -> List['PipelineStage']:
        """
        Get pipeline stages.
        """
    def setParams(self, *, stages: List['PipelineStage'] | None = None) -> Pipeline:
        """
        setParams(self, \\*, stages=None)
        Sets params for Pipeline.
        """
    def copy(self, extra: ParamMap | None = None) -> Pipeline:
        """
        Creates a copy of this instance.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        extra : dict, optional
            extra parameters

        Returns
        -------
        :py:class:`Pipeline`
            new instance
        """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    @classmethod
    def read(cls) -> PipelineReader:
        """Returns an MLReader instance for this class."""

class PipelineWriter(MLWriter):
    """
    (Private) Specialization of :py:class:`MLWriter` for :py:class:`Pipeline` types
    """
    instance: Incomplete
    def __init__(self, instance: Pipeline) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class PipelineReader(MLReader[Pipeline]):
    """
    (Private) Specialization of :py:class:`MLReader` for :py:class:`Pipeline` types
    """
    cls: Incomplete
    def __init__(self, cls: Type[Pipeline]) -> None: ...
    def load(self, path: str) -> Pipeline: ...

class PipelineModelWriter(MLWriter):
    """
    (Private) Specialization of :py:class:`MLWriter` for :py:class:`PipelineModel` types
    """
    instance: Incomplete
    def __init__(self, instance: PipelineModel) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class PipelineModelReader(MLReader['PipelineModel']):
    """
    (Private) Specialization of :py:class:`MLReader` for :py:class:`PipelineModel` types
    """
    cls: Incomplete
    def __init__(self, cls: Type['PipelineModel']) -> None: ...
    def load(self, path: str) -> PipelineModel: ...

class PipelineModel(Model, MLReadable['PipelineModel'], MLWritable):
    """
    Represents a compiled pipeline with transformers and fitted models.

    .. versionadded:: 1.3.0
    """
    stages: Incomplete
    def __init__(self, stages: List[Transformer]) -> None: ...
    def copy(self, extra: ParamMap | None = None) -> PipelineModel:
        """
        Creates a copy of this instance.

        .. versionadded:: 1.4.0

        :param extra: extra parameters
        :returns: new instance
        """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    @classmethod
    def read(cls) -> PipelineModelReader:
        """Returns an MLReader instance for this class."""

class PipelineSharedReadWrite:
    """
    Functions for :py:class:`MLReader` and :py:class:`MLWriter` shared between
    :py:class:`Pipeline` and :py:class:`PipelineModel`

    .. versionadded:: 2.3.0
    """
    @staticmethod
    def checkStagesForJava(stages: List['PipelineStage']) -> bool: ...
    @staticmethod
    def validateStages(stages: List['PipelineStage']) -> None:
        """
        Check that all stages are Writable
        """
    @staticmethod
    def saveImpl(instance: Pipeline | PipelineModel, stages: List['PipelineStage'], sc: SparkContext, path: str) -> None:
        """
        Save metadata and stages for a :py:class:`Pipeline` or :py:class:`PipelineModel`
        - save metadata to path/metadata
        - save stages to stages/IDX_UID
        """
    @staticmethod
    def load(metadata: Dict[str, Any], sc: SparkContext, path: str) -> Tuple[str, List['PipelineStage']]:
        """
        Load metadata and stages for a :py:class:`Pipeline` or :py:class:`PipelineModel`

        Returns
        -------
        tuple
            (UID, list of stages)
        """
    @staticmethod
    def getStagePath(stageUid: str, stageIdx: int, numStages: int, stagesDir: str) -> str:
        """
        Get path for saving the given stage.
        """
