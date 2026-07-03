from .constants_pruner import PRUNER_DICT as PRUNER_DICT
from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Pruner as Pruner
from nni.compression.pytorch.utils.config_validation import PrunerSchema as PrunerSchema
from nni.utils import OptimizeMode as OptimizeMode

class SimulatedAnnealingPruner(Pruner):
    '''
    A Pytorch implementation of Simulated Annealing compression algorithm.

    Parameters
    ----------
    model : pytorch model
        The model to be pruned.
    config_list : list
        Supported keys:
            - sparsity : The target overall sparsity.
            - op_types : The operation type to prune.
    evaluator : function
        Function to evaluate the pruned model.
        This function should include `model` as the only parameter, and returns a scalar value.
        Example::

            def evaluator(model):
                device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                val_loader = ...
                model.eval()
                correct = 0
                with torch.no_grad():
                    for data, target in val_loader:
                        data, target = data.to(device), target.to(device)
                        output = model(data)
                        # get the index of the max log-probability
                        pred = output.argmax(dim=1, keepdim=True)
                        correct += pred.eq(target.view_as(pred)).sum().item()
                accuracy = correct / len(val_loader.dataset)
                return accuracy
    optimize_mode : str
        Optimize mode, `maximize` or `minimize`, by default `maximize`.
    base_algo : str
        Base pruning algorithm. `level`, `l1`, `l2` or `fpgm`, by default `l1`. Given the sparsity distribution among the ops,
        the assigned `base_algo` is used to decide which filters/channels/weights to prune.
    start_temperature : float
        Start temperature of the simulated annealing process.
    stop_temperature : float
        Stop temperature of the simulated annealing process.
    cool_down_rate : float
        Cool down rate of the temperature.
    perturbation_magnitude : float
        Initial perturbation magnitude to the sparsities. The magnitude decreases with current temperature.
    experiment_data_dir : string
        PATH to save experiment data,
        including the config_list generated for the base pruning algorithm, the performance of the pruned model and the pruning history.

    '''
    def __init__(self, model, config_list, evaluator, optimize_mode: str = 'maximize', base_algo: str = 'l1', start_temperature: int = 100, stop_temperature: int = 20, cool_down_rate: float = 0.9, perturbation_magnitude: float = 0.35, experiment_data_dir: str = './') -> None: ...
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.Module
            Model to be pruned
        config_list : list
            List on pruning configs
        """
    def calc_mask(self, wrapper, **kwargs) -> None: ...
    bound_model: Incomplete
    modules_wrapper: Incomplete
    def compress(self, return_config_list: bool = False):
        """
        Compress the model with Simulated Annealing.

        Returns
        -------
        torch.nn.Module
            model with specified modules compressed.
        """
