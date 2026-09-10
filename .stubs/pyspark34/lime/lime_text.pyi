from . import explanation as explanation, lime_base as lime_base
from _typeshed import Incomplete

class TextDomainMapper(explanation.DomainMapper):
    """Maps feature ids to words or word-positions"""
    indexed_string: Incomplete
    def __init__(self, indexed_string) -> None:
        """Initializer.

        Args:
            indexed_string: lime_text.IndexedString, original string
        """
    def map_exp_ids(self, exp, positions: bool = False):
        """Maps ids to words or word-position strings.

        Args:
            exp: list of tuples [(id, weight), (id,weight)]
            positions: if True, also return word positions

        Returns:
            list of tuples (word, weight), or (word_positions, weight) if
            examples: ('bad', 1) or ('bad_3-6-12', 1)
        """
    def visualize_instance_html(self, exp, label, div_name, exp_object_name, text: bool = True, opacity: bool = True):
        """Adds text with highlighted words to visualization.

        Args:
             exp: list of tuples [(id, weight), (id,weight)]
             label: label id (integer)
             div_name: name of div object to be used for rendering(in js)
             exp_object_name: name of js explanation object
             text: if False, return empty
             opacity: if True, fade colors according to weight
        """

class IndexedString:
    """String with various indexes."""
    raw: Incomplete
    mask_string: Incomplete
    as_list: Incomplete
    as_np: Incomplete
    string_start: Incomplete
    inverse_vocab: Incomplete
    positions: Incomplete
    bow: Incomplete
    def __init__(self, raw_string, split_expression: str = '\\W+', bow: bool = True, mask_string: Incomplete | None = None) -> None:
        """Initializer.

        Args:
            raw_string: string with raw text in it
            split_expression: Regex string or callable. If regex string, will be used with re.split.
                If callable, the function should return a list of tokens.
            bow: if True, a word is the same everywhere in the text - i.e. we
                 will index multiple occurrences of the same word. If False,
                 order matters, so that the same word will have different ids
                 according to position.
            mask_string: If not None, replace words with this if bow=False
                if None, default value is UNKWORDZ
        """
    def raw_string(self):
        """Returns the original raw string"""
    def num_words(self):
        """Returns the number of tokens in the vocabulary for this document."""
    def word(self, id_):
        """Returns the word that corresponds to id_ (int)"""
    def string_position(self, id_):
        """Returns a np array with indices to id_ (int) occurrences"""
    def inverse_removing(self, words_to_remove):
        """Returns a string after removing the appropriate words.

        If self.bow is false, replaces word with UNKWORDZ instead of removing
        it.

        Args:
            words_to_remove: list of ids (ints) to remove

        Returns:
            original raw string with appropriate words removed.
        """

class IndexedCharacters:
    """String with various indexes."""
    raw: Incomplete
    as_list: Incomplete
    as_np: Incomplete
    mask_string: Incomplete
    string_start: Incomplete
    inverse_vocab: Incomplete
    positions: Incomplete
    bow: Incomplete
    def __init__(self, raw_string, bow: bool = True, mask_string: Incomplete | None = None) -> None:
        """Initializer.

        Args:
            raw_string: string with raw text in it
            bow: if True, a char is the same everywhere in the text - i.e. we
                 will index multiple occurrences of the same character. If False,
                 order matters, so that the same word will have different ids
                 according to position.
            mask_string: If not None, replace characters with this if bow=False
                if None, default value is chr(0)
        """
    def raw_string(self):
        """Returns the original raw string"""
    def num_words(self):
        """Returns the number of tokens in the vocabulary for this document."""
    def word(self, id_):
        """Returns the word that corresponds to id_ (int)"""
    def string_position(self, id_):
        """Returns a np array with indices to id_ (int) occurrences"""
    def inverse_removing(self, words_to_remove):
        """Returns a string after removing the appropriate words.

        If self.bow is false, replaces word with UNKWORDZ instead of removing
        it.

        Args:
            words_to_remove: list of ids (ints) to remove

        Returns:
            original raw string with appropriate words removed.
        """

class LimeTextExplainer:
    """Explains text classifiers.
       Currently, we are using an exponential kernel on cosine distance, and
       restricting explanations to words that are present in documents."""
    random_state: Incomplete
    base: Incomplete
    class_names: Incomplete
    vocabulary: Incomplete
    feature_selection: Incomplete
    bow: Incomplete
    mask_string: Incomplete
    split_expression: Incomplete
    char_level: Incomplete
    def __init__(self, kernel_width: int = 25, kernel: Incomplete | None = None, verbose: bool = False, class_names: Incomplete | None = None, feature_selection: str = 'auto', split_expression: str = '\\W+', bow: bool = True, mask_string: Incomplete | None = None, random_state: Incomplete | None = None, char_level: bool = False) -> None:
        """Init function.

        Args:
            kernel_width: kernel width for the exponential kernel.
            kernel: similarity kernel that takes euclidean distances and kernel
                width as input and outputs weights in (0,1). If None, defaults to
                an exponential kernel.
            verbose: if true, print local prediction values from linear model
            class_names: list of class names, ordered according to whatever the
                classifier is using. If not present, class names will be '0',
                '1', ...
            feature_selection: feature selection method. can be
                'forward_selection', 'lasso_path', 'none' or 'auto'.
                See function 'explain_instance_with_data' in lime_base.py for
                details on what each of the options does.
            split_expression: Regex string or callable. If regex string, will be used with re.split.
                If callable, the function should return a list of tokens.
            bow: if True (bag of words), will perturb input data by removing
                all occurrences of individual words or characters.
                Explanations will be in terms of these words. Otherwise, will
                explain in terms of word-positions, so that a word may be
                important the first time it appears and unimportant the second.
                Only set to false if the classifier uses word order in some way
                (bigrams, etc), or if you set char_level=True.
            mask_string: String used to mask tokens or characters if bow=False
                if None, will be 'UNKWORDZ' if char_level=False, chr(0)
                otherwise.
            random_state: an integer or numpy.RandomState that will be used to
                generate random numbers. If None, the random state will be
                initialized using the internal numpy seed.
            char_level: an boolean identifying that we treat each character
                as an independent occurence in the string
        """
    def explain_instance(self, text_instance, classifier_fn, labels=(1,), top_labels: Incomplete | None = None, num_features: int = 10, num_samples: int = 5000, distance_metric: str = 'cosine', model_regressor: Incomplete | None = None):
        """Generates explanations for a prediction.

        First, we generate neighborhood data by randomly hiding features from
        the instance (see __data_labels_distance_mapping). We then learn
        locally weighted linear models on this neighborhood data to explain
        each of the classes in an interpretable way (see lime_base.py).

        Args:
            text_instance: raw text string to be explained.
            classifier_fn: classifier prediction probability function, which
                takes a list of d strings and outputs a (d, k) numpy array with
                prediction probabilities, where k is the number of classes.
                For ScikitClassifiers , this is classifier.predict_proba.
            labels: iterable with labels to be explained.
            top_labels: if not None, ignore labels and produce explanations for
                the K labels with highest prediction probabilities, where K is
                this parameter.
            num_features: maximum number of features present in explanation
            num_samples: size of the neighborhood to learn the linear model
            distance_metric: the distance metric to use for sample weighting,
                defaults to cosine similarity
            model_regressor: sklearn regressor to use in explanation. Defaults
            to Ridge regression in LimeBase. Must have model_regressor.coef_
            and 'sample_weight' as a parameter to model_regressor.fit()
        Returns:
            An Explanation object (see explanation.py) with the corresponding
            explanations.
        """
