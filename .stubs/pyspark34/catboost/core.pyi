from .metrics import BuiltinMetric as BuiltinMetric
from .plot_helpers import OfflineMetricVisualizer as OfflineMetricVisualizer, save_plot_file as save_plot_file, try_plot_offline as try_plot_offline
from _typeshed import Incomplete
from collections.abc import Generator
from enum import Enum

class DataFrame: ...
class Series: ...

CatBoostError: Incomplete
is_classification_objective: Incomplete
is_cv_stratified_objective: Incomplete
is_regression_objective: Incomplete
is_multiregression_objective: Incomplete
is_multitarget_objective: Incomplete
is_survivalregression_objective: Incomplete
is_groupwise_metric: Incomplete
is_ranking_metric: Incomplete
is_maximizable_metric: Incomplete
is_minimizable_metric: Incomplete
FeaturesData: Incomplete
SPARSE_MATRIX_TYPES: Incomplete
MultiTargetCustomMetric: Incomplete
MultiTargetCustomObjective: Incomplete
MultiRegressionCustomMetric: Incomplete
MultiRegressionCustomObjective: Incomplete
fspath: Incomplete
logger: Incomplete
INTEGER_TYPES: Incomplete
FLOAT_TYPES: Incomplete
STRING_TYPES: Incomplete
ARRAY_TYPES: Incomplete
PATH_TYPES: Incomplete

class _StreamLikeWrapper:
    callable_object: Incomplete
    def __init__(self, callable_object) -> None: ...
    def write(self, message) -> None: ...

catboost_logger_lock: Incomplete

def log_fixup(log_cout=..., log_cerr=...) -> Generator[None, None, None]: ...
def metric_description_or_str_to_str(description): ...
def enum_from_enum_or_str(enum_type, arg): ...

class EFstrType(Enum):
    """Calculate score for every feature by values change."""
    PredictionValuesChange: int
    LossFunctionChange: int
    FeatureImportance: int
    Interaction: int
    ShapValues: int
    PredictionDiff: int
    ShapInteractionValues: int
    SageValues: int

class EShapCalcType(Enum):
    """Calculate regular SHAP values"""
    Regular: str
    Approximate: str
    Exact: str

class EFeaturesSelectionAlgorithm(Enum):
    """Use prediction values change as feature strength, eliminate batch of features at once"""
    RecursiveByPredictionValuesChange: str
    RecursiveByLossFunctionChange: str
    RecursiveByShapValues: str

class EFeaturesSelectionGrouping(Enum):
    """Select individual features"""
    Individual: str
    ByTags: str

def plot_features_selection_loss_graph(title, entities_name, entities_name_in_fields, eliminated_entities_indices, eliminated_entities_names, loss_graph, cost_graph: Incomplete | None = None): ...
def plot_features_selection_loss_graphs(summary): ...

class Pool(_PoolBase):
    """
    Pool used in CatBoost as a data structure to train model from.
    """
    def __init__(self, data, label: Incomplete | None = None, cat_features: Incomplete | None = None, text_features: Incomplete | None = None, embedding_features: Incomplete | None = None, embedding_features_data: Incomplete | None = None, column_description: Incomplete | None = None, pairs: Incomplete | None = None, delimiter: str = '\t', has_header: bool = False, ignore_csv_quoting: bool = False, weight: Incomplete | None = None, group_id: Incomplete | None = None, group_weight: Incomplete | None = None, subgroup_id: Incomplete | None = None, pairs_weight: Incomplete | None = None, baseline: Incomplete | None = None, timestamp: Incomplete | None = None, feature_names: Incomplete | None = None, feature_tags: Incomplete | None = None, thread_count: int = -1, log_cout=..., log_cerr=...) -> None:
        '''
        Pool is an internal data structure that is used by CatBoost.
        You can construct Pool from list, numpy.ndarray, pandas.DataFrame, pandas.Series.

        Parameters
        ----------
        data : list or numpy.ndarray or pandas.DataFrame or pandas.Series or FeaturesData or string or pathlib.Path
            Data source of Pool.
            If list or numpy.ndarrays or pandas.DataFrame or pandas.Series, giving 2 dimensional array like data.
            If FeaturesData - see FeaturesData description for details, \'cat_features\' and \'feature_names\'
              parameters must be equal to None in this case
            If string or pathlib.Path, giving the path to the file with data in catboost format.
              If string starts with "quantized://", the file has to contain quantized dataset saved with Pool.save().

        label : list or numpy.ndarrays or pandas.DataFrame or pandas.Series, optional (default=None)
            Label of the training data.
            If not None, giving 1 or 2 dimensional array like data with floats.
            If data is a file, then label must be in the file, that is label must be equals to None

        cat_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Categ features indices or names.
            If it contains feature names, Pool\'s feature names must be defined: either by passing \'feature_names\'
              parameter or if data is pandas.DataFrame (feature names are initialized from it\'s column names)
            Must be None if \'data\' parameter has FeaturesData type

        text_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Text features indices or names.
            If it contains feature names, Pool\'s feature names must be defined: either by passing \'feature_names\'
              parameter or if data is pandas.DataFrame (feature names are initialized from it\'s column names)
            Must be None if \'data\' parameter has FeaturesData type

        embedding_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Embedding features indices or names.
            If it contains feature names, Pool\'s feature names must be defined: either by passing \'feature_names\'
              parameter or if data is pandas.DataFrame (feature names are initialized from it\'s column names)
            Must be None if \'data\' parameter has FeaturesData type

        embedding_features_data : list or dict, optional (default=None)
            If not None, giving the data of Embedding features (instead of data in main \'data\' parameter).
            If list - list containing 2d arrays (lists or numpy.ndarrays or scipy.sparse.spmatrix) with [n_data_size x embedding_size] elements
            If dict - dict containing 2d arrays (lists or numpy.ndarrays or scipy.sparse.spmatrix) with [n_data_size x embedding_size] elements
                Dict keys must be the same as specified in \'embedding_features\' parameter

        column_description : string or pathlib.Path, optional (default=None)
            ColumnsDescription parameter.
            There are several columns description types: Label, Categ, Num, Auxiliary, DocId, Weight, Baseline, GroupId, Timestamp.
            All columns are Num as default, it\'s not necessary to specify
            this type of columns. Default Label column index is 0 (zero).
            If None, Label column is 0 (zero) as default, all data columns are Num as default.
            If string or pathlib.Path, giving the path to the file with ColumnsDescription in column_description format.

        pairs : list or numpy.ndarray or pandas.DataFrame or string or pathlib.Path
            The pairs description.
            If list or numpy.ndarrays or pandas.DataFrame, giving 2 dimensional.
            The shape should be Nx2, where N is the pairs\' count. The first element of the pair is
            the index of winner object in the training set. The second element of the pair is
            the index of loser object in the training set.
            If string or pathlib.Path, giving the path to the file with pairs description.

        delimiter : string, optional (default=\'\t\')
            Delimiter to use for separate features in file.
            Should be only one symbol, otherwise would be taken only the first character of the string.

        has_header : bool optional (default=False)
            If True, read column names from first line.

        ignore_csv_quoting : bool optional (default=False)
            If True ignore quoting \'"\'.

        weight : list or numpy.ndarray, optional (default=None)
            Weight for each instance.
            If not None, giving 1 dimensional array like data.

        group_id : list or numpy.ndarray, optional (default=None)
            group id for each instance.
            If not None, giving 1 dimensional array like data.

        group_weight : list or numpy.ndarray, optional (default=None)
            Group weight for each instance.
            If not None, giving 1 dimensional array like data.

        subgroup_id : list or numpy.ndarray, optional (default=None)
            subgroup id for each instance.
            If not None, giving 1 dimensional array like data.

        pairs_weight : list or numpy.ndarray, optional (default=None)
            Weight for each pair.
            If not None, giving 1 dimensional array like pairs.

        baseline : list or numpy.ndarray, optional (default=None)
            Baseline for each instance.
            If not None, giving 2 dimensional array like data.

        timestamp: list or numpy.ndarray, optional (default=None)
            Timestamp for each instance.
            Should be a non-negative integer.
            Useful for sorting a learning dataset by this field during training.

        feature_names : list or string or pathlib.Path, optional (default=None)
            If list - list of names for each given data_feature.
            If string or pathlib.Path - path with scheme for feature names data to load.
            If this parameter is None and \'data\' is pandas.DataFrame feature names will be initialized
              from DataFrame\'s column names.
            Must be None if \'data\' parameter has FeaturesData type

        feature_tags : json, optional (default=None)
            Format:
            {\'tag1\':
                {
                    \'features\': [<ids or names of features>],
                    \'cost\': <positive integer>
                }
             \'tag2\':
                {
                 ...
                }
            ...
            }

        thread_count : int, optional (default=-1)
            Thread count for data processing.
            If -1, then the number of threads is set to the number of CPU cores.

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        '''
    def slice(self, rindex): ...
    def train_eval_split(self, has_time, is_classification, eval_fraction, save_eval_pool): ...
    def set_pairs(self, pairs): ...
    def set_feature_names(self, feature_names): ...
    def set_baseline(self, baseline): ...
    def set_weight(self, weight): ...
    def set_group_id(self, group_id): ...
    def set_group_weight(self, group_weight): ...
    def set_subgroup_id(self, subgroup_id): ...
    def set_pairs_weight(self, pairs_weight): ...
    def set_timestamp(self, timestamp): ...
    def save(self, fname) -> None:
        """
        Save the quantized pool to a file.

        Parameters
        ----------
        fname : string or pathlib.Path
            Output file name.
        """
    def quantize(self, ignored_features: Incomplete | None = None, per_float_feature_quantization: Incomplete | None = None, border_count: Incomplete | None = None, max_bin: Incomplete | None = None, feature_border_type: Incomplete | None = None, sparse_features_conflict_fraction: Incomplete | None = None, nan_mode: Incomplete | None = None, input_borders: Incomplete | None = None, task_type: Incomplete | None = None, used_ram_limit: Incomplete | None = None, random_seed: Incomplete | None = None, **kwargs) -> None:
        """
        Quantize this pool

        Parameters
        ----------
        pool : catboost.Pool
            Dataset to quantize.

        ignored_features : list, [default=None]
            Indices or names of features that should be excluded when training.

        per_float_feature_quantization : list of strings, [default=None]
            List of float binarization descriptions.
            Format : described in documentation on catboost.ai
            Example 1: ['0:1024'] means that feature 0 will have 1024 borders.
            Example 2: ['0:border_count=1024', '1:border_count=1024', ...] means that two first features have 1024 borders.
            Example 3: ['0:nan_mode=Forbidden,border_count=32,border_type=GreedyLogSum',
                        '1:nan_mode=Forbidden,border_count=32,border_type=GreedyLogSum'] - defines more quantization properties for first two features.

        border_count : int, [default = 254 for training on CPU or 128 for training on GPU]
            The number of partitions in numeric features binarization. Used in the preliminary calculation.
            range: [1,65535] on CPU, [1,255] on GPU

        max_bin : float, synonym for border_count.

        feature_border_type : string, [default='GreedyLogSum']
            The binarization mode in numeric features binarization. Used in the preliminary calculation.
            Possible values:
                - 'Median'
                - 'Uniform'
                - 'UniformAndQuantiles'
                - 'GreedyLogSum'
                - 'MaxLogSum'
                - 'MinEntropy'

        sparse_features_conflict_fraction : float, [default=0.0]
            CPU only. Maximum allowed fraction of conflicting non-default values for features in exclusive features bundle.
            Should be a real value in [0, 1) interval.

        nan_mode : string, [default=None]
            Way to process missing values for numeric features.
            Possible values:
                - 'Forbidden' - raises an exception if there is a missing value for a numeric feature in a dataset.
                - 'Min' - each missing value will be processed as the minimum numerical value.
                - 'Max' - each missing value will be processed as the maximum numerical value.
            If None, then nan_mode=Min.

        input_borders : string or pathlib.Path, [default=None]
            input file with borders used in numeric features binarization.

        task_type : string, [default=None]
            The calcer type used to train the model.
            Possible values:
                - 'CPU'
                - 'GPU'

        used_ram_limit=None

        random_seed : int, [default=None]
            The random seed used for data sampling.
            If None, 0 is used.
        """

def plot_wrapper(plot, plot_file, plot_title, train_dirs) -> Generator[None, None, None]: ...
def stringify_builtin_metrics(params):
    """Replace all occurrences of BuiltinMetric with their string representations."""
def stringify_builtin_metrics_list(metrics): ...

class _CatBoostBase:
    def __init__(self, params) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, _): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def copy(self): ...
    def is_fitted(self): ...
    def get_test_eval(self): ...
    def get_test_evals(self): ...
    def get_evals_result(self): ...
    def get_best_score(self): ...
    def get_best_iteration(self): ...
    def get_n_features_in(self): ...
    def get_metadata(self): ...
    @property
    def tree_count_(self): ...
    @property
    def random_seed_(self): ...
    @property
    def learning_rate_(self): ...
    @property
    def n_features_in_(self): ...
    @property
    def feature_names_(self): ...
    @property
    def classes_(self): ...
    @property
    def evals_result_(self): ...
    @property
    def best_score_(self): ...
    @property
    def best_iteration_(self): ...
    def get_tree_leaf_counts(self):
        """
        Returns
        -------
        tree_leaf_counts : 1d-array of numpy.uint32 of size tree_count_.
        tree_leaf_counts[i] equals to the number of leafs in i-th tree of the ensemble.
        """
    def get_leaf_values(self):
        """
        Returns
        -------
        leaf_values : 1d-array of leaf values for all trees.
        Value corresponding to j-th leaf of i-th tree is at position
        sum(get_tree_leaf_counts()[:i]) + j (leaf and tree indexing starts from zero).
        """
    def get_leaf_weights(self):
        """
        Returns
        -------
        leaf_weights : 1d-array of leaf weights for all trees.
        Weight of j-th leaf of i-th tree is at position
        sum(get_tree_leaf_counts()[:i]) + j (leaf and tree indexing starts from zero).
        """
    def set_leaf_values(self, new_leaf_values) -> None:
        """
        Sets values at tree leafs of ensemble equal to new_leaf_values.

        Parameters
        ----------
        new_leaf_values : 1d-array with new leaf values for all trees.
        It's size should be equal to sum(get_tree_leaf_counts()).
        Value corresponding to j-th leaf of i-th tree should be at position
        sum(get_tree_leaf_counts()[:i]) + j (leaf and tree indexing starts from zero).
        """
    def set_feature_names(self, feature_names) -> None:
        """
        Sets feature names equal to feature_names

        Parameters
        ----------
        feature_names: 1-d array of strings with new feature names in the same order as in pool
        """
    def get_scale_and_bias(self): ...
    def set_scale_and_bias(self, scale, bias) -> None: ...

class CatBoost(_CatBoostBase):
    """
    CatBoost model. Contains training, prediction and evaluation methods.
    """
    def __init__(self, params: Incomplete | None = None) -> None:
        """
        Initialize the CatBoost.

        Parameters
        ----------
        params : dict
            Parameters for CatBoost.
            If  None, all params are set to their defaults.
            If  dict, overriding parameters present in dict.
        """
    def fit(self, X, y: Incomplete | None = None, cat_features: Incomplete | None = None, text_features: Incomplete | None = None, embedding_features: Incomplete | None = None, pairs: Incomplete | None = None, sample_weight: Incomplete | None = None, group_id: Incomplete | None = None, group_weight: Incomplete | None = None, subgroup_id: Incomplete | None = None, pairs_weight: Incomplete | None = None, baseline: Incomplete | None = None, use_best_model: Incomplete | None = None, eval_set: Incomplete | None = None, verbose: Incomplete | None = None, logging_level: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, column_description: Incomplete | None = None, verbose_eval: Incomplete | None = None, metric_period: Incomplete | None = None, silent: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, init_model: Incomplete | None = None, callbacks: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Fit the CatBoost model.

        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
             or string.
            If not catboost.Pool or catboost.FeaturesData it must be 2 dimensional Feature matrix
             or string - file with dataset.

             Must be non-empty (contain > 0 objects)

        y : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Labels, 1 dimensional array like.
            Use only if X is not catboost.Pool.

        cat_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Categ columns indices.
            Use only if X is not catboost.Pool and not catboost.FeaturesData

        text_features: list or numpy.ndarray, optional (default=None)
            If not none, giving the list of Text columns indices.
            Use only if X is not catboost.Pool and not catboost.FeaturesData

        embedding_features: list or numpy.ndarray, optional (default=None)
            If not none, giving the list of Embedding columns indices.
            Use only if X is not catboost.Pool and not catboost.FeaturesData

        pairs : list or numpy.ndarray or pandas.DataFrame
            The pairs description.
            If list or numpy.ndarrays or pandas.DataFrame, giving 2 dimensional.
            The shape should be Nx2, where N is the pairs' count. The first element of the pair is
            the index of the winner object in the training set. The second element of the pair is
            the index of the loser object in the training set.

        sample_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Instance weights, 1 dimensional array like.

        group_id : list or numpy.ndarray, optional (default=None)
            group id for each instance.
            If not None, giving 1 dimensional array like data.
            Use only if X is not catboost.Pool.

        group_weight : list or numpy.ndarray, optional (default=None)
            Group weight for each instance.
            If not None, giving 1 dimensional array like data.

        subgroup_id : list or numpy.ndarray, optional (default=None)
            subgroup id for each instance.
            If not None, giving 1 dimensional array like data.
            Use only if X is not catboost.Pool.

        pairs_weight : list or numpy.ndarray, optional (default=None)
            Weight for each pair.
            If not None, giving 1 dimensional array like pairs.

        baseline : list or numpy.ndarray, optional (default=None)
            If not None, giving 2 dimensional array like data.
            Use only if X is not catboost.Pool.

        use_best_model : bool, optional (default=None)
            Flag to use best model

        eval_set : catboost.Pool, or list of catboost.Pool, or list of (X, y) tuples, optional (default=None)
            Used as a validation set for early-stopping.

        logging_level : string, optional (default=None)
            Possible values:
                - 'Silent'
                - 'Verbose'
                - 'Info'
                - 'Debug'

        metric_period : int
            Frequency of evaluating metrics.

        verbose : bool or int
            If verbose is bool, then if set to True, logging_level is set to Verbose,
            if set to False, logging_level is set to Silent.
            If verbose is int, it determines the frequency of writing metrics to output and
            logging_level is set to Verbose.

        silent : bool
            If silent is True, logging_level is set to Silent.
            If silent is False, logging_level is set to Verbose.

        verbose_eval : bool or int
            Synonym for verbose. Only one of these parameters should be set.

        plot : bool, optional (default=False)
            If True, draw train and eval error in Jupyter notebook

        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error graphs to file

        early_stopping_rounds : int
            Activates Iter overfitting detector with od_wait parameter set to early_stopping_rounds.

        save_snapshot : bool, [default=None]
            Enable progress snapshotting for restoring progress after crashes or interruptions

        snapshot_file : string or pathlib.Path, [default=None]
            Learn progress snapshot file path, if None will use default filename

        snapshot_interval: int, [default=600]
            Interval between saving snapshots (seconds)

        init_model : CatBoost class or string or pathlib.Path, [default=None]
            Continue training starting from the existing model.
            If this parameter is a string or pathlib.Path, load initial model from the path specified by this string.

        callbacks : list, optional (default=None)
            List of callback objects that are applied at end of each iteration.

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        model : CatBoost
        """
    def predict(self, data, prediction_type: str = 'RawFormulaVal', ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: Incomplete | None = None, task_type: str = 'CPU'):
        """
        Predict with data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        prediction_type : string, optional (default='RawFormulaVal')
            Can be:
            - 'RawFormulaVal' : return raw value.
            - 'Class' : return class label.
            - 'Probability' : return probability for every class.
            - 'Exponent' : return Exponent of raw formula value.
            - 'RMSEWithUncertainty': return standard deviation for RMSEWithUncertainty loss function
              (logarithm of the standard deviation is returned by default).

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool, optional (default=False)
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction :
            If data is for a single object, the return value depends on prediction_type value:
                - 'RawFormulaVal' : return raw formula value.
                - 'Class' : return class label.
                - 'Probability' : return one-dimensional numpy.ndarray with probability for every class.
            otherwise numpy.ndarray, with values that depend on prediction_type value:
                - 'RawFormulaVal' : one-dimensional array of raw formula value for each object.
                - 'Class' : one-dimensional array of class label for each object.
                - 'Probability' : two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                  with probability for every class for each object.
        """
    def virtual_ensembles_predict(self, data, prediction_type: str = 'VirtEnsembles', ntree_end: int = 0, virtual_ensembles_count: int = 10, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict with data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        prediction_type : string, optional (default='RawFormulaVal')
            Can be:
            - 'VirtEnsembles': return V (virtual_ensembles_count) predictions.
                k-th virtEnsemle consists of trees [0, T/2] + [T/2 + T/(2V) * k, T/2 + T/(2V) * (k + 1)]  * constant.
            - 'TotalUncertainty': see returned predictions format in 'Returns' part

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        virtual_ensembles_count: int, optional (default=10)
            virtual ensembles count for 'TotalUncertainty' and 'VirtEnsembles' prediction types.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool, optional (default=False)
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction :
            (with V as virtual_ensembles_count and T as trees count,
            k-th virtEnsemle consists of trees [0, T/2] + [T/2 + T/(2V) * k, T/2 + T/(2V) * (k + 1)]  * constant)
            If data is for a single object, return 1-dimensional array of predictions with size depends on prediction type,
            otherwise return 2-dimensional numpy.ndarray with shape (number_of_objects x size depends on prediction type);
            Returned predictions depends on prediction type:
            If loss-function was RMSEWithUncertainty:
                - 'VirtEnsembles': [mean0, var0, mean1, var1, ..., vark-1].
                - 'TotalUncertainty': [mean_predict, KnowledgeUnc, DataUnc].
            otherwise for regression:
                - 'VirtEnsembles':  [mean0, mean1, ...].
                - 'TotalUncertainty': [mean_predicts, KnowledgeUnc].
            otherwise for binary classification:
                - 'VirtEnsembles':  [ApproxRawFormulaVal0, ApproxRawFormulaVal1, ..., ApproxRawFormulaValk-1].
                - 'TotalUncertainty':  [DataUnc, TotalUnc].
        """
    def staged_predict(self, data, prediction_type: str = 'RawFormulaVal', ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict target at each stage for data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        prediction_type : string, optional (default='RawFormulaVal')
            Can be:
            - 'RawFormulaVal' : return raw formula value.
            - 'Class' : return class label.
            - 'Probability' : return probability for every class.
            - 'RMSEWithUncertainty': return standard deviation for RMSEWithUncertainty loss function
              (logarithm of the standard deviation is returned by default).

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction : generator for each iteration that generates:
            If data is for a single object, the return value depends on prediction_type value:
                - 'RawFormulaVal' : return raw formula value.
                - 'Class' : return class label.
                - 'Probability' : return one-dimensional numpy.ndarray with probability for every class.
            otherwise numpy.ndarray, with values that depend on prediction_type value:
                - 'RawFormulaVal' : one-dimensional array of raw formula value for each object.
                - 'Class' : one-dimensional array of class label for each object.
                - 'Probability' : two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                  with probability for every class for each object.
        """
    def iterate_leaf_indexes(self, data, ntree_start: int = 0, ntree_end: int = 0):
        """
        Returns indexes of leafs to which objects from pool are mapped by model trees.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Index of first tree for which leaf indexes will be calculated (zero-based indexing).

        ntree_end: int, optional (default=0)
            Index of the tree after last tree for which leaf indexes will be calculated (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        Returns
        -------
        leaf_indexes : generator. For each object in pool yields one-dimensional numpy.ndarray of leaf indexes.
        """
    def calc_leaf_indexes(self, data, ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: bool = False):
        """
        Returns indexes of leafs to which objects from pool are mapped by model trees.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Index of first tree for which leaf indexes will be calculated (zero-based indexing).

        ntree_end: int, optional (default=0)
            Index of the tree after last tree for which leaf indexes will be calculated (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool (default=False)
            Enable debug logging level.

        Returns
        -------
        leaf_indexes : 2-dimensional numpy.ndarray of numpy.uint32 with shape (object count, ntree_end - ntree_start).
            i-th row is an array of leaf indexes for i-th object.
        """
    def get_cat_feature_indices(self): ...
    def get_text_feature_indices(self): ...
    def get_embedding_feature_indices(self): ...
    def eval_metrics(self, data, metrics, ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, tmp_dir: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Calculate metrics.

        Parameters
        ----------
        data : catboost.Pool
            Data to evaluate metrics on.

        metrics : list of strings or catboost.metrics.BuiltinMetric
            List of evaluated metrics.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        tmp_dir : string or pathlib.Path (default=None)
            The name of the temporary directory for intermediate results.
            If None, then the name will be generated.

        plot : bool, optional (default=False)
            If True, draw train and eval error in Jupyter notebook
            
        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error graphs to file

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        prediction : dict: metric -> array of shape [(ntree_end - ntree_start) / eval_period]
        """
    def compare(self, model, data, metrics, ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, tmp_dir: Incomplete | None = None, plot_file: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Draw train and eval errors in Jupyter notebook for both models

        Parameters
        ----------
        model: CatBoost model
            Another model to draw metrics

        data : catboost.Pool
            Data to evaluate metrics on.

        metrics : list of strings or catboost.metrics.BuiltinMetric
            List of evaluated metrics.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        tmp_dir : string or pathlib.Path (default=None)
            The name of the temporary directory for intermediate results.
            If None, then the name will be generated.

        plot_file : file-like or str, optional (default=None)
            If not None, save eval error graphs to file

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging
        """
    def create_metric_calcer(self, metrics, ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, tmp_dir: Incomplete | None = None):
        """
        Create batch metric calcer. Could be used to aggregate metric on several pools
        Parameters
        ----------
            Same as in eval_metrics except data
        Returns
        -------
            BatchMetricCalcer object

        Usage example
        -------
        # Large dataset is partitioned into parts [part1, part2]
        model.fit(params)
        batch_calcer = model.create_metric_calcer(['Logloss'])
        batch_calcer.add(part1)
        batch_calcer.add(part2)
        metrics = batch_calcer.eval_metrics()
        """
    @property
    def feature_importances_(self): ...
    def get_feature_importance(self, data: Incomplete | None = None, type=..., prettified: bool = False, thread_count: int = -1, verbose: bool = False, fstr_type: Incomplete | None = None, shap_mode: str = 'Auto', model_output: str = 'Raw', interaction_indices: Incomplete | None = None, shap_calc_type: str = 'Regular', reference_data: Incomplete | None = None, sage_n_samples: int = 128, sage_batch_size: int = 512, sage_detect_convergence: bool = True, log_cout=..., log_cerr=...):
        '''
        Parameters
        ----------
        data :
            Data to get feature importance.
            If type in (\'LossFunctionChange\', \'ShapValues\', \'ShapInteractionValues\') data must of Pool type.
                For every object in this dataset feature importances will be calculated.
            if type == \'SageValues\' data must of Pool type.
                For every feature in this dataset importance will be calculated.
            If type == \'PredictionValuesChange\', data is None or a dataset of Pool type
                Dataset specification is needed only in case if the model does not contain leaf weight information (trained with CatBoost v < 0.9).
            If type == \'PredictionDiff\' data must contain a matrix of feature values of shape (2, n_features).
                Possible types are catboost.Pool or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData or pandas.SparseDataFrame or scipy.sparse.spmatrix
            If type == \'FeatureImportance\'
                See \'PredictionValuesChange\' for non-ranking metrics and \'LossFunctionChange\' for ranking metrics.
            If type == \'Interaction\'
                This parameter is not used.

        type : EFstrType or string (converted to EFstrType), optional
                    (default=EFstrType.FeatureImportance)
            Possible values:
                - PredictionValuesChange
                    Calculate score for every feature.
                - LossFunctionChange
                    Calculate score for every feature by loss.
                - FeatureImportance
                    PredictionValuesChange for non-ranking metrics and LossFunctionChange for ranking metrics
                - ShapValues
                    Calculate SHAP Values for every object.
                - ShapInteractionValues
                    Calculate SHAP Interaction Values between each pair of features for every object
                - Interaction
                    Calculate pairwise score between every feature.
                - PredictionDiff
                    Calculate most important features explaining difference in predictions for a pair of documents.
                - SageValues
                    Calculate SAGE value for every feature

        prettified : bool, optional (default=False)
            change returned data format to the list of (feature_id, importance) pairs sorted by importance

        thread_count : int, optional (default=-1)
            Number of threads.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool or int
            If False, then evaluation is not logged. If True, then each possible iteration is logged.
            If a positive integer, then it stands for the size of batch N. After processing each batch, print progress
            and remaining time.

        fstr_type : string, deprecated, use type instead

        shap_mode : string, optional (default="Auto")
            used only for ShapValues type
            Possible values:
                - "Auto"
                    Use direct SHAP Values calculation only if data size is smaller than average leaves number
                    (the best of two strategies below is chosen).
                - "UsePreCalc"
                    Calculate SHAP Values for every leaf in preprocessing. Final complexity is
                    O(NT(D+F))+O(TL^2 D^2) where N is the number of documents(objects), T - number of trees,
                    D - average tree depth, F - average number of features in tree, L - average number of leaves in tree
                    This is much faster (because of a smaller constant) than direct calculation when N >> L
                - "NoPreCalc"
                    Use direct SHAP Values calculation calculation with complexity O(NTLD^2). Direct algorithm
                    is faster when N < L (algorithm from https://arxiv.org/abs/1802.03888)

        shap_calc_type : EShapCalcType or string, optional (default="Regular")
            used only for ShapValues type
            Possible values:
                - "Regular"
                    Calculate regular SHAP values
                - "Approximate"
                    Calculate approximate SHAP values
                - "Exact"
                    Calculate exact SHAP values

        interaction_indices : list of int or string (feature_idx_1, feature_idx_2), optional (default=None)
            used only for ShapInteractionValues type
            Calculate SHAP Interaction Values between pair of features feature_idx_1 and feature_idx_2 for every object

        reference_data: catboost.Pool or None
            Reference data for Independent Tree SHAP values from https://arxiv.org/abs/1905.04610v1
            if type == \'ShapValues\' and reference_data is not None, then Independent Tree SHAP values are calculated
        
        sage_n_samples: int, optional (default=32)
            Number of outer samples used in SAGE values approximation algorithm
        sage_batch_size: int, optional (default=min(512, number of samples in dataset))
            Number of samples used on each step of SAGE values approximation algorithm
        sage_detect_convergence: bool, optional (default=False)
            If set True, sage values calculation will be stopped either when sage values converge
            or when sage_n_samples iterations of algorithm pass

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        depends on type:
            - FeatureImportance
                See PredictionValuesChange for non-ranking metrics and LossFunctionChange for ranking metrics.
            - PredictionValuesChange, LossFunctionChange, PredictionDiff, SageValues with prettified=False (default)
                list of length [n_features] with feature_importance values (float) for feature
            - PredictionValuesChange, LossFunctionChange, PredictionDiff, SageValues with prettified=True
                list of length [n_features] with (feature_id (string), feature_importance (float)) pairs, sorted by feature_importance in descending order
            - ShapValues
                np.ndarray of shape (n_objects, n_features + 1) with Shap values (float) for (object, feature).
                In case of multiclass the returned value is np.ndarray of shape
                (n_objects, classes_count, n_features + 1). For each object it contains Shap values (float).
                Values are calculated for RawFormulaVal predictions.
            - ShapInteractionValues
                np.ndarray of shape (n_objects, n_features + 1, n_features + 1) with Shap interaction values (float) for (object, feature(i), feature(j)).
                In case of multiclass the returned value is np.ndarray of shape
                (n_objects, classes_count, n_features + 1, n_features + 1). For each object it contains Shap interaction values (float).
                Values are calculated for RawFormulaVal predictions.
            - Interaction
                list of length [n_features] of 3-element lists of (first_feature_index, second_feature_index, interaction_score (float))
        '''
    def get_object_importance(self, pool, train_pool, top_size: int = -1, type: str = 'Average', update_method: str = 'SinglePoint', importance_values_sign: str = 'All', thread_count: int = -1, verbose: bool = False, ostr_type: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        This is the implementation of the LeafInfluence algorithm from the following paper:
        https://arxiv.org/pdf/1802.06640.pdf

        Parameters
        ----------
        pool : Pool
            The pool for which you want to evaluate the object importances.

        train_pool : Pool
            The pool on which the model has been trained.

        top_size : int (default=-1)
            Method returns the result of the top_size most important train objects.
            If -1, then the top size is not limited.

        type : string, optional (default='Average')
            Possible values:
                - Average (Method returns the mean train objects scores for all input objects)
                - PerObject (Method returns the train objects scores for every input object)

        importance_values_sign : string, optional (default='All')
            Method returns only Positive, Negative or All values.
            Possible values:
                - Positive
                - Negative
                - All

        update_method : string, optional (default='SinglePoint')
            Possible values:
                - SinglePoint
                - TopKLeaves (It is posible to set top size : TopKLeaves:top=2)
                - AllPoints
            Description of the update set methods are given in section 3.1.3 of the paper.

        thread_count : int, optional (default=-1)
            Number of threads.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool or int
            If False, then evaluation is not logged. If True, then each possible iteration is logged.
            If a positive integer, then it stands for the size of batch N. After processing each batch, print progress
            and remaining time.

        ostr_type : string, deprecated, use type instead

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        object_importances : tuple of two arrays (indices and scores) of shape = [top_size]
        """
    def shrink(self, ntree_end, ntree_start: int = 0) -> None:
        """
        Shrink the model.

        Parameters
        ----------
        ntree_end: int
            Leave the trees with indices from the interval [ntree_start, ntree_end) (zero-based indexing).
        ntree_start: int, optional (default=0)
            Leave the trees with indices from the interval [ntree_start, ntree_end) (zero-based indexing).
        """
    def drop_unused_features(self) -> None:
        """
        Drop unused features information from model
        """
    def save_model(self, fname, format: str = 'cbm', export_parameters: Incomplete | None = None, pool: Incomplete | None = None) -> None:
        """
        Save the model to a file.

        Parameters
        ----------
        fname : string
            Output file name.
        format : string
            Possible values:
                * 'cbm' for catboost binary format,
                * 'coreml' to export into Apple CoreML format
                * 'onnx' to export into ONNX-ML format
                * 'pmml' to export into PMML format
                * 'cpp' to export as C++ code
                * 'python' to export as Python code.
        export_parameters : dict
            Parameters for CoreML export:
                * prediction_type : string - either 'probability' or 'raw'
                * coreml_description : string
                * coreml_model_version : string
                * coreml_model_author : string
                * coreml_model_license: string
            Parameters for PMML export:
                * pmml_copyright : string
                * pmml_description : string
                * pmml_model_version : string
        pool : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series or catboost.FeaturesData
            Training pool.
        """
    def load_model(self, fname: Incomplete | None = None, format: str = 'cbm', stream: Incomplete | None = None, blob: Incomplete | None = None):
        """
        Load model from a file, stream or blob.

        Parameters
        ----------
        fname : string
            Input file name.
        """
    def get_param(self, key):
        """
        Get param value from CatBoost model.

        Parameters
        ----------
        key : string
            The key to get param value from.

        Returns
        -------
        value :
            The param value of the key, returns None if param do not exist.
        """
    def get_params(self, deep: bool = True):
        """
        Get all params from CatBoost model.

        Returns
        -------
        result : dict
            Dictionary of {param_key: param_value}.
        """
    def get_all_params(self):
        """
        Get all params (specified by user and default params) that were set in training from CatBoost model.
        Full parameters documentation could be found here: https://catboost.ai/docs/concepts/python-reference_parameters-list.html

        Returns
        -------
        result : dict
            Dictionary of {param_key: param_value}.
        """
    def save_borders(self, fname) -> None:
        """
        Save the model borders to a file.

        Parameters
        ----------
        fname : string or pathlib.Path
            Output file name.
        """
    def get_borders(self):
        """
        Return map feature_index: borders for float features.

        """
    def set_params(self, **params):
        """
        Set parameters into CatBoost model.

        Parameters
        ----------
        **params : key=value format
            List of key=value paris. Example: model.set_params(iterations=500, thread_count=2).
        """
    def plot_predictions(self, data, features_to_change, plot: bool = True, plot_file: Incomplete | None = None):
        """
        To use this function, you should install plotly.
        data: numpy.ndarray or pandas.DataFrame or catboost.Pool
        feature:
            Float features indexes in pd.DataFrame for which you want vary prediction value.
        plot: bool
            Plot predictions.
        plot_file: str
            Output file for plot predictions.
        Returns
        -------
            List of list of predictions for all buckets for all documents in data
        """
    def plot_partial_dependence(self, data, features, plot: bool = True, plot_file: Incomplete | None = None, thread_count: int = -1):
        """
        To use this function, you should install plotly.
        data: numpy.ndarray or pandas.DataFrame or catboost.Pool
        features: int, str, list<int>, tuple<int>, list<string>, tuple<string>
            Float features to calculate partial dependence for. Number of features should be 1 or 2.
        plot: bool
            Plot predictions.
        plot_file: str
            Output file for plot predictions.
        thread_count: int
            Number of threads to use. If -1 use maximum available number of threads.
        Returns
        -------
            If number of features is one - 1d numpy array and figure with line plot.
            If number of features is two - 2d numpy array and figure with 2d heatmap.
        """
    def calc_feature_statistics(self, data, target: Incomplete | None = None, feature: Incomplete | None = None, prediction_type: Incomplete | None = None, cat_feature_values: Incomplete | None = None, plot: bool = True, max_cat_features_on_plot: int = 10, thread_count: int = -1, plot_file: Incomplete | None = None):
        """
        Get statistics for the feature using the model, dataset and target.
        To use this function, you should install plotly.

        The catboost model has borders for the float features used in it. The borders divide
        feature values into bins, and the model's prediction depends on the number of the bin where the
        feature value falls in.

        For float features this function takes model's borders and computes
        1) Mean target value for every bin;
        2) Mean model prediction for every bin;
        3) The number of objects in dataset which fall into each bin;
        4) Predictions on varying feature. For every object, varies the feature value
        so that it falls into bin #0, bin #1, ... and counts model predictions.
        Then counts average prediction for each bin.

        For categorical features (only one-hot supported) does the same, but takes feature values
        provided in cat_feature_values instead of borders.

        Parameters
        ----------
        data: numpy.ndarray or pandas.DataFrame or catboost. Pool or dict {'pool_name': pool} if you want several pools
            Data to compute statistics on
        target: numpy.ndarray or pandas.Series or dict {'pool_name': target} if you want several pools or None
            Target corresponding to data
            Use only if data is not catboost.Pool.
        feature: None, int, string, or list of int or strings
            Features indexes or names in pd.DataFrame for which you want to get statistics.
            None, if you need statistics for all features.
        prediction_type: str
            Prediction type used for counting mean_prediction: 'Class', 'Probability' or 'RawFormulaVal'.
            If not specified, is derived from the model.
        cat_feature_values: list or numpy.ndarray or pandas.Series or
                            dict: int or string to list or numpy.ndarray or pandas.Series
            Contains categorical feature values you need to get statistics on.
            Use dict, when parameter 'feature' is a list to specify cat values for different features.
            When parameter 'feature' is int or str, you can just pass list of cat values.
        plot: bool
            Plot statistics.
        max_cat_features_on_plot: int
            If categorical feature takes more than max_cat_features_on_plot different unique values,
            output result on several plots, not more than max_cat_features_on_plot feature values on each.
            Used only if plot=True or plot_file is not None.
        thread_count: int
            Number of threads to use for getting statistics.
        plot_file: str
            Output file for plot statistics.

        Returns
        -------
        dict if parameter 'feature' is int or string, else dict of dicts:
            For each unique feature contain
            python dict with binarized feature statistics.
            For float feature, includes
                    'borders' -- borders for the specified feature in model
                    'binarized_feature' -- numbers of bins where feature values fall
                    'mean_target' -- mean value of target over each bin
                    'mean_prediction' -- mean value of model prediction over each bin
                    'objects_per_bin' -- number of objects per bin
                    'predictions_on_varying_feature' -- averaged over dataset predictions for
                    varying feature (see above)
            For one-hot feature, returns the same, but with 'cat_values' instead of 'borders'
        """
    def plot_tree(self, tree_idx, pool: Incomplete | None = None): ...
    def grid_search(self, param_grid, X, y: Incomplete | None = None, cv: int = 3, partition_random_seed: int = 0, calc_cv_statistics: bool = True, search_by_train_test_split: bool = True, refit: bool = True, shuffle: bool = True, stratified: Incomplete | None = None, train_size: float = 0.8, verbose: bool = True, plot: bool = False, plot_file: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Exhaustive search over specified parameter values for a model.
        Aafter calling this method model is fitted and can be used, if not specified otherwise (refit=False).

        Parameters
        ----------
        param_grid: dict or list of dictionaries
            Dictionary with parameters names (string) as keys and lists of parameter settings
            to try as values, or a list of such dictionaries, in which case the grids spanned by each
            dictionary in the list are explored.
            This enables searching over any sequence of parameter settings.

        X: numpy.ndarray or pandas.DataFrame or catboost.Pool
            Data to compute statistics on

        y: numpy.ndarray or pandas.Series or None
            Target corresponding to data
            Use only if data is not catboost.Pool.

        cv: int, cross-validation generator or an iterable, optional (default=None)
            Determines the cross-validation splitting strategy. Possible inputs for cv are:
            - None, to use the default 3-fold cross validation,
            - integer, to specify the number of folds in a (Stratified)KFold
            - one of the scikit-learn splitter classes
                (https://scikit-learn.org/stable/modules/classes.html#splitter-classes)
            - An iterable yielding (train, test) splits as arrays of indices.

        partition_random_seed: int, optional (default=0)
            Use this as the seed value for random permutation of the data.
            Permutation is performed before splitting the data for cross validation.
            Each seed generates unique data splits.
            Used only when cv is None or int.

        search_by_train_test_split: bool, optional (default=True)
            If True, source dataset is splitted into train and test parts, models are trained
            on the train part and parameters are compared by loss function score on the test part.
            After that, if calc_cv_statistics=true, statistics on metrics are calculated
            using cross-validation using best parameters and the model is fitted with these parameters.

            If False, every iteration of grid search evaluates results on cross-validation.
            It is recommended to set parameter to True for large datasets, and to False for small datasets.

        calc_cv_statistics: bool, optional (default=True)
            The parameter determines whether quality should be estimated.
            using cross-validation with the found best parameters. Used only when search_by_train_test_split=True.

        refit: bool (default=True)
            Refit an estimator using the best found parameters on the whole dataset.

        shuffle: bool, optional (default=True)
            Shuffle the dataset objects before parameters searching.

        stratified: bool, optional (default=None)
            Perform stratified sampling. True for classification and False otherwise.
            Currently supported only for final cross-validation.

        train_size: float, optional (default=0.8)
            Should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split.

        verbose: bool or int, optional (default=True)
            If verbose is int, it determines the frequency of writing metrics to output
            verbose==True is equal to verbose==1
            When verbose==False, there is no messages

        plot : bool, optional (default=False)
            If True, draw train and eval error for every set of parameters in Jupyter notebook

        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error for every set of parameters to file

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        dict with two fields:
            'params': dict of best found parameters
            'cv_results': dict or pandas.core.frame.DataFrame with cross-validation results
                columns are: test-error-mean  test-error-std  train-error-mean  train-error-std
        """
    def randomized_search(self, param_distributions, X, y: Incomplete | None = None, cv: int = 3, n_iter: int = 10, partition_random_seed: int = 0, calc_cv_statistics: bool = True, search_by_train_test_split: bool = True, refit: bool = True, shuffle: bool = True, stratified: Incomplete | None = None, train_size: float = 0.8, verbose: bool = True, plot: bool = False, plot_file: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Randomized search on hyper parameters.
        After calling this method model is fitted and can be used, if not specified otherwise (refit=False).

        In contrast to grid_search, not all parameter values are tried out,
        but rather a fixed number of parameter settings is sampled from the specified distributions.
        The number of parameter settings that are tried is given by n_iter.

        Parameters
        ----------
        param_distributions: dict
            Dictionary with parameters names (string) as keys and distributions or lists of parameters to try.
            Distributions must provide a rvs method for sampling (such as those from scipy.stats.distributions).
            If a list is given, it is sampled uniformly.

        X: numpy.ndarray or pandas.DataFrame or catboost.Pool
            Data to compute statistics on

        y: numpy.ndarray or pandas.Series or None
            Target corresponding to data
            Use only if data is not catboost.Pool.

        cv: int, cross-validation generator or an iterable, optional (default=None)
            Determines the cross-validation splitting strategy. Possible inputs for cv are:
            - None, to use the default 3-fold cross validation,
            - integer, to specify the number of folds in a (Stratified)KFold
            - one of the scikit-learn splitter classes
                (https://scikit-learn.org/stable/modules/classes.html#splitter-classes)
            - An iterable yielding (train, test) splits as arrays of indices.

        n_iter: int
            Number of parameter settings that are sampled.
            n_iter trades off runtime vs quality of the solution.

        partition_random_seed: int, optional (default=0)
            Use this as the seed value for random permutation of the data.
            Permutation is performed before splitting the data for cross validation.
            Each seed generates unique data splits.
            Used only when cv is None or int.

        search_by_train_test_split: bool, optional (default=True)
            If True, source dataset is splitted into train and test parts, models are trained
            on the train part and parameters are compared by loss function score on the test part.
            After that, if calc_cv_statistics=true, statistics on metrics are calculated
            using cross-validation using best parameters and the model is fitted with these parameters.

            If False, every iteration of grid search evaluates results on cross-validation.
            It is recommended to set parameter to True for large datasets, and to False for small datasets.

        calc_cv_statistics: bool, optional (default=True)
            The parameter determines whether quality should be estimated.
            using cross-validation with the found best parameters. Used only when search_by_train_test_split=True.

        refit: bool (default=True)
            Refit an estimator using the best found parameters on the whole dataset.

        shuffle: bool, optional (default=True)
            Shuffle the dataset objects before parameters searching.

        stratified: bool, optional (default=None)
            Perform stratified sampling. True for classification and False otherwise.
            Currently supported only for cross-validation.

        train_size: float, optional (default=0.8)
            Should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split.

        verbose: bool or int, optional (default=True)
            If verbose is int, it determines the frequency of writing metrics to output
            verbose==True is equal to verbose==1
            When verbose==False, there is no messages

        plot : bool, optional (default=False)
            If True, draw train and eval error for every set of parameters in Jupyter notebook

        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error for every set of parameters to file

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        dict with two fields:
            'params': dict of best found parameters
            'cv_results': dict or pandas.core.frame.DataFrame with cross-validation results
                columns are: test-error-mean  test-error-std  train-error-mean  train-error-std
        """
    def select_features(self, X, y: Incomplete | None = None, eval_set: Incomplete | None = None, features_for_select: Incomplete | None = None, num_features_to_select: Incomplete | None = None, algorithm: Incomplete | None = None, steps: Incomplete | None = None, shap_calc_type: Incomplete | None = None, train_final_model: bool = True, verbose: Incomplete | None = None, logging_level: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, log_cout=..., log_cerr=..., grouping: Incomplete | None = None, features_tags_for_select: Incomplete | None = None, num_features_tags_to_select: Incomplete | None = None):
        '''
        Select best features from pool according to loss value.

        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            If not catboost.Pool, 2 dimensional Feature matrix or string - file with dataset.

        y : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Labels, 1 dimensional array like.
            Use only if X is not catboost.Pool.

        eval_set : catboost.Pool or tuple (X, y) or list [(X, y)], optional (default=None)
            Dataset for evaluation.

        features_for_select : str or list of feature indices, names or ranges
            (for grouping = Individual)
            Which features should participate in the selection.
            Format examples:
                - [0, 2, 3, 4, 17]
                - [0, "2-4", 17] (both ends in ranges are inclusive)
                - "0,2-4,20"
                - ["Name0", "Name2", "Name3", "Name4", "Name20"]

        num_features_to_select : positive int
            (for grouping = Individual)
            How many features to select from features_for_select.

        algorithm : EFeaturesSelectionAlgorithm or string, optional (default=RecursiveByShapValues)
            Which algorithm to use for features selection.
            Possible values:
                - RecursiveByPredictionValuesChange
                    Use prediction values change as feature strength, eliminate batch of features at once.
                - RecursiveByLossFunctionChange
                    Use loss function change as feature strength, eliminate batch of features at each step.
                - RecursiveByShapValues
                    Use shap values to estimate loss function change, eliminate features one by one.

        steps : positive int, optional (default=1)
            How many steps should be performed. In other words, how many times a full model will be trained.
            More steps give more accurate results.

        shap_calc_type : EShapCalcType or string, optional (default=Regular)
            Which method to use for calculation of shap values.
            Possible values:
                - Regular
                    Calculate regular SHAP values
                - Approximate
                    Calculate approximate SHAP values
                - Exact
                    Calculate exact SHAP values

        train_final_model : bool, optional (default=True)
            Need to fit model with selected features.

        verbose : bool or int
            If verbose is bool, then if set to True, logging_level is set to Verbose,
            if set to False, logging_level is set to Silent.
            If verbose is int, it determines the frequency of writing metrics to output and
            logging_level is set to Verbose.

        logging_level : string, optional (default=None)
            Possible values:
                - \'Silent\'
                - \'Verbose\'
                - \'Info\'
                - \'Debug\'

        plot : bool, optional (default=False)
            If True, draw train and eval error in Jupyter notebook.

        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error graphs to file

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        grouping : EFeaturesSelectionGrouping or string, optional (default=Individual)
            Which grouping to use for features selection.
            Possible values:
                - Individual
                    Select individual features
                - ByTags
                    Select feature groups (marked by tags)

        features_tags_for_select : list of strings
            (for grouping = ByTags)
            Which features tags should participate in the selection.

        num_features_tags_to_select : positive int
            (for grouping = ByTags)
            How many features tags to select from features_tags_for_select.

        Returns
        -------
        dict with fields:
            \'selected_features\': list of selected features indices
            \'eliminated_features\': list of eliminated features indices
            \'selected_features_tags\': list of selected features tags (optional, present if grouping == ByTags)
            \'eliminated_features_tags\': list of selected features tags (optional, present if grouping == ByTags)
        '''

class CatBoostClassifier(CatBoost):
    """
    Implementation of the scikit-learn API for CatBoost classification.

    Parameters
    ----------
    iterations : int, [default=500]
        Max count of trees.
        range: [1,+inf]
    learning_rate : float, [default value is selected automatically for binary classification with other parameters set to default. In all other cases default is 0.03]
        Step size shrinkage used in update to prevents overfitting.
        range: (0,1]
    depth : int, [default=6]
        Depth of a tree. All trees are the same depth.
        range: [1,+inf]
    l2_leaf_reg : float, [default=3.0]
        Coefficient at the L2 regularization term of the cost function.
        range: [0,+inf]
    model_size_reg : float, [default=None]
        Model size regularization coefficient.
        range: [0,+inf]
    rsm : float, [default=None]
        Subsample ratio of columns when constructing each tree.
        range: (0,1]
    loss_function : string or object, [default='Logloss']
        The metric to use in training and also selector of the machine learning
        problem to solve. If string, then the name of a supported metric,
        optionally suffixed with parameter description.
        If object, it shall provide methods 'calc_ders_range' or 'calc_ders_multi'.
    border_count : int, [default = 254 for training on CPU or 128 for training on GPU]
        The number of partitions in numeric features binarization. Used in the preliminary calculation.
        range: [1,65535] on CPU, [1,255] on GPU
    feature_border_type : string, [default='GreedyLogSum']
        The binarization mode in numeric features binarization. Used in the preliminary calculation.
        Possible values:
            - 'Median'
            - 'Uniform'
            - 'UniformAndQuantiles'
            - 'GreedyLogSum'
            - 'MaxLogSum'
            - 'MinEntropy'
    per_float_feature_quantization : list of strings, [default=None]
        List of float binarization descriptions.
        Format : described in documentation on catboost.ai
        Example 1: ['0:1024'] means that feature 0 will have 1024 borders.
        Example 2: ['0:border_count=1024', '1:border_count=1024', ...] means that two first features have 1024 borders.
        Example 3: ['0:nan_mode=Forbidden,border_count=32,border_type=GreedyLogSum',
                    '1:nan_mode=Forbidden,border_count=32,border_type=GreedyLogSum'] - defines more quantization properties for first two features.
    input_borders : string or pathlib.Path, [default=None]
        input file with borders used in numeric features binarization.
    output_borders : string, [default=None]
        output file for borders that were used in numeric features binarization.
    fold_permutation_block : int, [default=1]
        To accelerate the learning.
        The recommended value is within [1, 256]. On small samples, must be set to 1.
        range: [1,+inf]
    od_pval : float, [default=None]
        Use overfitting detector to stop training when reaching a specified threshold.
        Can be used only with eval_set.
        range: [0,1]
    od_wait : int, [default=None]
        Number of iterations which overfitting detector will wait after new best error.
    od_type : string, [default=None]
        Type of overfitting detector which will be used in program.
        Posible values:
            - 'IncToDec'
            - 'Iter'
        For 'Iter' type od_pval must not be set.
        If None, then od_type=IncToDec.
    nan_mode : string, [default=None]
        Way to process missing values for numeric features.
        Possible values:
            - 'Forbidden' - raises an exception if there is a missing value for a numeric feature in a dataset.
            - 'Min' - each missing value will be processed as the minimum numerical value.
            - 'Max' - each missing value will be processed as the maximum numerical value.
        If None, then nan_mode=Min.
    counter_calc_method : string, [default=None]
        The method used to calculate counters for dataset with Counter type.
        Possible values:
            - 'PrefixTest' - only objects up to current in the test dataset are considered
            - 'FullTest' - all objects are considered in the test dataset
            - 'SkipTest' - Objects from test dataset are not considered
            - 'Full' - all objects are considered for both learn and test dataset
        If None, then counter_calc_method=PrefixTest.
    leaf_estimation_iterations : int, [default=None]
        The number of steps in the gradient when calculating the values in the leaves.
        If None, then leaf_estimation_iterations=1.
        range: [1,+inf]
    leaf_estimation_method : string, [default=None]
        The method used to calculate the values in the leaves.
        Possible values:
            - 'Newton'
            - 'Gradient'
    thread_count : int, [default=None]
        Number of parallel threads used to run CatBoost.
        If None or -1, then the number of threads is set to the number of CPU cores.
        range: [1,+inf]
    random_seed : int, [default=None]
        Random number seed.
        If None, 0 is used.
        range: [0,+inf]
    use_best_model : bool, [default=None]
        To limit the number of trees in predict() using information about the optimal value of the error function.
        Can be used only with eval_set.
    best_model_min_trees : int, [default=None]
        The minimal number of trees the best model should have.
    verbose: bool
        When set to True, logging_level is set to 'Verbose'.
        When set to False, logging_level is set to 'Silent'.
    silent: bool, synonym for verbose
    logging_level : string, [default='Verbose']
        Possible values:
            - 'Silent'
            - 'Verbose'
            - 'Info'
            - 'Debug'
    metric_period : int, [default=1]
        The frequency of iterations to print the information to stdout. The value should be a positive integer.
    simple_ctr: list of strings, [default=None]
        Binarization settings for categorical features.
            Format : see documentation
            Example: ['Borders:CtrBorderCount=5:Prior=0:Prior=0.5', 'BinarizedTargetMeanValue:TargetBorderCount=10:TargetBorderType=MinEntropy', ...]
            CTR types:
                CPU and GPU
                - 'Borders'
                - 'Buckets'
                CPU only
                - 'BinarizedTargetMeanValue'
                - 'Counter'
                GPU only
                - 'FloatTargetMeanValue'
                - 'FeatureFreq'
            Number_of_borders, binarization type, target borders and binarizations, priors are optional parametrs
    combinations_ctr: list of strings, [default=None]
    per_feature_ctr: list of strings, [default=None]
    ctr_target_border_count: int, [default=None]
        Maximum number of borders used in target binarization for categorical features that need it.
        If TargetBorderCount is specified in 'simple_ctr', 'combinations_ctr' or 'per_feature_ctr' option it
        overrides this value.
        range: [1, 255]
    ctr_leaf_count_limit : int, [default=None]
        The maximum number of leaves with categorical features.
        If the number of leaves exceeds the specified limit, some leaves are discarded.
        The leaves to be discarded are selected as follows:
            - The leaves are sorted by the frequency of the values.
            - The top N leaves are selected, where N is the value specified in the parameter.
            - All leaves starting from N+1 are discarded.
        This option reduces the resulting model size
        and the amount of memory required for training.
        Note that the resulting quality of the model can be affected.
        range: [1,+inf] (for zero limit use ignored_features)
    store_all_simple_ctr : bool, [default=None]
        Ignore categorical features, which are not used in feature combinations,
        when choosing candidates for exclusion.
        Use this parameter with ctr_leaf_count_limit only.
    max_ctr_complexity : int, [default=4]
        The maximum number of Categ features that can be combined.
        range: [0,+inf]
    has_time : bool, [default=False]
        To use the order in which objects are represented in the input data
        (do not perform a random permutation of the dataset at the preprocessing stage).
    allow_const_label : bool, [default=False]
        To allow the constant label value in dataset.
    target_border: float, [default=None]
        Border for target binarization.
    classes_count : int, [default=None]
        The upper limit for the numeric class label.
        Defines the number of classes for multiclassification.
        Only non-negative integers can be specified.
        The given integer should be greater than any of the target values.
        If this parameter is specified the labels for all classes in the input dataset
        should be smaller than the given value.
        If several of 'classes_count', 'class_weights', 'class_names' parameters are defined
        the numbers of classes specified by each of them must be equal.
    class_weights : list or dict, [default=None]
        Classes weights. The values are used as multipliers for the object weights.
        If None, all classes are supposed to have weight one.
        If list - class weights in order of class_names or sequential classes if class_names is undefined
        If dict - dict of class_name -> class_weight.
        If several of 'classes_count', 'class_weights', 'class_names' parameters are defined
        the numbers of classes specified by each of them must be equal.
    auto_class_weights : string [default=None]
        Enables automatic class weights calculation. Possible values:
            - Balanced  # weight = maxSummaryClassWeight / summaryClassWeight, statistics determined from train pool
            - SqrtBalanced  # weight = sqrt(maxSummaryClassWeight / summaryClassWeight)
    class_names: list of strings, [default=None]
        Class names. Allows to redefine the default values for class labels (integer numbers).
        If several of 'classes_count', 'class_weights', 'class_names' parameters are defined
        the numbers of classes specified by each of them must be equal.
    one_hot_max_size : int, [default=None]
        Convert the feature to float
        if the number of different values that it takes exceeds the specified value.
        Ctrs are not calculated for such features.
    random_strength : float, [default=1]
        Score standard deviation multiplier.
    name : string, [default='experiment']
        The name that should be displayed in the visualization tools.
    ignored_features : list, [default=None]
        Indices or names of features that should be excluded when training.
    train_dir : string or pathlib.Path, [default=None]
        The directory in which you want to record generated in the process of learning files.
    custom_metric : string or list of strings, [default=None]
        To use your own metric function.
    custom_loss: alias to custom_metric
    eval_metric : string or object, [default=None]
        To optimize your custom metric in loss.
    bagging_temperature : float, [default=None]
        Controls intensity of Bayesian bagging. The higher the temperature the more aggressive bagging is.
        Typical values are in range [0, 1] (0 - no bagging, 1 - default).
    save_snapshot : bool, [default=None]
        Enable progress snapshotting for restoring progress after crashes or interruptions
    snapshot_file : string or pathlib.Path, [default=None]
        Learn progress snapshot file path, if None will use default filename
    snapshot_interval: int, [default=600]
        Interval between saving snapshots (seconds)
    fold_len_multiplier : float, [default=None]
        Fold length multiplier. Should be greater than 1
    used_ram_limit : string or number, [default=None]
        Set a limit on memory consumption (value like '1.2gb' or 1.2e9).
        WARNING: Currently this option affects CTR memory usage only.
    gpu_ram_part : float, [default=0.95]
        Fraction of the GPU RAM to use for training, a value from (0, 1].
    pinned_memory_size: int [default=None]
        Size of additional CPU pinned memory used for GPU learning,
        usually is estimated automatically, thus usually should not be set.
    allow_writing_files : bool, [default=True]
        If this flag is set to False, no files with different diagnostic info will be created during training.
        With this flag no snapshotting can be done. Plus visualisation will not
        work, because visualisation uses files that are created and updated during training.
    final_ctr_computation_mode : string, [default='Default']
        Possible values:
            - 'Default' - Compute final ctrs for all pools.
            - 'Skip' - Skip final ctr computation. WARNING: model without ctrs can't be applied.
    approx_on_full_history : bool, [default=False]
        If this flag is set to True, each approximated value is calculated using all the preceeding rows in the fold (slower, more accurate).
        If this flag is set to False, each approximated value is calculated using only the beginning 1/fold_len_multiplier fraction of the fold (faster, slightly less accurate).
    boosting_type : string, default value depends on object count and feature count in train dataset and on learning mode.
        Boosting scheme.
        Possible values:
            - 'Ordered' - Gives better quality, but may slow down the training.
            - 'Plain' - The classic gradient boosting scheme. May result in quality degradation, but does not slow down the training.
    task_type : string, [default=None]
        The calcer type used to train the model.
        Possible values:
            - 'CPU'
            - 'GPU'
    device_config : string, [default=None], deprecated, use devices instead
    devices : list or string, [default=None], GPU devices to use.
        String format is: '0' for 1 device or '0:1:3' for multiple devices or '0-3' for range of devices.
        List format is : [0] for 1 device or [0,1,3] for multiple devices.

    bootstrap_type : string, Bayesian, Bernoulli, Poisson, MVS.
        Default bootstrap is Bayesian for GPU and MVS for CPU.
        Poisson bootstrap is supported only on GPU.
        MVS bootstrap is supported only on CPU.

    subsample : float, [default=None]
        Sample rate for bagging. This parameter can be used Poisson or Bernoully bootstrap types.

    mvs_reg : float, [default is set automatically at each iteration based on gradient distribution]
        Regularization parameter for MVS sampling algorithm

    monotone_constraints : list or numpy.ndarray or string or dict, [default=None]
        Monotone constraints for features.

    feature_weights : list or numpy.ndarray or string or dict, [default=None]
        Coefficient to multiply split gain with specific feature use. Should be non-negative.

    penalties_coefficient : float, [default=1]
        Common coefficient for all penalties. Should be non-negative.

    first_feature_use_penalties : list or numpy.ndarray or string or dict, [default=None]
        Penalties to first use of specific feature in model. Should be non-negative.

    per_object_feature_penalties : list or numpy.ndarray or string or dict, [default=None]
        Penalties for first use of feature for each object. Should be non-negative.

    sampling_frequency : string, [default=PerTree]
        Frequency to sample weights and objects when building trees.
        Possible values:
            - 'PerTree' - Before constructing each new tree
            - 'PerTreeLevel' - Before choosing each new split of a tree

    sampling_unit : string, [default='Object'].
        Possible values:
            - 'Object'
            - 'Group'
        The parameter allows to specify the sampling scheme:
        sample weights for each object individually or for an entire group of objects together.

    dev_score_calc_obj_block_size: int, [default=5000000]
        CPU only. Size of block of samples in score calculation. Should be > 0
        Used only for learning speed tuning.
        Changing this parameter can affect results due to numerical accuracy differences

    dev_efb_max_buckets : int, [default=1024]
        CPU only. Maximum bucket count in exclusive features bundle. Should be in an integer between 0 and 65536.
        Used only for learning speed tuning.

    sparse_features_conflict_fraction : float, [default=0.0]
        CPU only. Maximum allowed fraction of conflicting non-default values for features in exclusive features bundle.
        Should be a real value in [0, 1) interval.

    grow_policy : string, [SymmetricTree,Lossguide,Depthwise], [default=SymmetricTree]
        The tree growing policy. It describes how to perform greedy tree construction.

    min_data_in_leaf : int, [default=1].
        The minimum training samples count in leaf.
        CatBoost will not search for new splits in leaves with samples count less than min_data_in_leaf.
        This parameter is used only for Depthwise and Lossguide growing policies.

    max_leaves : int, [default=31],
        The maximum leaf count in resulting tree.
        This parameter is used only for Lossguide growing policy.

    score_function : string, possible values L2, Cosine, NewtonL2, NewtonCosine, [default=Cosine]
        For growing policy Lossguide default=NewtonL2.
        GPU only. Score that is used during tree construction to select the next tree split.

    max_depth : int, Synonym for depth.

    n_estimators : int, synonym for iterations.

    num_trees : int, synonym for iterations.

    num_boost_round : int, synonym for iterations.

    colsample_bylevel : float, synonym for rsm.

    random_state : int, synonym for random_seed.

    reg_lambda : float, synonym for l2_leaf_reg.

    objective : string, synonym for loss_function.

    num_leaves : int, synonym for max_leaves.

    min_child_samples : int, synonym for min_data_in_leaf

    eta : float, synonym for learning_rate.

    max_bin : float, synonym for border_count.

    scale_pos_weight : float, synonym for class_weights.
        Can be used only for binary classification. Sets weight multiplier for
        class 1 to scale_pos_weight value.

    metadata : dict, string to string key-value pairs to be stored in model metadata storage

    early_stopping_rounds : int
        Synonym for od_wait. Only one of these parameters should be set.

    cat_features : list or numpy.ndarray, [default=None]
        If not None, giving the list of Categ features indices or names (names are represented as strings).
        If it contains feature names, feature names must be defined for the training dataset passed to 'fit'.

    text_features : list or numpy.ndarray, [default=None]
        If not None, giving the list of Text features indices or names (names are represented as strings).
        If it contains feature names, feature names must be defined for the training dataset passed to 'fit'.

    embedding_features : list or numpy.ndarray, [default=None]
        If not None, giving the list of Embedding features indices or names (names are represented as strings).
        If it contains feature names, feature names must be defined for the training dataset passed to 'fit'.

    leaf_estimation_backtracking : string, [default=None]
        Type of backtracking during gradient descent.
        Possible values:
            - 'No' - never backtrack; supported on CPU and GPU
            - 'AnyImprovement' - reduce the descent step until the value of loss function is less than before the step; supported on CPU and GPU
            - 'Armijo' - reduce the descent step until Armijo condition is satisfied; supported on GPU only

    model_shrink_rate : float, [default=0]
        This parameter enables shrinkage of model at the start of each iteration. CPU only.
        For Constant mode shrinkage coefficient is calculated as (1 - model_shrink_rate * learning_rate).
        For Decreasing mode shrinkage coefficient is calculated as (1 - model_shrink_rate / iteration).
        Shrinkage coefficient should be in [0, 1).

    model_shrink_mode : string, [default=None]
        Mode of shrinkage coefficient calculation. CPU only.
        Possible values:
            - 'Constant' - Shrinkage coefficient is constant at each iteration.
            - 'Decreasing' - Shrinkage coefficient decreases at each iteration.

    langevin : bool, [default=False]
        Enables the Stochastic Gradient Langevin Boosting. CPU only.

    diffusion_temperature : float, [default=0]
        Langevin boosting diffusion temperature. CPU only.

    posterior_sampling : bool, [default=False]
        Set group of parameters for further use Uncertainty prediction:
            - Langevin = True
            - Model Shrink Rate = 1/(2N), where N is dataset size
            - Model Shrink Mode = Constant
            - Diffusion-temperature = N, where N is dataset size. CPU only.

    boost_from_average : bool, [default=True for RMSE, False for other losses]
        Enables to initialize approx values by best constant value for specified loss function.
        Available for RMSE, Logloss, CrossEntropy, Quantile and MAE.

    tokenizers : list of dicts,
        Each dict is a tokenizer description. Example:
        ```
        [
            {
                'tokenizer_id': 'Tokenizer',  # Tokeinzer identifier.
                'lowercasing': 'false',  # Possible values: 'true', 'false'.
                'number_process_policy': 'LeaveAsIs',  # Possible values: 'Skip', 'LeaveAsIs', 'Replace'.
                'number_token': '%',  # Rarely used character. Used in conjunction with Replace NumberProcessPolicy.
                'separator_type': 'ByDelimiter',  # Possible values: 'ByDelimiter', 'BySense'.
                'delimiter': ' ',  # Used in conjunction with ByDelimiter SeparatorType.
                'split_by_set': 'false',  # Each single character in delimiter used as individual delimiter.
                'skip_empty': 'true',  # Possible values: 'true', 'false'.
                'token_types': ['Word', 'Number', 'Unknown'],  # Used in conjunction with BySense SeparatorType.
                    # Possible values: 'Word', 'Number', 'Punctuation', 'SentenceBreak', 'ParagraphBreak', 'Unknown'.
                'subtokens_policy': 'SingleToken',  # Possible values:
                    # 'SingleToken' - All subtokens are interpreted as single token).
                    # 'SeveralTokens' - All subtokens are interpreted as several token.
            },
            ...
        ]
        ```

    dictionaries : list of dicts,
        Each dict is a tokenizer description. Example:
        ```
        [
            {
                'dictionary_id': 'Dictionary',  # Dictionary identifier.
                'token_level_type': 'Word',  # Possible values: 'Word', 'Letter'.
                'gram_order': '1',  # 1 for Unigram, 2 for Bigram, ...
                'skip_step': '0',  # 1 for 1-skip-gram, ...
                'end_of_word_token_policy': 'Insert',  # Possible values: 'Insert', 'Skip'.
                'end_of_sentence_token_policy': 'Skip',  # Possible values: 'Insert', 'Skip'.
                'occurrence_lower_bound': '3',  # The lower bound of token occurrences in the text to include it in the dictionary.
                'max_dictionary_size': '50000',  # The max dictionary size.
            },
            ...
        ]
        ```

    feature_calcers : list of strings,
        Each string is a calcer description. Example:
        ```
        [
            'NaiveBayes',
            'BM25',
            'BoW:top_tokens_count=2000',
        ]
        ```

    text_processing : dict,
        Text processging description.
        
    eval_fraction : float, [default=None]
        Fraction of the train dataset to be used as the evaluation dataset.
    """
    def __init__(self, iterations: Incomplete | None = None, learning_rate: Incomplete | None = None, depth: Incomplete | None = None, l2_leaf_reg: Incomplete | None = None, model_size_reg: Incomplete | None = None, rsm: Incomplete | None = None, loss_function: Incomplete | None = None, border_count: Incomplete | None = None, feature_border_type: Incomplete | None = None, per_float_feature_quantization: Incomplete | None = None, input_borders: Incomplete | None = None, output_borders: Incomplete | None = None, fold_permutation_block: Incomplete | None = None, od_pval: Incomplete | None = None, od_wait: Incomplete | None = None, od_type: Incomplete | None = None, nan_mode: Incomplete | None = None, counter_calc_method: Incomplete | None = None, leaf_estimation_iterations: Incomplete | None = None, leaf_estimation_method: Incomplete | None = None, thread_count: Incomplete | None = None, random_seed: Incomplete | None = None, use_best_model: Incomplete | None = None, best_model_min_trees: Incomplete | None = None, verbose: Incomplete | None = None, silent: Incomplete | None = None, logging_level: Incomplete | None = None, metric_period: Incomplete | None = None, ctr_leaf_count_limit: Incomplete | None = None, store_all_simple_ctr: Incomplete | None = None, max_ctr_complexity: Incomplete | None = None, has_time: Incomplete | None = None, allow_const_label: Incomplete | None = None, target_border: Incomplete | None = None, classes_count: Incomplete | None = None, class_weights: Incomplete | None = None, auto_class_weights: Incomplete | None = None, class_names: Incomplete | None = None, one_hot_max_size: Incomplete | None = None, random_strength: Incomplete | None = None, name: Incomplete | None = None, ignored_features: Incomplete | None = None, train_dir: Incomplete | None = None, custom_loss: Incomplete | None = None, custom_metric: Incomplete | None = None, eval_metric: Incomplete | None = None, bagging_temperature: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, fold_len_multiplier: Incomplete | None = None, used_ram_limit: Incomplete | None = None, gpu_ram_part: Incomplete | None = None, pinned_memory_size: Incomplete | None = None, allow_writing_files: Incomplete | None = None, final_ctr_computation_mode: Incomplete | None = None, approx_on_full_history: Incomplete | None = None, boosting_type: Incomplete | None = None, simple_ctr: Incomplete | None = None, combinations_ctr: Incomplete | None = None, per_feature_ctr: Incomplete | None = None, ctr_description: Incomplete | None = None, ctr_target_border_count: Incomplete | None = None, task_type: Incomplete | None = None, device_config: Incomplete | None = None, devices: Incomplete | None = None, bootstrap_type: Incomplete | None = None, subsample: Incomplete | None = None, mvs_reg: Incomplete | None = None, sampling_unit: Incomplete | None = None, sampling_frequency: Incomplete | None = None, dev_score_calc_obj_block_size: Incomplete | None = None, dev_efb_max_buckets: Incomplete | None = None, sparse_features_conflict_fraction: Incomplete | None = None, max_depth: Incomplete | None = None, n_estimators: Incomplete | None = None, num_boost_round: Incomplete | None = None, num_trees: Incomplete | None = None, colsample_bylevel: Incomplete | None = None, random_state: Incomplete | None = None, reg_lambda: Incomplete | None = None, objective: Incomplete | None = None, eta: Incomplete | None = None, max_bin: Incomplete | None = None, scale_pos_weight: Incomplete | None = None, gpu_cat_features_storage: Incomplete | None = None, data_partition: Incomplete | None = None, metadata: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, cat_features: Incomplete | None = None, grow_policy: Incomplete | None = None, min_data_in_leaf: Incomplete | None = None, min_child_samples: Incomplete | None = None, max_leaves: Incomplete | None = None, num_leaves: Incomplete | None = None, score_function: Incomplete | None = None, leaf_estimation_backtracking: Incomplete | None = None, ctr_history_unit: Incomplete | None = None, monotone_constraints: Incomplete | None = None, feature_weights: Incomplete | None = None, penalties_coefficient: Incomplete | None = None, first_feature_use_penalties: Incomplete | None = None, per_object_feature_penalties: Incomplete | None = None, model_shrink_rate: Incomplete | None = None, model_shrink_mode: Incomplete | None = None, langevin: Incomplete | None = None, diffusion_temperature: Incomplete | None = None, posterior_sampling: Incomplete | None = None, boost_from_average: Incomplete | None = None, text_features: Incomplete | None = None, tokenizers: Incomplete | None = None, dictionaries: Incomplete | None = None, feature_calcers: Incomplete | None = None, text_processing: Incomplete | None = None, embedding_features: Incomplete | None = None, callback: Incomplete | None = None, eval_fraction: Incomplete | None = None) -> None: ...
    def fit(self, X, y: Incomplete | None = None, cat_features: Incomplete | None = None, text_features: Incomplete | None = None, embedding_features: Incomplete | None = None, sample_weight: Incomplete | None = None, baseline: Incomplete | None = None, use_best_model: Incomplete | None = None, eval_set: Incomplete | None = None, verbose: Incomplete | None = None, logging_level: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, column_description: Incomplete | None = None, verbose_eval: Incomplete | None = None, metric_period: Incomplete | None = None, silent: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, init_model: Incomplete | None = None, callbacks: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Fit the CatBoostClassifier model.

        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            If not catboost.Pool, 2 dimensional Feature matrix or string - file with dataset.

        y : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Labels, 1 dimensional array like.
            Use only if X is not catboost.Pool.

        cat_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Categ columns indices.
            Use only if X is not catboost.Pool.

        text_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Text columns indices.
            Use only if X is not catboost.Pool.

        embedding_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Embedding columns indices.
            Use only if X is not catboost.Pool.

        sample_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Instance weights, 1 dimensional array like.

        baseline : list or numpy.ndarray, optional (default=None)
            If not None, giving 2 dimensional array like data.
            Use only if X is not catboost.Pool.

        use_best_model : bool, optional (default=None)
            Flag to use best model

        eval_set : catboost.Pool or list, optional (default=None)
            A list of (X, y) tuple pairs to use as a validation set for early-stopping

        metric_period : int
            Frequency of evaluating metrics.

        verbose : bool or int
            If verbose is bool, then if set to True, logging_level is set to Verbose,
            if set to False, logging_level is set to Silent.
            If verbose is int, it determines the frequency of writing metrics to output and
            logging_level is set to Verbose.

        silent : bool
            If silent is True, logging_level is set to Silent.
            If silent is False, logging_level is set to Verbose.

        logging_level : string, optional (default=None)
            Possible values:
                - 'Silent'
                - 'Verbose'
                - 'Info'
                - 'Debug'

        plot : bool, optional (default=False)
            If True, draw train and eval error in Jupyter notebook

        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error graphs to file

        verbose_eval : bool or int
            Synonym for verbose. Only one of these parameters should be set.

        early_stopping_rounds : int
            Activates Iter overfitting detector with od_wait set to early_stopping_rounds.

        save_snapshot : bool, [default=None]
            Enable progress snapshotting for restoring progress after crashes or interruptions

        snapshot_file : string or pathlib.Path, [default=None]
            Learn progress snapshot file path, if None will use default filename

        snapshot_interval: int, [default=600]
            Interval between saving snapshots (seconds)

        init_model : CatBoost class or string or pathlib.Path, [default=None]
            Continue training starting from the existing model.
            If this parameter is a string or pathlib.Path, load initial model from the path specified by this string.

        callbacks : list, optional (default=None)
            List of callback objects that are applied at end of each iteration.

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        model : CatBoost
        """
    def predict(self, data, prediction_type: str = 'Class', ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: Incomplete | None = None, task_type: str = 'CPU'):
        """
        Predict with data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        prediction_type : string, optional (default='Class')
            Can be:
            - 'RawFormulaVal' : return raw formula value.
            - 'Class' : return class label.
            - 'Probability' : return probability for every class.
            - 'LogProbability' : return log probability for every class.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool, optional (default=False)
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction:
            If data is for a single object, the return value depends on prediction_type value:
                - 'RawFormulaVal' : return raw formula value.
                - 'Class' : return class label.
                - 'Probability' : return one-dimensional numpy.ndarray with probability for every class.
                - 'LogProbability' : return one-dimensional numpy.ndarray with
                  log probability for every class.
            otherwise numpy.ndarray, with values that depend on prediction_type value:
                - 'RawFormulaVal' : one-dimensional array of raw formula value for each object.
                - 'Class' : one-dimensional array of class label for each object.
                - 'Probability' : two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                  with probability for every class for each object.
                - 'LogProbability' : two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                  with log probability for every class for each object.
        """
    def predict_proba(self, X, ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: Incomplete | None = None, task_type: str = 'CPU'):
        """
        Predict class probability with X.

        Parameters
        ----------
        X : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If X is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction :
            If X is for a single object
                return one-dimensional numpy.ndarray with probability for every class.
            otherwise
                return two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                with probability for every class for each object.
        """
    def predict_log_proba(self, data, ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: Incomplete | None = None, task_type: str = 'CPU'):
        """
        Predict class log probability with data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction :
            If data is for a single object
                return one-dimensional numpy.ndarray with log probability for every class.
            otherwise
                return two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                with log probability for every class for each object.
        """
    def staged_predict(self, data, prediction_type: str = 'Class', ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict target at each stage for data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        prediction_type : string, optional (default='Class')
            Can be:
            - 'RawFormulaVal' : return raw formula value.
            - 'Class' : return class label.
            - 'Probability' : return probability for every class.
            - 'LogProbability' : return log probability for every class.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction : generator for each iteration that generates:
            If data is for a single object, the return value depends on prediction_type value:
                - 'RawFormulaVal' : return raw formula value.
                - 'Class' : return majority vote class.
                - 'Probability' : return one-dimensional numpy.ndarray with probability for every class.
                - 'LogProbability' : return one-dimensional numpy.ndarray with
                  log probability for every class.
            otherwise numpy.ndarray, with values that depend on prediction_type value:
                - 'RawFormulaVal' : one-dimensional array of raw formula value for each object.
                - 'Class' : one-dimensional array of class label for each object.
                - 'Probability' : two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                  with probability for every class for each object.
                - 'LogProbability' : two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                  with log probability for every class for each object.
        """
    def staged_predict_proba(self, data, ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict classification target at each stage for data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction : generator for each iteration that generates:
            If data is for a single object
                return one-dimensional numpy.ndarray with probability for every class.
            otherwise
                return two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                with probability for every class for each object.
        """
    def staged_predict_log_proba(self, data, ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict classification target at each stage for data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction : generator for each iteration that generates:
            If data is for a single object
                return one-dimensional numpy.ndarray with log probability for every class.
            otherwise
                return two-dimensional numpy.ndarray with shape (number_of_objects x number_of_classes)
                with log probability for every class for each object.
        """
    def score(self, X, y: Incomplete | None = None):
        """
        Calculate accuracy.

        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            Data to apply model on.
        y : list or numpy.ndarray
            True labels.

        Returns
        -------
        accuracy : float
        """
    def set_probability_threshold(self, binclass_probability_threshold: Incomplete | None = None) -> None:
        """
        Set a threshold for class separation in binary classification task for a trained model.
        :param binclass_probability_threshold: float number in [0, 1] or None to discard it
        """
    def get_probability_threshold(self):
        """
        Get a threshold for class separation in binary classification task
        """

class CatBoostRegressor(CatBoost):
    """
    Implementation of the scikit-learn API for CatBoost regression.

    Parameters
    ----------
    Like in CatBoostClassifier, except loss_function, classes_count, class_names and class_weights

    loss_function : string, [default='RMSE']
        'RMSE'
        'MAE'
        'Quantile:alpha=value'
        'LogLinQuantile:alpha=value'
        'Poisson'
        'MAPE'
        'Lq:q=value'
        'SurvivalAft:dist=value;scale=value'
    """
    def __init__(self, iterations: Incomplete | None = None, learning_rate: Incomplete | None = None, depth: Incomplete | None = None, l2_leaf_reg: Incomplete | None = None, model_size_reg: Incomplete | None = None, rsm: Incomplete | None = None, loss_function: str = 'RMSE', border_count: Incomplete | None = None, feature_border_type: Incomplete | None = None, per_float_feature_quantization: Incomplete | None = None, input_borders: Incomplete | None = None, output_borders: Incomplete | None = None, fold_permutation_block: Incomplete | None = None, od_pval: Incomplete | None = None, od_wait: Incomplete | None = None, od_type: Incomplete | None = None, nan_mode: Incomplete | None = None, counter_calc_method: Incomplete | None = None, leaf_estimation_iterations: Incomplete | None = None, leaf_estimation_method: Incomplete | None = None, thread_count: Incomplete | None = None, random_seed: Incomplete | None = None, use_best_model: Incomplete | None = None, best_model_min_trees: Incomplete | None = None, verbose: Incomplete | None = None, silent: Incomplete | None = None, logging_level: Incomplete | None = None, metric_period: Incomplete | None = None, ctr_leaf_count_limit: Incomplete | None = None, store_all_simple_ctr: Incomplete | None = None, max_ctr_complexity: Incomplete | None = None, has_time: Incomplete | None = None, allow_const_label: Incomplete | None = None, target_border: Incomplete | None = None, one_hot_max_size: Incomplete | None = None, random_strength: Incomplete | None = None, name: Incomplete | None = None, ignored_features: Incomplete | None = None, train_dir: Incomplete | None = None, custom_metric: Incomplete | None = None, eval_metric: Incomplete | None = None, bagging_temperature: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, fold_len_multiplier: Incomplete | None = None, used_ram_limit: Incomplete | None = None, gpu_ram_part: Incomplete | None = None, pinned_memory_size: Incomplete | None = None, allow_writing_files: Incomplete | None = None, final_ctr_computation_mode: Incomplete | None = None, approx_on_full_history: Incomplete | None = None, boosting_type: Incomplete | None = None, simple_ctr: Incomplete | None = None, combinations_ctr: Incomplete | None = None, per_feature_ctr: Incomplete | None = None, ctr_description: Incomplete | None = None, ctr_target_border_count: Incomplete | None = None, task_type: Incomplete | None = None, device_config: Incomplete | None = None, devices: Incomplete | None = None, bootstrap_type: Incomplete | None = None, subsample: Incomplete | None = None, mvs_reg: Incomplete | None = None, sampling_frequency: Incomplete | None = None, sampling_unit: Incomplete | None = None, dev_score_calc_obj_block_size: Incomplete | None = None, dev_efb_max_buckets: Incomplete | None = None, sparse_features_conflict_fraction: Incomplete | None = None, max_depth: Incomplete | None = None, n_estimators: Incomplete | None = None, num_boost_round: Incomplete | None = None, num_trees: Incomplete | None = None, colsample_bylevel: Incomplete | None = None, random_state: Incomplete | None = None, reg_lambda: Incomplete | None = None, objective: Incomplete | None = None, eta: Incomplete | None = None, max_bin: Incomplete | None = None, gpu_cat_features_storage: Incomplete | None = None, data_partition: Incomplete | None = None, metadata: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, cat_features: Incomplete | None = None, grow_policy: Incomplete | None = None, min_data_in_leaf: Incomplete | None = None, min_child_samples: Incomplete | None = None, max_leaves: Incomplete | None = None, num_leaves: Incomplete | None = None, score_function: Incomplete | None = None, leaf_estimation_backtracking: Incomplete | None = None, ctr_history_unit: Incomplete | None = None, monotone_constraints: Incomplete | None = None, feature_weights: Incomplete | None = None, penalties_coefficient: Incomplete | None = None, first_feature_use_penalties: Incomplete | None = None, per_object_feature_penalties: Incomplete | None = None, model_shrink_rate: Incomplete | None = None, model_shrink_mode: Incomplete | None = None, langevin: Incomplete | None = None, diffusion_temperature: Incomplete | None = None, posterior_sampling: Incomplete | None = None, boost_from_average: Incomplete | None = None, text_features: Incomplete | None = None, tokenizers: Incomplete | None = None, dictionaries: Incomplete | None = None, feature_calcers: Incomplete | None = None, text_processing: Incomplete | None = None, embedding_features: Incomplete | None = None, eval_fraction: Incomplete | None = None) -> None: ...
    def fit(self, X, y: Incomplete | None = None, cat_features: Incomplete | None = None, text_features: Incomplete | None = None, embedding_features: Incomplete | None = None, sample_weight: Incomplete | None = None, baseline: Incomplete | None = None, use_best_model: Incomplete | None = None, eval_set: Incomplete | None = None, verbose: Incomplete | None = None, logging_level: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, column_description: Incomplete | None = None, verbose_eval: Incomplete | None = None, metric_period: Incomplete | None = None, silent: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, init_model: Incomplete | None = None, callbacks: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Fit the CatBoost model.

        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            If not catboost.Pool, 2 dimensional Feature matrix or string - file with dataset.

        y : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Labels, 1 dimensional array like.
            Use only if X is not catboost.Pool.

        cat_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Categ columns indices.
            Use only if X is not catboost.Pool.
            
        text_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Text columns indices.
            Use only if X is not catboost.Pool.
        
        embedding_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Embedding columns indices.
            Use only if X is not catboost.Pool.

        sample_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Instance weights, 1 dimensional array like.

        baseline : list or numpy.ndarray, optional (default=None)
            If not None, giving 2 dimensional array like data.
            Use only if X is not catboost.Pool.

        use_best_model : bool, optional (default=None)
            Flag to use best model

        eval_set : catboost.Pool or list, optional (default=None)
            A list of (X, y) tuple pairs to use as a validation set for
            early-stopping

        metric_period : int
            Frequency of evaluating metrics.

        verbose : bool or int
            If verbose is bool, then if set to True, logging_level is set to Verbose,
            if set to False, logging_level is set to Silent.
            If verbose is int, it determines the frequency of writing metrics to output and
            logging_level is set to Verbose.

        silent : bool
            If silent is True, logging_level is set to Silent.
            If silent is False, logging_level is set to Verbose.

        logging_level : string, optional (default=None)
            Possible values:
                - 'Silent'
                - 'Verbose'
                - 'Info'
                - 'Debug'

        plot : bool, optional (default=False)
            If True, draw train and eval error in Jupyter notebook
            
        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error graphs to file (requires installed plotly)

        verbose_eval : bool or int
            Synonym for verbose. Only one of these parameters should be set.

        early_stopping_rounds : int
            Activates Iter overfitting detector with od_wait set to early_stopping_rounds.

        save_snapshot : bool, [default=None]
            Enable progress snapshotting for restoring progress after crashes or interruptions

        snapshot_file : string or pathlib.Path, [default=None]
            Learn progress snapshot file path, if None will use default filename

        snapshot_interval: int, [default=600]
            Interval between saving snapshots (seconds)

        init_model : CatBoost class or string or pathlib.Path, [default=None]
            Continue training starting from the existing model.
            If this parameter is a string or pathlib.Path, load initial model from the path specified by this string.

        callbacks : list, optional (default=None)
            List of callback objects that are applied at end of each iteration.

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        model : CatBoost
        """
    def predict(self, data, prediction_type: Incomplete | None = None, ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: Incomplete | None = None, task_type: str = 'CPU'):
        """
        Predict with data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        prediction_type : string, optional (default='RawFormulaVal')
            Can be:
            - 'RawFormulaVal' : return raw formula value.
            - 'Exponent' : return Exponent of raw formula value.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction :
            If data is for a single object, the return value is single float formula return value
            otherwise one-dimensional numpy.ndarray of formula return values for each object.
        """
    def staged_predict(self, data, prediction_type: str = 'RawFormulaVal', ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict target at each stage for data.

        Parameters
        ----------
        data : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.

        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.

        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).

        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.

        verbose : bool
            If True, writes the evaluation metric measured set to stderr.

        Returns
        -------
        prediction : generator for each iteration that generates:
            If data is for a single object, the return value is single float formula return value
            otherwise one-dimensional numpy.ndarray of formula return values for each object.
        """
    def score(self, X, y: Incomplete | None = None):
        """
        Calculate R^2.

        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            Data to apply model on.
        y : list or numpy.ndarray
            True labels.

        Returns
        -------
        R^2 : float
        """

class CatBoostRanker(CatBoost):
    """
    Implementation of the scikit-learn API for CatBoost ranking.
    Parameters
    ----------
    Like in CatBoostClassifier, except loss_function, classes_count, class_names and class_weights
    loss_function : string, [default='YetiRank']
        'YetiRank'
        'YetiRankPairwise'
        'StochasticFilter'
        'StochasticRank'
        'QueryCrossEntropy'
        'QueryRMSE'
        'QuerySoftMax'
        'PairLogit'
        'PairLogitPairwise'
    """
    def __init__(self, iterations: Incomplete | None = None, learning_rate: Incomplete | None = None, depth: Incomplete | None = None, l2_leaf_reg: Incomplete | None = None, model_size_reg: Incomplete | None = None, rsm: Incomplete | None = None, loss_function: str = 'YetiRank', border_count: Incomplete | None = None, feature_border_type: Incomplete | None = None, per_float_feature_quantization: Incomplete | None = None, input_borders: Incomplete | None = None, output_borders: Incomplete | None = None, fold_permutation_block: Incomplete | None = None, od_pval: Incomplete | None = None, od_wait: Incomplete | None = None, od_type: Incomplete | None = None, nan_mode: Incomplete | None = None, counter_calc_method: Incomplete | None = None, leaf_estimation_iterations: Incomplete | None = None, leaf_estimation_method: Incomplete | None = None, thread_count: Incomplete | None = None, random_seed: Incomplete | None = None, use_best_model: Incomplete | None = None, best_model_min_trees: Incomplete | None = None, verbose: Incomplete | None = None, silent: Incomplete | None = None, logging_level: Incomplete | None = None, metric_period: Incomplete | None = None, ctr_leaf_count_limit: Incomplete | None = None, store_all_simple_ctr: Incomplete | None = None, max_ctr_complexity: Incomplete | None = None, has_time: Incomplete | None = None, allow_const_label: Incomplete | None = None, target_border: Incomplete | None = None, one_hot_max_size: Incomplete | None = None, random_strength: Incomplete | None = None, name: Incomplete | None = None, ignored_features: Incomplete | None = None, train_dir: Incomplete | None = None, custom_metric: Incomplete | None = None, eval_metric: Incomplete | None = None, bagging_temperature: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, fold_len_multiplier: Incomplete | None = None, used_ram_limit: Incomplete | None = None, gpu_ram_part: Incomplete | None = None, pinned_memory_size: Incomplete | None = None, allow_writing_files: Incomplete | None = None, final_ctr_computation_mode: Incomplete | None = None, approx_on_full_history: Incomplete | None = None, boosting_type: Incomplete | None = None, simple_ctr: Incomplete | None = None, combinations_ctr: Incomplete | None = None, per_feature_ctr: Incomplete | None = None, ctr_description: Incomplete | None = None, ctr_target_border_count: Incomplete | None = None, task_type: Incomplete | None = None, device_config: Incomplete | None = None, devices: Incomplete | None = None, bootstrap_type: Incomplete | None = None, subsample: Incomplete | None = None, mvs_reg: Incomplete | None = None, sampling_frequency: Incomplete | None = None, sampling_unit: Incomplete | None = None, dev_score_calc_obj_block_size: Incomplete | None = None, dev_efb_max_buckets: Incomplete | None = None, sparse_features_conflict_fraction: Incomplete | None = None, max_depth: Incomplete | None = None, n_estimators: Incomplete | None = None, num_boost_round: Incomplete | None = None, num_trees: Incomplete | None = None, colsample_bylevel: Incomplete | None = None, random_state: Incomplete | None = None, reg_lambda: Incomplete | None = None, objective: Incomplete | None = None, eta: Incomplete | None = None, max_bin: Incomplete | None = None, gpu_cat_features_storage: Incomplete | None = None, data_partition: Incomplete | None = None, metadata: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, cat_features: Incomplete | None = None, grow_policy: Incomplete | None = None, min_data_in_leaf: Incomplete | None = None, min_child_samples: Incomplete | None = None, max_leaves: Incomplete | None = None, num_leaves: Incomplete | None = None, score_function: Incomplete | None = None, leaf_estimation_backtracking: Incomplete | None = None, ctr_history_unit: Incomplete | None = None, monotone_constraints: Incomplete | None = None, feature_weights: Incomplete | None = None, penalties_coefficient: Incomplete | None = None, first_feature_use_penalties: Incomplete | None = None, per_object_feature_penalties: Incomplete | None = None, model_shrink_rate: Incomplete | None = None, model_shrink_mode: Incomplete | None = None, langevin: Incomplete | None = None, diffusion_temperature: Incomplete | None = None, posterior_sampling: Incomplete | None = None, boost_from_average: Incomplete | None = None, text_features: Incomplete | None = None, tokenizers: Incomplete | None = None, dictionaries: Incomplete | None = None, feature_calcers: Incomplete | None = None, text_processing: Incomplete | None = None, embedding_features: Incomplete | None = None, eval_fraction: Incomplete | None = None) -> None: ...
    def fit(self, X, y: Incomplete | None = None, group_id: Incomplete | None = None, cat_features: Incomplete | None = None, text_features: Incomplete | None = None, embedding_features: Incomplete | None = None, pairs: Incomplete | None = None, sample_weight: Incomplete | None = None, group_weight: Incomplete | None = None, subgroup_id: Incomplete | None = None, pairs_weight: Incomplete | None = None, baseline: Incomplete | None = None, use_best_model: Incomplete | None = None, eval_set: Incomplete | None = None, verbose: Incomplete | None = None, logging_level: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, column_description: Incomplete | None = None, verbose_eval: Incomplete | None = None, metric_period: Incomplete | None = None, silent: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, init_model: Incomplete | None = None, callbacks: Incomplete | None = None, log_cout=..., log_cerr=...):
        """
        Fit the CatBoostRanker model.
        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            If not catboost.Pool, 2 dimensional Feature matrix or string - file with dataset.
        y : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Labels, 1 dimensional array like.
            Use only if X is not catboost.Pool.
        group_id : numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Ranking groups, 1 dimensional array like.
            Use only if X is not catboost.Pool.
        cat_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Categ columns indices.
            Use only if X is not catboost.Pool.
        text_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Text columns indices.
            Use only if X is not catboost.Pool.
        embedding_features : list or numpy.ndarray, optional (default=None)
            If not None, giving the list of Embedding columns indices.
            Use only if X is not catboost.Pool.
        pairs : list or numpy.ndarray or pandas.DataFrame, optional (default=None)
            The pairs description in the form of a two-dimensional matrix of shape N by 2:
            N is the number of pairs.
            The first element of the pair is the zero-based index of the winner object from the input dataset for pairwise comparison.
            The second element of the pair is the zero-based index of the loser object from the input dataset for pairwise comparison.
        sample_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
            Instance weights, 1 dimensional array like.
        group_weight : list or numpy.ndarray (default=None)
            The weights of all objects within the defined groups from the input data in the form of one-dimensional array-like data.
            Used for calculating the final values of trees. By default, it is set to 1 for all objects in all groups.
            Only a weight or group_weight parameter can be used at a time
        subgroup_id : list or numpy.ndarray (default=None)
            Subgroup identifiers for all input objects. Supported identifier types are:
            int
            string types (string or unicode for Python 2 and bytes or string for Python 3).
        pairs_weight : list or numpy.ndarray (default=None)
            The weight of each input pair of objects in the form of one-dimensional array-like pairs.
            The number of given values must match the number of specified pairs.
            This information is used for calculation and optimization of Pairwise metrics .
            By default, it is set to 1 for all pairs.
        baseline : list or numpy.ndarray, optional (default=None)
            If not None, giving 2 dimensional array like data.
            Use only if X is not catboost.Pool.
        use_best_model : bool, optional (default=None)
            Flag to use best model
        eval_set : catboost.Pool or list, optional (default=None)
            A list of (X, y) tuple pairs to use as a validation set for early-stopping
        verbose : bool or int
            If verbose is bool, then if set to True, logging_level is set to Verbose,
            if set to False, logging_level is set to Silent.
            If verbose is int, it determines the frequency of writing metrics to output and
            logging_level is set to Verbose.
        logging_level : string, optional (default=None)
            Possible values:
                - 'Silent'
                - 'Verbose'
                - 'Info'
                - 'Debug'
        plot : bool, optional (default=False)
            If True, draw train and eval error in Jupyter notebook
        plot_file : file-like or str, optional (default=None)
            If not None, save train and eval error graphs to file
        verbose_eval : bool or int
            Synonym for verbose. Only one of these parameters should be set.
        metric_period : int
            Frequency of evaluating metrics.
        silent : bool
            If silent is True, logging_level is set to Silent.
            If silent is False, logging_level is set to Verbose.
        early_stopping_rounds : int
            Activates Iter overfitting detector with od_wait set to early_stopping_rounds.
        save_snapshot : bool, [default=None]
            Enable progress snapshotting for restoring progress after crashes or interruptions
        snapshot_file : string or pathlib.Path, [default=None]
            Learn progress snapshot file path, if None will use default filename
        snapshot_interval: int, [default=600]
            Interval between saving snapshots (seconds)
        init_model : CatBoost class or string or pathlib.Path, [default=None]
            Continue training starting from the existing model.
            If this parameter is a string or pathlib.Path, load initial model from the path specified by this string.
        callbacks : list, optional (default=None)
            List of callback objects that are applied at end of each iteration.

        log_cout: output stream or callback for logging

        log_cerr: error stream or callback for logging

        Returns
        -------
        model : CatBoost
        """
    def predict(self, X, ntree_start: int = 0, ntree_end: int = 0, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict with data.
        Parameters
        ----------
        X : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.
        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.
        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.
        verbose : bool
            If True, writes the evaluation metric measured set to stderr.
        Returns
        -------
        prediction :
            If data is for a single object, the return value is single float formula return value
            otherwise one-dimensional numpy.ndarray of formula return values for each object.
        """
    def staged_predict(self, X, ntree_start: int = 0, ntree_end: int = 0, eval_period: int = 1, thread_count: int = -1, verbose: Incomplete | None = None):
        """
        Predict target at each stage for data.
        Parameters
        ----------
        X : catboost.Pool or list of features or list of lists or numpy.ndarray or pandas.DataFrame or pandas.Series
                or catboost.FeaturesData
            Data to apply model on.
            If data is a simple list (not list of lists) or a one-dimensional numpy.ndarray it is interpreted
            as a list of features for a single object.
        ntree_start: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
        ntree_end: int, optional (default=0)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
            If value equals to 0 this parameter is ignored and ntree_end equal to tree_count_.
        eval_period: int, optional (default=1)
            Model is applied on the interval [ntree_start, ntree_end) with the step eval_period (zero-based indexing).
        thread_count : int (default=-1)
            The number of threads to use when applying the model.
            Allows you to optimize the speed of execution. This parameter doesn't affect results.
            If -1, then the number of threads is set to the number of CPU cores.
        verbose : bool
            If True, writes the evaluation metric measured set to stderr.
        Returns
        -------
        prediction : generator for each iteration that generates:
            If data is for a single object, the return value is single float formula return value
            otherwise one-dimensional numpy.ndarray of formula return values for each object.
        """
    def score(self, X, y: Incomplete | None = None, group_id: Incomplete | None = None, top: Incomplete | None = None, type: Incomplete | None = None, denominator: Incomplete | None = None, group_weight: Incomplete | None = None, thread_count: int = -1):
        """
        Calculate NDCG@top
        Parameters
        ----------
        X : catboost.Pool or list or numpy.ndarray or pandas.DataFrame or pandas.Series
            Data to apply model on.
        y : list or numpy.ndarrays or pandas.DataFrame or pandas.Series
            True labels.
        group_id : list or numpy.ndarray or pandas.DataFrame or pandas.Series
            Ranking groups. If X is a Pool, group_id must be defined into X
        top : unsigned integer, up to `pow(2, 32) / 2 - 1`
            NDCG, Number of top-ranked objects to calculate NDCG
        type : str
            NDCG, Metric_type: 'Base' or 'Exp'
        denominator : str
            NDCG, Denominator type: 'LogPosition' or 'Position'
        group_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series
            Group weights.
        thread_count : int, optional (default=-1)
            Number of threads to work with.
        Returns
        -------
        NDCG@top : float
                   higher is better
        """

def train(pool: Incomplete | None = None, params: Incomplete | None = None, dtrain: Incomplete | None = None, logging_level: Incomplete | None = None, verbose: Incomplete | None = None, iterations: Incomplete | None = None, num_boost_round: Incomplete | None = None, evals: Incomplete | None = None, eval_set: Incomplete | None = None, plot: Incomplete | None = None, plot_file: Incomplete | None = None, verbose_eval: Incomplete | None = None, metric_period: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, init_model: Incomplete | None = None, log_cout=..., log_cerr=...):
    """
    Train CatBoost model.

    Parameters
    ----------
    params : dict
        Parameters for CatBoost.
        If  None, all params are set to their defaults.
        If  dict, overriding parameters present in the dict.

    pool : catboost.Pool or tuple (X, y)
        Data to train on.

    iterations : int
        Number of boosting iterations. Can be set in params dict.

    evals : catboost.Pool or tuple (X, y)
        Synonym for eval_set. Only one of these parameters should be set.

    dtrain : catboost.Pool or tuple (X, y)
        Synonym for pool parameter. Only one of these parameters should be set.

    logging_level : string, optional (default=None)
        Possible values:
            - 'Silent'
            - 'Verbose'
            - 'Info'
            - 'Debug'

    metric_period : int
        Frequency of evaluating metrics.

    verbose : bool or int
        If verbose is bool, then if set to True, logging_level is set to Verbose,
        if set to False, logging_level is set to Silent.
        If verbose is int, it determines the frequency of writing metrics to output and
        logging_level is set to Verbose.

    verbose_eval : bool or int
        Synonym for verbose. Only one of these parameters should be set.

    iterations : int
        Number of boosting iterations. Can be set in params dict.

    num_boost_round : int
        Synonym for iterations. Only one of these parameters should be set.

    eval_set : catboost.Pool or tuple (X, y) or list [(X, y)]
        Dataset for evaluation.

    plot : bool, optional (default=False)
        If True, draw train and eval error in Jupyter notebook
`
    plot_file : file-like or str, optional (default=None)
        If not None, save train and eval error graphs to file

    early_stopping_rounds : int
        Activates Iter overfitting detector with od_wait set to early_stopping_rounds.

    save_snapshot : bool, [default=None]
        Enable progress snapshotting for restoring progress after crashes or interruptions

    snapshot_file : string or pathlib.Path, [default=None]
        Learn progress snapshot file path, if None will use default filename

    snapshot_interval: int, [default=600]
        Interval between saving snapshots (seconds)

    init_model : CatBoost class or string or pathlib.Path, [default=None]
        Continue training starting from the existing model.
        If this parameter is a string or pathlib.Path, load initial model from the path specified by this string.

    log_cout: output stream or callback for logging

    log_cerr: error stream or callback for logging

    Returns
    -------
    model : CatBoost class
    """
def cv(pool: Incomplete | None = None, params: Incomplete | None = None, dtrain: Incomplete | None = None, iterations: Incomplete | None = None, num_boost_round: Incomplete | None = None, fold_count: Incomplete | None = None, nfold: Incomplete | None = None, inverted: bool = False, partition_random_seed: int = 0, seed: Incomplete | None = None, shuffle: bool = True, logging_level: Incomplete | None = None, stratified: Incomplete | None = None, as_pandas: bool = True, metric_period: Incomplete | None = None, verbose: Incomplete | None = None, verbose_eval: Incomplete | None = None, plot: bool = False, plot_file: Incomplete | None = None, early_stopping_rounds: Incomplete | None = None, save_snapshot: Incomplete | None = None, snapshot_file: Incomplete | None = None, snapshot_interval: Incomplete | None = None, metric_update_interval: float = 0.5, folds: Incomplete | None = None, type: str = 'Classical', return_models: bool = False, log_cout=..., log_cerr=...):
    """
    Cross-validate the CatBoost model.

    Parameters
    ----------
    pool : catboost.Pool
        Data to cross-validate on.

    params : dict
        Parameters for CatBoost.
        CatBoost has many of parameters, all have default values.
        If  None, all params still defaults.
        If  dict, overriding some (or all) params.

    dtrain : catboost.Pool or tuple (X, y)
        Synonym for pool parameter. Only one of these parameters should be set.

    iterations : int
        Number of boosting iterations. Can be set in params dict.

    num_boost_round : int
        Synonym for iterations. Only one of these parameters should be set.

    fold_count : int, optional (default=3)
        The number of folds to split the dataset into.

    nfold : int
        Synonym for fold_count.

    type : string, optional (default='Classical')
        Type of cross-validation
        Possible values:
            - 'Classical'
            - 'Inverted'
            - 'TimeSeries'

    inverted : bool, optional (default=False)
        Train on the test fold and evaluate the model on the training folds.

    partition_random_seed : int, optional (default=0)
        Use this as the seed value for random permutation of the data.
        Permutation is performed before splitting the data for cross validation.
        Each seed generates unique data splits.

    seed : int, optional
        Synonym for partition_random_seed. This parameter is deprecated. Use
        partition_random_seed instead.
        If both parameters are initialised partition_random_seed parameter is
        ignored.

    shuffle : bool, optional (default=True)
        Shuffle the dataset objects before splitting into folds.

    logging_level : string, optional (default=None)
        Possible values:
            - 'Silent'
            - 'Verbose'
            - 'Info'
            - 'Debug'

    stratified : bool, optional (default=None)
        Perform stratified sampling. True for classification and False otherwise.

    as_pandas : bool, optional (default=True)
        Return pd.DataFrame when pandas is installed.
        If False or pandas is not installed, return dict.

    metric_period : int, [default=1]
        The frequency of iterations to print the information to stdout. The value should be a positive integer.

    verbose : bool or int
        If verbose is bool, then if set to True, logging_level is set to Verbose,
        if set to False, logging_level is set to Silent.
        If verbose is int, it determines the frequency of writing metrics to output and
        logging_level is set to Verbose.

    verbose_eval : bool or int
        Synonym for verbose. Only one of these parameters should be set.

    plot : bool, optional (default=False)
        If True, draw train and eval error in Jupyter notebook

    plot_file : file-like or str, optional (default=None)
        If not None, save train and eval error graphs to file

    early_stopping_rounds : int
        Activates Iter overfitting detector with od_wait set to early_stopping_rounds.

    save_snapshot : bool, [default=None]
        Enable progress snapshotting for restoring progress after crashes or interruptions

    snapshot_file : string or pathlib.Path, [default=None]
        Learn progress snapshot file path, if None will use default filename

    snapshot_interval: int, [default=600]
        Interval between saving snapshots (seconds)

    metric_update_interval: float, [default=0.5]
        Interval between updating metrics (seconds)

    folds: generator or iterator of (train_idx, test_idx) tuples, scikit-learn splitter object or None, optional (default=None)
        If generator or iterator, it should yield the train and test indices for each fold.
        If object, it should be one of the scikit-learn splitter classes
        (https://scikit-learn.org/stable/modules/classes.html#splitter-classes)
        and have ``split`` method.
        if folds is not None, then all of fold_count, shuffle, partition_random_seed, inverted are None

    return_models: bool, optional (default=False)
        if True, return a list of models fitted for each CV fold

    log_cout: output stream or callback for logging

    log_cerr: error stream or callback for logging

    Returns
    -------
    cv results : pandas.core.frame.DataFrame with cross-validation results
        columns are: test-error-mean  test-error-std  train-error-mean  train-error-std
    cv models : list of trained models, if return_models=True
    """

class BatchMetricCalcer(_MetricCalcerBase):
    def __init__(self, catboost, metrics, ntree_start, ntree_end, eval_period, thread_count, tmp_dir) -> None: ...

def sum_models(models, weights: Incomplete | None = None, ctr_merge_policy: str = 'IntersectingCountersAverage'): ...
def to_regressor(model): ...
def to_classifier(model): ...
def to_ranker(model): ...

class _TrainCallbacksWrapper:
    def __init__(self, callbacks) -> None: ...
    def after_iteration(self, info): ...
