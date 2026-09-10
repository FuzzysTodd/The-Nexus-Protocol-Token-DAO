from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator, parameter_expressions as parameter_expressions
from nni.common.hpo_utils import validate_search_space as validate_search_space
from nni.runtime.common import multi_phase_enabled as multi_phase_enabled
from nni.runtime.msg_dispatcher_base import MsgDispatcherBase as MsgDispatcherBase
from nni.runtime.tuner_command_channel import CommandType as CommandType
from nni.utils import MetricType as MetricType, NodeType as NodeType, OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward

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
    brackets_id: string
        brackets id
    brackets_curr_decay:
        brackets curr decay
    increased_id: int
        increased id

    Returns
    -------
    int
        params id
    """
def json2parameter(ss_spec, random_state):
    """Randomly generate values for hyperparameters from hyperparameter space i.e., x.

    Parameters
    ----------
    ss_spec:
        hyperparameter space
    random_state:
        random operator to generate random values

    Returns
    -------
    Parameter:
        Parameters in this experiment
    """

class Bracket:
    """
    A bracket in Hyperband, all the information of a bracket is managed by an instance of this class

    Parameters
    ----------
    bracket_id: string
        The id of this bracket, usually be set as '{Hyperband index}-{SH iteration index}'
    s: int
        The current SH iteration index.
    s_max: int
        total number of SH iterations
    eta: float
        In each iteration, a complete run of sequential halving is executed. In it,
\t\tafter evaluating each configuration on the same subset size, only a fraction of
\t\t1/eta of them 'advances' to the next round.
    R:
        the budget associated with each stage
    optimize_mode: str
        optimize mode, 'maximize' or 'minimize'
    """
    bracket_id: Incomplete
    s: Incomplete
    s_max: Incomplete
    eta: Incomplete
    n: Incomplete
    r: Incomplete
    i: int
    hyper_configs: Incomplete
    configs_perf: Incomplete
    num_configs_to_run: Incomplete
    num_finished_configs: Incomplete
    optimize_mode: Incomplete
    no_more_trial: bool
    def __init__(self, bracket_id, s, s_max, eta, R, optimize_mode) -> None: ...
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
        """
    def get_hyperparameter_configurations(self, num, r, searchspace_json, random_state):
        """Randomly generate num hyperparameter configurations from search space

        Parameters
        ----------
        num: int
            the number of hyperparameter configurations

        Returns
        -------
        list
            a list of hyperparameter configurations. Format: [[key1, value1], [key2, value2], ...]
        """

class HyperbandClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class Hyperband(MsgDispatcherBase):
    """
    `Hyperband <https://arxiv.org/pdf/1603.06560.pdf>`__ is a multi-fidelity hyperparameter tuning algorithm
    based on successive halving.

    The basic idea of Hyperband is to create several buckets,
    each having ``n`` randomly generated hyperparameter configurations,
    each configuration using ``r`` resources (e.g., epoch number, batch number).
    After the ``n`` configurations are finished, it chooses the top ``n/eta`` configurations
    and runs them using increased ``r*eta`` resources.
    At last, it chooses the best configuration it has found so far.
    Please refer to the paper :footcite:t:`li2017hyperband` for detailed algorithm.

    Examples
    --------

    .. code-block::

        config.tuner.name = 'Hyperband'
        config.tuner.class_args = {
            'optimize_mode': 'maximize',
            'R': 60,
            'eta': 3
        }


    Note that once you use Advisor, you are not allowed to add a Tuner and Assessor spec in the config file.
    When Hyperband is used, the dict returned by :func:`nni.get_next_parameter` one more key
    called ``TRIAL_BUDGET`` besides the hyperparameters and their values.
    **With this TRIAL_BUDGET, users can control in trial code how long a trial runs by following
    the suggested trial budget from Hyperband.** ``TRIAL_BUDGET`` is a relative number,
    users can interpret them as number of epochs, number of mini-batches, running time, etc.

    Here is a concrete example of ``R=81`` and ``eta=3``:

    .. list-table::
        :header-rows: 1
        :widths: auto

        * -
          - s=4
          - s=3
          - s=2
          - s=1
          - s=0
        * - i
          - n r
          - n r
          - n r
          - n r
          - n r
        * - 0
          - 81 1
          - 27 3
          - 9 9
          - 6 27
          - 5 81
        * - 1
          - 27 3
          - 9 9
          - 3 27
          - 2 81
          -
        * - 2
          - 9 9
          - 3 27
          - 1 81
          -
          -
        * - 3
          - 3 27
          - 1 81
          -
          -
          -
        * - 4
          - 1 81
          -
          -
          -
          -


    ``s`` means bucket, ``n`` means the number of configurations that are generated,
    the corresponding ``r`` means how many budgets these configurations run.
    ``i`` means round, for example, bucket 4 has 5 rounds, bucket 3 has 4 rounds.

    A complete example can be found :githublink:`examples/trials/mnist-advisor`.

    Parameters
    ----------
    optimize_mode: str
        Optimize mode, 'maximize' or 'minimize'.

    R: int
        The maximum amount of budget that can be allocated to a single configuration.
        Here, trial budget could mean the number of epochs, number of mini-batches, etc.,
        depending on how users interpret it.
        Each trial should use ``TRIAL_BUDGET`` to control how long it runs.

    eta: int
        The variable that controls the proportion of configurations discarded in each round of SuccessiveHalving.
        ``1/eta`` configurations will survive and rerun using more budgets in each round.

    exec_mode: str
        Execution mode, 'serial' or 'parallelism'.
        If 'parallelism', the tuner will try to use available resources to start new bucket immediately.
        If 'serial', the tuner will only start new bucket after the current bucket is done.


    Notes
    -----

    First, Hyperband an example of how to write an autoML algorithm based on MsgDispatcherBase,
    rather than based on Tuner and Assessor. Hyperband is implemented in this way
    because it integrates the functions of both Tuner and Assessor,thus, we call it Advisor.

    Second, this implementation fully leverages Hyperband's internal parallelism.
    Specifically, the next bucket is not started strictly after the current bucket.
    Instead, it starts when there are available resources. If you want to use full parallelism mode,
    set ``exec_mode`` to ``parallelism``.

    Or if you want to set ``exec_mode`` with ``serial`` according to the original algorithm.
    In this mode, the next bucket will start strictly after the current bucket.

    ``parallelism`` mode may lead to multiple unfinished buckets,
    in contrast, there is at most one unfinished bucket under ``serial`` mode.
    The advantage of ``parallelism`` mode is to make full use of resources,
    which may reduce the experiment duration multiple times.
    """
    R: Incomplete
    eta: Incomplete
    brackets: Incomplete
    generated_hyper_configs: Incomplete
    completed_hyper_configs: Incomplete
    s_max: Incomplete
    curr_s: Incomplete
    curr_hb: int
    exec_mode: Incomplete
    curr_bracket_id: Incomplete
    searchspace_json: Incomplete
    random_state: Incomplete
    optimize_mode: Incomplete
    credit: int
    job_id_para_id_map: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', R: int = 60, eta: int = 3, exec_mode: str = 'parallelism') -> None:
        """B = (s_max + 1)R"""
    def handle_initialize(self, data) -> None:
        """callback for initializing the advisor
        Parameters
        ----------
        data: dict
            search space
        """
    def handle_request_trial_jobs(self, data) -> None:
        """
        Parameters
        ----------
        data: int
            number of trial jobs
        """
    def handle_update_search_space(self, data) -> None:
        """data: JSON object, which is search space
        """
    def handle_trial_end(self, data) -> None:
        """
        Parameters
        ----------
        data: dict()
            it has three keys: trial_job_id, event, hyper_params
            trial_job_id: the id generated by training service
            event: the job's state
            hyper_params: the hyperparameters (a string) generated and returned by tuner
        """
    def handle_report_metric_data(self, data) -> None:
        """
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
    def handle_import_data(self, data) -> None: ...
