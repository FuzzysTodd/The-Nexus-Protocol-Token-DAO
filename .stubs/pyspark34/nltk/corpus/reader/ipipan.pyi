from _typeshed import Incomplete
from nltk.corpus.reader.api import CorpusReader as CorpusReader
from nltk.corpus.reader.util import StreamBackedCorpusView as StreamBackedCorpusView, concat as concat

class IPIPANCorpusReader(CorpusReader):
    '''
    Corpus reader designed to work with corpus created by IPI PAN.
    See http://korpus.pl/en/ for more details about IPI PAN corpus.

    The corpus includes information about text domain, channel and categories.
    You can access possible values using ``domains()``, ``channels()`` and
    ``categories()``. You can use also this metadata to filter files, e.g.:
    ``fileids(channel=\'prasa\')``, ``fileids(categories=\'publicystyczny\')``.

    The reader supports methods: words, sents, paras and their tagged versions.
    You can get part of speech instead of full tag by giving "simplify_tags=True"
    parameter, e.g.: ``tagged_sents(simplify_tags=True)``.

    Also you can get all tags disambiguated tags specifying parameter
    "one_tag=False", e.g.: ``tagged_paras(one_tag=False)``.

    You can get all tags that were assigned by a morphological analyzer specifying
    parameter "disamb_only=False", e.g. ``tagged_words(disamb_only=False)``.

    The IPIPAN Corpus contains tags indicating if there is a space between two
    tokens. To add special "no space" markers, you should specify parameter
    "append_no_space=True", e.g. ``tagged_words(append_no_space=True)``.
    As a result in place where there should be no space between two tokens new
    pair (\'\', \'no-space\') will be inserted (for tagged data) and just \'\' for
    methods without tags.

    The corpus reader can also try to append spaces between words. To enable this
    option, specify parameter "append_space=True", e.g. ``words(append_space=True)``.
    As a result either \' \' or (\' \', \'space\') will be inserted between tokens.

    By default, xml entities like &quot; and &amp; are replaced by corresponding
    characters. You can turn off this feature, specifying parameter
    "replace_xmlentities=False", e.g. ``words(replace_xmlentities=False)``.
    '''
    def __init__(self, root, fileids) -> None: ...
    def channels(self, fileids: Incomplete | None = None): ...
    def domains(self, fileids: Incomplete | None = None): ...
    def categories(self, fileids: Incomplete | None = None): ...
    def fileids(self, channels: Incomplete | None = None, domains: Incomplete | None = None, categories: Incomplete | None = None): ...
    def sents(self, fileids: Incomplete | None = None, **kwargs): ...
    def paras(self, fileids: Incomplete | None = None, **kwargs): ...
    def words(self, fileids: Incomplete | None = None, **kwargs): ...
    def tagged_sents(self, fileids: Incomplete | None = None, **kwargs): ...
    def tagged_paras(self, fileids: Incomplete | None = None, **kwargs): ...
    def tagged_words(self, fileids: Incomplete | None = None, **kwargs): ...

class IPIPANCorpusView(StreamBackedCorpusView):
    WORDS_MODE: int
    SENTS_MODE: int
    PARAS_MODE: int
    in_sentence: bool
    position: int
    show_tags: Incomplete
    disamb_only: Incomplete
    mode: Incomplete
    simplify_tags: Incomplete
    one_tag: Incomplete
    append_no_space: Incomplete
    append_space: Incomplete
    replace_xmlentities: Incomplete
    def __init__(self, filename, startpos: int = 0, **kwargs) -> None: ...
    def read_block(self, stream): ...
