from . import explanation as explanation, lime_base as lime_base
from _typeshed import Incomplete
from lime.discretize import BaseDiscretizer as BaseDiscretizer, DecileDiscretizer as DecileDiscretizer, EntropyDiscretizer as EntropyDiscretizer, QuartileDiscretizer as QuartileDiscretizer, StatsDiscretizer as StatsDiscretizer

class TableDomainMapper(explanation.DomainMapper):
    """Maps feature ids to names, generates table views, etc"""
    exp_feature_names: Incomplete
    discretized_feature_names: Incomplete
    feature_names: Incomplete
    feature_values: Incomplete
    feature_indexes: Incomplete
    scaled_row: Incomplete
    all_categorical: bool
    categorical_features: Incomplete
    def __init__(self, feature_names, feature_values, scaled_row, categorical_features, discretized_feature_names: Incomplete | None = None, feature_indexes: Incomplete | None = None) -> None:
        """Init.

        Args:
            feature_names: list of feature names, in order
            feature_values: list of strings with the values of the original row
            scaled_row: scaled row
            categorical_features: list of categorical features ids (ints)
            feature_indexes: optional feature indexes used in the sparse case
        """
    def map_exp_ids(self, exp):
        """Maps ids to feature names.

        Args:
            exp: list of tuples [(id, weight), (id,weight)]

        Returns:
            list of tuples (feature_name, weight)
        """
    def visualize_instance_html(self, exp, label, div_name, exp_object_name, show_table: bool = True, show_all: bool = False):
        """Shows the current example in a table format.

        Args:
             exp: list of tuples [(id, weight), (id,weight)]
             label: label id (integer)
             div_name: name of div object to be used for rendering(in js)
             exp_object_name: name of js explanation object
             show_table: if False, don't show table visualization.
             show_all: if True, show zero-weighted features in the table.
        """

class LimeTabularExplainer:
    """Explains predictions on tabular (i.e. matrix) data.
    For numerical features, perturb them by sampling from a Normal(0,1) and
    doing the inverse operation of mean-centering and scaling, according to the
    means and stds in the training data. For categorical features, perturb by
    sampling according to the training distribution, and making a binary
    feature that is 1 when the value is the same as the instance being
    explained."""
    random_state: Incomplete
    mode: Incomplete
    categorical_names: Incomplete
    sample_around_instance: Incomplete
    training_data_stats: Incomplete
    categorical_features: Incomplete
    feature_names: Incomplete
    discretizer: Incomplete
    feature_selection: Incomplete
    base: Incomplete
    class_names: Incomplete
    scaler: Incomplete
    feature_values: Incomplete
    feature_frequencies: Incomplete
    def __init__(self, training_data, mode: str = 'classification', training_labels: Incomplete | None = None, feature_names: Incomplete | None = None, categorical_features: Incomplete | None = None, categorical_names: Incomplete | None = None, kernel_width: Incomplete | None = None, kernel: Incomplete | None = None, verbose: bool = False, class_names: Incomplete | None = None, feature_selection: str = 'auto', discretize_continuous: bool = True, discretizer: str = 'quartile', sample_around_instance: bool = False, random_state: Incomplete | None = None, training_data_stats: Incomplete | None = None) -> None:
        '''Init function.

        Args:
            training_data: numpy 2d array
            mode: "classification" or "regression"
            training_labels: labels for training data. Not required, but may be
                used by discretizer.
            feature_names: list of names (strings) corresponding to the columns
                in the training data.
            categorical_features: list of indices (ints) corresponding to the
                categorical columns. Everything else will be considered
                continuous. Values in these columns MUST be integers.
            categorical_names: map from int to list of names, where
                categorical_names[x][y] represents the name of the yth value of
                column x.
            kernel_width: kernel width for the exponential kernel.
                If None, defaults to sqrt (number of columns) * 0.75
            kernel: similarity kernel that takes euclidean distances and kernel
                width as input and outputs weights in (0,1). If None, defaults to
                an exponential kernel.
            verbose: if true, print local prediction values from linear model
            class_names: list of class names, ordered according to whatever the
                classifier is using. If not present, class names will be \'0\',
                \'1\', ...
            feature_selection: feature selection method. can be
                \'forward_selection\', \'lasso_path\', \'none\' or \'auto\'.
                See function \'explain_instance_with_data\' in lime_base.py for
                details on what each of the options does.
            discretize_continuous: if True, all non-categorical features will
                be discretized into quartiles.
            discretizer: only matters if discretize_continuous is True
                and data is not sparse. Options are \'quartile\', \'decile\',
                \'entropy\' or a BaseDiscretizer instance.
            sample_around_instance: if True, will sample continuous features
                in perturbed samples from a normal centered at the instance
                being explained. Otherwise, the normal is centered on the mean
                of the feature data.
            random_state: an integer or numpy.RandomState that will be used to
                generate random numbers. If None, the random state will be
                initialized using the internal numpy seed.
            training_data_stats: a dict object having the details of training data
                statistics. If None, training data information will be used, only matters
                if discretize_continuous is True. Must have the following keys:
                means", "mins", "maxs", "stds", "feature_values",
                "feature_frequencies"
        '''
    @staticmethod
    def convert_and_round(values): ...
    @staticmethod
    def validate_training_data_stats(training_data_stats) -> None:
        """
            Method to validate the structure of training data stats
        """
    def explain_instance(self, data_row, predict_fn, labels=(1,), top_labels: Incomplete | None = None, num_features: int = 10, num_samples: int = 5000, distance_metric: str = 'euclidean', model_regressor: Incomplete | None = None):
        """Generates explanations for a prediction.

        First, we generate neighborhood data by randomly perturbing features
        from the instance (see __data_inverse). We then learn locally weighted
        linear models on this neighborhood data to explain each of the classes
        in an interpretable way (see lime_base.py).

        Args:
            data_row: 1d numpy array or scipy.sparse matrix, corresponding to a row
            predict_fn: prediction function. For classifiers, this should be a
                function that takes a numpy array and outputs prediction
                probabilities. For regressors, this takes a numpy array and
                returns the predictions. For ScikitClassifiers, this is
                `classifier.predict_proba()`. For ScikitRegressors, this
                is `regressor.predict()`. The prediction function needs to work
                on multiple feature vectors (the vectors randomly perturbed
                from the data_row).
            labels: iterable with labels to be explained.
            top_labels: if not None, ignore labels and produce explanations for
                the K labels with highest prediction probabilities, where K is
                this parameter.
            num_features: maximum number of features present in explanation
            num_samples: size of the neighborhood to learn the linear model
            distance_metric: the distance metric to use for weights.
            model_regressor: sklearn regressor to use in explanation. Defaults
                to Ridge regression in LimeBase. Must have model_regressor.coef_
                and 'sample_weight' as a parameter to model_regressor.fit()

        Returns:
            An Explanation object (see explanation.py) with the corresponding
            explanations.
        """

class RecurrentTabularExplainer(LimeTabularExplainer):
    """
    An explainer for keras-style recurrent neural networks, where the
    input shape is (n_samples, n_timesteps, n_features). This class
    just extends the LimeTabularExplainer class and reshapes the training
    data and feature names such that they become something like

    (val1_t1, val1_t2, val1_t3, ..., val2_t1, ..., valn_tn)

    Each of the methods that take data reshape it appropriately,
    so you can pass in the training/testing data exactly as you
    would to the recurrent neural network.

    """
    n_timesteps: Incomplete
    n_features: Incomplete
    def __init__(self, training_data, mode: str = 'classification', training_labels: Incomplete | None = None, feature_names: Incomplete | None = None, categorical_features: Incomplete | None = None, categorical_names: Incomplete | None = None, kernel_width: Incomplete | None = None, kernel: Incomplete | None = None, verbose: bool = False, class_names: Incomplete | None = None, feature_selection: str = 'auto', discretize_continuous: bool = True, discretizer: str = 'quartile', random_state: Incomplete | None = None) -> None:
        '''
        Args:
            training_data: numpy 3d array with shape
                (n_samples, n_timesteps, n_features)
            mode: "classification" or "regression"
            training_labels: labels for training data. Not required, but may be
                used by discretizer.
            feature_names: list of names (strings) corresponding to the columns
                in the training data.
            categorical_features: list of indices (ints) corresponding to the
                categorical columns. Everything else will be considered
                continuous. Values in these columns MUST be integers.
            categorical_names: map from int to list of names, where
                categorical_names[x][y] represents the name of the yth value of
                column x.
            kernel_width: kernel width for the exponential kernel.
            If None, defaults to sqrt(number of columns) * 0.75
            kernel: similarity kernel that takes euclidean distances and kernel
                width as input and outputs weights in (0,1). If None, defaults to
                an exponential kernel.
            verbose: if true, print local prediction values from linear model
            class_names: list of class names, ordered according to whatever the
                classifier is using. If not present, class names will be \'0\',
                \'1\', ...
            feature_selection: feature selection method. can be
                \'forward_selection\', \'lasso_path\', \'none\' or \'auto\'.
                See function \'explain_instance_with_data\' in lime_base.py for
                details on what each of the options does.
            discretize_continuous: if True, all non-categorical features will
                be discretized into quartiles.
            discretizer: only matters if discretize_continuous is True. Options
                are \'quartile\', \'decile\', \'entropy\' or a BaseDiscretizer
                instance.
            random_state: an integer or numpy.RandomState that will be used to
                generate random numbers. If None, the random state will be
                initialized using the internal numpy seed.
        '''
    def explain_instance(self, data_row, classifier_fn, labels=(1,), top_labels: Incomplete | None = None, num_features: int = 10, num_samples: int = 5000, distance_metric: str = 'euclidean', model_regressor: Incomplete | None = None):
        """Generates explanations for a prediction.

        First, we generate neighborhood data by randomly perturbing features
        from the instance (see __data_inverse). We then learn locally weighted
        linear models on this neighborhood data to explain each of the classes
        in an interpretable way (see lime_base.py).

        Args:
            data_row: 2d numpy array, corresponding to a row
            classifier_fn: classifier prediction probability function, which
                takes a numpy array and outputs prediction probabilities. For
                ScikitClassifiers , this is classifier.predict_proba.
            labels: iterable with labels to be explained.
            top_labels: if not None, ignore labels and produce explanations for
                the K labels with highest prediction probabilities, where K is
                this parameter.
            num_features: maximum number of features present in explanation
            num_samples: size of the neighborhood to learn the linear model
            distance_metric: the distance metric to use for weights.
            model_regressor: sklearn regressor to use in explanation. Defaults
                to Ridge regression in LimeBase. Must have
                model_regressor.coef_ and 'sample_weight' as a parameter
                to model_regressor.fit()

        Returns:
            An Explanation object (see explanation.py) with the corresponding
            explanations.
        """
