from .graph_util import hash_module as hash_module, infer_num_vertices as infer_num_vertices
from .model import Nb101TrialConfig as Nb101TrialConfig, Nb101TrialStats as Nb101TrialStats, proxy as proxy
from _typeshed import Incomplete
from collections.abc import Generator
from nni.nas.benchmarks.utils import load_benchmark as load_benchmark

def query_nb101_trial_stats(arch, num_epochs, isomorphism: bool = True, reduction: Incomplete | None = None, include_intermediates: bool = False) -> Generator[Incomplete, None, Incomplete]:
    """
    Query trial stats of NAS-Bench-101 given conditions.

    Parameters
    ----------
    arch : dict or None
        If a dict, it is in the format that is described in
        :class:`nni.nas.benchmark.nasbench101.Nb101TrialConfig`. Only trial stats
        matched will be returned. If none, all architectures in the database will be matched.
    num_epochs : int or None
        If int, matching results will be returned. Otherwise a wildcard.
    isomorphism : boolean
        Whether to match essentially-same architecture, i.e., architecture with the
        same graph-invariant hash value.
    reduction : str or None
        If 'none' or None, all trial stats will be returned directly.
        If 'mean', fields in trial stats will be averaged given the same trial config.
    include_intermediates : boolean
        If true, intermediate results will be returned.

    Returns
    -------
    generator of dict
        A generator of :class:`nni.nas.benchmark.nasbench101.Nb101TrialStats` objects,
        where each of them has been converted into a dict.
    """
