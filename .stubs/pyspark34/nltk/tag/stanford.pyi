import abc
from _typeshed import Incomplete
from nltk.internals import config_java as config_java, find_file as find_file, find_jar as find_jar, java as java
from nltk.tag.api import TaggerI as TaggerI

class StanfordTagger(TaggerI, metaclass=abc.ABCMeta):
    """
    An interface to Stanford taggers. Subclasses must define:

    - ``_cmd`` property: A property that returns the command that will be
      executed.
    - ``_SEPARATOR``: Class constant that represents that character that
      is used to separate the tokens from their tags.
    - ``_JAR`` file: Class constant that represents the jar file name.
    """
    java_options: Incomplete
    def __init__(self, model_filename, path_to_jar: Incomplete | None = None, encoding: str = 'utf8', verbose: bool = False, java_options: str = '-mx1000m') -> None: ...
    def tag(self, tokens): ...
    def tag_sents(self, sentences): ...
    def parse_output(self, text, sentences: Incomplete | None = None): ...

class StanfordPOSTagger(StanfordTagger):
    """
    A class for pos tagging with Stanford Tagger. The input is the paths to:
     - a model trained on training data
     - (optionally) the path to the stanford tagger jar file. If not specified here,
       then this jar file must be specified in the CLASSPATH environment variable.
     - (optionally) the encoding of the training data (default: UTF-8)

    Example:

        >>> from nltk.tag import StanfordPOSTagger
        >>> st = StanfordPOSTagger('english-bidirectional-distsim.tagger') # doctest: +SKIP
        >>> st.tag('What is the airspeed of an unladen swallow ?'.split()) # doctest: +SKIP
        [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'), ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'), ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]
    """
    def __init__(self, *args, **kwargs) -> None: ...

class StanfordNERTagger(StanfordTagger):
    """
    A class for Named-Entity Tagging with Stanford Tagger. The input is the paths to:

    - a model trained on training data
    - (optionally) the path to the stanford tagger jar file. If not specified here,
      then this jar file must be specified in the CLASSPATH environment variable.
    - (optionally) the encoding of the training data (default: UTF-8)

    Example:

        >>> from nltk.tag import StanfordNERTagger
        >>> st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') # doctest: +SKIP
        >>> st.tag('Rami Eid is studying at Stony Brook University in NY'.split()) # doctest: +SKIP
        [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'),
         ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'),
         ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'LOCATION')]
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def parse_output(self, text, sentences): ...
