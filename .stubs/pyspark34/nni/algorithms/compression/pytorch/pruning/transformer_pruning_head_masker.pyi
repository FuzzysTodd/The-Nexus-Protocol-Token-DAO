from .weight_masker import WeightMasker
from _typeshed import Incomplete

__all__ = ['L1WeightHeadMasker', 'L2WeightHeadMasker', 'L1ActivationHeadMasker', 'L2ActivationHeadMasker', 'TaylorFOHeadMasker']

class AttentionHeadMasker(WeightMasker):
    """
    A structured pruning masker base class that prunes attention heads in attention layers.

    Parameters
    ----------
    model: nn.Module
        model to be pruned
    pruner: Pruner
        A Pruner instance used to prune the model
    head_hidden_dim: int
        Hidden dimension for each attention head (e.g., 64 for BERT base)
    """
    head_hidden_dim: Incomplete
    def __init__(self, model, pruner, head_hidden_dim: Incomplete | None = None) -> None: ...
    def reset(self) -> None:
        """
        Derived classes can override this method to do preparations necessary for calculating importance scores.
        This method is called during iterative pruning, before each iteration starts (except the first one).
        """
    def calc_mask(self, sparsity, wrapper: Incomplete | None = None, wrapper_idx: Incomplete | None = None, weight_group: Incomplete | None = None, **kwargs):
        """
        Calculate all the masks for a group of wrappers (specified in weight_group).
        This function only utilizes local information for mask calculation. If global_sort is specified for the pruner,
        the pruner should call calc_mask_global instead of this function.

        Parameters
        ----------
        sparsity: float
            The target (amount of increase of) sparsity of the wrapper list.
        weight_group: list
            A four-element list of module wrappers
        wrapper: PrunerModuleWrapper/list of PrunerModuleWrappers
            Should be None. Not used in this masker, just for consistency with the parent API.
        wrapper_idx: int/list of int
            Should be None. Not used in this masker, just for consistency with the parent API.
        Returns
        -------
        masks : list
            masks for each element in the group.
            Each element in the list masks is a dictionary for storing masks, keys of the dict:
                'weight_mask':  weight mask tensor
                'bias_mask': bias mask tensor (optional)
        """
    def calc_mask_global(self, n_heads_to_prune):
        """
        Calculate all the masks for all groups in the pruner.

        Parameters
        ----------
        n_heads_to_prune : int
            Total number of attention heads to prune.
        Returns
        -------
        all_masks : list
            A list of masks for all groups, where each element is a list of masks for each module in the group.
        """
    def get_mask(self, num_prune, weight_group, **kwargs) -> None:
        """
        Calculate the mask of given layer (weight_group).

        Parameters
        ----------
        num_prune: int
            Num of heads to prune
        weight_group: list
            A four-element list of module wrappers
        Returns
        -------
        masks : list
            masks for each element in the group.
            Each element in the list masks is a dictionary for storing masks, keys of the dict:
                'weight_mask':  weight mask tensor
                'bias_mask': bias mask tensor (optional)
        """
    def get_mask_by_importance_ranking(self, num_prune, weight_group):
        """
        Calculate the mask of given layer by pruning out heads with lowest importance scores.

        Parameters
        ----------
        num_prune: int
            Num of heads to prune
        weight_group: list
            list of a group of weights for an attention layer
        Returns
        -------
        masks : list
            masks for each element in the group.
            Each element in the list masks is a dictionary for storing masks, keys of the dict:
                'weight_mask':  weight mask tensor
                'bias_mask': bias mask tensor (optional)
        """
    def get_head_importance_scores(self, weight_group) -> None:
        """
        Calculate the importance score for each head.
        Parameters
        ----------
        weight_group: list
            list of a group of weights for an attention layer

        Returns
        -------
        importance_scores: tensor
            Tensor that indicates the importance of each head
        """

class L1WeightHeadMasker(AttentionHeadMasker):
    """
    A structured pruning algorithm that prunes the heads weight smallest weight magnitude for the query, head,
    and key projection matrices. L1 norm is used for magnitude calculation. Note that in this implementation, weight
    norms of q_proj, k_proj, v_proj from each head are summed as the final importance score for the head.
    """
    def get_head_importance_scores(self, weight_group): ...
    def get_mask(self, num_prune, weight_group, **kwargs): ...

class L2WeightHeadMasker(AttentionHeadMasker):
    """
    A structured pruning algorithm that prunes the heads weight smallest weight magnitude for the query, head,
    and key projection matrices. L2 norm is used for magnitude calculation. Note that in this implementation, weight
    norms of q_proj, k_proj, v_proj from each head are summed as the final importance score for the head.
    """
    def get_head_importance_scores(self, weight_group): ...
    def get_mask(self, num_prune, weight_group, **kwargs): ...

class L1ActivationHeadMasker(AttentionHeadMasker):
    """
    A structured pruning algorithm that prunes the heads with smallest final output value.
    Note that this masker only relies on the output of the output layer of each attention layer.
    The masker collects the L1 norm of the output of the last weight (output projection) in each group on the entire
    train set, and prunes the heads producing the smallest output.
    """
    def __init__(self, model, pruner, head_hidden_dim: Incomplete | None = None) -> None: ...
    def reset(self) -> None: ...
    def get_head_importance_scores(self, weight_group): ...
    def get_mask(self, num_prune, weight_group, **kwargs): ...

class L2ActivationHeadMasker(AttentionHeadMasker):
    """
    A structured pruning algorithm that prunes the heads with smallest final output value.
    Note that this masker only relies on the output of the output layer of each attention layer.
    The masker collects the L2 norm of the output of the last weight (output projection) in each group on the entire
    train set, and prunes the heads producing the smallest output.
    """
    def __init__(self, model, pruner, head_hidden_dim: Incomplete | None = None) -> None: ...
    def reset(self) -> None: ...
    def get_head_importance_scores(self, weight_group): ...
    def get_mask(self, num_prune, weight_group, **kwargs): ...

class TaylorFOHeadMasker(AttentionHeadMasker):
    '''
    A structured pruning algorithm that prunes the heads with smallest final output contribution.
    Note that this masker only relies on the output of the output layer of each attention layer.
    The masker collects the output the last weight (output projection) in each group and the corresponding gradient
    on the entire train set, and prunes the heads producing the smallest contribution as used in the following papers:
        "Are Sixteen Heads Really Better than One?" (Michel et.al, 2019)
        "Pruning convolutional neural networks for resource efficient inference." (Molchanov et. al., 2017)
    '''
    def __init__(self, model, pruner, head_hidden_dim: Incomplete | None = None) -> None: ...
    backward_hooks: Incomplete
    def reset(self) -> None: ...
    def get_head_importance_scores(self, weight_group): ...
    def get_mask(self, num_prune, weight_group, **kwargs): ...
