from _typeshed import Incomplete
from bleach import html5lib_shim as html5lib_shim
from collections.abc import Generator

DEFAULT_CALLBACKS: Incomplete
TLDS: Incomplete

def build_url_re(tlds=..., protocols=...):
    """Builds the url regex used by linkifier

    If you want a different set of tlds or allowed protocols, pass those in
    and stomp on the existing ``url_re``::

        from bleach import linkifier

        my_url_re = linkifier.build_url_re(my_tlds_list, my_protocols)

        linker = LinkifyFilter(url_re=my_url_re)

    """

URL_RE: Incomplete
PROTO_RE: Incomplete

def build_email_re(tlds=...):
    """Builds the email regex used by linkifier

    If you want a different set of tlds, pass those in and stomp on the existing ``email_re``::

        from bleach import linkifier

        my_email_re = linkifier.build_email_re(my_tlds_list)

        linker = LinkifyFilter(email_re=my_url_re)

    """

EMAIL_RE: Incomplete

class Linker:
    """Convert URL-like strings in an HTML fragment to links

    This function converts strings that look like URLs, domain names and email
    addresses in text that may be an HTML fragment to links, while preserving:

    1. links already in the string
    2. urls found in attributes
    3. email addresses

    linkify does a best-effort approach and tries to recover from bad
    situations due to crazy text.

    """
    callbacks: Incomplete
    skip_tags: Incomplete
    parse_email: Incomplete
    url_re: Incomplete
    email_re: Incomplete
    parser: Incomplete
    walker: Incomplete
    serializer: Incomplete
    def __init__(self, callbacks=..., skip_tags: Incomplete | None = None, parse_email: bool = False, url_re=..., email_re=..., recognized_tags=...) -> None:
        """Creates a Linker instance

        :arg list callbacks: list of callbacks to run when adjusting tag attributes;
            defaults to ``bleach.linkifier.DEFAULT_CALLBACKS``

        :arg set skip_tags: set of tags that you don't want to linkify the
            contents of; for example, you could set this to ``{'pre'}`` to skip
            linkifying contents of ``pre`` tags; ``None`` means you don't
            want linkify to skip any tags

        :arg bool parse_email: whether or not to linkify email addresses

        :arg url_re: url matching regex

        :arg email_re: email matching regex

        :arg set recognized_tags: the set of tags that linkify knows about;
            everything else gets escaped

        :returns: linkified text as unicode

        """
    def linkify(self, text):
        """Linkify specified text

        :arg str text: the text to add links to

        :returns: linkified text as unicode

        :raises TypeError: if ``text`` is not a text type

        """

class LinkifyFilter(html5lib_shim.Filter):
    '''html5lib filter that linkifies text

    This will do the following:

    * convert email addresses into links
    * convert urls into links
    * edit existing links by running them through callbacks--the default is to
      add a ``rel="nofollow"``

    This filter can be used anywhere html5lib filters can be used.

    '''
    callbacks: Incomplete
    skip_tags: Incomplete
    parse_email: Incomplete
    url_re: Incomplete
    email_re: Incomplete
    def __init__(self, source, callbacks=..., skip_tags: Incomplete | None = None, parse_email: bool = False, url_re=..., email_re=...) -> None:
        """Creates a LinkifyFilter instance

        :arg source: stream as an html5lib TreeWalker

        :arg list callbacks: list of callbacks to run when adjusting tag attributes;
            defaults to ``bleach.linkifier.DEFAULT_CALLBACKS``

        :arg set skip_tags: set of tags that you don't want to linkify the
            contents of; for example, you could set this to ``{'pre'}`` to skip
            linkifying contents of ``pre`` tags

        :arg bool parse_email: whether or not to linkify email addresses

        :arg url_re: url matching regex

        :arg email_re: email matching regex

        """
    def apply_callbacks(self, attrs, is_new):
        """Given an attrs dict and an is_new bool, runs through callbacks

        Callbacks can return an adjusted attrs dict or ``None``. In the case of
        ``None``, we stop going through callbacks and return that and the link
        gets dropped.

        :arg dict attrs: map of ``(namespace, name)`` -> ``value``

        :arg bool is_new: whether or not this link was added by linkify

        :returns: adjusted attrs dict or ``None``

        """
    def extract_character_data(self, token_list):
        """Extracts and squashes character sequences in a token stream"""
    def handle_email_addresses(self, src_iter) -> Generator[Incomplete, Incomplete, None]:
        """Handle email addresses in character tokens"""
    def strip_non_url_bits(self, fragment):
        """Strips non-url bits from the url

        This accounts for over-eager matching by the regex.

        """
    def handle_links(self, src_iter) -> Generator[Incomplete, Incomplete, None]:
        """Handle links in character tokens"""
    def handle_a_tag(self, token_buffer) -> Generator[Incomplete, Incomplete, None]:
        '''Handle the "a" tag

        This could adjust the link or drop it altogether depending on what the
        callbacks return.

        This yields the new set of tokens.

        '''
    def extract_entities(self, token) -> Generator[Incomplete, Incomplete, None]:
        """Handles Characters tokens with entities

        Our overridden tokenizer doesn't do anything with entities. However,
        that means that the serializer will convert all ``&`` in Characters
        tokens to ``&amp;``.

        Since we don't want that, we extract entities here and convert them to
        Entity tokens so the serializer will let them be.

        :arg token: the Characters token to work on

        :returns: generator of tokens

        """
    def __iter__(self): ...
