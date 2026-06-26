from _typeshed import Incomplete
from collections.abc import Generator

maketrans: Incomplete

def text_to_word_sequence(text, filters: str = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower: bool = True, split: str = ' '):
    '''Converts a text to a sequence of words (or tokens).

    # Arguments
        text: Input text (string).
        filters: list (or concatenation) of characters to filter out, such as
            punctuation. Default: ``!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\\t\\n``,
            includes basic punctuation, tabs, and newlines.
        lower: boolean. Whether to convert the input to lowercase.
        split: str. Separator for word splitting.

    # Returns
        A list of words (or tokens).
    '''
def one_hot(text, n, filters: str = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower: bool = True, split: str = ' '):
    '''One-hot encodes a text into a list of word indexes of size n.

    This is a wrapper to the `hashing_trick` function using `hash` as the
    hashing function; unicity of word to index mapping non-guaranteed.

    # Arguments
        text: Input text (string).
        n: int. Size of vocabulary.
        filters: list (or concatenation) of characters to filter out, such as
            punctuation. Default: ``!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\\t\\n``,
            includes basic punctuation, tabs, and newlines.
        lower: boolean. Whether to set the text to lowercase.
        split: str. Separator for word splitting.

    # Returns
        List of integers in [1, n]. Each integer encodes a word
        (unicity non-guaranteed).
    '''
def hashing_trick(text, n, hash_function: Incomplete | None = None, filters: str = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower: bool = True, split: str = ' '):
    '''Converts a text to a sequence of indexes in a fixed-size hashing space.

    # Arguments
        text: Input text (string).
        n: Dimension of the hashing space.
        hash_function: defaults to python `hash` function, can be \'md5\' or
            any function that takes in input a string and returns a int.
            Note that \'hash\' is not a stable hashing function, so
            it is not consistent across different runs, while \'md5\'
            is a stable hashing function.
        filters: list (or concatenation) of characters to filter out, such as
            punctuation. Default: ``!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\\t\\n``,
            includes basic punctuation, tabs, and newlines.
        lower: boolean. Whether to set the text to lowercase.
        split: str. Separator for word splitting.

    # Returns
        A list of integer word indices (unicity non-guaranteed).

    `0` is a reserved index that won\'t be assigned to any word.

    Two or more words may be assigned to the same index, due to possible
    collisions by the hashing function.
    The [probability](
        https://en.wikipedia.org/wiki/Birthday_problem#Probability_table)
    of a collision is in relation to the dimension of the hashing space and
    the number of distinct objects.
    '''

class Tokenizer:
    """Text tokenization utility class.

    This class allows to vectorize a text corpus, by turning each
    text into either a sequence of integers (each integer being the index
    of a token in a dictionary) or into a vector where the coefficient
    for each token could be binary, based on word count, based on tf-idf...

    # Arguments
        num_words: the maximum number of words to keep, based
            on word frequency. Only the most common `num_words-1` words will
            be kept.
        filters: a string where each element is a character that will be
            filtered from the texts. The default is all punctuation, plus
            tabs and line breaks, minus the `'` character.
        lower: boolean. Whether to convert the texts to lowercase.
        split: str. Separator for word splitting.
        char_level: if True, every character will be treated as a token.
        oov_token: if given, it will be added to word_index and used to
            replace out-of-vocabulary words during text_to_sequence calls

    By default, all punctuation is removed, turning the texts into
    space-separated sequences of words
    (words maybe include the `'` character). These sequences are then
    split into lists of tokens. They will then be indexed or vectorized.

    `0` is a reserved index that won't be assigned to any word.
    """
    word_counts: Incomplete
    word_docs: Incomplete
    filters: Incomplete
    split: Incomplete
    lower: Incomplete
    num_words: Incomplete
    document_count: Incomplete
    char_level: Incomplete
    oov_token: Incomplete
    index_docs: Incomplete
    word_index: Incomplete
    index_word: Incomplete
    def __init__(self, num_words: Incomplete | None = None, filters: str = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower: bool = True, split: str = ' ', char_level: bool = False, oov_token: Incomplete | None = None, document_count: int = 0, **kwargs) -> None: ...
    def fit_on_texts(self, texts):
        """Updates internal vocabulary based on a list of texts.

        In the case where texts contains lists,
        we assume each entry of the lists to be a token.

        Required before using `texts_to_sequences` or `texts_to_matrix`.

        # Arguments
            texts: can be a list of strings,
                a generator of strings (for memory-efficiency),
                or a list of list of strings.
        """
    def fit_on_sequences(self, sequences) -> None:
        '''Updates internal vocabulary based on a list of sequences.

        Required before using `sequences_to_matrix`
        (if `fit_on_texts` was never called).

        # Arguments
            sequences: A list of sequence.
                A "sequence" is a list of integer word indices.
        '''
    def texts_to_sequences(self, texts):
        """Transforms each text in texts to a sequence of integers.

        Only top `num_words-1` most frequent words will be taken into account.
        Only words known by the tokenizer will be taken into account.

        # Arguments
            texts: A list of texts (strings).

        # Returns
            A list of sequences.
        """
    def texts_to_sequences_generator(self, texts) -> Generator[Incomplete, None, None]:
        """Transforms each text in `texts` to a sequence of integers.

        Each item in texts can also be a list,
        in which case we assume each item of that list to be a token.

        Only top `num_words-1` most frequent words will be taken into account.
        Only words known by the tokenizer will be taken into account.

        # Arguments
            texts: A list of texts (strings).

        # Yields
            Yields individual sequences.
        """
    def sequences_to_texts(self, sequences):
        """Transforms each sequence into a list of text.

        Only top `num_words-1` most frequent words will be taken into account.
        Only words known by the tokenizer will be taken into account.

        # Arguments
            sequences: A list of sequences (list of integers).

        # Returns
            A list of texts (strings)
        """
    def sequences_to_texts_generator(self, sequences) -> Generator[Incomplete, None, None]:
        """Transforms each sequence in `sequences` to a list of texts(strings).

        Each sequence has to a list of integers.
        In other words, sequences should be a list of sequences

        Only top `num_words-1` most frequent words will be taken into account.
        Only words known by the tokenizer will be taken into account.

        # Arguments
            sequences: A list of sequences.

        # Yields
            Yields individual texts.
        """
    def texts_to_matrix(self, texts, mode: str = 'binary'):
        '''Convert a list of texts to a Numpy matrix.

        # Arguments
            texts: list of strings.
            mode: one of "binary", "count", "tfidf", "freq".

        # Returns
            A Numpy matrix.
        '''
    def sequences_to_matrix(self, sequences, mode: str = 'binary'):
        '''Converts a list of sequences into a Numpy matrix.

        # Arguments
            sequences: list of sequences
                (a sequence is a list of integer word indices).
            mode: one of "binary", "count", "tfidf", "freq"

        # Returns
            A Numpy matrix.

        # Raises
            ValueError: In case of invalid `mode` argument,
                or if the Tokenizer requires to be fit to sample data.
        '''
    def get_config(self):
        """Returns the tokenizer configuration as Python dictionary.
        The word count dictionaries used by the tokenizer get serialized
        into plain JSON, so that the configuration can be read by other
        projects.

        # Returns
            A Python dictionary with the tokenizer configuration.
        """
    def to_json(self, **kwargs):
        """Returns a JSON string containing the tokenizer configuration.
        To load a tokenizer from a JSON string, use
        `keras.preprocessing.text.tokenizer_from_json(json_string)`.

        # Arguments
            **kwargs: Additional keyword arguments
                to be passed to `json.dumps()`.

        # Returns
            A JSON string containing the tokenizer configuration.
        """

def tokenizer_from_json(json_string):
    """Parses a JSON tokenizer configuration file and returns a
    tokenizer instance.

    # Arguments
        json_string: JSON string encoding a tokenizer configuration.

    # Returns
        A Keras Tokenizer instance
    """
