from optuna import Study as Study
from optuna.distributions import UniformDistribution as UniformDistribution
from optuna.study import create_study as create_study
from optuna.trial import create_trial as create_trial

def prepare_study_with_trials(no_trials: bool = False, less_than_two: bool = False, more_than_three: bool = False, with_c_d: bool = True, n_objectives: int = 1) -> Study:
    """Prepare a study for tests.

    Args:
        no_trials: If ``False``, create a study with no trials.
        less_than_two: If ``True``, create a study with two/four hyperparameters where
            'param_a' (and 'param_c') appear(s) only once while 'param_b' (and 'param_d')
            appear(s) twice in `study.trials`.
        more_than_three: If ``True``, create a study with two/four hyperparameters where
            'param_a' (and 'param_c') appear(s) only three times while 'param_b' (and 'param_d')
            appear(s) four times in `study.trials`.
        with_c_d: If ``True``, the study has four hyperparameters named 'param_a',
            'param_b', 'param_c', and 'param_d'. Otherwise, there are only two
            hyperparameters ('param_a' and 'param_b').
        n_objectives: Number of objective values.

    Returns:
        :class:`~optuna.study.Study`

    """
