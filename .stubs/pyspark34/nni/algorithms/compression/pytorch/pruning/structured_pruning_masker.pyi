from .weight_masker import WeightMasker
from _typeshed import Incomplete

__all__ = ['L1FilterPrunerMasker', 'L2FilterPrunerMasker', 'FPGMPrunerMasker', 'TaylorFOWeightFilterPrunerMasker', 'ActivationAPoZRankFilterPrunerMasker', 'ActivationMeanRankFilterPrunerMasker', 'SlimPrunerMasker', 'AMCWeightMasker']

class StructuredWeightMasker(WeightMasker):
    """
    A structured pruning masker base class that prunes convolutional layer filters.

    Parameters
    ----------
    model: nn.Module
        model to be pruned
    pruner: Pruner
        A Pruner instance used to prune the model
    preserve_round: int
        after pruning, preserve filters/channels round to `preserve_round`, for example:
        for a Conv2d layer, output channel is 32, sparsity is 0.2, if preserve_round is
        1 (no preserve round), then there will be int(32 * 0.2) = 6 filters pruned, and
        32 - 6 = 26 filters are preserved. If preserve_round is 4, preserved filters will
        be round up to 28 (which can be divided by 4) and only 4 filters are pruned.

    """
    model: Incomplete
    pruner: Incomplete
    preserve_round: Incomplete
    dependency_aware: Incomplete
    global_sort: Incomplete
    def __init__(self, model, pruner, preserve_round: int = 1, dependency_aware: bool = False, global_sort: bool = False) -> None: ...
    def calc_mask(self, sparsity, wrapper, wrapper_idx: Incomplete | None = None, **depen_kwargs):
        """
        calculate the mask for `wrapper`.

        Parameters
        ----------
        sparsity: float/list of float
            The target sparsity of the wrapper. If we calculate the mask in
            the normal way, then sparsity is a float number. In contrast, if
            we calculate the mask in the dependency-aware way, sparsity is a
            list of float numbers, each float number corressponds to a sparsity
            of a layer.
        wrapper: PrunerModuleWrapper/list of PrunerModuleWrappers
            The wrapper of the target layer. If we calculate the mask in the normal
            way, then `wrapper` is an instance of PrunerModuleWrapper, else `wrapper`
            is a list of PrunerModuleWrapper.
        wrapper_idx: int/list of int
            The index of the wrapper.
        depen_kwargs: dict
            The kw_args for the dependency-aware mode.
        """
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None) -> None:
        """
        Calculate the mask of given layer.

        Parameters
        ----------
        base_mask: dict
            The basic mask with the same shape of weight, all item in the basic mask is 1.
        weight: tensor
            the module weight to be pruned
        num_prune: int
            Num of filters to prune
        wrapper: PrunerModuleWrapper
            layer wrapper of this layer
        wrapper_idx: int
            index of this wrapper in pruner's all wrappers
        channel_masks: Tensor
            If mask some channels for this layer in advance. In the dependency-aware
            mode, before calculating the masks for each layer, we will calculate a common
            mask for all the layers in the dependency set. For the pruners that doesnot
            support dependency-aware mode, they can just ignore this parameter.

        Returns
        -------
        dict
            dictionary for storing masks
        """
    def get_channel_sum(self, wrapper, wrapper_idx) -> None:
        """
        Calculate the importance weight for each channel. If want to support the
        dependency-aware mode for this one-shot pruner, this function must be
        implemented.
        Parameters
        ----------
        wrapper: PrunerModuleWrapper
            layer wrapper of this layer
        wrapper_idx: int
            index of this wrapper in pruner's all wrappers
        Returns
        -------
        tensor
            Tensor that indicates the importance of each channel
        """

class L1FilterPrunerMasker(StructuredWeightMasker):
    '''
    A structured pruning algorithm that prunes the filters of smallest magnitude
    weights sum in the convolution layers to achieve a preset level of network sparsity.
    Hao Li, Asim Kadav, Igor Durdanovic, Hanan Samet and Hans Peter Graf,
    "PRUNING FILTERS FOR EFFICIENT CONVNETS", 2017 ICLR
    https://arxiv.org/abs/1608.08710
    '''
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None): ...
    def get_channel_sum(self, wrapper, wrapper_idx): ...

class L2FilterPrunerMasker(StructuredWeightMasker):
    """
    A structured pruning algorithm that prunes the filters with the
    smallest L2 norm of the weights.
    """
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None): ...
    def get_channel_sum(self, wrapper, wrapper_idx): ...

class FPGMPrunerMasker(StructuredWeightMasker):
    '''
    A filter pruner via geometric median.
    "Filter Pruning via Geometric Median for Deep Convolutional Neural Networks Acceleration",
    https://arxiv.org/pdf/1811.00250.pdf
    '''
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None): ...
    def get_channel_sum(self, wrapper, wrapper_idx): ...

class TaylorFOWeightFilterPrunerMasker(StructuredWeightMasker):
    '''
    A structured pruning algorithm that prunes the filters with the smallest
    importance approximations based on the first order taylor expansion on the weight.
    Molchanov, Pavlo and Mallya, Arun and Tyree, Stephen and Frosio, Iuri and Kautz, Jan,
    "Importance Estimation for Neural Network Pruning", CVPR 2019.
    http://jankautz.com/publications/Importance4NNPruning_CVPR19.pdf
    '''
    statistics_batch_num: Incomplete
    global_threshold: Incomplete
    def __init__(self, model, pruner, statistics_batch_num: int = 1) -> None: ...
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None): ...
    def calc_contributions(self) -> None:
        """
        Calculate the estimated importance of filters as a sum of individual contribution
        based on the first order taylor expansion.
        """
    def get_channel_sum(self, wrapper, wrapper_idx): ...

class ActivationFilterPrunerMasker(StructuredWeightMasker):
    statistics_batch_num: Incomplete
    def __init__(self, model, pruner, statistics_batch_num: int = 1, activation: str = 'relu') -> None: ...

class ActivationAPoZRankFilterPrunerMasker(ActivationFilterPrunerMasker):
    '''
    A structured pruning algorithm that prunes the filters with the
    smallest APoZ(average percentage of zeros) of output activations.
    Hengyuan Hu, Rui Peng, Yu-Wing Tai and Chi-Keung Tang,
    "Network Trimming: A Data-Driven Neuron Pruning Approach towards Efficient Deep Architectures", ICLR 2016.
    https://arxiv.org/abs/1607.03250
    '''
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None): ...
    def get_channel_sum(self, wrapper, wrapper_idx): ...

class ActivationMeanRankFilterPrunerMasker(ActivationFilterPrunerMasker):
    '''
    A structured pruning algorithm that prunes the filters with the
    smallest mean value of output activations.
    Pavlo Molchanov, Stephen Tyree, Tero Karras, Timo Aila and Jan Kautz,
    "Pruning Convolutional Neural Networks for Resource Efficient Inference", ICLR 2017.
    https://arxiv.org/abs/1611.06440
    '''
    def get_mask(self, base_mask, weight, num_prune, wrapper, wrapper_idx, channel_masks: Incomplete | None = None): ...
    def get_channel_sum(self, wrapper, wrapper_idx): ...

class SlimPrunerMasker(WeightMasker):
    '''
    A structured pruning algorithm that prunes channels by pruning the weights of BN layers.
    Zhuang Liu, Jianguo Li, Zhiqiang Shen, Gao Huang, Shoumeng Yan and Changshui Zhang
    "Learning Efficient Convolutional Networks through Network Slimming", 2017 ICCV
    https://arxiv.org/pdf/1708.06519.pdf
    '''
    global_threshold: Incomplete
    def __init__(self, model, pruner, **kwargs) -> None: ...
    def calc_mask(self, sparsity, wrapper, wrapper_idx: Incomplete | None = None): ...

class AMCWeightMasker(WeightMasker):
    """
    Weight maskser class for AMC pruner. Currently, AMCPruner only supports pruning kernel
    size 1x1 pointwise Conv2d layer. Before using this class to prune kernels, AMCPruner
    collected input and output feature maps for each layer, the features maps are flattened
    and save into wrapper.input_feat and wrapper.output_feat.

    Parameters
    ----------
    model: nn.Module
        model to be pruned
    pruner: Pruner
        A Pruner instance used to prune the model
    preserve_round: int
        after pruning, preserve filters/channels round to `preserve_round`, for example:
        for a Conv2d layer, output channel is 32, sparsity is 0.2, if preserve_round is
        1 (no preserve round), then there will be int(32 * 0.2) = 6 filters pruned, and
        32 - 6 = 26 filters are preserved. If preserve_round is 4, preserved filters will
        be round up to 28 (which can be divided by 4) and only 4 filters are pruned.
    """
    model: Incomplete
    pruner: Incomplete
    preserve_round: Incomplete
    def __init__(self, model, pruner, preserve_round: int = 1) -> None: ...
    def calc_mask(self, sparsity, wrapper, wrapper_idx: Incomplete | None = None, preserve_idx: Incomplete | None = None):
        """
        Calculate the mask of given layer.
        Parameters
        ----------
        sparsity: float
            pruning ratio,  preserved weight ratio is `1 - sparsity`
        wrapper: PrunerModuleWrapper
            layer wrapper of this layer
        wrapper_idx: int
            index of this wrapper in pruner's all wrappers
        Returns
        -------
        dict
            dictionary for storing masks, keys of the dict:
            'weight_mask':  weight mask tensor
            'bias_mask': bias mask tensor (optional)
        """
    def get_mask(self, base_mask, weight, num_preserve, wrapper, wrapper_idx, preserve_idx): ...
