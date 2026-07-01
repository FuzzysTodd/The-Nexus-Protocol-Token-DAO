__all__ = ['install', 'NullFinder']

def install(cls):
    """
    Class decorator for installation on sys.meta_path.

    Adds the backport DistributionFinder to sys.meta_path and
    attempts to disable the finder functionality of the stdlib
    DistributionFinder.
    """

class NullFinder:
    '''
    A "Finder" (aka "MetaClassFinder") that never finds any modules,
    but may find distributions.
    '''
    @staticmethod
    def find_spec(*args, **kwargs) -> None: ...
