from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Pruner

__all__ = ['TransformerHeadPruner']

class TransformerHeadPruner(Pruner):
    '''
    A pruner specialized for pruning attention heads in models belong to the transformer family.

    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned. Expect a model from transformers library (e.g., BertModel).
        This pruner can work with other customized transformer models, but some ranking modes might fail.
    config_list : list
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : Optional. Operation types to prune. (Should be \'Linear\' for this pruner.)
            - op_names : Optional. Operation names to prune.
    head_hidden_dim : int
        Dimension of the hidden dimension of each attention head. (e.g., 64 for BERT)
        We assume that this head_hidden_dim is constant across the entire model.
    attention_name_groups : list (Optional)
        List of groups of names for weights of each attention layer. Each element should be a four-element list, with
        the first three corresponding to Q_proj, K_proj, V_proj (in any order) and the last one being output_proj.
    dummy_input : torch.Tensor (Optional)
        Input to model\'s forward method, used to infer module grouping if attention_name_groups is not specified.
        This tensor is used by the underlying torch.jit.trace to infer the module graph.
    ranking_criterion : str
        The criterion for ranking attention heads. Currently we support:
            - l1_weight: l1 norm of Q_proj, K_proj, and V_proj
            - l2_weight: l2 norm of Q_proj, K_proj, and V_proj
            - l1_activation: l1 norm of the output of attention computation
            - l2_activation: l2 norm of the output of attention computation
            - taylorfo: l1 norm of the output of attention computation * gradient for this output
                        (check more details in the masker documentation)
    global_sort : bool
        Whether rank the heads globally or locally before deciding heads to prune.
    num_iterations : int
        Number of pruning iterations. Defaults to 1 (ont-shot pruning). If num_iterations > 1, the pruner will split
        the sparsity specified in config_list uniformly and assign a fraction to each pruning iteration.
    epochs_per_iteration : int
        Number of finetuning epochs before the next pruning iteration.
        Only used when num_iterations > 1.
        If num_iterations is 1, then no finetuning is performed by the pruner after pruning.
    optimizer: torch.optim.Optimizer
        Optimizer used to train model
    trainer: function
        Function used to finetune the model between pruning iterations.
        Only used when  num_iterations > 1 or ranking_criterion is \'taylorfo\'.
        Users should write this function as a normal function to train the PyTorch model and include
        `model, optimizer, criterion, epoch` as function arguments. Note that the trainer is also used for collecting
        gradients for pruning if ranking_criterion is \'taylorfo\'. In that case, ``epoch=None`` will be passed.
    criterion: function
        Function used to calculate the loss between the target and the output.
        Only used when  num_iterations > 1 or ranking_criterion is \'taylorfo\'.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    forward_runner: function
        Function used to perform a "dry run" on the model on the entire train/validation dataset in order to collect
        data for pruning required by the criteria \'l1_activation\' or \'l2_activation\'.
        Only used when ranking_criterion is \'l1_activation\' or \'l2_activation\'.
        Users should write this function as a normal function that accepts a PyTorch model and runs forward on the model
        using the entire train/validation dataset. This function is not expected to perform any backpropagation or
        parameter updates.
    '''
    head_hidden_dim: Incomplete
    attention_name_groups: Incomplete
    dummy_input: Incomplete
    ranking_criterion: Incomplete
    global_sort: Incomplete
    num_iterations: Incomplete
    epochs_per_iteration: Incomplete
    masking_groups: Incomplete
    masker: Incomplete
    pruned_heads: Incomplete
    def __init__(self, model, config_list, head_hidden_dim, attention_name_groups: Incomplete | None = None, dummy_input: Incomplete | None = None, ranking_criterion: str = 'l1_weight', global_sort: bool = False, num_iterations: int = 1, epochs_per_iteration: int = 1, optimizer: Incomplete | None = None, trainer: Incomplete | None = None, criterion: Incomplete | None = None, forward_runner: Incomplete | None = None, **algo_kwargs) -> None: ...
    def group_weights_by_name(self) -> None:
        """
        Populate self.masking_groups using the groups specified by user in attention_name_groups.
        """
    def group_weight_names_by_graph(self) -> None:
        """
        Populate self.attention_name_groups by running inference on the module graph.
        Currently, the group inferred AttentionWeightDependency is limited to a set of four weights, with the first
        three corresponding to Q_proj, K_proj, V_proj (in any order) and the last one being output_proj.
        """
    def validate_weight_groups(self) -> None:
        """
        Sanity checks:
            - Q, K, V projection weights in each groups must have the same shape
            - output projection weight shape must match total hidden dimension (inferred from Q, K, V projection)
            - Four weights in a group must have the same sparsity in their config
            - If global_sort is specified, all weights must have the same sparsity
            - head_hidden_dim must be a divisor of the output dimension of the projection weights (i.e., the resulting
              head number must be an integer)
        """
    modules_wrapper: Incomplete
    modules_to_compress: Incomplete
    def remove_ungrouped_modules(self) -> None:
        """
        Remove non-attention weights that might be mistakenly captured by a simplified config_list.
        Also update the corresponding list of layer information (self.modules_to_compress)
        """
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list
            List on pruning configs
        """
    def compress(self) -> None: ...
    def update_mask(self) -> None:
        """
        Calculate and update masks for each masking group. If global_sort is set, the masks for all groups are
        calculated altogether, and then the groups are updated individually.
        """
    def calc_mask(self, wrapper, **kwargs) -> None: ...
