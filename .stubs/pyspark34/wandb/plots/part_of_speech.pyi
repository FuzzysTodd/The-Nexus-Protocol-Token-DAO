from wandb import util as util
from wandb.plots.utils import deprecation_notice as deprecation_notice, encode_labels as encode_labels, test_missing as test_missing, test_types as test_types

def part_of_speech(docs):
    """
    Adds support for spaCy's dependency visualizer which shows
        part-of-speech tags and syntactic dependencies.

    Arguments:
     docs (list, Doc, Span): Document(s) to visualize.

    Returns:
     Nothing. To see plots, go to your W&B run page.

    Example:
     wandb.log({'part_of_speech': wandb.plots.POS(docs=doc)})
    """
