import typing as t
from argcomplete import CompletionFinder

class StubModule:
    def __getattr__(self, attr: str) -> t.Any: ...
CompletionFinder = object

def get_argcomplete_cwords() -> t.List[str] | None:
    """Get current words prior to completion point

    This is normally done in the `argcomplete.CompletionFinder` constructor,
    but is exposed here to allow `traitlets` to follow dynamic code-paths such
    as determining whether to evaluate a subcommand.
    """
def increment_argcomplete_index() -> None:
    '''Assumes ``$_ARGCOMPLETE`` is set and `argcomplete` is importable

    Increment the index pointed to by ``$_ARGCOMPLETE``, which is used to
    determine which word `argcomplete` should start evaluating the command-line.
    This may be useful to "inform" `argcomplete` that we have already evaluated
    the first word as a subcommand.
    '''

class ExtendedCompletionFinder(CompletionFinder):
    """An extension of CompletionFinder which dynamically completes class-trait based options

    This finder adds a few functionalities:

    1. When completing options, it will add ``--Class.`` to the list of completions, for each
    class in `Application.classes` that could complete the current option.
    2. If it detects that we are currently trying to complete an option related to ``--Class.``,
    it will add the corresponding config traits of Class to the `ArgumentParser` instance,
    so that the traits' completers can be used.
    3. If there are any subcommands, they are added as completions for the first word

    Note that we are avoiding adding all config traits of all classes to the `ArgumentParser`,
    which would be easier but would add more runtime overhead and would also make completions
    appear more spammy.

    These changes do require using the internals of `argcomplete.CompletionFinder`.
    """
    config_classes: t.List[t.Any]
    subcommands: t.List[str]
    def match_class_completions(self, cword_prefix: str) -> t.List[t.Tuple[t.Any, str]]:
        """Match the word to be completed against our Configurable classes

        Check if cword_prefix could potentially match against --{class}. for any class
        in Application.classes.
        """
    def inject_class_to_parser(self, cls: t.Any) -> None:
        """Add dummy arguments to our ArgumentParser for the traits of this class

        The argparse-based loader currently does not actually add any class traits to
        the constructed ArgumentParser, only the flags & aliaes. In order to work nicely
        with argcomplete's completers functionality, this method adds dummy arguments
        of the form --Class.trait to the ArgumentParser instance.

        This method should be called selectively to reduce runtime overhead and to avoid
        spamming options across all of Application.classes.
        """
