from .iterative_pruner import ADMMPruner as ADMMPruner
from .simulated_annealing_pruner import SimulatedAnnealingPruner as SimulatedAnnealingPruner
from _typeshed import Incomplete
from nni.compression.pytorch import ModelSpeedup as ModelSpeedup
from nni.compression.pytorch.compressor import Pruner as Pruner
from nni.compression.pytorch.utils.config_validation import PrunerSchema as PrunerSchema
from nni.utils import OptimizeMode as OptimizeMode

class AutoCompressPruner(Pruner):
    '''
    A Pytorch implementation of AutoCompress pruning algorithm.

    Parameters
    ----------
    model : pytorch model
        The model to be pruned.
    config_list : list
        Supported keys:
            - sparsity : The target overall sparsity.
            - op_types : The operation type to prune.
    trainer : function
        Function used for the first subproblem of ADMM Pruner.
        Users should write this function as a normal function to train the Pytorch model
        and include `model, optimizer, criterion, epoch` as function arguments.
    criterion: function
        Function used to calculate the loss between the target and the output. By default, we use CrossEntropyLoss.
        For example, you can use ``torch.nn.CrossEntropyLoss()`` as input.
    evaluator : function
        function to evaluate the pruned model.
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
    dummy_input : pytorch tensor
        The dummy input for ```jit.trace```, users should put it on right device before pass in.
    num_iterations : int
        Number of overall iterations.
    optimize_mode : str
        optimize mode, `maximize` or `minimize`, by default `maximize`.
    base_algo : str
        Base pruning algorithm. `level`, `l1`, `l2` or `fpgm`, by default `l1`. Given the sparsity distribution among
        the ops, the assigned `base_algo` is used to decide which filters/channels/weights to prune.
    start_temperature : float
        Start temperature of the simulated annealing process.
    stop_temperature : float
        Stop temperature of the simulated annealing process.
    cool_down_rate : float
        Cool down rate of the temperature.
    perturbation_magnitude : float
        Initial perturbation magnitude to the sparsities. The magnitude decreases with current temperature.
    admm_num_iterations : int
        Number of iterations of ADMM Pruner.
    admm_epochs_per_iteration : int
        Training epochs of the first optimization subproblem of ADMMPruner.
    row : float
        Penalty parameters for ADMM training.
    experiment_data_dir : string
        PATH to store temporary experiment data.
    '''
    def __init__(self, model, config_list, trainer, evaluator, dummy_input, criterion=..., num_iterations: int = 3, optimize_mode: str = 'maximize', base_algo: str = 'l1', start_temperature: int = 100, stop_temperature: int = 20, cool_down_rate: float = 0.9, perturbation_magnitude: float = 0.35, admm_num_iterations: int = 30, admm_epochs_per_iteration: int = 5, row: float = 0.0001, experiment_data_dir: str = './') -> None: ...
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
    def compress(self):
        """
        Compress the model with AutoCompress.

        Returns
        -------
        torch.nn.Module
            model with specified modules compressed.
        """
    def export_model(self, model_path, mask_path: Incomplete | None = None, onnx_path: Incomplete | None = None, input_shape: Incomplete | None = None, device: Incomplete | None = None) -> None: ...
