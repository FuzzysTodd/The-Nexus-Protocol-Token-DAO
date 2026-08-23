from . import base
from _typeshed import Incomplete
from git.repo import Repo
from git.types import Literal
from git.util import Actor

__all__ = ['TagObject']

class TagObject(base.Object):
    """Non-Lightweight tag carrying additional information about an object we are pointing to."""
    type: Literal['tag']
    object: Incomplete
    tag: Incomplete
    tagger: Incomplete
    tagged_date: Incomplete
    tagger_tz_offset: Incomplete
    message: Incomplete
    def __init__(self, repo: Repo, binsha: bytes, object: None | base.Object = None, tag: None | str = None, tagger: None | Actor = None, tagged_date: int | None = None, tagger_tz_offset: int | None = None, message: str | None = None) -> None:
        """Initialize a tag object with additional data

        :param repo: repository this object is located in
        :param binsha: 20 byte SHA1
        :param object: Object instance of object we are pointing to
        :param tag: name of this tag
        :param tagger: Actor identifying the tagger
        :param tagged_date: int_seconds_since_epoch
            is the DateTime of the tag creation - use time.gmtime to convert
            it into a different format
        :param tagged_tz_offset: int_seconds_west_of_utc is the timezone that the
            authored_date is in, in a format similar to time.altzone"""
