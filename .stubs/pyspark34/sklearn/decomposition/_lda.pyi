from ..base import BaseEstimator as BaseEstimator, ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin, TransformerMixin as TransformerMixin
from ..utils import check_random_state as check_random_state, gen_batches as gen_batches, gen_even_slices as gen_even_slices
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted, check_non_negative as check_non_negative
from _typeshed import Incomplete

EPS: Incomplete

class LatentDirichletAllocation(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    '''Latent Dirichlet Allocation with online variational Bayes algorithm.

    The implementation is based on [1]_ and [2]_.

    .. versionadded:: 0.17

    Read more in the :ref:`User Guide <LatentDirichletAllocation>`.

    Parameters
    ----------
    n_components : int, default=10
        Number of topics.

        .. versionchanged:: 0.19
            ``n_topics`` was renamed to ``n_components``

    doc_topic_prior : float, default=None
        Prior of document topic distribution `theta`. If the value is None,
        defaults to `1 / n_components`.
        In [1]_, this is called `alpha`.

    topic_word_prior : float, default=None
        Prior of topic word distribution `beta`. If the value is None, defaults
        to `1 / n_components`.
        In [1]_, this is called `eta`.

    learning_method : {\'batch\', \'online\'}, default=\'batch\'
        Method used to update `_component`. Only used in :meth:`fit` method.
        In general, if the data size is large, the online update will be much
        faster than the batch update.

        Valid options::

            \'batch\': Batch variational Bayes method. Use all training data in
                each EM update.
                Old `components_` will be overwritten in each iteration.
            \'online\': Online variational Bayes method. In each EM update, use
                mini-batch of training data to update the ``components_``
                variable incrementally. The learning rate is controlled by the
                ``learning_decay`` and the ``learning_offset`` parameters.

        .. versionchanged:: 0.20
            The default learning method is now ``"batch"``.

    learning_decay : float, default=0.7
        It is a parameter that control learning rate in the online learning
        method. The value should be set between (0.5, 1.0] to guarantee
        asymptotic convergence. When the value is 0.0 and batch_size is
        ``n_samples``, the update method is same as batch learning. In the
        literature, this is called kappa.

    learning_offset : float, default=10.0
        A (positive) parameter that downweights early iterations in online
        learning.  It should be greater than 1.0. In the literature, this is
        called tau_0.

    max_iter : int, default=10
        The maximum number of passes over the training data (aka epochs).
        It only impacts the behavior in the :meth:`fit` method, and not the
        :meth:`partial_fit` method.

    batch_size : int, default=128
        Number of documents to use in each EM iteration. Only used in online
        learning.

    evaluate_every : int, default=-1
        How often to evaluate perplexity. Only used in `fit` method.
        set it to 0 or negative number to not evaluate perplexity in
        training at all. Evaluating perplexity can help you check convergence
        in training process, but it will also increase total training time.
        Evaluating perplexity in every iteration might increase training time
        up to two-fold.

    total_samples : int, default=1e6
        Total number of documents. Only used in the :meth:`partial_fit` method.

    perp_tol : float, default=1e-1
        Perplexity tolerance in batch learning. Only used when
        ``evaluate_every`` is greater than 0.

    mean_change_tol : float, default=1e-3
        Stopping tolerance for updating document topic distribution in E-step.

    max_doc_update_iter : int, default=100
        Max number of iterations for updating document topic distribution in
        the E-step.

    n_jobs : int, default=None
        The number of jobs to use in the E-step.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    verbose : int, default=0
        Verbosity level.

    random_state : int, RandomState instance or None, default=None
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Variational parameters for topic word distribution. Since the complete
        conditional for topic word distribution is a Dirichlet,
        ``components_[i, j]`` can be viewed as pseudocount that represents the
        number of times word `j` was assigned to topic `i`.
        It can also be viewed as distribution over the words for each topic
        after normalization:
        ``model.components_ / model.components_.sum(axis=1)[:, np.newaxis]``.

    exp_dirichlet_component_ : ndarray of shape (n_components, n_features)
        Exponential value of expectation of log topic word distribution.
        In the literature, this is `exp(E[log(beta)])`.

    n_batch_iter_ : int
        Number of iterations of the EM step.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        Number of passes over the dataset.

    bound_ : float
        Final perplexity score on training set.

    doc_topic_prior_ : float
        Prior of document topic distribution `theta`. If the value is None,
        it is `1 / n_components`.

    random_state_ : RandomState instance
        RandomState instance that is generated either from a seed, the random
        number generator or by `np.random`.

    topic_word_prior_ : float
        Prior of topic word distribution `beta`. If the value is None, it is
        `1 / n_components`.

    See Also
    --------
    sklearn.discriminant_analysis.LinearDiscriminantAnalysis:
        A classifier with a linear decision boundary, generated by fitting
        class conditional densities to the data and using Bayes\' rule.

    References
    ----------
    .. [1] "Online Learning for Latent Dirichlet Allocation", Matthew D.
           Hoffman, David M. Blei, Francis Bach, 2010
           https://github.com/blei-lab/onlineldavb

    .. [2] "Stochastic Variational Inference", Matthew D. Hoffman,
           David M. Blei, Chong Wang, John Paisley, 2013

    Examples
    --------
    >>> from sklearn.decomposition import LatentDirichletAllocation
    >>> from sklearn.datasets import make_multilabel_classification
    >>> # This produces a feature matrix of token counts, similar to what
    >>> # CountVectorizer would produce on text.
    >>> X, _ = make_multilabel_classification(random_state=0)
    >>> lda = LatentDirichletAllocation(n_components=5,
    ...     random_state=0)
    >>> lda.fit(X)
    LatentDirichletAllocation(...)
    >>> # get topics for some given samples:
    >>> lda.transform(X[-2:])
    array([[0.00360392, 0.25499205, 0.0036211 , 0.64236448, 0.09541846],
           [0.15297572, 0.00362644, 0.44412786, 0.39568399, 0.003586  ]])
    '''
    n_components: Incomplete
    doc_topic_prior: Incomplete
    topic_word_prior: Incomplete
    learning_method: Incomplete
    learning_decay: Incomplete
    learning_offset: Incomplete
    max_iter: Incomplete
    batch_size: Incomplete
    evaluate_every: Incomplete
    total_samples: Incomplete
    perp_tol: Incomplete
    mean_change_tol: Incomplete
    max_doc_update_iter: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(self, n_components: int = 10, *, doc_topic_prior: Incomplete | None = None, topic_word_prior: Incomplete | None = None, learning_method: str = 'batch', learning_decay: float = 0.7, learning_offset: float = 10.0, max_iter: int = 10, batch_size: int = 128, evaluate_every: int = -1, total_samples: float = 1000000.0, perp_tol: float = 0.1, mean_change_tol: float = 0.001, max_doc_update_iter: int = 100, n_jobs: Incomplete | None = None, verbose: int = 0, random_state: Incomplete | None = None) -> None: ...
    def partial_fit(self, X, y: Incomplete | None = None):
        """Online VB with Mini-Batch update.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Document word matrix.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        self
            Partially fitted estimator.
        """
    bound_: Incomplete
    def fit(self, X, y: Incomplete | None = None):
        """Learn model for the data X with variational Bayes method.

        When `learning_method` is 'online', use mini-batch update.
        Otherwise, use batch update.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Document word matrix.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        self
            Fitted estimator.
        """
    def transform(self, X):
        """Transform data X according to the fitted model.

           .. versionchanged:: 0.18
              *doc_topic_distr* is now normalized

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Document word matrix.

        Returns
        -------
        doc_topic_distr : ndarray of shape (n_samples, n_components)
            Document topic distribution for X.
        """
    def score(self, X, y: Incomplete | None = None):
        """Calculate approximate log-likelihood as score.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Document word matrix.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        score : float
            Use approximate bound as score.
        """
    def perplexity(self, X, sub_sampling: bool = False):
        """Calculate approximate perplexity for data X.

        Perplexity is defined as exp(-1. * log-likelihood per word)

        .. versionchanged:: 0.19
           *doc_topic_distr* argument has been deprecated and is ignored
           because user no longer has access to unnormalized distribution

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Document word matrix.

        sub_sampling : bool
            Do sub-sampling or not.

        Returns
        -------
        score : float
            Perplexity score.
        """
