from .config_generator import CG_BOHB as CG_BOHB
from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.runtime.common import multi_phase_enabled as multi_phase_enabled
from nni.runtime.msg_dispatcher_base import MsgDispatcherBase as MsgDispatcherBase
from nni.runtime.tuner_command_channel import CommandType as CommandType
from nni.utils import MetricType as MetricType, OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward

logger: Incomplete

def create_parameter_id():
    """Create an id

    Returns
    -------
    int
        parameter id
    """
def create_bracket_parameter_id(brackets_id, brackets_curr_decay, increased_id: int = -1):
    """Create a full id for a specific bracket's hyperparameter configuration

    Parameters
    ----------
    brackets_id: int
        brackets id
    brackets_curr_decay: int
        brackets curr decay
    increased_id: int
        increased id
    Returns
    -------
    int
        params id
    """

class Bracket:
    """
    A bracket in BOHB, all the information of a bracket is managed by
    an instance of this class.

    Parameters
    ----------
    s: int
        The current Successive Halving iteration index.
    s_max: int
        total number of Successive Halving iterations
    eta: float
        In each iteration, a complete run of sequential halving is executed. In it,
\t\tafter evaluating each configuration on the same subset size, only a fraction of
\t\t1/eta of them 'advances' to the next round.
\tmax_budget : float
\t\tThe largest budget to consider. Needs to be larger than min_budget!
\t\tThe budgets will be geometrically distributed
        :math:`a^2 + b^2 = c^2 \\sim \\eta^k` for :math:`k\\in [0, 1, ... , num\\_subsets - 1]`.
    optimize_mode: str
        optimize mode, 'maximize' or 'minimize'
    """
    s: Incomplete
    s_max: Incomplete
    eta: Incomplete
    max_budget: Incomplete
    optimize_mode: Incomplete
    n: Incomplete
    r: Incomplete
    i: int
    hyper_configs: Incomplete
    configs_perf: Incomplete
    num_configs_to_run: Incomplete
    num_finished_configs: Incomplete
    no_more_trial: bool
    def __init__(self, s, s_max, eta, max_budget, optimize_mode) -> None: ...
    def is_completed(self):
        """check whether this bracket has sent out all the hyperparameter configurations"""
    def get_n_r(self):
        """return the values of n and r for the next round"""
    def increase_i(self) -> None:
        """i means the ith round. Increase i by 1"""
    def set_config_perf(self, i, parameter_id, seq, value) -> None:
        """update trial's latest result with its sequence number, e.g., epoch number or batch number

        Parameters
        ----------
        i: int
            the ith round
        parameter_id: int
            the id of the trial/parameter
        seq: int
            sequence number, e.g., epoch number or batch number
        value: int
            latest result with sequence number seq

        Returns
        -------
        None
        """
    def inform_trial_end(self, i):
        """If the trial is finished and the corresponding round (i.e., i) has all its trials finished,
        it will choose the top k trials for the next round (i.e., i+1)

        Parameters
        ----------
        i: int
            the ith round

        Returns
        -------
        new trial or None:
            If we have generated new trials after this trial end, we will return a new trial parameters.
            Otherwise, we will return None.
        """
    def get_hyperparameter_configurations(self, num, r, config_generator):
        """generate num hyperparameter configurations from search space using Bayesian optimization

        Parameters
        ----------
        num: int
            the number of hyperparameter configurations

        Returns
        -------
        list
            a list of hyperparameter configurations. Format: [[key1, value1], [key2, value2], ...]
        """

class BOHBClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class BOHB(MsgDispatcherBase):
    '''
    `BOHB <https://arxiv.org/abs/1807.01774>`__ is a robust and efficient hyperparameter tuning algorithm at scale.
    BO is an abbreviation for "Bayesian Optimization" and HB is an abbreviation for "Hyperband".

    BOHB relies on HB (Hyperband) to determine how many configurations to evaluate with which budget,
    but it replaces the random selection of configurations at the beginning of each HB iteration
    by a model-based search (Bayesian Optimization).
    Once the desired number of configurations for the iteration is reached,
    the standard successive halving procedure is carried out using these configurations.
    It keeps track of the performance of all function evaluations g(x, b) of configurations x
    on all budgets b to use as a basis for our models in later iterations.
    Please refer to the paper :footcite:t:`falkner2018bohb` for detailed algorithm.

    Note that BOHB needs additional installation using the following command:

    .. code-block:: bash

        pip install nni[BOHB]

    Examples
    --------

    .. code-block::

        config.tuner.name = \'BOHB\'
        config.tuner.class_args = {
            \'optimize_mode\': \'maximize\',
            \'min_budget\': 1,
            \'max_budget\': 27,
            \'eta\': 3,
            \'min_points_in_model\': 7,
            \'top_n_percent\': 15,
            \'num_samples\': 64,
            \'random_fraction\': 0.33,
            \'bandwidth_factor\': 3.0,
            \'min_bandwidth\': 0.001
        }

    Parameters
    ----------
    optimize_mode: str
        Optimize mode, \'maximize\' or \'minimize\'.
    min_budget: float
        The smallest budget to assign to a trial job, (budget can be the number of mini-batches or epochs).
        Needs to be positive.
    max_budget: float
        The largest budget to assign to a trial job. Needs to be larger than min_budget.
        The budgets will be geometrically distributed
        :math:`a^2 + b^2 = c^2 \\sim \\eta^k` for :math:`k\\in [0, 1, ... , num\\_subsets - 1]`.
    eta: int
        In each iteration, a complete run of sequential halving is executed. In it,
        after evaluating each configuration on the same subset size, only a fraction of
        1/eta of them \'advances\' to the next round.
        Must be greater or equal to 2.
    min_points_in_model: int
        Number of observations to start building a KDE. Default \'None\' means dim+1;
        when the number of completed trials in this budget is equal to or larger than ``max{dim+1, min_points_in_model}``,
        BOHB will start to build a KDE model of this budget then use said KDE model to guide configuration selection.
        Needs to be positive. (dim means the number of hyperparameters in search space)
    top_n_percent: int
        Percentage (between 1 and 99, default 15) of the observations which are considered good.
        Good points and bad points are used for building KDE models.
        For example, if you have 100 observed trials and top_n_percent is 15,
        then the top 15% of points will be used for building the good points models "l(x)".
        The remaining 85% of points will be used for building the bad point models "g(x)".
    num_samples: int
        Number of samples to optimize EI (default 64).
        In this case, it will sample "num_samples" points and compare the result of l(x)/g(x).
        Then it will return the one with the maximum l(x)/g(x) value as the next configuration
        if the optimize_mode is ``maximize``. Otherwise, it returns the smallest one.
    random_fraction: float
        Fraction of purely random configurations that are sampled from the prior without the model.
    bandwidth_factor: float
        To encourage diversity, the points proposed to optimize EI are sampled
        from a \'widened\' KDE where the bandwidth is multiplied by this factor (default: 3).
        It is suggested to use the default value if you are not familiar with KDE.
    min_bandwidth: float
        To keep diversity, even when all (good) samples have the same value for one of the parameters,
        a minimum bandwidth (default: 1e-3) is used instead of zero.
        It is suggested to use the default value if you are not familiar with KDE.
    config_space: str
        Directly use a .pcs file serialized by `ConfigSpace <https://automl.github.io/ConfigSpace/>` in "pcs new" format.
        In this case, search space file (if provided in config) will be ignored.
        Note that this path needs to be an absolute path. Relative path is currently not supported.

    Notes
    -----

    Below is the introduction of the BOHB process separated in two parts:

    **The first part HB (Hyperband).**
    BOHB follows Hyperband’s way of choosing the budgets and continue to use SuccessiveHalving.
    For more details, you can refer to the :class:`nni.algorithms.hpo.hyperband_advisor.Hyperband`
    and the `reference paper for Hyperband <https://arxiv.org/abs/1603.06560>`__.
    This procedure is summarized by the pseudocode below.

    .. image:: ../../img/bohb_1.png
        :scale: 80 %
        :align: center

    **The second part BO (Bayesian Optimization)**
    The BO part of BOHB closely resembles TPE with one major difference:
    It opted for a single multidimensional KDE compared to the hierarchy of one-dimensional KDEs used in TPE
    in order to better handle interaction effects in the input space.
    Tree Parzen Estimator(TPE): uses a KDE (kernel density estimator) to model the densities.

    .. image:: ../../img/bohb_2.png
        :scale: 80 %
        :align: center

    To fit useful KDEs, we require a minimum number of data points Nmin;
    this is set to d + 1 for our experiments, where d is the number of hyperparameters.
    To build a model as early as possible, we do not wait until Nb = \\|Db\\|,
    where the number of observations for budget b is large enough to satisfy q · Nb ≥ Nmin.
    Instead, after initializing with Nmin + 2 random configurations, we choose the
    best and worst configurations, respectively, to model the two densities.
    Note that it also samples a constant fraction named **random fraction** of the configurations uniformly at random.

    .. image:: ../../img/bohb_3.png
        :scale: 80 %
        :align: center


    .. image:: ../../img/bohb_6.jpg
        :scale: 65 %
        :align: center

    **The above image shows the workflow of BOHB.**
    Here set max_budget = 9, min_budget = 1, eta = 3, others as default.
    In this case, s_max = 2, so we will continuously run the {s=2, s=1, s=0, s=2, s=1, s=0, ...} cycle.
    In each stage of SuccessiveHalving (the orange box), it will pick the top 1/eta configurations and run them again with more budget,
    repeating the SuccessiveHalving stage until the end of this iteration.
    At the same time, it collects the configurations, budgets and final metrics of each trial
    and use these to build a multidimensional KDEmodel with the key "budget".
    Multidimensional KDE is used to guide the selection of configurations for the next iteration.
    The sampling procedure (using Multidimensional KDE to guide selection) is summarized by the pseudocode below.

    .. image:: ../../img/bohb_4.png
        :scale: 80 %
        :align: center

    **Here is a simple experiment which tunes MNIST with BOHB.**
    Code implementation: :githublink:`examples/trials/mnist-advisor <examples/trials/mnist-advisor>`
    The following is the experimental final results:

    .. image:: ../../img/bohb_5.png
        :scale: 80 %
        :align: center

    More experimental results can be found in the `reference paper <https://arxiv.org/abs/1807.01774>`__.
    It shows that BOHB makes good use of previous results and has a balanced trade-off in exploration and exploitation.
    '''
    optimize_mode: Incomplete
    min_budget: Incomplete
    max_budget: Incomplete
    eta: Incomplete
    min_points_in_model: Incomplete
    top_n_percent: Incomplete
    num_samples: Incomplete
    random_fraction: Incomplete
    bandwidth_factor: Incomplete
    min_bandwidth: Incomplete
    config_space: Incomplete
    generated_hyper_configs: Incomplete
    completed_hyper_configs: Incomplete
    s_max: Incomplete
    curr_s: Incomplete
    credit: int
    brackets: Incomplete
    search_space: Incomplete
    parameters: Incomplete
    cg: Incomplete
    job_id_para_id_map: Incomplete
    unsatisfied_jobs: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', min_budget: int = 1, max_budget: int = 3, eta: int = 3, min_points_in_model: Incomplete | None = None, top_n_percent: int = 15, num_samples: int = 64, random_fraction=..., bandwidth_factor: int = 3, min_bandwidth: float = 0.001, config_space: Incomplete | None = None) -> None: ...
    def handle_initialize(self, data) -> None:
        """Initialize Tuner, including creating Bayesian optimization-based parametric models
        and search space formations

        Parameters
        ----------
        data: search space
            search space of this experiment

        Raises
        ------
        ValueError
            Error: Search space is None
        """
    def generate_new_bracket(self) -> None:
        """generate a new bracket"""
    def handle_request_trial_jobs(self, data) -> None:
        """recerive the number of request and generate trials

        Parameters
        ----------
        data: int
            number of trial jobs that nni manager ask to generate
        """
    def handle_update_search_space(self, data) -> None:
        """change json format to ConfigSpace format dict<dict> -> configspace

        Parameters
        ----------
        data: JSON object
            search space of this experiment
        """
    def handle_trial_end(self, data) -> None:
        """receive the information of trial end and generate next configuaration.

        Parameters
        ----------
        data: dict()
            it has three keys: trial_job_id, event, hyper_params
            trial_job_id: the id generated by training service
            event: the job's state
            hyper_params: the hyperparameters (a string) generated and returned by tuner
        """
    def handle_report_metric_data(self, data) -> None:
        """reveice the metric data and update Bayesian optimization with final result

        Parameters
        ----------
        data:
            it is an object which has keys 'parameter_id', 'value', 'trial_job_id', 'type', 'sequence'.

        Raises
        ------
        ValueError
            Data type not supported
        """
    def handle_add_customized_trial(self, data) -> None: ...
    def handle_import_data(self, data) -> None:
        """Import additional data for tuning

        Parameters
        ----------
        data:
            a list of dictionarys, each of which has at least two keys, 'parameter' and 'value'

        Raises
        ------
        AssertionError
            data doesn't have required key 'parameter' and 'value'
        """
