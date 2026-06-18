from _typeshed import Incomplete
from collections.abc import Generator
from unittest import TestCase

def isstr(s): ...

class NotebookTest(TestCase):
    """Validate a notebook. All code cells are executed in order. The output is either checked
    for errors (if no reference output is present), or is compared against expected output.


    Useful references:
    http://nbformat.readthedocs.org/en/latest/format_description.html
    http://jupyter-client.readthedocs.org/en/latest/messaging.html
"""
    IGNORE_TYPES: Incomplete
    STRIP_KEYS: Incomplete
    NBFORMAT_VERSION: int
    def dump_canonical(self, obj): ...
    def scrub_outputs(self, outputs) -> Generator[Incomplete, None, Incomplete]:
        """
        remove all scrubs from output data and text
        """
    def strip_keys(self, d):
        """
        remove keys from STRIP_KEYS to ensure comparability
        """
    def sanitize_cell(self, cell):
        """
        remove non-reproducible things
        """
    def transform_message(self, msg, expected):
        """
        transform a message into something like the notebook
        """
    def should_continue(self, msg):
        """
        determine whether the current message is the last for this cell
        """
