from _typeshed import Incomplete
from nltk.corpus import CategorizedPlaintextCorpusReader as CategorizedPlaintextCorpusReader
from nltk.data import load as load
from nltk.tokenize.casual import EMOTICON_RE as EMOTICON_RE

NEGATION: str
NEGATION_RE: Incomplete
CLAUSE_PUNCT: str
CLAUSE_PUNCT_RE: Incomplete
HAPPY: Incomplete
SAD: Incomplete

def timer(method):
    """
    A timer decorator to measure execution performance of methods.
    """
def extract_unigram_feats(document, unigrams, handle_negation: bool = False):
    """
    Populate a dictionary of unigram features, reflecting the presence/absence in
    the document of each of the tokens in `unigrams`.

    :param document: a list of words/tokens.
    :param unigrams: a list of words/tokens whose presence/absence has to be
        checked in `document`.
    :param handle_negation: if `handle_negation == True` apply `mark_negation`
        method to `document` before checking for unigram presence/absence.
    :return: a dictionary of unigram features {unigram : boolean}.

    >>> words = ['ice', 'police', 'riot']
    >>> document = 'ice is melting due to global warming'.split()
    >>> sorted(extract_unigram_feats(document, words).items())
    [('contains(ice)', True), ('contains(police)', False), ('contains(riot)', False)]
    """
def extract_bigram_feats(document, bigrams):
    """
    Populate a dictionary of bigram features, reflecting the presence/absence in
    the document of each of the tokens in `bigrams`. This extractor function only
    considers contiguous bigrams obtained by `nltk.bigrams`.

    :param document: a list of words/tokens.
    :param unigrams: a list of bigrams whose presence/absence has to be
        checked in `document`.
    :return: a dictionary of bigram features {bigram : boolean}.

    >>> bigrams = [('global', 'warming'), ('police', 'prevented'), ('love', 'you')]
    >>> document = 'ice is melting due to global warming'.split()
    >>> sorted(extract_bigram_feats(document, bigrams).items()) # doctest: +NORMALIZE_WHITESPACE
    [('contains(global - warming)', True), ('contains(love - you)', False),
    ('contains(police - prevented)', False)]
    """
def mark_negation(document, double_neg_flip: bool = False, shallow: bool = False):
    '''
    Append _NEG suffix to words that appear in the scope between a negation
    and a punctuation mark.

    :param document: a list of words/tokens, or a tuple (words, label).
    :param shallow: if True, the method will modify the original document in place.
    :param double_neg_flip: if True, double negation is considered affirmation
        (we activate/deactivate negation scope every time we find a negation).
    :return: if `shallow == True` the method will modify the original document
        and return it. If `shallow == False` the method will return a modified
        document, leaving the original unmodified.

    >>> sent = "I didn\'t like this movie . It was bad .".split()
    >>> mark_negation(sent)
    [\'I\', "didn\'t", \'like_NEG\', \'this_NEG\', \'movie_NEG\', \'.\', \'It\', \'was\', \'bad\', \'.\']
    '''
def output_markdown(filename, **kwargs) -> None:
    """
    Write the output of an analysis to a file.
    """
def split_train_test(all_instances, n: Incomplete | None = None):
    """
    Randomly split `n` instances of the dataset into train and test sets.

    :param all_instances: a list of instances (e.g. documents) that will be split.
    :param n: the number of instances to consider (in case we want to use only a
        subset).
    :return: two lists of instances. Train set is 8/10 of the total and test set
        is 2/10 of the total.
    """
def json2csv_preprocess(json_file, outfile, fields, encoding: str = 'utf8', errors: str = 'replace', gzip_compress: bool = False, skip_retweets: bool = True, skip_tongue_tweets: bool = True, skip_ambiguous_tweets: bool = True, strip_off_emoticons: bool = True, remove_duplicates: bool = True, limit: Incomplete | None = None) -> None:
    '''
    Convert json file to csv file, preprocessing each row to obtain a suitable
    dataset for tweets Semantic Analysis.

    :param json_file: the original json file containing tweets.
    :param outfile: the output csv filename.
    :param fields: a list of fields that will be extracted from the json file and
        kept in the output csv file.
    :param encoding: the encoding of the files.
    :param errors: the error handling strategy for the output writer.
    :param gzip_compress: if True, create a compressed GZIP file.

    :param skip_retweets: if True, remove retweets.
    :param skip_tongue_tweets: if True, remove tweets containing ":P" and ":-P"
        emoticons.
    :param skip_ambiguous_tweets: if True, remove tweets containing both happy
        and sad emoticons.
    :param strip_off_emoticons: if True, strip off emoticons from all tweets.
    :param remove_duplicates: if True, remove tweets appearing more than once.
    :param limit: an integer to set the number of tweets to convert. After the
        limit is reached the conversion will stop. It can be useful to create
        subsets of the original tweets json data.
    '''
def parse_tweets_set(filename, label, word_tokenizer: Incomplete | None = None, sent_tokenizer: Incomplete | None = None, skip_header: bool = True):
    """
    Parse csv file containing tweets and output data a list of (text, label) tuples.

    :param filename: the input csv filename.
    :param label: the label to be appended to each tweet contained in the csv file.
    :param word_tokenizer: the tokenizer instance that will be used to tokenize
        each sentence into tokens (e.g. WordPunctTokenizer() or BlanklineTokenizer()).
        If no word_tokenizer is specified, tweets will not be tokenized.
    :param sent_tokenizer: the tokenizer that will be used to split each tweet into
        sentences.
    :param skip_header: if True, skip the first line of the csv file (which usually
        contains headers).

    :return: a list of (text, label) tuples.
    """
def demo_tweets(trainer, n_instances: Incomplete | None = None, output: Incomplete | None = None) -> None:
    """
    Train and test Naive Bayes classifier on 10000 tweets, tokenized using
    TweetTokenizer.
    Features are composed of:

    - 1000 most frequent unigrams
    - 100 top bigrams (using BigramAssocMeasures.pmi)

    :param trainer: `train` method of a classifier.
    :param n_instances: the number of total tweets that have to be used for
        training and testing. Tweets will be equally split between positive and
        negative.
    :param output: the output file where results have to be reported.
    """
def demo_movie_reviews(trainer, n_instances: Incomplete | None = None, output: Incomplete | None = None) -> None:
    """
    Train classifier on all instances of the Movie Reviews dataset.
    The corpus has been preprocessed using the default sentence tokenizer and
    WordPunctTokenizer.
    Features are composed of:

    - most frequent unigrams

    :param trainer: `train` method of a classifier.
    :param n_instances: the number of total reviews that have to be used for
        training and testing. Reviews will be equally split between positive and
        negative.
    :param output: the output file where results have to be reported.
    """
def demo_subjectivity(trainer, save_analyzer: bool = False, n_instances: Incomplete | None = None, output: Incomplete | None = None):
    """
    Train and test a classifier on instances of the Subjective Dataset by Pang and
    Lee. The dataset is made of 5000 subjective and 5000 objective sentences.
    All tokens (words and punctuation marks) are separated by a whitespace, so
    we use the basic WhitespaceTokenizer to parse the data.

    :param trainer: `train` method of a classifier.
    :param save_analyzer: if `True`, store the SentimentAnalyzer in a pickle file.
    :param n_instances: the number of total sentences that have to be used for
        training and testing. Sentences will be equally split between positive
        and negative.
    :param output: the output file where results have to be reported.
    """
def demo_sent_subjectivity(text) -> None:
    """
    Classify a single sentence as subjective or objective using a stored
    SentimentAnalyzer.

    :param text: a sentence whose subjectivity has to be classified.
    """
def demo_liu_hu_lexicon(sentence, plot: bool = False) -> None:
    """
    Basic example of sentiment classification using Liu and Hu opinion lexicon.
    This function simply counts the number of positive, negative and neutral words
    in the sentence and classifies it depending on which polarity is more represented.
    Words that do not appear in the lexicon are considered as neutral.

    :param sentence: a sentence whose polarity has to be classified.
    :param plot: if True, plot a visual representation of the sentence polarity.
    """
def demo_vader_instance(text) -> None:
    """
    Output polarity scores for a text using Vader approach.

    :param text: a text whose polarity has to be evaluated.
    """
def demo_vader_tweets(n_instances: Incomplete | None = None, output: Incomplete | None = None) -> None:
    """
    Classify 10000 positive and negative tweets using Vader approach.

    :param n_instances: the number of total tweets that have to be classified.
    :param output: the output file where results have to be reported.
    """
