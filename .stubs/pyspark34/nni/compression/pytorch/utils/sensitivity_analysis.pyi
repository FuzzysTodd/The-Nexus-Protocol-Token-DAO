from _typeshed import Incomplete

SUPPORTED_OP_NAME: Incomplete
SUPPORTED_OP_TYPE: Incomplete
logger: Incomplete

class SensitivityAnalysis:
    """
    Perform sensitivity analysis for this model.

    Parameters
    ----------
    model : torch.nn.Module
        the model to perform sensitivity analysis
    val_func : function
        validation function for the model. Due to
        different models may need different dataset/criterion
        , therefore the user need to cover this part by themselves.
        In the val_func, the model should be tested on the validation dateset,
        and the validation accuracy/loss should be returned as the output of val_func.
        There are no restrictions on the input parameters of the val_function.
        User can use the val_args, val_kwargs parameters in analysis
        to pass all the parameters that val_func needed.
    sparsities : list
        The sparsity list provided by users. This parameter is set when the user
        only wants to test some specific sparsities. In the sparsity list, each element
        is a sparsity value which means how much weight the pruner should prune. Take
        [0.25, 0.5, 0.75] for an example, the SensitivityAnalysis will prune 25% 50% 75%
        weights gradually for each layer.
    prune_type : str
        The pruner type used to prune the conv layers, default is 'l1',
        and 'l2', 'fine-grained' is also supported.
    early_stop_mode : str
        If this flag is set, the sensitivity analysis
        for a conv layer will early stop when the validation metric(
        for example, accurracy/loss) has alreay meet the threshold. We
        support four different early stop modes: minimize, maximize, dropped,
        raised. The default value is None, which means the analysis won't stop
        until all given sparsities are tested. This option should be used with
        early_stop_value together.

        minimize: The analysis stops when the validation metric return by the val_func
        lower than early_stop_value.
        maximize: The analysis stops when the validation metric return by the val_func
        larger than early_stop_value.
        dropped: The analysis stops when the validation metric has dropped by early_stop_value.
        raised: The analysis stops when the validation metric has raised by early_stop_value.
    early_stop_value : float
        This value is used as the threshold for different earlystop modes.
        This value is effective only when the early_stop_mode is set.
    """
    model: Incomplete
    val_func: Incomplete
    target_layer: Incomplete
    ori_state_dict: Incomplete
    sensitivities: Incomplete
    sparsities: Incomplete
    Pruner: Incomplete
    early_stop_mode: Incomplete
    early_stop_value: Incomplete
    ori_metric: Incomplete
    already_pruned: Incomplete
    def __init__(self, model, val_func, sparsities: Incomplete | None = None, prune_type: str = 'l1', early_stop_mode: Incomplete | None = None, early_stop_value: Incomplete | None = None) -> None: ...
    @property
    def layers_count(self): ...
    def model_parse(self) -> None: ...
    def analysis(self, val_args: Incomplete | None = None, val_kwargs: Incomplete | None = None, specified_layers: Incomplete | None = None):
        """
        This function analyze the sensitivity to pruning for
        each conv layer in the target model.
        If start and end are not set, we analyze all the conv
        layers by default. Users can specify several layers to
        analyze or parallelize the analysis process easily through
        the start and end parameter.

        Parameters
        ----------
        val_args : list
            args for the val_function
        val_kwargs : dict
            kwargs for the val_funtion
        specified_layers : list
            list of layer names to analyze sensitivity.
            If this variable is set, then only analyze
            the conv layers that specified in the list.
            User can also use this option to parallelize
            the sensitivity analysis easily.
        Returns
        -------
        sensitivities : dict
            dict object that stores the trajectory of the
            accuracy/loss when the prune ratio changes
        """
    def export(self, filepath) -> None:
        """
        Export the results of the sensitivity analysis
        to a csv file. The firstline of the csv file describe the content
        structure. The first line is constructed by 'layername' and sparsity
        list. Each line below records the validation metric returned by val_func
        when this layer is under different sparsities. Note that, due to the early_stop
        option, some layers may not have the metrics under all sparsities.

        layername, 0.25, 0.5, 0.75
        conv1, 0.6, 0.55
        conv2, 0.61, 0.57, 0.56

        Parameters
        ----------
        filepath : str
            Path of the output file
        """
    def update_already_pruned(self, layername, ratio) -> None:
        """
        Set the already pruned ratio for the target layer.
        """
    def load_state_dict(self, state_dict) -> None:
        """
        Update the weight of the model
        """
