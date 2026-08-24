from charset_normalizer import from_fp as from_fp
from charset_normalizer.models import CliDetectionResult as CliDetectionResult
from charset_normalizer.version import __version__ as __version__
from typing import List

def query_yes_no(question: str, default: str = 'yes') -> bool:
    '''Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".

    Credit goes to (c) https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
    '''
def cli_detect(argv: List[str] | None = None) -> int:
    """
    CLI assistant using ARGV and ArgumentParser
    :param argv:
    :return: 0 if everything is fine, anything else equal trouble
    """
