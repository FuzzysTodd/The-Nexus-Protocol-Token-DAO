from .. import maskers as maskers
from .._explanation import Explanation as Explanation
from ..utils import assert_import as assert_import, record_import_error as record_import_error, safe_isinstance as safe_isinstance
from ..utils._exceptions import ExplainerError as ExplainerError, InvalidFeaturePerturbationError as InvalidFeaturePerturbationError, InvalidMaskerError as InvalidMaskerError, InvalidModelError as InvalidModelError
from ..utils._legacy import DenseData as DenseData
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

output_transform_codes: Incomplete
feature_perturbation_codes: Incomplete

class Tree(Explainer):
    """ Uses Tree SHAP algorithms to explain the output of ensemble tree models.

    Tree SHAP is a fast and exact method to estimate SHAP values for tree models and ensembles of trees,
    under several different possible assumptions about feature dependence. It depends on fast C++
    implementations either inside an external model package or in the local compiled C extension.
    """
    data_feature_names: Incomplete
    data: Incomplete
    data_missing: Incomplete
    feature_perturbation: Incomplete
    expected_value: Incomplete
    model: Incomplete
    model_output: Incomplete
    approximate: Incomplete
    def __init__(self, model, data: Incomplete | None = None, model_output: str = 'raw', feature_perturbation: str = 'interventional', feature_names: Incomplete | None = None, approximate: bool = False, **deprecated_options) -> None:
        ''' Build a new Tree explainer for the passed model.

        Parameters
        ----------
        model : model object
            The tree based machine learning model that we want to explain. XGBoost, LightGBM, CatBoost, Pyspark
            and most tree-based scikit-learn models are supported.

        data : numpy.array or pandas.DataFrame
            The background dataset to use for integrating out features. This argument is optional when
            ``feature_perturbation="tree_path_dependent"``, since in that case we can use the number of training
            samples that went down each tree path as our background dataset (this is recorded in the ``model``
            object).

        feature_perturbation : "interventional" (default) or "tree_path_dependent" (default when data=None)
            Since SHAP values rely on conditional expectations, we need to decide how to handle correlated
            (or otherwise dependent) input features.
            The "interventional" approach breaks the dependencies between features according to the rules
            dictated by causal inference (Janzing et al. 2019). Note that the "interventional" option
            requires a background dataset ``data``, and its runtime scales linearly with the size of the
            background dataset you use. Anywhere from 100 to 1000 random background samples are good
            sizes to use.
            The "tree_path_dependent" approach is to just follow the trees and use the number of training
            examples that went down each leaf to represent the background distribution. This approach
            does not require a background dataset, and so is used by default when no background dataset
            is provided.

        model_output : "raw", "probability", "log_loss", or model method name
            What output of the model should be explained.
            If "raw", then we explain the raw output of the trees, which varies by model. For regression models,
            "raw" is the standard output. For binary classification in XGBoost, this is the log odds ratio.
            If ``model_output`` is the name of a supported prediction method on the ``model`` object, then we
            explain the output of that model method name. For example, ``model_output="predict_proba"``
            explains the result of calling ``model.predict_proba``.
            If "probability", then we explain the output of the model transformed into probability space
            (note that this means the SHAP values now sum to the probability output of the model).
            If "log_loss", then we explain the log base e of the model loss function, so that the SHAP values
            sum up to the log loss of the model for each sample. This is helpful for breaking down model
            performance by feature.
            Currently the "probability" and "log_loss" options are only supported when
            ``feature_perturbation="interventional"``.

        Examples
        --------
        See `Tree explainer examples <https://shap.readthedocs.io/en/latest/api_examples/explainers/Tree.html>`_
        '''
    def __call__(self, X, y: Incomplete | None = None, interactions: bool = False, check_additivity: bool = True): ...
    def shap_values(self, X, y: Incomplete | None = None, tree_limit: Incomplete | None = None, approximate: bool = False, check_additivity: bool = True, from_call: bool = False):
        """ Estimate the SHAP values for a set of samples.

        Parameters
        ----------
        X : numpy.array, pandas.DataFrame or catboost.Pool (for catboost)
            A matrix of samples (# samples x # features) on which to explain the model's output.

        y : numpy.array
            An array of label values for each sample. Used when explaining loss functions.

        tree_limit : None (default) or int
            Limit the number of trees used by the model. By default, the limit of the original model
            is used (``None``). ``-1`` means no limit.

        approximate : bool
            Run fast, but only roughly approximate the Tree SHAP values. This runs a method
            previously proposed by Saabas which only considers a single feature ordering. Take care
            since this does not have the consistency guarantees of Shapley values and places too
            much weight on lower splits in the tree.

        check_additivity : bool
            Run a validation check that the sum of the SHAP values equals the output of the model. This
            check takes only a small amount of time, and will catch potential unforeseen errors.
            Note that this check only runs right now when explaining the margin of the model.

        Returns
        -------
        array or list
            For models with a single output, this returns a matrix of SHAP values
            (# samples x # features). Each row sums to the difference between the model output for that
            sample and the expected value of the model output (which is stored in the ``expected_value``
            attribute of the explainer when it is constant). For models with vector outputs, this returns
            a list of such matrices, one for each output.
        """
    def shap_interaction_values(self, X, y: Incomplete | None = None, tree_limit: Incomplete | None = None):
        ''' Estimate the SHAP interaction values for a set of samples.

        Parameters
        ----------
        X : numpy.array, pandas.DataFrame or catboost.Pool (for catboost)
            A matrix of samples (# samples x # features) on which to explain the model\'s output.

        y : numpy.array
            An array of label values for each sample. Used when explaining loss functions (not yet supported).

        tree_limit : None (default) or int
            Limit the number of trees used by the model. By default, the limit of the original model
            is used (``None``). ``-1`` means no limit.

        Returns
        -------
        array or list
            For models with a single output, this returns a tensor of SHAP values
            (# samples x # features x # features). The matrix (# features x # features) for each sample sums
            to the difference between the model output for that sample and the expected value of the model output
            (which is stored in the ``expected_value`` attribute of the explainer). Each row of this matrix sums to the
            SHAP value for that feature for that sample. The diagonal entries of the matrix represent the
            "main effect" of that feature on the prediction. The symmetric off-diagonal entries represent the
            interaction effects between all pairs of features for that sample.
            For models with vector outputs, this returns a list of tensors, one for each output.
        '''
    def assert_additivity(self, phi, model_output) -> None: ...
    @staticmethod
    def supports_model_with_masker(model, masker):
        """ Determines if this explainer can handle the given model.

        This is an abstract static method meant to be implemented by each subclass.
        """

class TreeEnsemble:
    """ An ensemble of decision trees.

    This object provides a common interface to many different types of models.
    """
    model_type: str
    trees: Incomplete
    base_offset: int
    model_output: Incomplete
    objective: Incomplete
    tree_output: Incomplete
    internal_dtype: Incomplete
    input_dtype: Incomplete
    data: Incomplete
    data_missing: Incomplete
    fully_defined_weighting: bool
    tree_limit: Incomplete
    num_stacked_models: int
    cat_feature_indices: Incomplete
    dtype: Incomplete
    original_model: Incomplete
    num_outputs: Incomplete
    children_left: Incomplete
    children_right: Incomplete
    children_default: Incomplete
    features: Incomplete
    thresholds: Incomplete
    values: Incomplete
    node_sample_weight: Incomplete
    num_nodes: Incomplete
    max_depth: Incomplete
    def __init__(self, model, data: Incomplete | None = None, data_missing: Incomplete | None = None, model_output: Incomplete | None = None) -> None: ...
    def get_transform(self):
        """ A consistent interface to make predictions from this model.
        """
    def predict(self, X, y: Incomplete | None = None, output: Incomplete | None = None, tree_limit: Incomplete | None = None):
        """ A consistent interface to make predictions from this model.

        Parameters
        ----------
        tree_limit : None (default) or int
            Limit the number of trees used by the model. By default None means no use the limit of the
            original model, and -1 means no limit.
        """

class SingleTree:
    """A single decision tree.

    The primary point of this object is to parse many different tree types into a common format.

    Attributes
    ----------
    children_left : numpy.array
        A 1d array of length #nodes. The index ``i`` of this array contains the index of
        the left-child of the ``i-th`` node in the tree. An index of -1 is used to
        represent that the ``i-th`` node is a leaf/terminal node.

    children_right : numpy.array
        Same as ``children_left``, except it contains the index of the right child of
        each ``i-th`` node in the tree.

    children_default : numpy.array
        A 1d numpy array of length #nodes. The index ``i`` of this array contains either
        the index of the left-child / right-child of the ``i-th`` node in the tree,
        depending on whether the default split (for handling missing values) is left /
        right. An index of -1 is used to represent that the ``i-th`` node is a leaf
        node.

    features : numpy.array
        A 1d numpy array of length #nodes. The value at the ``i-th`` position is the
        index of the feature chosen for the split at node ``i``. Leaf nodes have no
        splits, so is -1.

    thresholds : numpy.array
        A 1d numpy array of length #nodes. The value at the ``i-th`` position is the
        threshold used for the split at node ``i``. Leaf nodes have no thresholds, so is
        -1.

    values : numpy.array
        A 1d numpy array of length #nodes. The index ``i`` of this array contains the
        raw predicted value that would be produced by node ``i`` if it were a leaf node.

    node_sample_weight : numpy.array
        A 1d numpy array of length #nodes. The index ``i`` contains the number of
        records (usually from the training data) that falls into node ``i``.

    max_depth : int
        The max depth of the tree.
    """
    children_left: Incomplete
    children_right: Incomplete
    children_default: Incomplete
    features: Incomplete
    thresholds: Incomplete
    values: Incomplete
    node_sample_weight: Incomplete
    max_depth: Incomplete
    def __init__(self, tree, normalize: bool = False, scaling: float = 1.0, data: Incomplete | None = None, data_missing: Incomplete | None = None) -> None: ...

class IsoTree(SingleTree):
    """
    In sklearn the tree of the Isolation Forest does not calculated in a good way.
    """
    values: Incomplete
    features: Incomplete
    def __init__(self, tree, tree_features, normalize: bool = False, scaling: float = 1.0, data: Incomplete | None = None, data_missing: Incomplete | None = None) -> None: ...

def get_xgboost_json(model):
    """ This gets a JSON dump of an XGBoost model while ensuring the features names are their indexes.
    """

class XGBTreeModelLoader:
    """ This loads an XGBoost model directly from a raw memory dump.

    We can't use the JSON dump because due to numerical precision issues those
    tree can actually be wrong when feature values land almost on a threshold.
    """
    buf: Incomplete
    pos: int
    base_score: Incomplete
    num_feature: Incomplete
    num_class: Incomplete
    contain_extra_attrs: Incomplete
    contain_eval_metrics: Incomplete
    name_obj_len: Incomplete
    name_obj: Incomplete
    name_gbm_len: Incomplete
    name_gbm: Incomplete
    num_trees: Incomplete
    num_roots: Incomplete
    pad_32bit: Incomplete
    num_pbuffer_deprecated: Incomplete
    num_output_group: Incomplete
    size_leaf_vector: Incomplete
    num_nodes: Incomplete
    num_deleted: Incomplete
    max_depth: Incomplete
    node_parents: Incomplete
    node_cleft: Incomplete
    node_cright: Incomplete
    node_sindex: Incomplete
    node_info: Incomplete
    loss_chg: Incomplete
    sum_hess: Incomplete
    base_weight: Incomplete
    leaf_child_cnt: Incomplete
    def __init__(self, xgb_model) -> None: ...
    children_default: Incomplete
    features: Incomplete
    thresholds: Incomplete
    values: Incomplete
    def get_trees(self, data: Incomplete | None = None, data_missing: Incomplete | None = None): ...
    def read(self, dtype): ...
    def read_arr(self, dtype, n_items): ...
    def read_str(self, size): ...
    def print_info(self) -> None: ...

class CatBoostTreeModelLoader:
    loaded_cb_model: Incomplete
    num_trees: Incomplete
    max_depth: Incomplete
    def __init__(self, cb_model) -> None: ...
    def get_trees(self, data: Incomplete | None = None, data_missing: Incomplete | None = None): ...
