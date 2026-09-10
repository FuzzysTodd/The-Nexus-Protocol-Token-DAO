from .formatting import FormattedParameters as FormattedParameters, FormattedSearchSpace as FormattedSearchSpace, ParameterSpec as ParameterSpec, deformat_parameters as deformat_parameters
from nni.algorithms.hpo.gridsearch_tuner import GridSearchTuner as GridSearchTuner

class Deduplicator:
    """
    A helper for tuners to deduplicate generated parameters.

    When the tuner generates an already existing parameter,
    calling this will return a new parameter generated with grid search.
    Otherwise it returns the orignial parameter object.

    If all parameters have been generated, raise ``NoMoreTrialError``.

    All search space types, including nested choice, are supported.

    Resuming and updating search space are not supported for now.
    It will not raise error, but may return duplicate parameters.

    See random tuner's source code for example usage.
    """
    def __init__(self, formatted_search_space: FormattedSearchSpace) -> None: ...
    def __call__(self, formatted_parameters: FormattedParameters) -> FormattedParameters: ...
    def add_history(self, formatted_parameters: FormattedParameters) -> None: ...
