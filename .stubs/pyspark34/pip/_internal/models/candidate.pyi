from _typeshed import Incomplete
from pip._internal.models.link import Link as Link
from pip._internal.utils.models import KeyBasedCompareMixin as KeyBasedCompareMixin

class InstallationCandidate(KeyBasedCompareMixin):
    '''Represents a potential "candidate" for installation.'''
    name: Incomplete
    version: Incomplete
    link: Incomplete
    def __init__(self, name: str, version: str, link: Link) -> None: ...
