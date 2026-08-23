from ..readers import InputExample as InputExample
from _typeshed import Incomplete
from torch.utils.data import IterableDataset
from typing import List

logger: Incomplete

class SentenceLabelDataset(IterableDataset):
    """
    This dataset can be used for some specific Triplet Losses like BATCH_HARD_TRIPLET_LOSS which requires
    multiple examples with the same label in a batch.

    It draws n consecutive, random and unique samples from one label at a time. This is repeated for each label.

    Labels with fewer than n unique samples are ignored.
    This also applied to drawing without replacement, once less than n samples remain for a label, it is skipped.

    This *DOES NOT* check if there are more labels than the batch is large or if the batch size is divisible
    by the samples drawn per label.
    """
    samples_per_label: Incomplete
    grouped_inputs: Incomplete
    groups_right_border: Incomplete
    label_range: Incomplete
    with_replacement: Incomplete
    def __init__(self, examples: List[InputExample], samples_per_label: int = 2, with_replacement: bool = False) -> None:
        """
        Creates a LabelSampler for a SentenceLabelDataset.

        :param examples:
            a list with InputExamples
        :param samples_per_label:
            the number of consecutive, random and unique samples drawn per label. Batch size should be a multiple of samples_per_label
        :param with_replacement:
            if this is True, then each sample is drawn at most once (depending on the total number of samples per label).
            if this is False, then one sample can be drawn in multiple draws, but still not multiple times in the same
            drawing.
        """
    def __iter__(self): ...
    def __len__(self) -> int: ...
