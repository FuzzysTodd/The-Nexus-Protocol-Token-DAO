from .core import ARRAY_TYPES as ARRAY_TYPES, CatBoostError as CatBoostError, PATH_TYPES as PATH_TYPES, Pool as Pool, STRING_TYPES as STRING_TYPES, fspath as fspath
from _typeshed import Incomplete

compute_wx_test: Incomplete
TargetStats: Incomplete
DataMetaInfo: Incomplete
compute_training_options: Incomplete

def create_cd(label: Incomplete | None = None, cat_features: Incomplete | None = None, text_features: Incomplete | None = None, embedding_features: Incomplete | None = None, weight: Incomplete | None = None, baseline: Incomplete | None = None, doc_id: Incomplete | None = None, group_id: Incomplete | None = None, subgroup_id: Incomplete | None = None, timestamp: Incomplete | None = None, auxiliary_columns: Incomplete | None = None, feature_names: Incomplete | None = None, output_path: str = 'train.cd'): ...
def read_cd(cd_file, column_count: Incomplete | None = None, data_file: Incomplete | None = None, canonize_column_types: bool = False):
    '''
    Reads CatBoost column description file
    (see https://catboost.ai/docs/concepts/input-data_column-descfile.html#input-data_column-descfile)

    Parameters
    ----------
    cd_file : str or pathlib.Path
        path to column description file

    column_count : integer
        total number of columns

    data_file : str or pathlib.Path
        path to dataset file in CatBoost format
        specify either column_count directly or data_file to detect it

    canonize_column_types : bool
        if set to True types for columns with synonyms are renamed to canonical type.

    Returns
    -------
    dict with keys:
        "column_type_to_indices" :
            dict of column_type -> column_indices list, column_type is \'Label\', \'Categ\' etc.

        "column_dtypes" : dict of column_name -> numpy.dtype or \'category\'

        "cat_feature_indices" : list of integers
            indices of categorical features in array of all features.
            Note: indices in array of features, not indices in array of all columns!

        "text_feature_indices" : list of integers
            indices of text features in array of all features.
            Note: indices in array of features, not indices in array of all columns!

        "embedding_feature_indices" : list of integers
            indices of embedding features in array of all features.
            Note: indices in array of features, not indices in array of all columns!

        "column_names" : list of strings

        "non_feature_column_indices" : list of integers
    '''
def eval_metric(label, approx, metric, weight: Incomplete | None = None, group_id: Incomplete | None = None, group_weight: Incomplete | None = None, subgroup_id: Incomplete | None = None, pairs: Incomplete | None = None, thread_count: int = -1):
    """
    Evaluate metrics with raw approxes and labels.

    Parameters
    ----------
    label : list or numpy.ndarrays or pandas.DataFrame or pandas.Series
        Object labels with shape (n_objects,) or (n_object, n_target_dimension)

    approx : list or numpy.ndarrays or pandas.DataFrame or pandas.Series
        Object approxes with shape (n_objects,) or (n_object, n_approx_dimension).

    metric : string
        Metric name.

    weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
        Object weights.

    group_id : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
        Object group ids.

    group_weight : list or numpy.ndarray or pandas.DataFrame or pandas.Series, optional (default=None)
        Group weights.

    subgroup_id : list or numpy.ndarray, optional (default=None)
        subgroup id for each instance.
        If not None, giving 1 dimensional array like data.

    pairs : list or numpy.ndarray or pandas.DataFrame or string or pathlib.Path
        The pairs description.
        If list or numpy.ndarrays or pandas.DataFrame, giving 2 dimensional.
        The shape should be Nx2, where N is the pairs' count. The first element of the pair is
        the index of winner object in the training set. The second element of the pair is
        the index of loser object in the training set.
        If string or pathlib.Path, giving the path to the file with pairs description.

    thread_count : int, optional (default=-1)
        Number of threads to work with.
        If -1, then the number of threads is set to the number of CPU cores.

    Returns
    -------
    metric results : list with metric values.
    """
def get_gpu_device_count(): ...
def reset_trace_backend(filename) -> None: ...
def get_confusion_matrix(model, data, thread_count: int = -1):
    """
    Build confusion matrix.

    Parameters
    ----------
    model : catboost.CatBoost
        The trained model.

    data : catboost.Pool
        A set of samples to build confusion matrix with.

    thread_count : int (default=-1)
        Number of threads to work with.
        If -1, then the number of threads is set to the number of CPU cores.

    Returns
    -------
    confusion matrix : array, shape = [n_classes, n_classes]
    """
def get_roc_curve(model, data, thread_count: int = -1, plot: bool = False):
    """
    Build points of ROC curve.

    Parameters
    ----------
    model : catboost.CatBoost
        The trained model.

    data : catboost.Pool or list of catboost.Pool
        A set of samples to build ROC curve with.

    thread_count : int (default=-1)
        Number of threads to work with.
        If -1, then the number of threads is set to the number of CPU cores.

    plot : bool, optional (default=False)
        If True, draw curve.

    Returns
    -------
    curve points : tuple of three arrays (fpr, tpr, thresholds)
    """
def get_fpr_curve(model: Incomplete | None = None, data: Incomplete | None = None, curve: Incomplete | None = None, thread_count: int = -1, plot: bool = False):
    """
    Build points of FPR curve.

    Parameters
    ----------
    model : catboost.CatBoost
        The trained model.

    data : catboost.Pool or list of catboost.Pool
        A set of samples to build ROC curve with.

    curve : tuple of three arrays (fpr, tpr, thresholds)
        ROC curve points in format of get_roc_curve returned value.
        If set, data parameter must not be set.

    thread_count : int (default=-1)
        Number of threads to work with.
        If -1, then the number of threads is set to the number of CPU cores.

    plot : bool, optional (default=False)
        If True, draw curve.

    Returns
    -------
    curve points : tuple of two arrays (thresholds, fpr)
    """
def get_fnr_curve(model: Incomplete | None = None, data: Incomplete | None = None, curve: Incomplete | None = None, thread_count: int = -1, plot: bool = False):
    """
    Build points of FNR curve.

    Parameters
    ----------
    model : catboost.CatBoost
        The trained model.

    data : catboost.Pool or list of catboost.Pool
        A set of samples to build ROC curve with.

    curve : tuple of three arrays (fpr, tpr, thresholds)
        ROC curve points in format of get_roc_curve returned value.
        If set, data parameter must not be set.

    thread_count : int (default=-1)
        Number of threads to work with.
        If -1, then the number of threads is set to the number of CPU cores.

    plot : bool, optional (default=False)
        If True, draw curve.

    Returns
    -------
    curve points : tuple of two arrays (thresholds, fnr)
    """
def select_threshold(model: Incomplete | None = None, data: Incomplete | None = None, curve: Incomplete | None = None, FPR: Incomplete | None = None, FNR: Incomplete | None = None, thread_count: int = -1):
    """
    Selects a threshold for prediction.

    Parameters
    ----------
    model : catboost.CatBoost
        The trained model.

    data : catboost.Pool or list of catboost.Pool
        Set of samples to build ROC curve with.
        If set, curve parameter must not be set.

    curve : tuple of three arrays (fpr, tpr, thresholds)
        ROC curve points in format of get_roc_curve returned value.
        If set, data parameter must not be set.

    FPR : desired false-positive rate

    FNR : desired false-negative rate (only one of FPR and FNR should be chosen)

    thread_count : int (default=-1)
        Number of threads to work with.
        If -1, then the number of threads is set to the number of CPU cores.

    Returns
    -------
    threshold : double
    """
def quantize(data_path, column_description: Incomplete | None = None, pairs: Incomplete | None = None, delimiter: str = '\t', has_header: bool = False, ignore_csv_quoting: bool = False, feature_names: Incomplete | None = None, thread_count: int = -1, ignored_features: Incomplete | None = None, per_float_feature_quantization: Incomplete | None = None, border_count: Incomplete | None = None, max_bin: Incomplete | None = None, feature_border_type: Incomplete | None = None, nan_mode: Incomplete | None = None, input_borders: Incomplete | None = None, task_type: Incomplete | None = None, used_ram_limit: Incomplete | None = None, random_seed: Incomplete | None = None, log_cout=..., log_cerr=..., **kwargs):
    '''
    Construct quantized Pool from non-quantized pool stored in file.
    This method does not load whole non-quantized source dataset into memory
    so it can be used for huge datasets that fit in memory only after quantization.

    Parameters
    ----------
    data_path : string or pathlib.Path
        Path (with optional scheme) to non-quantized dataset.

    column_description : string, [default=None]
        ColumnsDescription parameter.
        There are several columns description types: Label, Categ, Num, Auxiliary, DocId, Weight, Baseline, GroupId, Timestamp.
        All columns are Num as default, it\'s not necessary to specify
        this type of columns. Default Label column index is 0 (zero).
        If None, Label column is 0 (zero) as default, all data columns are Num as default.
        If string or pathlib.Path, giving the path to the file with ColumnsDescription in column_description format.

    pairs : string or pathlib.Path, [default=None]
        Path to the file with pairs description.

    has_header : bool, [default=False]
        If True, read column names from first line.

    ignore_csv_quoting : bool optional (default=False)
        If True ignore quoting \'"\'.

    feature_names : string or pathlib.Path, [default=None]
        Path with scheme for feature names data to load.

    thread_count : int, [default=-1]
        Thread count for data processing.
        If -1, then the number of threads is set to the number of CPU cores.

    ignored_features : list, [default=None]
        Indices or names of features that should be excluded when training.

    per_float_feature_quantization : list of strings, [default=None]
        List of float binarization descriptions.
        Format : described in documentation on catboost.ai
        Example 1: [\'0:1024\'] means that feature 0 will have 1024 borders.
        Example 2: [\'0:border_count=1024\', \'1:border_count=1024\', ...] means that two first features have 1024 borders.
        Example 3: [\'0:nan_mode=Forbidden,border_count=32,border_type=GreedyLogSum\',
                    \'1:nan_mode=Forbidden,border_count=32,border_type=GreedyLogSum\'] - defines more quantization properties for first two features.

    border_count : int, [default = 254 for training on CPU or 128 for training on GPU]
        The number of partitions in numeric features binarization. Used in the preliminary calculation.
        range: [1,65535] on CPU, [1,255] on GPU

    max_bin : float, synonym for border_count.

    feature_border_type : string, [default=\'GreedyLogSum\']
        The binarization mode in numeric features binarization. Used in the preliminary calculation.
        Possible values:
            - \'Median\'
            - \'Uniform\'
            - \'UniformAndQuantiles\'
            - \'GreedyLogSum\'
            - \'MaxLogSum\'
            - \'MinEntropy\'

    nan_mode : string, [default=None]
        Way to process missing values for numeric features.
        Possible values:
            - \'Forbidden\' - raises an exception if there is a missing value for a numeric feature in a dataset.
            - \'Min\' - each missing value will be processed as the minimum numerical value.
            - \'Max\' - each missing value will be processed as the maximum numerical value.
        If None, then nan_mode=Min.

    input_borders : string or pathlib.Path, [default=None]
        input file with borders used in numeric features binarization.

    task_type : string, [default=None]
        The calcer type used to train the model.
        Possible values:
            - \'CPU\'
            - \'GPU\'

    used_ram_limit=None

    random_seed : int, [default=None]
        The random seed used for data sampling.
        If None, 0 is used.

    Returns
    -------
    pool : Pool
        Constructed and quantized pool.
    '''
def convert_to_onnx_object(model, export_parameters: Incomplete | None = None, **kwargs):
    """
    Convert given CatBoost model to ONNX-ML model.
    Categorical Features are not supported.

    Parameters
    ----------
    model : CatBoost trained model
    export_parameters : dict [default=None]
        Parameters for ONNX-ML export:
            * onnx_graph_name : string
                The name property of onnx Graph
            * onnx_domain : string
                The domain component of onnx Model
            * onnx_model_version : int
                The model_version component of onnx Model
            * onnx_doc_string : string
                The doc_string component of onnx Model
    Returns
    -------
    onnx_object : ModelProto
        The model in ONNX format
    """
def calculate_quantization_grid(values, border_count, border_type: str = 'Median'): ...
