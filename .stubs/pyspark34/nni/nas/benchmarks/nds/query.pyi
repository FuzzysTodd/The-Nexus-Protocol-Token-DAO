from .model import NdsTrialConfig as NdsTrialConfig, NdsTrialStats as NdsTrialStats, proxy as proxy
from _typeshed import Incomplete
from collections.abc import Generator
from nni.nas.benchmarks.utils import load_benchmark as load_benchmark

def query_nds_trial_stats(model_family, proposer, generator, model_spec, cell_spec, dataset, num_epochs: Incomplete | None = None, reduction: Incomplete | None = None, include_intermediates: bool = False) -> Generator[Incomplete, None, Incomplete]:
    """
    Query trial stats of NDS given conditions.

    Parameters
    ----------
    model_family : str or None
        If str, can be one of the model families available in :class:`nni.nas.benchmark.nds.NdsTrialConfig`.
        Otherwise a wildcard.
    proposer : str or None
        If str, can be one of the proposers available in :class:`nni.nas.benchmark.nds.NdsTrialConfig`. Otherwise a wildcard.
    generator : str or None
        If str, can be one of the generators available in :class:`nni.nas.benchmark.nds.NdsTrialConfig`. Otherwise a wildcard.
    model_spec : dict or None
        If specified, can be one of the model spec available in :class:`nni.nas.benchmark.nds.NdsTrialConfig`.
        Otherwise a wildcard.
    cell_spec : dict or None
        If specified, can be one of the cell spec available in :class:`nni.nas.benchmark.nds.NdsTrialConfig`.
        Otherwise a wildcard.
    dataset : str or None
        If str, can be one of the datasets available in :class:`nni.nas.benchmark.nds.NdsTrialConfig`. Otherwise a wildcard.
    num_epochs : float or None
        If int, matching results will be returned. Otherwise a wildcard.
    reduction : str or None
        If 'none' or None, all trial stats will be returned directly.
        If 'mean', fields in trial stats will be averaged given the same trial config.
    include_intermediates : boolean
        If true, intermediate results will be returned.

    Returns
    -------
    generator of dict
        A generator of :class:`nni.nas.benchmark.nds.NdsTrialStats` objects,
        where each of them has been converted into a dict.
    """
