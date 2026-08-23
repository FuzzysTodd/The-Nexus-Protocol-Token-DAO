from wandb import util as util
from wandb.plots.utils import deprecation_notice as deprecation_notice, encode_labels as encode_labels, test_missing as test_missing, test_types as test_types

def named_entity(docs):
    """
    Adds support for spaCy's entity visualizer, which highlights named
        entities and their labels in a text.

    Arguments:
     docs (list, Doc, Span): Document(s) to visualize.

    Returns:
     Nothing. To see plots, go to your W&B run page.

    Example:
     wandb.log({'NER': wandb.plots.NER(docs=doc)})
    """
