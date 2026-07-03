from _typeshed import Incomplete
from typing import List

class InputExample:
    """
    Structure for one input example with texts, the label and a unique id
    """
    guid: Incomplete
    texts: Incomplete
    label: Incomplete
    def __init__(self, guid: str = '', texts: List[str] = None, label: int | float = 0) -> None:
        """
        Creates one InputExample with the given texts, guid and label


        :param guid
            id for the example
        :param texts
            the texts for the example. Note, str.strip() is called on the texts
        :param label
            the label for the example
        """
