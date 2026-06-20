import plotly.graph_objs as go
from _typeshed import Incomplete
from flaml.automl import AutoML as AutoML
from flaml.automl.training_log import training_log_reader as training_log_reader
from flaml.tune.sample import Categorical as Categorical, Domain as Domain, Float as Float, Integer as Integer
from flaml.tune.tune import ExperimentAnalysis as ExperimentAnalysis

def get_hp_df(result, learner: Incomplete | None = None, params: Incomplete | None = None): ...
def optuna_space(result, learner: Incomplete | None = None, params: Incomplete | None = None): ...
def get_param_importance(result, learner: Incomplete | None = None, params: Incomplete | None = None): ...
def plot(result, fig_type, **kwargs) -> go.Figure:
    '''
    An unified entry point for plotting.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.
        fig_type: The type of figure you want to plot. Available options are:
            - "optimization_history": Plot optimization history of all trials in the experiment.
            - "feature_importance": Plot importance for each feature in the dataset.
            - "parallel_coordinate": Plot the high-dimensional parameter relationships in the experiment.
                Extra arguments for this figure:
                    - learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
                    - params: The parameters you want to plot. Plot all parameters if not specified.

            - "contour": Plot the parameter relationship as contour plot in the experiment.
                Extra arguments for this figure:
                    - learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
                    - params: The parameters you want to plot. Plot all parameters if not specified.

            - "edf": Plot the objective value EDF (empirical distribution function) of the experiment.
            - "timeline": Plot the timeline of the experiment.
            - "slice": Plot the parameter relationship as slice plot in a study.
                Extra arguments for this figure:
                    - learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
                    - params: The parameters you want to plot. Plot all parameters if not specified.
            - "param_importance": Plot the hyperparameter importance of the experiment.
                This plot use f-ANOVA to evaluate hyperparameter importance.
                Extra arguments for this figure:
                    - learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
                    - params: The parameters you want to plot. Plot all parameters if not specified.

        **kwargs: Extra arguments for the plot function.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    '''
def plot_optimization_history(result) -> go.Figure:
    """
    Plot optimization history of all trials in the experiment.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_feature_importance(result) -> go.Figure:
    """
    Plot importance for each feature in the dataset.

    Args:
        result: Your experiment result from AutoML. Not available for Hyperparameter Tuning.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_parallel_coordinate(result, learner: Incomplete | None = None, params: Incomplete | None = None) -> go.Figure:
    """
    Plot the high-dimensional parameter relationships in the experiment.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.
        learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
        params: The parameters you want to plot. Plot all parameters if not specified.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_contour(result, learner: Incomplete | None = None, params: Incomplete | None = None) -> go.Figure:
    """
    Plot the parameter relationship as contour plot in the experiment.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.
        learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
        params: The parameters you want to plot. Plot all parameters if not specified.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_edf(result) -> go.Figure:
    """
    Plot the objective value EDF (empirical distribution function) of the experiment.
    EDF is useful to analyze and improve search spaces.
    For instance, you can see a practical use case of EDF in the paper
    [Designing Network Design Spaces](https://arxiv.org/abs/2003.13678).

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.
            For AutoML experiments, each learner's trials form an optimization series.
            For hyperparameter tuning, you can provide either a single result or
                multiple results (in a list or dictionary) to this function.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_timeline(result) -> go.Figure:
    """
    Plot the timeline of the experiment.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_slice(result, learner: Incomplete | None = None, params: Incomplete | None = None) -> go.Figure:
    """
    Plot the parameter relationship as slice plot in a study.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.
        learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
        params: The parameters you want to plot. Plot all parameters if not specified.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
def plot_param_importance(result, learner: Incomplete | None = None, params: Incomplete | None = None) -> go.Figure:
    """
    Plot the hyperparameter importance of the experiment.
    This plot use f-ANOVA(implement by https://github.com/optuna/optuna-fast-fanova/)
    to evaluate hyperparameter importance.

    Args:
        result: The experiment result of AutoML.fit() or Tune.run(). Must be an instance of AutoML or ExperimentAnalysis.
        learner: The learner you want to plot. Only available for AutoML. Plot best learner if not specified.
        params: The parameters you want to plot. Plot all parameters if not specified.

    Returns:
        A `plotly.graph_objs.Figure()` object.
    """
