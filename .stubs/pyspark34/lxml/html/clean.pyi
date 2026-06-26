from _typeshed import Incomplete

__all__ = ['clean_html', 'clean', 'Cleaner', 'autolink', 'autolink_html', 'word_break', 'word_break_html']

unichr = chr
unicode = str

class Cleaner:
    '''
    Instances cleans the document of each of the possible offending
    elements.  The cleaning is controlled by attributes; you can
    override attributes in a subclass, or set them in the constructor.

    ``scripts``:
        Removes any ``<script>`` tags.

    ``javascript``:
        Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets
        as they could contain Javascript.

    ``comments``:
        Removes any comments.

    ``style``:
        Removes any style tags.

    ``inline_style``
        Removes any style attributes.  Defaults to the value of the ``style`` option.

    ``links``:
        Removes any ``<link>`` tags

    ``meta``:
        Removes any ``<meta>`` tags

    ``page_structure``:
        Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.

    ``processing_instructions``:
        Removes any processing instructions.

    ``embedded``:
        Removes any embedded objects (flash, iframes)

    ``frames``:
        Removes any frame-related tags

    ``forms``:
        Removes any form tags

    ``annoying_tags``:
        Tags that aren\'t *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``

    ``remove_tags``:
        A list of tags to remove.  Only the tags will be removed,
        their content will get pulled up into the parent tag.

    ``kill_tags``:
        A list of tags to kill.  Killing also removes the tag\'s content,
        i.e. the whole subtree, not just the tag itself.

    ``allow_tags``:
        A list of tags to include (default include all).

    ``remove_unknown_tags``:
        Remove any tags that aren\'t standard parts of HTML.

    ``safe_attrs_only``:
        If true, only include \'safe\' attributes (specifically the list
        from the feedparser HTML sanitisation web site).

    ``safe_attrs``:
        A set of attribute names to override the default list of attributes
        considered \'safe\' (when safe_attrs_only=True).

    ``add_nofollow``:
        If true, then any <a> tags will have ``rel="nofollow"`` added to them.

    ``host_whitelist``:
        A list or set of hosts that you can use for embedded content
        (for content like ``<object>``, ``<link rel="stylesheet">``, etc).
        You can also implement/override the method
        ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to
        implement more complex rules for what can be embedded.
        Anything that passes this test will be shown, regardless of
        the value of (for instance) ``embedded``.

        Note that this parameter might not work as intended if you do not
        make the links absolute before doing the cleaning.

        Note that you may also need to set ``whitelist_tags``.

    ``whitelist_tags``:
        A set of tags that can be included with ``host_whitelist``.
        The default is ``iframe`` and ``embed``; you may wish to
        include other tags like ``script``, or you may want to
        implement ``allow_embedded_url`` for more control.  Set to None to
        include all tags.

    This modifies the document *in place*.
    '''
    scripts: bool
    javascript: bool
    comments: bool
    style: bool
    inline_style: Incomplete
    links: bool
    meta: bool
    page_structure: bool
    processing_instructions: bool
    embedded: bool
    frames: bool
    forms: bool
    annoying_tags: bool
    remove_tags: Incomplete
    allow_tags: Incomplete
    kill_tags: Incomplete
    remove_unknown_tags: bool
    safe_attrs_only: bool
    safe_attrs: Incomplete
    add_nofollow: bool
    host_whitelist: Incomplete
    whitelist_tags: Incomplete
    def __init__(self, **kw) -> None: ...
    def __call__(self, doc) -> None:
        """
        Cleans the document.
        """
    def allow_follow(self, anchor):
        '''
        Override to suppress rel="nofollow" on some anchors.
        '''
    def allow_element(self, el):
        """
        Decide whether an element is configured to be accepted or rejected.

        :param el: an element.
        :return: true to accept the element or false to reject/discard it.
        """
    def allow_embedded_url(self, el, url):
        """
        Decide whether a URL that was found in an element's attributes or text
        if configured to be accepted or rejected.

        :param el: an element.
        :param url: a URL found on the element.
        :return: true to accept the URL and false to reject it.
        """
    def kill_conditional_comments(self, doc):
        """
        IE conditional comments basically embed HTML that the parser
        doesn't normally see.  We can't allow anything like that, so
        we'll kill any comments that could be conditional.
        """
    def clean_html(self, html): ...

clean: Incomplete
clean_html: Incomplete

def autolink(el, link_regexes=..., avoid_elements=..., avoid_hosts=..., avoid_classes=...) -> None:
    """
    Turn any URLs into links.

    It will search for links identified by the given regular
    expressions (by default mailto and http(s) links).

    It won't link text in an element in avoid_elements, or an element
    with a class in avoid_classes.  It won't link to anything with a
    host that matches one of the regular expressions in avoid_hosts
    (default localhost and 127.0.0.1).

    If you pass in an element, the element's tail will not be
    substituted, only the contents of the element.
    """
def autolink_html(html, *args, **kw): ...
def word_break(el, max_width: int = 40, avoid_elements=..., avoid_classes=..., break_character=...) -> None:
    """
    Breaks any long words found in the body of the text (not attributes).

    Doesn't effect any of the tags in avoid_elements, by default
    ``<textarea>`` and ``<pre>``

    Breaks words by inserting &#8203;, which is a unicode character
    for Zero Width Space character.  This generally takes up no space
    in rendering, but does copy as a space, and in monospace contexts
    usually takes up space.

    See http://www.cs.tut.fi/~jkorpela/html/nobr.html for a discussion
    """
def word_break_html(html, *args, **kw): ...
