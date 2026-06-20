from . import check_pandas_support as check_pandas_support
from .._config import get_config as get_config
from ._available_if import available_if as available_if
from _typeshed import Incomplete

class _SetOutputMixin:
    """Mixin that dynamically wraps methods to return container based on config.

    Currently `_SetOutputMixin` wraps `transform` and `fit_transform` and configures
    it based on `set_output` of the global configuration.

    `set_output` is only defined if `get_feature_names_out` is defined and
    `auto_wrap_output_keys` is the default value.
    """
    def __init_subclass__(cls, auto_wrap_output_keys=('transform',), **kwargs) -> None: ...
    def set_output(self, *, transform: Incomplete | None = None):
        '''Set output container.

        See :ref:`sphx_glr_auto_examples_miscellaneous_plot_set_output.py`
        for an example on how to use the API.

        Parameters
        ----------
        transform : {"default", "pandas"}, default=None
            Configure output of `transform` and `fit_transform`.

            - `"default"`: Default output format of a transformer
            - `"pandas"`: DataFrame output
            - `None`: Transform configuration is unchanged

        Returns
        -------
        self : estimator instance
            Estimator instance.
        '''
