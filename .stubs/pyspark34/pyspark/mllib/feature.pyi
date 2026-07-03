from _typeshed import Incomplete
from py4j.java_collections import JavaMap
from pyspark.context import SparkContext
from pyspark.mllib._typing import VectorLike
from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Vector
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.util import JavaLoader, JavaSaveable
from pyspark.rdd import RDD
from typing import Hashable, Iterable, List, Tuple, overload

__all__ = ['Normalizer', 'StandardScalerModel', 'StandardScaler', 'HashingTF', 'IDFModel', 'IDF', 'Word2Vec', 'Word2VecModel', 'ChiSqSelector', 'ChiSqSelectorModel', 'ElementwiseProduct']

class VectorTransformer:
    """
    Base class for transformation of a vector or RDD of vector
    """
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD['VectorLike']) -> RDD[Vector]: ...

class Normalizer(VectorTransformer):
    '''
    Normalizes samples individually to unit L\\ :sup:`p`\\  norm

    For any 1 <= `p` < float(\'inf\'), normalizes samples using
    sum(abs(vector) :sup:`p`) :sup:`(1/p)` as norm.

    For `p` = float(\'inf\'), max(abs(vector)) will be used as norm for
    normalization.

    .. versionadded:: 1.2.0

    Parameters
    ----------
    p : float, optional
        Normalization in L^p^ space, p = 2 by default.

    Examples
    --------
    >>> from pyspark.mllib.linalg import Vectors
    >>> v = Vectors.dense(range(3))
    >>> nor = Normalizer(1)
    >>> nor.transform(v)
    DenseVector([0.0, 0.3333, 0.6667])

    >>> rdd = sc.parallelize([v])
    >>> nor.transform(rdd).collect()
    [DenseVector([0.0, 0.3333, 0.6667])]

    >>> nor2 = Normalizer(float("inf"))
    >>> nor2.transform(v)
    DenseVector([0.0, 0.5, 1.0])
    '''
    p: Incomplete
    def __init__(self, p: float = 2.0) -> None: ...
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD['VectorLike']) -> RDD[Vector]: ...

class JavaVectorTransformer(JavaModelWrapper, VectorTransformer):
    """
    Wrapper for the model in JVM
    """
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD['VectorLike']) -> RDD[Vector]: ...

class StandardScalerModel(JavaVectorTransformer):
    """
    Represents a StandardScaler model that can transform vectors.

    .. versionadded:: 1.2.0
    """
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD['VectorLike']) -> RDD[Vector]: ...
    def setWithMean(self, withMean: bool) -> StandardScalerModel:
        """
        Setter of the boolean which decides
        whether it uses mean or not
        """
    def setWithStd(self, withStd: bool) -> StandardScalerModel:
        """
        Setter of the boolean which decides
        whether it uses std or not
        """
    @property
    def withStd(self) -> bool:
        """
        Returns if the model scales the data to unit standard deviation.
        """
    @property
    def withMean(self) -> bool:
        """
        Returns if the model centers the data before scaling.
        """
    @property
    def std(self) -> Vector:
        """
        Return the column standard deviation values.
        """
    @property
    def mean(self) -> Vector:
        """
        Return the column mean values.
        """

class StandardScaler:
    """
    Standardizes features by removing the mean and scaling to unit
    variance using column summary statistics on the samples in the
    training set.

    .. versionadded:: 1.2.0

    Parameters
    ----------
    withMean : bool, optional
        False by default. Centers the data with mean
        before scaling. It will build a dense output, so take
        care when applying to sparse input.
    withStd : bool, optional
        True by default. Scales the data to unit
        standard deviation.

    Examples
    --------
    >>> vs = [Vectors.dense([-2.0, 2.3, 0]), Vectors.dense([3.8, 0.0, 1.9])]
    >>> dataset = sc.parallelize(vs)
    >>> standardizer = StandardScaler(True, True)
    >>> model = standardizer.fit(dataset)
    >>> result = model.transform(dataset)
    >>> for r in result.collect(): r
    DenseVector([-0.7071, 0.7071, -0.7071])
    DenseVector([0.7071, -0.7071, 0.7071])
    >>> int(model.std[0])
    4
    >>> int(model.mean[0]*10)
    9
    >>> model.withStd
    True
    >>> model.withMean
    True
    """
    withMean: Incomplete
    withStd: Incomplete
    def __init__(self, withMean: bool = False, withStd: bool = True) -> None: ...
    def fit(self, dataset: RDD['VectorLike']) -> StandardScalerModel:
        """
        Computes the mean and variance and stores as a model to be used
        for later scaling.

        .. versionadded:: 1.2.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.RDD`
            The data used to compute the mean and variance
            to build the transformation model.

        Returns
        -------
        :py:class:`StandardScalerModel`
        """

class ChiSqSelectorModel(JavaVectorTransformer):
    """
    Represents a Chi Squared selector model.

    .. versionadded:: 1.4.0
    """
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD['VectorLike']) -> RDD[Vector]: ...

class ChiSqSelector:
    '''
    Creates a ChiSquared feature selector.
    The selector supports different selection methods: `numTopFeatures`, `percentile`, `fpr`,
    `fdr`, `fwe`.

     * `numTopFeatures` chooses a fixed number of top features according to a chi-squared test.

     * `percentile` is similar but chooses a fraction of all features
       instead of a fixed number.

     * `fpr` chooses all features whose p-values are below a threshold,
       thus controlling the false positive rate of selection.

     * `fdr` uses the `Benjamini-Hochberg procedure <https://en.wikipedia.org/wiki/
       False_discovery_rate#Benjamini.E2.80.93Hochberg_procedure>`_
       to choose all features whose false discovery rate is below a threshold.

     * `fwe` chooses all features whose p-values are below a threshold. The threshold is scaled by
       1/numFeatures, thus controlling the family-wise error rate of selection.

    By default, the selection method is `numTopFeatures`, with the default number of top features
    set to 50.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from pyspark.mllib.linalg import SparseVector, DenseVector
    >>> from pyspark.mllib.regression import LabeledPoint
    >>> data = sc.parallelize([
    ...     LabeledPoint(0.0, SparseVector(3, {0: 8.0, 1: 7.0})),
    ...     LabeledPoint(1.0, SparseVector(3, {1: 9.0, 2: 6.0})),
    ...     LabeledPoint(1.0, [0.0, 9.0, 8.0]),
    ...     LabeledPoint(2.0, [7.0, 9.0, 5.0]),
    ...     LabeledPoint(2.0, [8.0, 7.0, 3.0])
    ... ])
    >>> model = ChiSqSelector(numTopFeatures=1).fit(data)
    >>> model.transform(SparseVector(3, {1: 9.0, 2: 6.0}))
    SparseVector(1, {})
    >>> model.transform(DenseVector([7.0, 9.0, 5.0]))
    DenseVector([7.0])
    >>> model = ChiSqSelector(selectorType="fpr", fpr=0.2).fit(data)
    >>> model.transform(SparseVector(3, {1: 9.0, 2: 6.0}))
    SparseVector(1, {})
    >>> model.transform(DenseVector([7.0, 9.0, 5.0]))
    DenseVector([7.0])
    >>> model = ChiSqSelector(selectorType="percentile", percentile=0.34).fit(data)
    >>> model.transform(DenseVector([7.0, 9.0, 5.0]))
    DenseVector([7.0])
    '''
    numTopFeatures: Incomplete
    selectorType: Incomplete
    percentile: Incomplete
    fpr: Incomplete
    fdr: Incomplete
    fwe: Incomplete
    def __init__(self, numTopFeatures: int = 50, selectorType: str = 'numTopFeatures', percentile: float = 0.1, fpr: float = 0.05, fdr: float = 0.05, fwe: float = 0.05) -> None: ...
    def setNumTopFeatures(self, numTopFeatures: int) -> ChiSqSelector:
        '''
        set numTopFeature for feature selection by number of top features.
        Only applicable when selectorType = "numTopFeatures".
        '''
    def setPercentile(self, percentile: float) -> ChiSqSelector:
        '''
        set percentile [0.0, 1.0] for feature selection by percentile.
        Only applicable when selectorType = "percentile".
        '''
    def setFpr(self, fpr: float) -> ChiSqSelector:
        '''
        set FPR [0.0, 1.0] for feature selection by FPR.
        Only applicable when selectorType = "fpr".
        '''
    def setFdr(self, fdr: float) -> ChiSqSelector:
        '''
        set FDR [0.0, 1.0] for feature selection by FDR.
        Only applicable when selectorType = "fdr".
        '''
    def setFwe(self, fwe: float) -> ChiSqSelector:
        '''
        set FWE [0.0, 1.0] for feature selection by FWE.
        Only applicable when selectorType = "fwe".
        '''
    def setSelectorType(self, selectorType: str) -> ChiSqSelector:
        '''
        set the selector type of the ChisqSelector.
        Supported options: "numTopFeatures" (default), "percentile", "fpr", "fdr", "fwe".
        '''
    def fit(self, data: RDD[LabeledPoint]) -> ChiSqSelectorModel:
        """
        Returns a ChiSquared feature selector.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD` of :py:class:`pyspark.mllib.regression.LabeledPoint`
            containing the labeled dataset with categorical features.
            Real-valued features will be treated as categorical for each
            distinct value. Apply feature discretizer before using this function.
        """

class PCAModel(JavaVectorTransformer):
    """
    Model fitted by [[PCA]] that can project vectors to a low-dimensional space using PCA.

    .. versionadded:: 1.5.0
    """

class PCA:
    """
    A feature transformer that projects vectors to a low-dimensional space using PCA.

    .. versionadded:: 1.5.0

    Examples
    --------
    >>> data = [Vectors.sparse(5, [(1, 1.0), (3, 7.0)]),
    ...     Vectors.dense([2.0, 0.0, 3.0, 4.0, 5.0]),
    ...     Vectors.dense([4.0, 0.0, 0.0, 6.0, 7.0])]
    >>> model = PCA(2).fit(sc.parallelize(data))
    >>> pcArray = model.transform(Vectors.sparse(5, [(1, 1.0), (3, 7.0)])).toArray()
    >>> pcArray[0]
    1.648...
    >>> pcArray[1]
    -4.013...
    """
    k: Incomplete
    def __init__(self, k: int) -> None:
        """
        Parameters
        ----------
        k : int
            number of principal components.
        """
    def fit(self, data: RDD['VectorLike']) -> PCAModel:
        """
        Computes a [[PCAModel]] that contains the principal components of the input vectors.

        .. versionadded:: 1.5.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            source vectors
        """

class HashingTF:
    '''
    Maps a sequence of terms to their term frequencies using the hashing
    trick.

    .. versionadded:: 1.2.0

    Parameters
    ----------
    numFeatures : int, optional
        number of features (default: 2^20)

    Notes
    -----
    The terms must be hashable (can not be dict/set/list...).

    Examples
    --------
    >>> htf = HashingTF(100)
    >>> doc = "a a b b c d".split(" ")
    >>> htf.transform(doc)
    SparseVector(100, {...})
    '''
    numFeatures: Incomplete
    binary: bool
    def __init__(self, numFeatures: int = ...) -> None: ...
    def setBinary(self, value: bool) -> HashingTF:
        """
        If True, term frequency vector will be binary such that non-zero
        term counts will be set to 1
        (default: False)
        """
    def indexOf(self, term: Hashable) -> int:
        """Returns the index of the input term."""
    @overload
    def transform(self, document: Iterable[Hashable]) -> Vector: ...
    @overload
    def transform(self, document: RDD[Iterable[Hashable]]) -> RDD[Vector]: ...

class IDFModel(JavaVectorTransformer):
    """
    Represents an IDF model that can transform term frequency vectors.

    .. versionadded:: 1.2.0
    """
    @overload
    def transform(self, x: VectorLike) -> Vector: ...
    @overload
    def transform(self, x: RDD['VectorLike']) -> RDD[Vector]: ...
    def idf(self) -> Vector:
        """
        Returns the current IDF vector.
        """
    def docFreq(self) -> List[int]:
        """
        Returns the document frequency.
        """
    def numDocs(self) -> int:
        """
        Returns number of documents evaluated to compute idf
        """

class IDF:
    """
    Inverse document frequency (IDF).

    The standard formulation is used: `idf = log((m + 1) / (d(t) + 1))`,
    where `m` is the total number of documents and `d(t)` is the number
    of documents that contain term `t`.

    This implementation supports filtering out terms which do not appear
    in a minimum number of documents (controlled by the variable
    `minDocFreq`). For terms that are not in at least `minDocFreq`
    documents, the IDF is found as 0, resulting in TF-IDFs of 0.

    .. versionadded:: 1.2.0

    Parameters
    ----------
    minDocFreq : int
        minimum of documents in which a term should appear for filtering

    Examples
    --------
    >>> n = 4
    >>> freqs = [Vectors.sparse(n, (1, 3), (1.0, 2.0)),
    ...          Vectors.dense([0.0, 1.0, 2.0, 3.0]),
    ...          Vectors.sparse(n, [1], [1.0])]
    >>> data = sc.parallelize(freqs)
    >>> idf = IDF()
    >>> model = idf.fit(data)
    >>> tfidf = model.transform(data)
    >>> for r in tfidf.collect(): r
    SparseVector(4, {1: 0.0, 3: 0.5754})
    DenseVector([0.0, 0.0, 1.3863, 0.863])
    SparseVector(4, {1: 0.0})
    >>> model.transform(Vectors.dense([0.0, 1.0, 2.0, 3.0]))
    DenseVector([0.0, 0.0, 1.3863, 0.863])
    >>> model.transform([0.0, 1.0, 2.0, 3.0])
    DenseVector([0.0, 0.0, 1.3863, 0.863])
    >>> model.transform(Vectors.sparse(n, (1, 3), (1.0, 2.0)))
    SparseVector(4, {1: 0.0, 3: 0.5754})
    """
    minDocFreq: Incomplete
    def __init__(self, minDocFreq: int = 0) -> None: ...
    def fit(self, dataset: RDD['VectorLike']) -> IDFModel:
        """
        Computes the inverse document frequency.

        .. versionadded:: 1.2.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.RDD`
            an RDD of term frequency vectors
        """

class Word2VecModel(JavaVectorTransformer, JavaSaveable, JavaLoader['Word2VecModel']):
    """
    class for Word2Vec model
    """
    def transform(self, word: str) -> Vector:
        """
        Transforms a word to its vector representation

        .. versionadded:: 1.2.0

        Parameters
        ----------
        word : str
            a word

        Returns
        -------
        :py:class:`pyspark.mllib.linalg.Vector`
            vector representation of word(s)

        Notes
        -----
        Local use only
        """
    def findSynonyms(self, word: str | VectorLike, num: int) -> Iterable[Tuple[str, float]]:
        """
        Find synonyms of a word

        .. versionadded:: 1.2.0

        Parameters
        ----------

        word : str or  :py:class:`pyspark.mllib.linalg.Vector`
            a word or a vector representation of word
        num : int
            number of synonyms to find

        Returns
        -------
        :py:class:`collections.abc.Iterable`
            array of (word, cosineSimilarity)

        Notes
        -----
        Local use only
        """
    def getVectors(self) -> JavaMap:
        """
        Returns a map of words to their vector representations.
        """
    @classmethod
    def load(cls, sc: SparkContext, path: str) -> Word2VecModel:
        """
        Load a model from the given path.
        """

class Word2Vec:
    '''Word2Vec creates vector representation of words in a text corpus.
    The algorithm first constructs a vocabulary from the corpus
    and then learns vector representation of words in the vocabulary.
    The vector representation can be used as features in
    natural language processing and machine learning algorithms.

    We used skip-gram model in our implementation and hierarchical
    softmax method to train the model. The variable names in the
    implementation matches the original C implementation.

    For original C implementation,
    see https://code.google.com/p/word2vec/
    For research papers, see
    Efficient Estimation of Word Representations in Vector Space
    and Distributed Representations of Words and Phrases and their
    Compositionality.

    .. versionadded:: 1.2.0

    Examples
    --------
    >>> sentence = "a b " * 100 + "a c " * 10
    >>> localDoc = [sentence, sentence]
    >>> doc = sc.parallelize(localDoc).map(lambda line: line.split(" "))
    >>> model = Word2Vec().setVectorSize(10).setSeed(42).fit(doc)

    Querying for synonyms of a word will not return that word:

    >>> syms = model.findSynonyms("a", 2)
    >>> [s[0] for s in syms]
    [\'b\', \'c\']

    But querying for synonyms of a vector may return the word whose
    representation is that vector:

    >>> vec = model.transform("a")
    >>> syms = model.findSynonyms(vec, 2)
    >>> [s[0] for s in syms]
    [\'a\', \'b\']

    >>> import os, tempfile
    >>> path = tempfile.mkdtemp()
    >>> model.save(sc, path)
    >>> sameModel = Word2VecModel.load(sc, path)
    >>> model.transform("a") == sameModel.transform("a")
    True
    >>> syms = sameModel.findSynonyms("a", 2)
    >>> [s[0] for s in syms]
    [\'b\', \'c\']
    >>> from shutil import rmtree
    >>> try:
    ...     rmtree(path)
    ... except OSError:
    ...     pass
    '''
    vectorSize: int
    learningRate: float
    numPartitions: int
    numIterations: int
    seed: Incomplete
    minCount: int
    windowSize: int
    def __init__(self) -> None:
        """
        Construct Word2Vec instance
        """
    def setVectorSize(self, vectorSize: int) -> Word2Vec:
        """
        Sets vector size (default: 100).
        """
    def setLearningRate(self, learningRate: float) -> Word2Vec:
        """
        Sets initial learning rate (default: 0.025).
        """
    def setNumPartitions(self, numPartitions: int) -> Word2Vec:
        """
        Sets number of partitions (default: 1). Use a small number for
        accuracy.
        """
    def setNumIterations(self, numIterations: int) -> Word2Vec:
        """
        Sets number of iterations (default: 1), which should be smaller
        than or equal to number of partitions.
        """
    def setSeed(self, seed: int) -> Word2Vec:
        """
        Sets random seed.
        """
    def setMinCount(self, minCount: int) -> Word2Vec:
        """
        Sets minCount, the minimum number of times a token must appear
        to be included in the word2vec model's vocabulary (default: 5).
        """
    def setWindowSize(self, windowSize: int) -> Word2Vec:
        """
        Sets window size (default: 5).
        """
    def fit(self, data: RDD[List[str]]) -> Word2VecModel:
        """
        Computes the vector representation of each word in vocabulary.

        .. versionadded:: 1.2.0

        Parameters
        ----------
        data : :py:class:`pyspark.RDD`
            training data. RDD of list of string

        Returns
        -------
        :py:class:`Word2VecModel`
        """

class ElementwiseProduct(VectorTransformer):
    """
    Scales each column of the vector, with the supplied weight vector.
    i.e the elementwise product.

    .. versionadded:: 1.5.0

    Examples
    --------
    >>> weight = Vectors.dense([1.0, 2.0, 3.0])
    >>> eprod = ElementwiseProduct(weight)
    >>> a = Vectors.dense([2.0, 1.0, 3.0])
    >>> eprod.transform(a)
    DenseVector([2.0, 2.0, 9.0])
    >>> b = Vectors.dense([9.0, 3.0, 4.0])
    >>> rdd = sc.parallelize([a, b])
    >>> eprod.transform(rdd).collect()
    [DenseVector([2.0, 2.0, 9.0]), DenseVector([9.0, 6.0, 12.0])]
    """
    scalingVector: Incomplete
    def __init__(self, scalingVector: Vector) -> None: ...
    @overload
    def transform(self, vector: VectorLike) -> Vector: ...
    @overload
    def transform(self, vector: RDD['VectorLike']) -> RDD[Vector]: ...
