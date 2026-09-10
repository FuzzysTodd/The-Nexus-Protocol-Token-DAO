from .cd import coherence_ratio as coherence_ratio, encoding_languages as encoding_languages, mb_encoding_languages as mb_encoding_languages, merge_coherence_ratios as merge_coherence_ratios
from .constant import IANA_SUPPORTED as IANA_SUPPORTED, TOO_BIG_SEQUENCE as TOO_BIG_SEQUENCE, TOO_SMALL_SEQUENCE as TOO_SMALL_SEQUENCE, TRACE as TRACE
from .md import mess_ratio as mess_ratio
from .models import CharsetMatch as CharsetMatch, CharsetMatches as CharsetMatches
from .utils import any_specified_encoding as any_specified_encoding, cut_sequence_chunks as cut_sequence_chunks, iana_name as iana_name, identify_sig_or_bom as identify_sig_or_bom, is_cp_similar as is_cp_similar, is_multi_byte_encoding as is_multi_byte_encoding, should_strip_sig_or_bom as should_strip_sig_or_bom
from _typeshed import Incomplete
from os import PathLike
from typing import BinaryIO, List

logger: Incomplete
explain_handler: Incomplete

def from_bytes(sequences: bytes | bytearray, steps: int = 5, chunk_size: int = 512, threshold: float = 0.2, cp_isolation: List[str] | None = None, cp_exclusion: List[str] | None = None, preemptive_behaviour: bool = True, explain: bool = False, language_threshold: float = 0.1, enable_fallback: bool = True) -> CharsetMatches:
    """
    Given a raw bytes sequence, return the best possibles charset usable to render str objects.
    If there is no results, it is a strong indicator that the source is binary/not text.
    By default, the process will extract 5 blocks of 512o each to assess the mess and coherence of a given sequence.
    And will give up a particular code page after 20% of measured mess. Those criteria are customizable at will.

    The preemptive behavior DOES NOT replace the traditional detection workflow, it prioritize a particular code page
    but never take it for granted. Can improve the performance.

    You may want to focus your attention to some code page or/and not others, use cp_isolation and cp_exclusion for that
    purpose.

    This function will strip the SIG in the payload/sequence every time except on UTF-16, UTF-32.
    By default the library does not setup any handler other than the NullHandler, if you choose to set the 'explain'
    toggle to True it will alter the logger configuration to add a StreamHandler that is suitable for debugging.
    Custom logging format and handler can be set manually.
    """
def from_fp(fp: BinaryIO, steps: int = 5, chunk_size: int = 512, threshold: float = 0.2, cp_isolation: List[str] | None = None, cp_exclusion: List[str] | None = None, preemptive_behaviour: bool = True, explain: bool = False, language_threshold: float = 0.1, enable_fallback: bool = True) -> CharsetMatches:
    """
    Same thing than the function from_bytes but using a file pointer that is already ready.
    Will not close the file pointer.
    """
def from_path(path: str | bytes | PathLike, steps: int = 5, chunk_size: int = 512, threshold: float = 0.2, cp_isolation: List[str] | None = None, cp_exclusion: List[str] | None = None, preemptive_behaviour: bool = True, explain: bool = False, language_threshold: float = 0.1, enable_fallback: bool = True) -> CharsetMatches:
    """
    Same thing than the function from_bytes but with one extra step. Opening and reading given file path in binary mode.
    Can raise IOError.
    """
def is_binary(fp_or_path_or_payload: PathLike | str | BinaryIO | bytes, steps: int = 5, chunk_size: int = 512, threshold: float = 0.2, cp_isolation: List[str] | None = None, cp_exclusion: List[str] | None = None, preemptive_behaviour: bool = True, explain: bool = False, language_threshold: float = 0.1, enable_fallback: bool = False) -> bool:
    """
    Detect if the given input (file, bytes, or path) points to a binary file. aka. not a string.
    Based on the same main heuristic algorithms and default kwargs at the sole exception that fallbacks match
    are disabled to be stricter around ASCII-compatible but unlikely to be a string.
    """
