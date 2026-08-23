from .model import Nb201TrialConfig as Nb201TrialConfig, Nb201TrialStats as Nb201TrialStats, proxy as proxy
from _typeshed import Incomplete
from collections.abc import Generator
from nni.nas.benchmarks.utils import load_benchmark as load_benchmark

def query_nb201_trial_stats(arch, num_epochs, dataset, reduction: Incomplete | None = None, include_intermediates: bool = False) -> Generator[Incomplete, None, Incomplete]:
    """
    Query trial stats of NAS-Bench-201 given conditions.

    Parameters
    ----------
    arch : dict or None
        If a dict, it is in the format that is described in
        :class:`nni.nas.benchmark.nasbench201.Nb201TrialConfig`. Only trial stats
        matched will be returned. If none, all architectures in the database will be matched.
    num_epochs : int or None
        If int, matching results will be returned. Otherwise a wildcard.
    dataset : str or None
        If specified, can be one of the dataset available in :class:`nni.nas.benchmark.nasbench201.Nb201TrialConfig`.
        Otherwise a wildcard.
    reduction : str or None
        If 'none' or None, all trial stats will be returned directly.
        If 'mean', fields in trial stats will be averaged given the same trial config.
    include_intermediates : boolean
        If true, intermediate results will be returned.

    Returns
    -------
    generator of dict
        A generator of :class:`nni.nas.benchmark.nasbench201.Nb201TrialStats` objects,
        where each of them has been converted into a dict.
    """
