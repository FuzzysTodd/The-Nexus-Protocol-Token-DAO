from pip._vendor.packaging.version import parse as parse

DEPRECATION_MSG_PREFIX: str

class PipDeprecationWarning(Warning): ...

def install_warning_logger() -> None: ...
def deprecated(*, reason: str, replacement: str | None, gone_in: str | None, feature_flag: str | None = None, issue: int | None = None) -> None:
    """Helper to deprecate existing functionality.

    reason:
        Textual reason shown to the user about why this functionality has
        been deprecated. Should be a complete sentence.
    replacement:
        Textual suggestion shown to the user about what alternative
        functionality they can use.
    gone_in:
        The version of pip does this functionality should get removed in.
        Raises an error if pip's current version is greater than or equal to
        this.
    feature_flag:
        Command-line flag of the form --use-feature={feature_flag} for testing
        upcoming functionality.
    issue:
        Issue number on the tracker that would serve as a useful place for
        users to find related discussion and provide feedback.
    """
