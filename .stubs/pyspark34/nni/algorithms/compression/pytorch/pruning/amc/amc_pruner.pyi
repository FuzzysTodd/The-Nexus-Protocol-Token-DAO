from .channel_pruning_env import ChannelPruningEnv as ChannelPruningEnv
from .lib.agent import DDPG as DDPG
from .lib.utils import get_output_folder as get_output_folder
from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Pruner as Pruner

class AMCPruner(Pruner):
    """
    A pytorch implementation of AMC: AutoML for Model Compression and Acceleration on Mobile Devices.
    (https://arxiv.org/pdf/1802.03494.pdf)

    Parameters:
        model: nn.Module
            The model to be pruned.
        config_list: list
            Configuration list to configure layer pruning.
            Supported keys:
            - op_types: operation type to be pruned
            - op_names: operation name to be pruned
        evaluator: function
            function to evaluate the pruned model.
            The prototype of the function:
            >>> def evaluator(val_loader, model):
            >>>     ...
            >>>     return acc
        val_loader: torch.utils.data.DataLoader
            Data loader of validation dataset.
        suffix: str
            suffix to help you remember what experiment you ran. Default: None.

        # parameters for pruning environment
        model_type: str
            model type to prune, currently 'mobilenet' and 'mobilenetv2' are supported. Default: mobilenet
        flops_ratio: float
            preserve flops ratio. Default: 0.5
        lbound: float
            minimum weight preserve ratio for each layer. Default: 0.2
        rbound: float
            maximum weight preserve ratio for each layer. Default: 1.0
        reward: function
            reward function type:
            - acc_reward: accuracy * 0.01
            - acc_flops_reward: - (100 - accuracy) * 0.01 * np.log(flops)
            Default: acc_reward
        # parameters for channel pruning
        n_calibration_batches: int
            number of batches to extract layer information. Default: 60
        n_points_per_layer: int
            number of feature points per layer. Default: 10
        channel_round: int
            round channel to multiple of channel_round. Default: 8

        # parameters for ddpg agent
        hidden1: int
            hidden num of first fully connect layer. Default: 300
        hidden2: int
            hidden num of second fully connect layer. Default: 300
        lr_c: float
            learning rate for critic. Default: 1e-3
        lr_a: float
            learning rate for actor. Default: 1e-4
        warmup: int
            number of episodes without training but only filling the replay memory. During warmup episodes,
            random actions ares used for pruning. Default: 100
        discount: float
            next Q value discount for deep Q value target. Default: 0.99
        bsize: int
            minibatch size for training DDPG agent. Default: 64
        rmsize: int
            memory size for each layer. Default: 100
        window_length: int
            replay buffer window length. Default: 1
        tau: float
            moving average for target network being used by soft_update. Default: 0.99
        # noise
        init_delta: float
            initial variance of truncated normal distribution
        delta_decay: float
            delta decay during exploration

        # parameters for training ddpg agent
        max_episode_length: int
            maximum episode length
        output_dir: str
            output directory to save log files and model files. Default: ./logs
        debug: boolean
            debug mode
        train_episode: int
            train iters each timestep. Default: 800
        epsilon: int
            linear decay of exploration policy. Default: 50000
        seed: int
            random seed to set for reproduce experiment. Default: None
    """
    val_loader: Incomplete
    evaluator: Incomplete
    output_dir: Incomplete
    env_args: Incomplete
    env: Incomplete
    tfwriter: Incomplete
    text_writer: Incomplete
    ddpg_args: Incomplete
    agent: Incomplete
    def __init__(self, model, config_list, evaluator, val_loader, suffix: Incomplete | None = None, model_type: str = 'mobilenet', dataset: str = 'cifar10', flops_ratio: float = 0.5, lbound: float = 0.2, rbound: float = 1.0, reward: str = 'acc_reward', n_calibration_batches: int = 60, n_points_per_layer: int = 10, channel_round: int = 8, hidden1: int = 300, hidden2: int = 300, lr_c: float = 0.001, lr_a: float = 0.0001, warmup: int = 100, discount: float = 1.0, bsize: int = 64, rmsize: int = 100, window_length: int = 1, tau: float = 0.01, init_delta: float = 0.5, delta_decay: float = 0.99, max_episode_length: float = 1000000000.0, output_dir: str = './logs', debug: bool = False, train_episode: int = 800, epsilon: int = 50000, seed: Incomplete | None = None) -> None: ...
    def compress(self) -> None: ...
    def train(self, num_episode, agent, env, output_dir) -> None: ...
