from pyspark import since as since
from pyspark.ml._typing import P as P
from pyspark.ml.common import inherit_doc as inherit_doc
from pyspark.ml.linalg import Vector as Vector
from pyspark.ml.param import Params as Params
from pyspark.ml.param.shared import HasCheckpointInterval as HasCheckpointInterval, HasMaxIter as HasMaxIter, HasSeed as HasSeed, HasStepSize as HasStepSize, HasValidationIndicatorCol as HasValidationIndicatorCol, HasWeightCol as HasWeightCol, Param as Param, TypeConverters as TypeConverters
from pyspark.ml.wrapper import JavaPredictionModel as JavaPredictionModel
from typing import List, Sequence, TypeVar

T = TypeVar('T')

class _DecisionTreeModel(JavaPredictionModel[T]):
    """
    Abstraction for Decision Tree models.

    .. versionadded:: 1.5.0
    """
    @property
    def numNodes(self) -> int:
        """Return number of nodes of the decision tree."""
    @property
    def depth(self) -> int:
        """Return depth of the decision tree."""
    @property
    def toDebugString(self) -> str:
        """Full description of model."""
    def predictLeaf(self, value: Vector) -> float:
        """
        Predict the indices of the leaves corresponding to the feature vector.
        """

class _DecisionTreeParams(HasCheckpointInterval, HasSeed, HasWeightCol):
    """
    Mixin for Decision Tree parameters.
    """
    leafCol: Param[str]
    maxDepth: Param[int]
    maxBins: Param[int]
    minInstancesPerNode: Param[int]
    minWeightFractionPerNode: Param[float]
    minInfoGain: Param[float]
    maxMemoryInMB: Param[int]
    cacheNodeIds: Param[bool]
    def __init__(self) -> None: ...
    def setLeafCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`leafCol`.
        """
    def getLeafCol(self) -> str:
        """
        Gets the value of leafCol or its default value.
        """
    def getMaxDepth(self) -> int:
        """
        Gets the value of maxDepth or its default value.
        """
    def getMaxBins(self) -> int:
        """
        Gets the value of maxBins or its default value.
        """
    def getMinInstancesPerNode(self) -> int:
        """
        Gets the value of minInstancesPerNode or its default value.
        """
    def getMinWeightFractionPerNode(self) -> float:
        """
        Gets the value of minWeightFractionPerNode or its default value.
        """
    def getMinInfoGain(self) -> float:
        """
        Gets the value of minInfoGain or its default value.
        """
    def getMaxMemoryInMB(self) -> int:
        """
        Gets the value of maxMemoryInMB or its default value.
        """
    def getCacheNodeIds(self) -> bool:
        """
        Gets the value of cacheNodeIds or its default value.
        """

class _TreeEnsembleModel(JavaPredictionModel[T]):
    """
    (private abstraction)
    Represents a tree ensemble model.
    """
    @property
    def trees(self) -> Sequence['_DecisionTreeModel']:
        """Trees in this ensemble. Warning: These have null parent Estimators."""
    @property
    def getNumTrees(self) -> int:
        """Number of trees in ensemble."""
    @property
    def treeWeights(self) -> List[float]:
        """Return the weights for each tree"""
    @property
    def totalNumNodes(self) -> int:
        """Total number of nodes, summed over all trees in the ensemble."""
    @property
    def toDebugString(self) -> str:
        """Full description of model."""
    def predictLeaf(self, value: Vector) -> float:
        """
        Predict the indices of the leaves corresponding to the feature vector.
        """

class _TreeEnsembleParams(_DecisionTreeParams):
    """
    Mixin for Decision Tree-based ensemble algorithms parameters.
    """
    subsamplingRate: Param[float]
    supportedFeatureSubsetStrategies: List[str]
    featureSubsetStrategy: Param[str]
    def __init__(self) -> None: ...
    def getSubsamplingRate(self) -> float:
        """
        Gets the value of subsamplingRate or its default value.
        """
    def getFeatureSubsetStrategy(self) -> str:
        """
        Gets the value of featureSubsetStrategy or its default value.
        """

class _RandomForestParams(_TreeEnsembleParams):
    """
    Private class to track supported random forest parameters.
    """
    numTrees: Param[int]
    bootstrap: Param[bool]
    def __init__(self) -> None: ...
    def getNumTrees(self) -> int:
        """
        Gets the value of numTrees or its default value.
        """
    def getBootstrap(self) -> bool:
        """
        Gets the value of bootstrap or its default value.
        """

class _GBTParams(_TreeEnsembleParams, HasMaxIter, HasStepSize, HasValidationIndicatorCol):
    """
    Private class to track supported GBT params.
    """
    stepSize: Param[float]
    validationTol: Param[float]
    def getValidationTol(self) -> float:
        """
        Gets the value of validationTol or its default value.
        """

class _HasVarianceImpurity(Params):
    """
    Private class to track supported impurity measures.
    """
    supportedImpurities: List[str]
    impurity: Param[str]
    def __init__(self) -> None: ...
    def getImpurity(self) -> str:
        """
        Gets the value of impurity or its default value.
        """

class _TreeClassifierParams(Params):
    """
    Private class to track supported impurity measures.

    .. versionadded:: 1.4.0
    """
    supportedImpurities: List[str]
    impurity: Param[str]
    def __init__(self) -> None: ...
    def getImpurity(self) -> str:
        """
        Gets the value of impurity or its default value.
        """

class _TreeRegressorParams(_HasVarianceImpurity):
    """
    Private class to track supported impurity measures.
    """
