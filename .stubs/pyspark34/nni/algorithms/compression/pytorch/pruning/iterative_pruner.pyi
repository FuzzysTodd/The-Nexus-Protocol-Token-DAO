from .dependency_aware_pruner import DependencyAwarePruner
from _typeshed import Incomplete

__all__ = ['AGPPruner', 'ADMMPruner', 'SlimPruner', 'TaylorFOWeightFilterPruner', 'ActivationAPoZRankFilterPruner', 'ActivationMeanRankFilterPruner']

class IterativePruner(DependencyAwarePruner):
    """
    Prune model during the training process.
    """
    epochs_per_iteration: Incomplete
    def __init__(self, model, config_list, optimizer: Incomplete | None = None, pruning_algorithm: str = 'slim', trainer: Incomplete | None = None, criterion: Incomplete | None = None, num_iterations: int = 20, epochs_per_iteration: int = 5, dependency_aware: bool = False, dummy_input: Incomplete | None = None, **algo_kwargs) -> None:
        """
        Parameters
        ----------
        model: torch.nn.Module
            Model to be pruned
        config_list: list
            List on pruning configs
        optimizer: torch.optim.Optimizer
            Optimizer used to train model
        pruning_algorithm: str
            algorithms being used to prune model
        trainer: function
            Function used to train the model.
            Users should write this function as a normal function to train the Pytorch model
            and include `model, optimizer, criterion, epoch` as function arguments.
        criterion: function
            Function used to calculate the loss between the target and the output.
            For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
        num_iterations: int
            Total number of iterations in pruning process. We will calculate mask at the end of an iteration.
        epochs_per_iteration: Union[int, list]
            The number of training epochs for each iteration. `int` represents the same value for each iteration.
            `list` represents the specific value for each iteration.
        dependency_aware: bool
            If prune the model in a dependency-aware way.
        dummy_input: torch.Tensor
            The dummy input to analyze the topology constraints. Note that,
            the dummy_input should on the same device with the model.
        algo_kwargs: dict
            Additional parameters passed to pruning algorithm masker class
        """
    iterations: Incomplete
    def compress(self): ...

class AGPPruner(IterativePruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned.
    config_list : listlist
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : See supported type in your specific pruning algorithm.
    optimizer: torch.optim.Optimizer
        Optimizer used to train model.
    trainer: function
        Function to train the model
    criterion: function
        Function used to calculate the loss between the target and the output.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    num_iterations: int
        Total number of iterations in pruning process. We will calculate mask at the end of an iteration.
    epochs_per_iteration: int
        The number of training epochs for each iteration.
    pruning_algorithm: str
        Algorithms being used to prune model,
        choose from `['level', 'slim', 'l1', 'l2', 'fpgm', 'taylorfo', 'apoz', 'mean_activation']`, by default `level`
    """
    masker: Incomplete
    now_epoch: int
    freq: Incomplete
    end_epoch: Incomplete
    def __init__(self, model, config_list, optimizer, trainer, criterion, num_iterations: int = 10, epochs_per_iteration: int = 1, pruning_algorithm: str = 'level') -> None: ...
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list
            List on pruning configs
        """
    def calc_mask(self, wrapper, wrapper_idx: Incomplete | None = None):
        """
        Calculate the mask of given layer.
        Scale factors with the smallest absolute value in the BN layer are masked.
        Parameters
        ----------
        wrapper : Module
            the layer to instrument the compression operation
        wrapper_idx: int
            index of this wrapper in pruner's all wrappers
        Returns
        -------
        dict | None
            Dictionary for storing masks, keys of the dict:
            'weight_mask':  weight mask tensor
            'bias_mask': bias mask tensor (optional)
        """
    target_sparsity: Incomplete
    def compute_target_sparsity(self, config):
        """
        Calculate the sparsity for pruning
        Parameters
        ----------
        config : dict
            Layer's pruning config
        Returns
        -------
        float
            Target sparsity to be pruned
        """
    def update_epoch(self, epoch) -> None:
        """
        Update epoch
        Parameters
        ----------
        epoch : int
            current training epoch
        """
    def compress(self): ...

class ADMMPruner(IterativePruner):
    """
    A Pytorch implementation of ADMM Pruner algorithm.

    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned.
    config_list : list
        List on pruning configs.
    trainer : function
        Function used for the first subproblem.
        Users should write this function as a normal function to train the Pytorch model
        and include `model, optimizer, criterion, epoch` as function arguments.
    criterion: function
        Function used to calculate the loss between the target and the output. By default, we use CrossEntropyLoss in ADMMPruner.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    num_iterations: int
        Total number of iterations in pruning process. We will calculate mask after we finish all iterations in ADMMPruner.
    epochs_per_iteration: int
        Training epochs of the first subproblem.
    row : float
        Penalty parameters for ADMM training.
    base_algo : str
        Base pruning algorithm. `level`, `l1`, `l2` or `fpgm`, by default `l1`. Given the sparsity distribution among
        the ops, the assigned `base_algo` is used to decide which filters/channels/weights to prune.
    """
    optimizer: Incomplete
    masker: Incomplete
    def __init__(self, model, config_list, trainer, criterion=..., num_iterations: int = 30, epochs_per_iteration: int = 5, row: float = 0.0001, base_algo: str = 'l1') -> None: ...
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list
            List on pruning configs
        """
    Z: Incomplete
    U: Incomplete
    def compress(self):
        """
        Compress the model with ADMM.

        Returns
        -------
        torch.nn.Module
            model with specified modules compressed.
        """

class SlimPruner(IterativePruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : Only BatchNorm2d is supported in Slim Pruner.
    optimizer : torch.optim.Optimizer
            Optimizer used to train model
    trainer : function
        Function used to sparsify BatchNorm2d scaling factors.
        Users should write this function as a normal function to train the Pytorch model
        and include `model, optimizer, criterion, epoch` as function arguments.
    criterion : function
        Function used to calculate the loss between the target and the output.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    sparsifying_training_epochs: int
        The number of channel sparsity regularization training epochs before pruning.
    scale : float
        Penalty parameters for sparsification.
    dependency_aware: bool
        If prune the model in a dependency-aware way. If it is `True`, this pruner will
        prune the model according to the l2-norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if this flag is set True
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input : torch.Tensor
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.
    """
    scale: Incomplete
    def __init__(self, model, config_list, optimizer, trainer, criterion, sparsifying_training_epochs: int = 10, scale: float = 0.0001, dependency_aware: bool = False, dummy_input: Incomplete | None = None) -> None: ...
    def validate_config(self, model, config_list): ...

class TaylorFOWeightFilterPruner(IterativePruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : How much percentage of convolutional filters are to be pruned.
            - op_types : Currently only Conv2d is supported in TaylorFOWeightFilterPruner.
    optimizer: torch.optim.Optimizer
            Optimizer used to train model
    trainer : function
        Function used to sparsify BatchNorm2d scaling factors.
        Users should write this function as a normal function to train the Pytorch model
        and include `model, optimizer, criterion, epoch` as function arguments.
    criterion : function
        Function used to calculate the loss between the target and the output.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    sparsifying_training_batches: int
        The number of batches to collect the contributions. Note that the number need to be less than the maximum batch number in one epoch.
    dependency_aware: bool
        If prune the model in a dependency-aware way. If it is `True`, this pruner will
        prune the model according to the l2-norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if this flag is set True
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input : torch.Tensor
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.
    global_sort: bool
        Only support TaylorFOWeightFilterPruner currently.
        If prune the model in a global-sort way. If it is `True`, this pruner will prune
        the model according to the global contributions information which means channel contributions
        will be sorted globally and whether specific channel will be pruned depends on global information.
    """
    def __init__(self, model, config_list, optimizer, trainer, criterion, sparsifying_training_batches: int = 1, dependency_aware: bool = False, dummy_input: Incomplete | None = None, global_sort: bool = False) -> None: ...

class ActivationAPoZRankFilterPruner(IterativePruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : How much percentage of convolutional filters are to be pruned.
            - op_types : Only Conv2d is supported in ActivationAPoZRankFilterPruner.
    optimizer: torch.optim.Optimizer
            Optimizer used to train model
    trainer: function
        Function used to train the model.
        Users should write this function as a normal function to train the Pytorch model
        and include `model, optimizer, criterion, epoch` as function arguments.
    criterion : function
        Function used to calculate the loss between the target and the output.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    activation: str
        The activation type.
    sparsifying_training_batches: int
        The number of batches to collect the contributions. Note that the number need to be less than the maximum batch number in one epoch.
    dependency_aware: bool
        If prune the model in a dependency-aware way. If it is `True`, this pruner will
        prune the model according to the l2-norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if this flag is set True
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input : torch.Tensor
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.

    """
    def __init__(self, model, config_list, optimizer, trainer, criterion, activation: str = 'relu', sparsifying_training_batches: int = 1, dependency_aware: bool = False, dummy_input: Incomplete | None = None) -> None: ...

class ActivationMeanRankFilterPruner(IterativePruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : How much percentage of convolutional filters are to be pruned.
            - op_types : Only Conv2d is supported in ActivationMeanRankFilterPruner.
    optimizer: torch.optim.Optimizer
            Optimizer used to train model.
    trainer: function
            Function used to train the model.
            Users should write this function as a normal function to train the Pytorch model
            and include `model, optimizer, criterion, epoch` as function arguments.
    criterion : function
        Function used to calculate the loss between the target and the output.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    activation: str
        The activation type.
    sparsifying_training_batches: int
        The number of batches to collect the contributions. Note that the number need to be less than the maximum batch number in one epoch.
    dependency_aware: bool
        If prune the model in a dependency-aware way. If it is `True`, this pruner will
        prune the model according to the l2-norm of weights and the channel-dependency or
        group-dependency of the model. In this way, the pruner will force the conv layers
        that have dependencies to prune the same channels, so the speedup module can better
        harvest the speed benefit from the pruned model. Note that, if this flag is set True
        , the dummy_input cannot be None, because the pruner needs a dummy input to trace the
        dependency between the conv layers.
    dummy_input : torch.Tensor
        The dummy input to analyze the topology constraints. Note that, the dummy_input
        should on the same device with the model.
    """
    def __init__(self, model, config_list, optimizer, trainer, criterion, activation: str = 'relu', sparsifying_training_batches: int = 1, dependency_aware: bool = False, dummy_input: Incomplete | None = None) -> None: ...
