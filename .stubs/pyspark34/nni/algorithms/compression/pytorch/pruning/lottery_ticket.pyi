from .finegrained_pruning_masker import LevelPrunerMasker as LevelPrunerMasker
from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Pruner as Pruner
from nni.compression.pytorch.utils.config_validation import PrunerSchema as PrunerSchema

logger: Incomplete

class LotteryTicketPruner(Pruner):
    """
    Parameters
    ----------
    model : pytorch model
        The model to be pruned
    config_list : list
        Supported keys:
            - prune_iterations : The number of rounds for the iterative pruning.
            - sparsity : The final sparsity when the compression is done.
    optimizer : pytorch optimizer
        The optimizer for the model
    lr_scheduler : pytorch lr scheduler
        The lr scheduler for the model if used
    reset_weights : bool
        Whether reset weights and optimizer at the beginning of each round.
    """
    reset_weights: Incomplete
    curr_prune_iteration: Incomplete
    prune_iterations: Incomplete
    masker: Incomplete
    def __init__(self, model, config_list, optimizer: Incomplete | None = None, lr_scheduler: Incomplete | None = None, reset_weights: bool = True) -> None: ...
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list
            Supported keys:
                - prune_iterations : The number of rounds for the iterative pruning.
                - sparsity : The final sparsity when the compression is done.
        """
    def calc_mask(self, wrapper, **kwargs) -> None:
        """
        Generate mask for the given ``weight``.

        Parameters
        ----------
        wrapper : Module
            The layer to be pruned

        Returns
        -------
        tensor
            The mask for this weight, it is ```None``` because this pruner
            calculates and assigns masks in ```prune_iteration_start```,
            no need to do anything in this function.
        """
    def get_prune_iterations(self):
        """
        Return the range for iterations.
        In the first prune iteration, masks are all one, thus, add one more iteration

        Returns
        -------
        list
            A list for pruning iterations
        """
    def prune_iteration_start(self) -> None:
        """
        Control the pruning procedure on updated epoch number.
        Should be called at the beginning of the epoch.
        """
