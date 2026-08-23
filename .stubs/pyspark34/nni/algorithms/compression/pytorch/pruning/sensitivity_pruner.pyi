from .constants_pruner import PRUNER_DICT as PRUNER_DICT
from _typeshed import Incomplete
from nni.compression.pytorch.compressor import Pruner as Pruner
from nni.compression.pytorch.utils import SensitivityAnalysis as SensitivityAnalysis
from nni.compression.pytorch.utils.config_validation import PrunerSchema as PrunerSchema

MAX_PRUNE_RATIO_PER_ITER: float

class SensitivityPruner(Pruner):
    '''
    This function prune the model based on the sensitivity
    for each layer.

    Parameters
    ----------
    model: torch.nn.Module
        model to be compressed
    evaluator: function
        validation function for the model. This function should return the accuracy
        of the validation dataset. The input parameters of evaluator can be specified
        in the parameter `eval_args` and \'eval_kwargs\' of the compress function if needed.
        Example:
        >>> def evaluator(model):
        >>>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        >>>     val_loader = ...
        >>>     model.eval()
        >>>     correct = 0
        >>>     with torch.no_grad():
        >>>         for data, target in val_loader:
        >>>             data, target = data.to(device), target.to(device)
        >>>             output = model(data)
        >>>             # get the index of the max log-probability
        >>>             pred = output.argmax(dim=1, keepdim=True)
        >>>             correct += pred.eq(target.view_as(pred)).sum().item()
        >>>     accuracy = correct / len(val_loader.dataset)
        >>>     return accuracy
    finetuner: function
        finetune function for the model. This parameter is not essential, if is not None,
        the sensitivity pruner will finetune the model after pruning in each iteration.
        The input parameters of finetuner can be specified in the parameter of compress
        called `finetune_args` and `finetune_kwargs` if needed.
        Example:
        >>> def finetuner(model, epoch=3):
        >>>     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        >>>     train_loader = ...
        >>>     criterion = torch.nn.CrossEntropyLoss()
        >>>     optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        >>>     model.train()
        >>>     for _ in range(epoch):
        >>>         for _, (data, target) in enumerate(train_loader):
        >>>             data, target = data.to(device), target.to(device)
        >>>             optimizer.zero_grad()
        >>>             output = model(data)
        >>>             loss = criterion(output, target)
        >>>             loss.backward()
        >>>             optimizer.step()
    base_algo: str
        base pruning algorithm. `level`, `l1`, `l2` or `fpgm`, by default `l1`.
    sparsity_proportion_calc: function
        This function generate the sparsity proportion between the conv layers according to the
        sensitivity analysis results. We provide a default function to quantify the sparsity
        proportion according to the sensitivity analysis results. Users can also customize
        this function according to their needs. The input of this function is a dict,
        for example : {\'conv1\' : {0.1: 0.9, 0.2 : 0.8}, \'conv2\' : {0.1: 0.9, 0.2 : 0.8}},
        in which, \'conv1\' and is the name of the conv layer, and 0.1:0.9 means when the
        sparsity of conv1 is 0.1 (10%), the model\'s val accuracy equals to 0.9.
    sparsity_per_iter: float
        The sparsity of the model that the pruner try to prune in each iteration.
    acc_drop_threshold : float
        The hyperparameter used to quantifiy the sensitivity for each layer.
    checkpoint_dir: str
        The dir path to save the checkpoints during the pruning.
    '''
    base_algo: Incomplete
    model: Incomplete
    evaluator: Incomplete
    finetuner: Incomplete
    analyzer: Incomplete
    ori_acc: Incomplete
    ori_state_dict: Incomplete
    sensitivities: Incomplete
    weight_count: Incomplete
    weight_sum: int
    named_module: Incomplete
    Pruner: Incomplete
    sparsity_proportion_calc: Incomplete
    remained_ratio: float
    sparsity_per_iter: Incomplete
    acc_drop_threshold: Incomplete
    checkpoint_dir: Incomplete
    def __init__(self, model, config_list, evaluator, finetuner: Incomplete | None = None, base_algo: str = 'l1', sparsity_proportion_calc: Incomplete | None = None, sparsity_per_iter: float = 0.1, acc_drop_threshold: float = 0.05, checkpoint_dir: Incomplete | None = None) -> None: ...
    def validate_config(self, model, config_list):
        """
        Parameters
        ----------
        model : torch.nn.module
            Model to be pruned
        config_list : list
            List on pruning configs
        """
    def load_sensitivity(self, filepath):
        """
        load the sensitivity results exported by the sensitivity analyzer
        """
    def normalize(self, ratios, target_pruned):
        """
        Normalize the prune ratio of each layer according to the
        total already pruned ratio and the final target total pruning
        ratio

        Parameters
        ----------
            ratios:
                Dict object that save the prune ratio for each layer
            target_pruned:
                The amount of the weights expected to be pruned in this
                iteration

        Returns
        -------
            new_ratios:
                return the normalized prune ratios for each layer.

        """
    def create_cfg(self, ratios):
        """
        Generate the cfg_list for the pruner according to the prune ratios.

        Parameters
        ---------
            ratios:
                For example: {'conv1' : 0.2}

        Returns
        -------
            cfg_list:
                For example: [{'sparsity':0.2, 'op_names':['conv1'], 'op_types':['Conv2d']}]
        """
    def current_sparsity(self):
        """
        The sparsity of the weight.
        """
    modules_wrapper: Incomplete
    def compress(self, eval_args: Incomplete | None = None, eval_kwargs: Incomplete | None = None, finetune_args: Incomplete | None = None, finetune_kwargs: Incomplete | None = None, resume_sensitivity: Incomplete | None = None):
        """
        This function iteratively prune the model according to the results of
        the sensitivity analysis.

        Parameters
        ----------
        eval_args: list
        eval_kwargs: list& dict
            Parameters for the val_funtion, the val_function will be called like
            evaluator(\\*eval_args, \\*\\*eval_kwargs)
        finetune_args: list
        finetune_kwargs: dict
            Parameters for the finetuner function if needed.
        resume_sensitivity:
            resume the sensitivity results from this file.
        """
    def calc_mask(self, wrapper, **kwargs) -> None: ...
