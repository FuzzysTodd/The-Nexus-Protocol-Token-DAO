from _typeshed import Incomplete
from lime.utils.generic_utils import has_arg as has_arg

class BaseWrapper:
    """Base class for LIME Scikit-Image wrapper


    Args:
        target_fn: callable function or class instance
        target_params: dict, parameters to pass to the target_fn


    'target_params' takes parameters required to instanciate the
        desired Scikit-Image class/model
    """
    target_fn: Incomplete
    target_params: Incomplete
    def __init__(self, target_fn: Incomplete | None = None, **target_params) -> None: ...
    def set_params(self, **params) -> None:
        """Sets the parameters of this estimator.
        Args:
            **params: Dictionary of parameter names mapped to their values.

        Raises :
            ValueError: if any parameter is not a valid argument
                for the target function
        """
    def filter_params(self, fn, override: Incomplete | None = None):
        """Filters `target_params` and return those in `fn`'s arguments.
        Args:
            fn : arbitrary function
            override: dict, values to override target_params
        Returns:
            result : dict, dictionary containing variables
            in both target_params and fn's arguments.
        """

class SegmentationAlgorithm(BaseWrapper):
    """ Define the image segmentation function based on Scikit-Image
            implementation and a set of provided parameters

        Args:
            algo_type: string, segmentation algorithm among the following:
                'quickshift', 'slic', 'felzenszwalb'
            target_params: dict, algorithm parameters (valid model paramters
                as define in Scikit-Image documentation)
    """
    algo_type: Incomplete
    def __init__(self, algo_type, **target_params) -> None: ...
    def __call__(self, *args): ...
