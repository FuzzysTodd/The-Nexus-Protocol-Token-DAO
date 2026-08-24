from .model import NlpTrialConfig as NlpTrialConfig, NlpTrialStats as NlpTrialStats
from _typeshed import Incomplete
from collections.abc import Generator

def query_nlp_trial_stats(arch, dataset, reduction: Incomplete | None = None, include_intermediates: bool = False) -> Generator[Incomplete, None, Incomplete]:
    '''
    Query trial stats of NLP benchmark given conditions, including config(arch + dataset) and training results after 50 epoch.

    Parameters
    ----------
    arch : dict or None
        If a dict, it is in the format that is described in
        :class:`nni.nas.benchmark.nlp.NlpTrialConfig`. Only trial stats matched will be returned.
        If none, all architectures in the database will be matched.
    dataset : str or None
        If specified, can be one of the dataset available in :class:`nni.nas.benchmark.nlp.NlpTrialConfig`.
        Otherwise a wildcard.
    reduction : str or None
        If \'none\' or None, all trial stats will be returned directly.
        If \'mean\', fields in trial stats will be averaged given the same trial config.
        Please note that some trial configs have multiple runs which make "reduction" meaningful, while some may not.
    include_intermediates : boolean
        If true, intermediate results will be returned.

    Returns
    -------
    generator of dict
        A generator of :class:`nni.nas.benchmark.nlp.NlpTrialStats` objects,
        where each of them has been converted into a dict.
    '''
