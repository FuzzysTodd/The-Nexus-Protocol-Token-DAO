from _typeshed import Incomplete
from collections.abc import Generator
from nltk.classify import Senna as Senna

class SennaTagger(Senna):
    def __init__(self, path, encoding: str = 'utf-8') -> None: ...
    def tag_sents(self, sentences):
        """
        Applies the tag method over a list of sentences. This method will return
        for each sentence a list of tuples of (word, tag).
        """

class SennaChunkTagger(Senna):
    def __init__(self, path, encoding: str = 'utf-8') -> None: ...
    def tag_sents(self, sentences):
        """
        Applies the tag method over a list of sentences. This method will return
        for each sentence a list of tuples of (word, tag).
        """
    def bio_to_chunks(self, tagged_sent, chunk_type) -> Generator[Incomplete, None, None]:
        """
        Extracts the chunks in a BIO chunk-tagged sentence.

        >>> from nltk.tag import SennaChunkTagger
        >>> chktagger = SennaChunkTagger('/usr/share/senna-v3.0')  # doctest: +SKIP
        >>> sent = 'What is the airspeed of an unladen swallow ?'.split()
        >>> tagged_sent = chktagger.tag(sent)  # doctest: +SKIP
        >>> tagged_sent  # doctest: +SKIP
        [('What', 'B-NP'), ('is', 'B-VP'), ('the', 'B-NP'), ('airspeed', 'I-NP'),
        ('of', 'B-PP'), ('an', 'B-NP'), ('unladen', 'I-NP'), ('swallow', 'I-NP'),
        ('?', 'O')]
        >>> list(chktagger.bio_to_chunks(tagged_sent, chunk_type='NP'))  # doctest: +SKIP
        [('What', '0'), ('the airspeed', '2-3'), ('an unladen swallow', '5-6-7')]

        :param tagged_sent: A list of tuples of word and BIO chunk tag.
        :type tagged_sent: list(tuple)
        :param tagged_sent: The chunk tag that users want to extract, e.g. 'NP' or 'VP'
        :type tagged_sent: str

        :return: An iterable of tuples of chunks that users want to extract
          and their corresponding indices.
        :rtype: iter(tuple(str))
        """

class SennaNERTagger(Senna):
    def __init__(self, path, encoding: str = 'utf-8') -> None: ...
    def tag_sents(self, sentences):
        """
        Applies the tag method over a list of sentences. This method will return
        for each sentence a list of tuples of (word, tag).
        """
