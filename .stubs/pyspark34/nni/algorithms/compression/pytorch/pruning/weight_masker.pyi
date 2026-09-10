from _typeshed import Incomplete

class WeightMasker:
    model: Incomplete
    pruner: Incomplete
    def __init__(self, model, pruner, **kwargs) -> None: ...
    def calc_mask(self, sparsity, wrapper, wrapper_idx: Incomplete | None = None) -> None:
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
