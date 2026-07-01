from .model import Model as Model
from .policy import build_lstm_policy as build_lstm_policy
from .util import set_global_seeds as set_global_seeds
from _typeshed import Incomplete
from nni import ClassArgsValidator as ClassArgsValidator
from nni.tuner import Tuner as Tuner
from nni.utils import OptimizeMode as OptimizeMode, extract_scalar_reward as extract_scalar_reward

logger: Incomplete

class ModelConfig:
    """
    Configurations of the PPO model
    """
    observation_space: Incomplete
    action_space: Incomplete
    num_envs: int
    nsteps: int
    ent_coef: float
    lr: float
    vf_coef: float
    max_grad_norm: float
    gamma: float
    lam: float
    cliprange: float
    embedding_size: Incomplete
    noptepochs: int
    total_timesteps: int
    nminibatches: int
    def __init__(self) -> None: ...

class TrialsInfo:
    """
    Informations of each trial from one model inference
    """
    iter: int
    obs: Incomplete
    actions: Incomplete
    values: Incomplete
    neglogpacs: Incomplete
    dones: Incomplete
    last_value: Incomplete
    rewards: Incomplete
    returns: Incomplete
    inf_batch_size: Incomplete
    def __init__(self, obs, actions, values, neglogpacs, dones, last_value, inf_batch_size) -> None: ...
    def get_next(self):
        """
        Get actions of the next trial
        """
    def update_rewards(self, rewards, returns) -> None:
        """
        After the trial is finished, reward and return of this trial is updated
        """
    def convert_shape(self):
        """
        Convert shape
        """

class PPOModel:
    """
    PPO Model
    """
    model_config: Incomplete
    states: Incomplete
    nupdates: Incomplete
    cur_update: int
    np_mask: Incomplete
    lr: Incomplete
    cliprange: Incomplete
    nbatch: Incomplete
    model: Incomplete
    def __init__(self, model_config, mask) -> None: ...
    def inference(self, num):
        """
        Generate actions along with related info from policy network.
        observation is the action of the last step.

        Parameters
        ----------
        num: int
            The number of trials to generate

        Returns
        -------
        mb_obs : list
            Observation of the ``num`` configurations
        mb_actions : list
            Actions of the ``num`` configurations
        mb_values : list
            Values from the value function of the ``num`` configurations
        mb_neglogpacs : list
            ``neglogp`` of the ``num`` configurations
        mb_dones : list
            To show whether the play is done, always ``True``
        last_values : tensorflow tensor
            The last values of the ``num`` configurations, got with session run
        """
    def compute_rewards(self, trials_info, trials_result) -> None:
        """
        Compute the rewards of the trials in trials_info based on trials_result,
        and update the rewards in trials_info

        Parameters
        ----------
        trials_info : TrialsInfo
            Info of the generated trials
        trials_result : list
            Final results (e.g., acc) of the generated trials
        """
    def train(self, trials_info, nenvs) -> None:
        """
        Train the policy/value network using trials_info

        Parameters
        ----------
        trials_info : TrialsInfo
            Complete info of the generated trials from the previous inference
        nenvs : int
            The batch size of the (previous) inference
        """

class PPOClassArgsValidator(ClassArgsValidator):
    def validate_class_args(self, **kwargs) -> None: ...

class PPOTuner(Tuner):
    """
    PPOTuner, the implementation inherits the main logic of the implementation
    `ppo2 from openai <https://github.com/openai/baselines/tree/master/baselines/ppo2>`__ and is adapted for NAS scenario.
    It uses ``lstm`` for its policy network and value network, policy and value share the same network.

    Parameters
    ----------
    optimize_mode : str
        maximize or minimize
    trials_per_update : int
        Number of trials to have for each model update
    epochs_per_update : int
        Number of epochs to run for each model update
    minibatch_size : int
        Minibatch size (number of trials) for the update
    ent_coef : float
        Policy entropy coefficient in the optimization objective
    lr : float
        Learning rate of the model (lstm network), constant
    vf_coef : float
        Value function loss coefficient in the optimization objective
    max_grad_norm : float
        Gradient norm clipping coefficient
    gamma : float
        Discounting factor
    lam : float
        Advantage estimation discounting factor (lambda in the paper)
    cliprange : float
        Cliprange in the PPO algorithm, constant
    """
    optimize_mode: Incomplete
    model_config: Incomplete
    model: Incomplete
    search_space: Incomplete
    running_trials: Incomplete
    inf_batch_size: Incomplete
    first_inf: bool
    trials_result: Incomplete
    credit: int
    param_ids: Incomplete
    finished_trials: int
    chosen_arch_template: Incomplete
    actions_spaces: Incomplete
    actions_to_config: Incomplete
    full_act_space: Incomplete
    trials_info: Incomplete
    all_trials: Incomplete
    send_trial_callback: Incomplete
    def __init__(self, optimize_mode, trials_per_update: int = 20, epochs_per_update: int = 4, minibatch_size: int = 4, ent_coef: float = 0.0, lr: float = 0.0003, vf_coef: float = 0.5, max_grad_norm: float = 0.5, gamma: float = 0.99, lam: float = 0.95, cliprange: float = 0.2) -> None: ...
    def update_search_space(self, search_space) -> None:
        """
        Get search space, currently the space only includes that for NAS

        Parameters
        ----------
        search_space : dict
            Search space for NAS
            the format could be referred to search space spec (https://nni.readthedocs.io/en/latest/Tutorial/SearchSpaceSpec.html).
        """
    def generate_multiple_parameters(self, parameter_id_list, **kwargs):
        """
        Returns multiple sets of trial (hyper-)parameters, as iterable of serializable objects.

        Parameters
        ----------
        parameter_id_list : list of int
            Unique identifiers for each set of requested hyper-parameters.
            These will later be used in :meth:`receive_trial_result`.
        **kwargs
            Not used

        Returns
        -------
        list
            A list of newly generated configurations
        """
    def generate_parameters(self, parameter_id, **kwargs):
        """
        Generate parameters, if no trial configration for now, self.credit plus 1 to send the config later

        Parameters
        ----------
        parameter_id : int
            Unique identifier for requested hyper-parameters.
            This will later be used in :meth:`receive_trial_result`.
        **kwargs
            Not used

        Returns
        -------
        dict
            One newly generated configuration

        """
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None:
        """
        Receive trial's result. if the number of finished trials equals self.inf_batch_size, start the next update to
        train the model.

        Parameters
        ----------
        parameter_id : int
            Unique identifier of used hyper-parameters, same with :meth:`generate_parameters`.
        parameters : dict
            Hyper-parameters generated by :meth:`generate_parameters`.
        value : dict
            Result from trial (the return value of :func:`nni.report_final_result`).
        """
    def trial_end(self, parameter_id, success, **kwargs) -> None:
        """
        To deal with trial failure. If a trial fails, it is popped out from ``self.running_trials``,
        and the final result of this trial is assigned with the average of the finished trials.

        Parameters
        ----------
        parameter_id : int
            Unique identifier for hyper-parameters used by this trial.
        success : bool
            True if the trial successfully completed; False if failed or terminated.
        **kwargs
            Not used
        """
    def import_data(self, data) -> None:
        """
        Import additional data for tuning, not supported yet.

        Parameters
        ----------
        data : list
            A list of dictionarys, each of which has at least two keys, ``parameter`` and ``value``
        """
