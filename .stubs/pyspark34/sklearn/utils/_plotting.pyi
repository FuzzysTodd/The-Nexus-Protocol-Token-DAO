from . import check_consistent_length as check_consistent_length, check_matplotlib_support as check_matplotlib_support
from .multiclass import type_of_target as type_of_target

class _BinaryClassifierCurveDisplayMixin:
    """Mixin class to be used in Displays requiring a binary classifier.

    The aim of this class is to centralize some validations regarding the estimator and
    the target and gather the response of the estimator.
    """
