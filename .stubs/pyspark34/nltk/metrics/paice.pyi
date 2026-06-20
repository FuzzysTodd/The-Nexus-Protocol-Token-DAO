from _typeshed import Incomplete

def get_words_from_dictionary(lemmas):
    """
    Get original set of words used for analysis.

    :param lemmas: A dictionary where keys are lemmas and values are sets
        or lists of words corresponding to that lemma.
    :type lemmas: dict(str): list(str)
    :return: Set of words that exist as values in the dictionary
    :rtype: set(str)
    """

class Paice:
    """Class for storing lemmas, stems and evaluation metrics."""
    lemmas: Incomplete
    stems: Incomplete
    coords: Incomplete
    errt: Incomplete
    def __init__(self, lemmas, stems) -> None:
        """
        :param lemmas: A dictionary where keys are lemmas and values are sets
            or lists of words corresponding to that lemma.
        :param stems: A dictionary where keys are stems and values are sets
            or lists of words corresponding to that stem.
        :type lemmas: dict(str): list(str)
        :type stems: dict(str): set(str)
        """
    def update(self) -> None:
        """Update statistics after lemmas and stems have been set."""

def demo() -> None:
    """Demonstration of the module."""
