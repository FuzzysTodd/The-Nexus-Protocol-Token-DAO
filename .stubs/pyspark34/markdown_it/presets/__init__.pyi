from . import commonmark as commonmark, default as default, zero as zero
from ..utils import PresetType

__all__ = ['commonmark', 'default', 'zero', 'js_default', 'gfm_like']

js_default = default

class gfm_like:
    """GitHub Flavoured Markdown (GFM) like.

    This adds the linkify, table and strikethrough components to CommmonMark.

    Note, it lacks task-list items and raw HTML filtering,
    to meet the the full GFM specification
    (see https://github.github.com/gfm/#autolinks-extension-).
    """
    @staticmethod
    def make() -> PresetType: ...
