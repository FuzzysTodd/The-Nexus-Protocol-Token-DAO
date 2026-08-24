from nltk.corpus.reader.api import *
from _typeshed import Incomplete
from nltk.internals import import_from_stdlib as import_from_stdlib
from nltk.tree import Tree as Tree

class TimitCorpusReader(CorpusReader):
    """
    Reader for the TIMIT corpus (or any other corpus with the same
    file layout and use of file formats).  The corpus root directory
    should contain the following files:

      - timitdic.txt: dictionary of standard transcriptions
      - spkrinfo.txt: table of speaker information

    In addition, the root directory should contain one subdirectory
    for each speaker, containing three files for each utterance:

      - <utterance-id>.txt: text content of utterances
      - <utterance-id>.wrd: tokenized text content of utterances
      - <utterance-id>.phn: phonetic transcription of utterances
      - <utterance-id>.wav: utterance sound file
    """
    speakers: Incomplete
    def __init__(self, root, encoding: str = 'utf8') -> None:
        """
        Construct a new TIMIT corpus reader in the given directory.
        :param root: The root directory for this corpus.
        """
    def fileids(self, filetype: Incomplete | None = None):
        """
        Return a list of file identifiers for the files that make up
        this corpus.

        :param filetype: If specified, then ``filetype`` indicates that
            only the files that have the given type should be
            returned.  Accepted values are: ``txt``, ``wrd``, ``phn``,
            ``wav``, or ``metadata``,
        """
    def utteranceids(self, dialect: Incomplete | None = None, sex: Incomplete | None = None, spkrid: Incomplete | None = None, sent_type: Incomplete | None = None, sentid: Incomplete | None = None):
        """
        :return: A list of the utterance identifiers for all
            utterances in this corpus, or for the given speaker, dialect
            region, gender, sentence type, or sentence number, if
            specified.
        """
    def transcription_dict(self):
        """
        :return: A dictionary giving the 'standard' transcription for
            each word.
        """
    def spkrid(self, utterance): ...
    def sentid(self, utterance): ...
    def utterance(self, spkrid, sentid): ...
    def spkrutteranceids(self, speaker):
        """
        :return: A list of all utterances associated with a given
            speaker.
        """
    def spkrinfo(self, speaker):
        """
        :return: A dictionary mapping .. something.
        """
    def phones(self, utterances: Incomplete | None = None): ...
    def phone_times(self, utterances: Incomplete | None = None):
        """
        offset is represented as a number of 16kHz samples!
        """
    def words(self, utterances: Incomplete | None = None): ...
    def word_times(self, utterances: Incomplete | None = None): ...
    def sents(self, utterances: Incomplete | None = None): ...
    def sent_times(self, utterances: Incomplete | None = None): ...
    def phone_trees(self, utterances: Incomplete | None = None): ...
    def wav(self, utterance, start: int = 0, end: Incomplete | None = None): ...
    def audiodata(self, utterance, start: int = 0, end: Incomplete | None = None): ...
    def play(self, utterance, start: int = 0, end: Incomplete | None = None) -> None:
        """
        Play the given audio sample.

        :param utterance: The utterance id of the sample to play
        """

class SpeakerInfo:
    id: Incomplete
    sex: Incomplete
    dr: Incomplete
    use: Incomplete
    recdate: Incomplete
    birthdate: Incomplete
    ht: Incomplete
    race: Incomplete
    edu: Incomplete
    comments: Incomplete
    def __init__(self, id, sex, dr, use, recdate, birthdate, ht, race, edu, comments: Incomplete | None = None) -> None: ...

def read_timit_block(stream):
    """
    Block reader for timit tagged sentences, which are preceded by a sentence
    number that will be ignored.
    """
