from .dependency_aware_pruner import DependencyAwarePruner
from _typeshed import Incomplete

__all__ = ['LevelPruner', 'L1FilterPruner', 'L2FilterPruner', 'FPGMPruner']

class OneshotPruner(DependencyAwarePruner):
    """
    Prune model to an exact pruning level for one time.
    """
    def __init__(self, model, config_list, pruning_algorithm: str = 'level', dependency_aware: bool = False, dummy_input: Incomplete | None = None, **algo_kwargs) -> None:
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list
            List on pruning configs
        pruning_algorithm: str
            algorithms being used to prune model
        dependency_aware: bool
            If prune the model in a dependency-aware way.
        dummy_input : torch.Tensor
            The dummy input to analyze the topology constraints. Note that,
            the dummy_input should on the same device with the model.
        algo_kwargs: dict
            Additional parameters passed to pruning algorithm masker class
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

class LevelPruner(OneshotPruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : Operation types to prune.
    """
    def __init__(self, model, config_list) -> None: ...

class L1FilterPruner(OneshotPruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : Only Conv2d is supported in L1FilterPruner.
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
    def __init__(self, model, config_list, dependency_aware: bool = False, dummy_input: Incomplete | None = None) -> None: ...

class L2FilterPruner(OneshotPruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : Only Conv2d is supported in L2FilterPruner.
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
    def __init__(self, model, config_list, dependency_aware: bool = False, dummy_input: Incomplete | None = None) -> None: ...

class FPGMPruner(OneshotPruner):
    """
    Parameters
    ----------
    model : torch.nn.Module
        Model to be pruned
    config_list : list
        Supported keys:
            - sparsity : This is to specify the sparsity operations to be compressed to.
            - op_types : Only Conv2d is supported in FPGM Pruner.
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
    def __init__(self, model, config_list, dependency_aware: bool = False, dummy_input: Incomplete | None = None) -> None: ...
