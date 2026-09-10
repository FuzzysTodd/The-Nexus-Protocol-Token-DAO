from .. import AMCWeightMasker as AMCWeightMasker
from _typeshed import Incomplete
from nni.compression.pytorch.compressor import PrunerModuleWrapper as PrunerModuleWrapper

def acc_reward(net, acc, flops): ...
def acc_flops_reward(net, acc, flops): ...

class ChannelPruningEnv:
    """
    Env for channel pruning search.
    This class is used to prune model using specified pruner. It prunes one layer when
    step() is called. When the last layer is pruned, it evaluate the pruned model using
    evaluator, and use the returned value of evaluator as reward of the episode.

    Usage:
        env = ChannelPruningEnv(pruner, evaluator, val_loader, checkpoint, env_args)
        episode = 0
        T = []
        while episode < num_episode:
            action = agent.select_action(observation)
            observation2, reward, done, info = env.step(action)
            T.append([reward, deepcopy(observation), deepcopy(observation2), action, done])

            if done: # end of episode, last layer pruned
                episode += 1
                # train agent with episode data
                for _, s_t, s_t1, a_t, done in T:
                    agent.observe(final_reward, s_t, s_t1, a_t, done)
                    agent.update_policy()
                T = []

    Attributes:
        prunable_idx: layer indices for pruable layers, the index values are the index
            of list(self.model.modules()). Pruable layers are pointwise Conv2d layers and Linear
            layers.
        buffer_idx: layer indices for buffer layers which refers the depthwise layers.
            Each depthwise layer is always followd by a pointwise layer for both mobilenet and
            mobilenetv2. The depthwise layer's filters are pruned when its next pointwise layer's
            corresponding input channels are pruned.
        shared_idx: layer indices for layers which share input.
            For example: [[1,4], [8, 10, 15]] means layer 1 and 4 share same input, and layer
            8, 10 and 15 share another input.
        layer_embedding: embeddings for each prunable layers, the embedding is used as
            observation for DDPG agent.
        layer_info_dict: flops and number of parameters of each layer.
        min_strategy_dict: key is layer index, value is a tuple, the first value is the minimum
            action of input channel, the second value is the minimum action value of output channel.
        strategy_dict: key is layer index, value is a tuple, the first value is the action of input
            channel, the second value is the action of output channel.

    Parameters:
        pruner: Pruner
            NNI Pruner instance used to prune model.
        evaluator: function
            function to evaluate the pruned model.
            The prototype of the function:
                >>> def evaluator(val_loader, model):
                >>>     ...
                >>>     return acc
        val_loader: torch.utils.data.DataLoader
            Data loader of validation dataset.
        checkpoint: dict
            checkpoint of the model to be pruned. It is used to reset model at beginning of each
            episode.
        args:
            A Namespace object containing following arguments:
            model_type: str
                model type to prune, currently 'mobilenet', 'mobilenetv2' and 'resnet' are supported.
            flops_ratio: float
                preserve flops ratio.
            lbound: float
                minimum weight preserve ratio for each layer.
            rbound: float
                maximum weight preserve ratio for each layer.
            reward: function
                reward function type

            # parameters for channel pruning
            n_calibration_batches: int
                number of batches to extract layer information.
            n_points_per_layer: int
                number of feature points per layer.
            channel_round: int
                round channel to multiple of channel_round.

    """
    pruner: Incomplete
    model: Incomplete
    checkpoint: Incomplete
    batch_size: Incomplete
    preserve_ratio: Incomplete
    channel_prune_masker: Incomplete
    args: Incomplete
    lbound: Incomplete
    rbound: Incomplete
    n_calibration_batches: Incomplete
    n_points_per_layer: Incomplete
    channel_round: Incomplete
    n_prunable_layer: Incomplete
    org_acc: Incomplete
    org_model_size: Incomplete
    org_flops: Incomplete
    expected_preserve_computation: Incomplete
    reward: Incomplete
    best_reward: Incomplete
    best_strategy: Incomplete
    best_d_prime_list: Incomplete
    best_masks: Incomplete
    org_w_size: Incomplete
    def __init__(self, pruner, evaluator, val_loader, checkpoint, args) -> None: ...
    val_time: Incomplete
    def step(self, action): ...
    cur_ind: int
    strategy: Incomplete
    d_prime_list: Incomplete
    strategy_dict: Incomplete
    extract_time: int
    fit_time: int
    visited: Incomplete
    index_buffer: Incomplete
    def reset(self): ...
    def prune_kernel(self, op_idx, preserve_ratio, preserve_idx: Incomplete | None = None): ...
