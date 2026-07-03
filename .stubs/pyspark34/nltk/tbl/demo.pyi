from _typeshed import Incomplete
from nltk.corpus import treebank as treebank
from nltk.tag import BrillTaggerTrainer as BrillTaggerTrainer, RegexpTagger as RegexpTagger, UnigramTagger as UnigramTagger
from nltk.tag.brill import Pos as Pos, Word as Word
from nltk.tbl import Template as Template, error_list as error_list

def demo() -> None:
    """
    Run a demo with defaults. See source comments for details,
    or docstrings of any of the more specific demo_* functions.
    """
def demo_repr_rule_format() -> None:
    '''
    Exemplify repr(Rule) (see also str(Rule) and Rule.format("verbose"))
    '''
def demo_str_rule_format() -> None:
    '''
    Exemplify repr(Rule) (see also str(Rule) and Rule.format("verbose"))
    '''
def demo_verbose_rule_format() -> None:
    '''
    Exemplify Rule.format("verbose")
    '''
def demo_multiposition_feature() -> None:
    """
    The feature/s of a template takes a list of positions
    relative to the current word where the feature should be
    looked for, conceptually joined by logical OR. For instance,
    Pos([-1, 1]), given a value V, will hold whenever V is found
    one step to the left and/or one step to the right.

    For contiguous ranges, a 2-arg form giving inclusive end
    points can also be used: Pos(-3, -1) is the same as the arg
    below.
    """
def demo_multifeature_template() -> None:
    """
    Templates can have more than a single feature.
    """
def demo_template_statistics() -> None:
    """
    Show aggregate statistics per template. Little used templates are
    candidates for deletion, much used templates may possibly be refined.

    Deleting unused templates is mostly about saving time and/or space:
    training is basically O(T) in the number of templates T
    (also in terms of memory usage, which often will be the limiting factor).
    """
def demo_generated_templates() -> None:
    """
    Template.expand and Feature.expand are class methods facilitating
    generating large amounts of templates. See their documentation for
    details.

    Note: training with 500 templates can easily fill all available
    even on relatively small corpora
    """
def demo_learning_curve() -> None:
    """
    Plot a learning curve -- the contribution on tagging accuracy of
    the individual rules.
    Note: requires matplotlib
    """
def demo_error_analysis() -> None:
    """
    Writes a file with context for each erroneous word after tagging testing data
    """
def demo_serialize_tagger() -> None:
    """
    Serializes the learned tagger to a file in pickle format; reloads it
    and validates the process.
    """
def demo_high_accuracy_rules() -> None:
    """
    Discard rules with low accuracy. This may hurt performance a bit,
    but will often produce rules which are more interesting read to a human.
    """
def postag(templates: Incomplete | None = None, tagged_data: Incomplete | None = None, num_sents: int = 1000, max_rules: int = 300, min_score: int = 3, min_acc: Incomplete | None = None, train: float = 0.8, trace: int = 3, randomize: bool = False, ruleformat: str = 'str', incremental_stats: bool = False, template_stats: bool = False, error_output: Incomplete | None = None, serialize_output: Incomplete | None = None, learning_curve_output: Incomplete | None = None, learning_curve_take: int = 300, baseline_backoff_tagger: Incomplete | None = None, separate_baseline_data: bool = False, cache_baseline_tagger: Incomplete | None = None) -> None:
    '''
    Brill Tagger Demonstration
    :param templates: how many sentences of training and testing data to use
    :type templates: list of Template

    :param tagged_data: maximum number of rule instances to create
    :type tagged_data: C{int}

    :param num_sents: how many sentences of training and testing data to use
    :type num_sents: C{int}

    :param max_rules: maximum number of rule instances to create
    :type max_rules: C{int}

    :param min_score: the minimum score for a rule in order for it to be considered
    :type min_score: C{int}

    :param min_acc: the minimum score for a rule in order for it to be considered
    :type min_acc: C{float}

    :param train: the fraction of the the corpus to be used for training (1=all)
    :type train: C{float}

    :param trace: the level of diagnostic tracing output to produce (0-4)
    :type trace: C{int}

    :param randomize: whether the training data should be a random subset of the corpus
    :type randomize: C{bool}

    :param ruleformat: rule output format, one of "str", "repr", "verbose"
    :type ruleformat: C{str}

    :param incremental_stats: if true, will tag incrementally and collect stats for each rule (rather slow)
    :type incremental_stats: C{bool}

    :param template_stats: if true, will print per-template statistics collected in training and (optionally) testing
    :type template_stats: C{bool}

    :param error_output: the file where errors will be saved
    :type error_output: C{string}

    :param serialize_output: the file where the learned tbl tagger will be saved
    :type serialize_output: C{string}

    :param learning_curve_output: filename of plot of learning curve(s) (train and also test, if available)
    :type learning_curve_output: C{string}

    :param learning_curve_take: how many rules plotted
    :type learning_curve_take: C{int}

    :param baseline_backoff_tagger: the file where rules will be saved
    :type baseline_backoff_tagger: tagger

    :param separate_baseline_data: use a fraction of the training data exclusively for training baseline
    :type separate_baseline_data: C{bool}

    :param cache_baseline_tagger: cache baseline tagger to this file (only interesting as a temporary workaround to get
                                  deterministic output from the baseline unigram tagger between python versions)
    :type cache_baseline_tagger: C{string}


    Note on separate_baseline_data: if True, reuse training data both for baseline and rule learner. This
    is fast and fine for a demo, but is likely to generalize worse on unseen data.
    Also cannot be sensibly used for learning curves on training data (the baseline will be artificially high).
    '''

NN_CD_TAGGER: Incomplete
REGEXP_TAGGER: Incomplete

def corpus_size(seqs): ...
