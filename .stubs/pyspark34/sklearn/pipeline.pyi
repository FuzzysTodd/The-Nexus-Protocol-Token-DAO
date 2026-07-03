from .base import TransformerMixin
from .utils.metaestimators import _BaseComposition
from _typeshed import Incomplete

__all__ = ['Pipeline', 'FeatureUnion', 'make_pipeline', 'make_union']

class Pipeline(_BaseComposition):
    """
    Pipeline of transforms with a final estimator.

    Sequentially apply a list of transforms and a final estimator.
    Intermediate steps of the pipeline must be 'transforms', that is, they
    must implement `fit` and `transform` methods.
    The final estimator only needs to implement `fit`.
    The transformers in the pipeline can be cached using ``memory`` argument.

    The purpose of the pipeline is to assemble several steps that can be
    cross-validated together while setting different parameters. For this, it
    enables setting parameters of the various steps using their names and the
    parameter name separated by a `'__'`, as in the example below. A step's
    estimator may be replaced entirely by setting the parameter with its name
    to another estimator, or a transformer removed by setting it to
    `'passthrough'` or `None`.

    Read more in the :ref:`User Guide <pipeline>`.

    .. versionadded:: 0.5

    Parameters
    ----------
    steps : list of tuple
        List of (name, transform) tuples (implementing `fit`/`transform`) that
        are chained in sequential order. The last transform must be an
        estimator.

    memory : str or object with the joblib.Memory interface, default=None
        Used to cache the fitted transformers of the pipeline. The last step
        will never be cached, even if it is a transformer. By default, no
        caching is performed. If a string is given, it is the path to the
        caching directory. Enabling caching triggers a clone of the transformers
        before fitting. Therefore, the transformer instance given to the
        pipeline cannot be inspected directly. Use the attribute ``named_steps``
        or ``steps`` to inspect estimators within the pipeline. Caching the
        transformers is advantageous when fitting is time consuming.

    verbose : bool, default=False
        If True, the time elapsed while fitting each step will be printed as it
        is completed.

    Attributes
    ----------
    named_steps : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.
        Read-only attribute to access any step parameter by user given name.
        Keys are step names and values are steps parameters.

    classes_ : ndarray of shape (n_classes,)
        The classes labels. Only exist if the last step of the pipeline is a
        classifier.

    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying first estimator in `steps` exposes such an attribute
        when fit.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 1.0

    See Also
    --------
    make_pipeline : Convenience function for simplified pipeline construction.

    Examples
    --------
    >>> from sklearn.svm import SVC
    >>> from sklearn.preprocessing import StandardScaler
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.pipeline import Pipeline
    >>> X, y = make_classification(random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y,
    ...                                                     random_state=0)
    >>> pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
    >>> # The pipeline can be used as any other estimator
    >>> # and avoids leaking the test set into the train set
    >>> pipe.fit(X_train, y_train)
    Pipeline(steps=[('scaler', StandardScaler()), ('svc', SVC())])
    >>> pipe.score(X_test, y_test)
    0.88
    """
    steps: Incomplete
    memory: Incomplete
    verbose: Incomplete
    def __init__(self, steps, *, memory: Incomplete | None = None, verbose: bool = False) -> None: ...
    def set_output(self, *, transform: Incomplete | None = None):
        '''Set the output container when `"transform"` and `"fit_transform"` are called.

        Calling `set_output` will set the output of all estimators in `steps`.

        Parameters
        ----------
        transform : {"default", "pandas"}, default=None
            Configure output of `transform` and `fit_transform`.

            - `"default"`: Default output format of a transformer
            - `"pandas"`: DataFrame output
            - `None`: Transform configuration is unchanged

        Returns
        -------
        self : estimator instance
            Estimator instance.
        '''
    def get_params(self, deep: bool = True):
        """Get parameters for this estimator.

        Returns the parameters given in the constructor as well as the
        estimators contained within the `steps` of the `Pipeline`.

        Parameters
        ----------
        deep : bool, default=True
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : mapping of string to any
            Parameter names mapped to their values.
        """
    def set_params(self, **kwargs):
        """Set the parameters of this estimator.

        Valid parameter keys can be listed with ``get_params()``. Note that
        you can directly set the parameters of the estimators contained in
        `steps`.

        Parameters
        ----------
        **kwargs : dict
            Parameters of this estimator or parameters of estimators contained
            in `steps`. Parameters of the steps may be set using its name and
            the parameter name separated by a '__'.

        Returns
        -------
        self : object
            Pipeline class instance.
        """
    def __len__(self) -> int:
        """
        Returns the length of the Pipeline
        """
    def __getitem__(self, ind):
        """Returns a sub-pipeline or a single estimator in the pipeline

        Indexing with an integer will return an estimator; using a slice
        returns another Pipeline instance which copies a slice of this
        Pipeline. This copy is shallow: modifying (or fitting) estimators in
        the sub-pipeline will affect the larger pipeline and vice-versa.
        However, replacing a value in `step` will not affect a copy.
        """
    @property
    def named_steps(self):
        """Access the steps by name.

        Read-only attribute to access any step by given name.
        Keys are steps names and values are the steps objects."""
    def fit(self, X, y: Incomplete | None = None, **fit_params):
        """Fit the model.

        Fit all the transformers one after the other and transform the
        data. Finally, fit the transformed data using the final estimator.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of the
            pipeline.

        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps of
            the pipeline.

        **fit_params : dict of string -> object
            Parameters passed to the ``fit`` method of each step, where
            each parameter name is prefixed such that parameter ``p`` for step
            ``s`` has key ``s__p``.

        Returns
        -------
        self : object
            Pipeline with fitted steps.
        """
    def fit_transform(self, X, y: Incomplete | None = None, **fit_params):
        """Fit the model and transform with the final estimator.

        Fits all the transformers one after the other and transform the
        data. Then uses `fit_transform` on transformed data with the final
        estimator.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of the
            pipeline.

        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps of
            the pipeline.

        **fit_params : dict of string -> object
            Parameters passed to the ``fit`` method of each step, where
            each parameter name is prefixed such that parameter ``p`` for step
            ``s`` has key ``s__p``.

        Returns
        -------
        Xt : ndarray of shape (n_samples, n_transformed_features)
            Transformed samples.
        """
    def predict(self, X, **predict_params):
        """Transform the data, and apply `predict` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls `predict`
        method. Only valid if the final estimator implements `predict`.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.

        **predict_params : dict of string -> object
            Parameters to the ``predict`` called at the end of all
            transformations in the pipeline. Note that while this may be
            used to return uncertainties from some models with return_std
            or return_cov, uncertainties that are generated by the
            transformations in the pipeline are not propagated to the
            final estimator.

            .. versionadded:: 0.20

        Returns
        -------
        y_pred : ndarray
            Result of calling `predict` on the final estimator.
        """
    def fit_predict(self, X, y: Incomplete | None = None, **fit_params):
        """Transform the data, and apply `fit_predict` with the final estimator.

        Call `fit_transform` of each transformer in the pipeline. The
        transformed data are finally passed to the final estimator that calls
        `fit_predict` method. Only valid if the final estimator implements
        `fit_predict`.

        Parameters
        ----------
        X : iterable
            Training data. Must fulfill input requirements of first step of
            the pipeline.

        y : iterable, default=None
            Training targets. Must fulfill label requirements for all steps
            of the pipeline.

        **fit_params : dict of string -> object
            Parameters passed to the ``fit`` method of each step, where
            each parameter name is prefixed such that parameter ``p`` for step
            ``s`` has key ``s__p``.

        Returns
        -------
        y_pred : ndarray
            Result of calling `fit_predict` on the final estimator.
        """
    def predict_proba(self, X, **predict_proba_params):
        """Transform the data, and apply `predict_proba` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls
        `predict_proba` method. Only valid if the final estimator implements
        `predict_proba`.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.

        **predict_proba_params : dict of string -> object
            Parameters to the `predict_proba` called at the end of all
            transformations in the pipeline.

        Returns
        -------
        y_proba : ndarray of shape (n_samples, n_classes)
            Result of calling `predict_proba` on the final estimator.
        """
    def decision_function(self, X):
        """Transform the data, and apply `decision_function` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls
        `decision_function` method. Only valid if the final estimator
        implements `decision_function`.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.

        Returns
        -------
        y_score : ndarray of shape (n_samples, n_classes)
            Result of calling `decision_function` on the final estimator.
        """
    def score_samples(self, X):
        """Transform the data, and apply `score_samples` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls
        `score_samples` method. Only valid if the final estimator implements
        `score_samples`.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.

        Returns
        -------
        y_score : ndarray of shape (n_samples,)
            Result of calling `score_samples` on the final estimator.
        """
    def predict_log_proba(self, X, **predict_log_proba_params):
        """Transform the data, and apply `predict_log_proba` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls
        `predict_log_proba` method. Only valid if the final estimator
        implements `predict_log_proba`.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.

        **predict_log_proba_params : dict of string -> object
            Parameters to the ``predict_log_proba`` called at the end of all
            transformations in the pipeline.

        Returns
        -------
        y_log_proba : ndarray of shape (n_samples, n_classes)
            Result of calling `predict_log_proba` on the final estimator.
        """
    def transform(self, X):
        """Transform the data, and apply `transform` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls
        `transform` method. Only valid if the final estimator
        implements `transform`.

        This also works where final estimator is `None` in which case all prior
        transformations are applied.

        Parameters
        ----------
        X : iterable
            Data to transform. Must fulfill input requirements of first step
            of the pipeline.

        Returns
        -------
        Xt : ndarray of shape (n_samples, n_transformed_features)
            Transformed data.
        """
    def inverse_transform(self, Xt):
        """Apply `inverse_transform` for each step in a reverse order.

        All estimators in the pipeline must support `inverse_transform`.

        Parameters
        ----------
        Xt : array-like of shape (n_samples, n_transformed_features)
            Data samples, where ``n_samples`` is the number of samples and
            ``n_features`` is the number of features. Must fulfill
            input requirements of last step of pipeline's
            ``inverse_transform`` method.

        Returns
        -------
        Xt : ndarray of shape (n_samples, n_features)
            Inverse transformed data, that is, data in the original feature
            space.
        """
    def score(self, X, y: Incomplete | None = None, sample_weight: Incomplete | None = None):
        """Transform the data, and apply `score` with the final estimator.

        Call `transform` of each transformer in the pipeline. The transformed
        data are finally passed to the final estimator that calls
        `score` method. Only valid if the final estimator implements `score`.

        Parameters
        ----------
        X : iterable
            Data to predict on. Must fulfill input requirements of first step
            of the pipeline.

        y : iterable, default=None
            Targets used for scoring. Must fulfill label requirements for all
            steps of the pipeline.

        sample_weight : array-like, default=None
            If not None, this argument is passed as ``sample_weight`` keyword
            argument to the ``score`` method of the final estimator.

        Returns
        -------
        score : float
            Result of calling `score` on the final estimator.
        """
    @property
    def classes_(self):
        """The classes labels. Only exist if the last step is a classifier."""
    def get_feature_names_out(self, input_features: Incomplete | None = None):
        """Get output feature names for transformation.

        Transform input features using the pipeline.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Input features.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Transformed feature names.
        """
    @property
    def n_features_in_(self):
        """Number of features seen during first step `fit` method."""
    @property
    def feature_names_in_(self):
        """Names of features seen during first step `fit` method."""
    def __sklearn_is_fitted__(self):
        """Indicate whether pipeline has been fit."""

def make_pipeline(*steps, memory: Incomplete | None = None, verbose: bool = False):
    """Construct a :class:`Pipeline` from the given estimators.

    This is a shorthand for the :class:`Pipeline` constructor; it does not
    require, and does not permit, naming the estimators. Instead, their names
    will be set to the lowercase of their types automatically.

    Parameters
    ----------
    *steps : list of Estimator objects
        List of the scikit-learn estimators that are chained together.

    memory : str or object with the joblib.Memory interface, default=None
        Used to cache the fitted transformers of the pipeline. The last step
        will never be cached, even if it is a transformer. By default, no
        caching is performed. If a string is given, it is the path to the
        caching directory. Enabling caching triggers a clone of the transformers
        before fitting. Therefore, the transformer instance given to the
        pipeline cannot be inspected directly. Use the attribute ``named_steps``
        or ``steps`` to inspect estimators within the pipeline. Caching the
        transformers is advantageous when fitting is time consuming.

    verbose : bool, default=False
        If True, the time elapsed while fitting each step will be printed as it
        is completed.

    Returns
    -------
    p : Pipeline
        Returns a scikit-learn :class:`Pipeline` object.

    See Also
    --------
    Pipeline : Class for creating a pipeline of transforms with a final
        estimator.

    Examples
    --------
    >>> from sklearn.naive_bayes import GaussianNB
    >>> from sklearn.preprocessing import StandardScaler
    >>> from sklearn.pipeline import make_pipeline
    >>> make_pipeline(StandardScaler(), GaussianNB(priors=None))
    Pipeline(steps=[('standardscaler', StandardScaler()),
                    ('gaussiannb', GaussianNB())])
    """

class FeatureUnion(TransformerMixin, _BaseComposition):
    '''Concatenates results of multiple transformer objects.

    This estimator applies a list of transformer objects in parallel to the
    input data, then concatenates the results. This is useful to combine
    several feature extraction mechanisms into a single transformer.

    Parameters of the transformers may be set using its name and the parameter
    name separated by a \'__\'. A transformer may be replaced entirely by
    setting the parameter with its name to another transformer, removed by
    setting to \'drop\' or disabled by setting to \'passthrough\' (features are
    passed without transformation).

    Read more in the :ref:`User Guide <feature_union>`.

    .. versionadded:: 0.13

    Parameters
    ----------
    transformer_list : list of (str, transformer) tuples
        List of transformer objects to be applied to the data. The first
        half of each tuple is the name of the transformer. The transformer can
        be \'drop\' for it to be ignored or can be \'passthrough\' for features to
        be passed unchanged.

        .. versionadded:: 1.1
           Added the option `"passthrough"`.

        .. versionchanged:: 0.22
           Deprecated `None` as a transformer in favor of \'drop\'.

    n_jobs : int, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

        .. versionchanged:: v0.20
           `n_jobs` default changed from 1 to None

    transformer_weights : dict, default=None
        Multiplicative weights for features per transformer.
        Keys are transformer names, values the weights.
        Raises ValueError if key not present in ``transformer_list``.

    verbose : bool, default=False
        If True, the time elapsed while fitting each transformer will be
        printed as it is completed.

    Attributes
    ----------
    named_transformers : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.
        Read-only attribute to access any transformer parameter by user
        given name. Keys are transformer names and values are
        transformer parameters.

        .. versionadded:: 1.2

    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying first transformer in `transformer_list` exposes such an
        attribute when fit.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when
        `X` has feature names that are all strings.

        .. versionadded:: 1.3

    See Also
    --------
    make_union : Convenience function for simplified feature union
        construction.

    Examples
    --------
    >>> from sklearn.pipeline import FeatureUnion
    >>> from sklearn.decomposition import PCA, TruncatedSVD
    >>> union = FeatureUnion([("pca", PCA(n_components=1)),
    ...                       ("svd", TruncatedSVD(n_components=2))])
    >>> X = [[0., 1., 3], [2., 2., 5]]
    >>> union.fit_transform(X)
    array([[ 1.5       ,  3.0...,  0.8...],
           [-1.5       ,  5.7..., -0.4...]])
    '''
    transformer_list: Incomplete
    n_jobs: Incomplete
    transformer_weights: Incomplete
    verbose: Incomplete
    def __init__(self, transformer_list, *, n_jobs: Incomplete | None = None, transformer_weights: Incomplete | None = None, verbose: bool = False) -> None: ...
    def set_output(self, *, transform: Incomplete | None = None):
        '''Set the output container when `"transform"` and `"fit_transform"` are called.

        `set_output` will set the output of all estimators in `transformer_list`.

        Parameters
        ----------
        transform : {"default", "pandas"}, default=None
            Configure output of `transform` and `fit_transform`.

            - `"default"`: Default output format of a transformer
            - `"pandas"`: DataFrame output
            - `None`: Transform configuration is unchanged

        Returns
        -------
        self : estimator instance
            Estimator instance.
        '''
    @property
    def named_transformers(self): ...
    def get_params(self, deep: bool = True):
        """Get parameters for this estimator.

        Returns the parameters given in the constructor as well as the
        estimators contained within the `transformer_list` of the
        `FeatureUnion`.

        Parameters
        ----------
        deep : bool, default=True
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : mapping of string to any
            Parameter names mapped to their values.
        """
    def set_params(self, **kwargs):
        """Set the parameters of this estimator.

        Valid parameter keys can be listed with ``get_params()``. Note that
        you can directly set the parameters of the estimators contained in
        `transformer_list`.

        Parameters
        ----------
        **kwargs : dict
            Parameters of this estimator or parameters of estimators contained
            in `transform_list`. Parameters of the transformers may be set
            using its name and the parameter name separated by a '__'.

        Returns
        -------
        self : object
            FeatureUnion class instance.
        """
    def get_feature_names_out(self, input_features: Incomplete | None = None):
        """Get output feature names for transformation.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Input features.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Transformed feature names.
        """
    def fit(self, X, y: Incomplete | None = None, **fit_params):
        """Fit all transformers using X.

        Parameters
        ----------
        X : iterable or array-like, depending on transformers
            Input data, used to fit transformers.

        y : array-like of shape (n_samples, n_outputs), default=None
            Targets for supervised learning.

        **fit_params : dict, default=None
            Parameters to pass to the fit method of the estimator.

        Returns
        -------
        self : object
            FeatureUnion class instance.
        """
    def fit_transform(self, X, y: Incomplete | None = None, **fit_params):
        """Fit all transformers, transform the data and concatenate results.

        Parameters
        ----------
        X : iterable or array-like, depending on transformers
            Input data to be transformed.

        y : array-like of shape (n_samples, n_outputs), default=None
            Targets for supervised learning.

        **fit_params : dict, default=None
            Parameters to pass to the fit method of the estimator.

        Returns
        -------
        X_t : array-like or sparse matrix of                 shape (n_samples, sum_n_components)
            The `hstack` of results of transformers. `sum_n_components` is the
            sum of `n_components` (output dimension) over transformers.
        """
    def transform(self, X):
        """Transform X separately by each transformer, concatenate results.

        Parameters
        ----------
        X : iterable or array-like, depending on transformers
            Input data to be transformed.

        Returns
        -------
        X_t : array-like or sparse matrix of                 shape (n_samples, sum_n_components)
            The `hstack` of results of transformers. `sum_n_components` is the
            sum of `n_components` (output dimension) over transformers.
        """
    @property
    def n_features_in_(self):
        """Number of features seen during :term:`fit`."""
    @property
    def feature_names_in_(self):
        """Names of features seen during :term:`fit`."""
    def __sklearn_is_fitted__(self): ...
    def __getitem__(self, name):
        """Return transformer with name."""

def make_union(*transformers, n_jobs: Incomplete | None = None, verbose: bool = False):
    """Construct a FeatureUnion from the given transformers.

    This is a shorthand for the FeatureUnion constructor; it does not require,
    and does not permit, naming the transformers. Instead, they will be given
    names automatically based on their types. It also does not allow weighting.

    Parameters
    ----------
    *transformers : list of estimators
        One or more estimators.

    n_jobs : int, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

        .. versionchanged:: v0.20
           `n_jobs` default changed from 1 to None.

    verbose : bool, default=False
        If True, the time elapsed while fitting each transformer will be
        printed as it is completed.

    Returns
    -------
    f : FeatureUnion
        A :class:`FeatureUnion` object for concatenating the results of multiple
        transformer objects.

    See Also
    --------
    FeatureUnion : Class for concatenating the results of multiple transformer
        objects.

    Examples
    --------
    >>> from sklearn.decomposition import PCA, TruncatedSVD
    >>> from sklearn.pipeline import make_union
    >>> make_union(PCA(), TruncatedSVD())
     FeatureUnion(transformer_list=[('pca', PCA()),
                                   ('truncatedsvd', TruncatedSVD())])
    """
