from . import Distribution as Distribution, EntryPoint as EntryPoint

def normalized_name(dist: Distribution) -> str | None:
    """
    Honor name normalization for distributions that don't provide ``_normalized_name``.
    """
def ep_matches(ep: EntryPoint, **params) -> bool:
    """
    Workaround for ``EntryPoint`` objects without the ``matches`` method.
    """
