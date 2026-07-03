from _typeshed import Incomplete
from nltk.internals import config_java as config_java, find_dir as find_dir, find_file as find_file, find_jar as find_jar, java as java
from nltk.tokenize.api import TokenizerI as TokenizerI

class StanfordSegmenter(TokenizerI):
    """Interface to the Stanford Segmenter

    If stanford-segmenter version is older than 2016-10-31, then path_to_slf4j
    should be provieded, for example::

        seg = StanfordSegmenter(path_to_slf4j='/YOUR_PATH/slf4j-api.jar')

    >>> from nltk.tokenize.stanford_segmenter import StanfordSegmenter
    >>> seg = StanfordSegmenter() # doctest: +SKIP
    >>> seg.default_config('zh') # doctest: +SKIP
    >>> sent = u'这是斯坦福中文分词器测试'
    >>> print(seg.segment(sent)) # doctest: +SKIP
    这 是 斯坦福 中文 分词器 测试
    <BLANKLINE>
    >>> seg.default_config('ar') # doctest: +SKIP
    >>> sent = u'هذا هو تصنيف ستانفورد العربي للكلمات'
    >>> print(seg.segment(sent.split())) # doctest: +SKIP
    هذا هو تصنيف ستانفورد العربي ل الكلمات
    <BLANKLINE>
    """
    java_options: Incomplete
    def __init__(self, path_to_jar: Incomplete | None = None, path_to_slf4j: Incomplete | None = None, java_class: Incomplete | None = None, path_to_model: Incomplete | None = None, path_to_dict: Incomplete | None = None, path_to_sihan_corpora_dict: Incomplete | None = None, sihan_post_processing: str = 'false', keep_whitespaces: str = 'false', encoding: str = 'UTF-8', options: Incomplete | None = None, verbose: bool = False, java_options: str = '-mx2g') -> None: ...
    def default_config(self, lang) -> None:
        """
        Attempt to initialize Stanford Word Segmenter for the specified language
        using the STANFORD_SEGMENTER and STANFORD_MODELS environment variables
        """
    def tokenize(self, s) -> None: ...
    def segment_file(self, input_file_path):
        """ """
    def segment(self, tokens): ...
    def segment_sents(self, sentences):
        """ """
