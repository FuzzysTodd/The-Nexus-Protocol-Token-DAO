import shap
from _typeshed import Incomplete

class _PatchedKernelExplainer(shap.KernelExplainer):
    @staticmethod
    def not_equal(i, j): ...
    def save(self, out_file, model_saver: Incomplete | None = None, masker_saver: Incomplete | None = None) -> None:
        '''
        This patched `save` method fix `KernelExplainer.save`.
        Issues in original `KernelExplainer.save`:
         - It saves model by calling model.save, but shap.utils._legacy.Model has no save method
         - It tries to save "masker", but there\'s no "masker" in KernelExplainer
         - It does not save "KernelExplainer.data" attribute, the attribute is required when
           loading back
        Note: `model_saver` and `masker_saver` are meaningless argument for `KernelExplainer.save`,
        the model in "KernelExplainer" is an instance of `shap.utils._legacy.Model`
        (it wraps the predict function), we can only use pickle to dump it.
        and no `masker` for KernelExplainer so `masker_saver` is meaningless.
        but I preserve the 2 argument for overridden API compatibility.
        '''
    @classmethod
    def load(cls, in_file, model_loader: Incomplete | None = None, masker_loader: Incomplete | None = None, instantiate: bool = True):
        '''
        This patched `load` method fix `KernelExplainer.load`.
        Issues in original KernelExplainer.load:
         - Use mismatched model loader to load model
         - Try to load non-existent "masker" attribute
         - Does not load "data" attribute and then cause calling " KernelExplainer"
           constructor lack of "data" argument.
        Note: `model_loader` and `masker_loader` are meaningless argument for
        `KernelExplainer.save`, because the `model` object is saved by pickle dump,
        we must use pickle load to load it.
        and no `masker` for KernelExplainer so `masker_loader` is meaningless.
        but I preserve the 2 argument for overridden API compatibility.
        '''
