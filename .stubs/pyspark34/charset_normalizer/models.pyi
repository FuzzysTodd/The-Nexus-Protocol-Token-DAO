from .constant import TOO_BIG_SEQUENCE as TOO_BIG_SEQUENCE
from .utils import iana_name as iana_name, is_multi_byte_encoding as is_multi_byte_encoding, unicode_range as unicode_range
from _typeshed import Incomplete
from typing import Any, Dict, Iterator, List, Tuple

class CharsetMatch:
    def __init__(self, payload: bytes, guessed_encoding: str, mean_mess_ratio: float, has_sig_or_bom: bool, languages: CoherenceMatches, decoded_payload: str | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool:
        """
        Implemented to make sorted available upon CharsetMatches items.
        """
    @property
    def multi_byte_usage(self) -> float: ...
    def add_submatch(self, other: CharsetMatch) -> None: ...
    @property
    def encoding(self) -> str: ...
    @property
    def encoding_aliases(self) -> List[str]:
        """
        Encoding name are known by many name, using this could help when searching for IBM855 when it's listed as CP855.
        """
    @property
    def bom(self) -> bool: ...
    @property
    def byte_order_mark(self) -> bool: ...
    @property
    def languages(self) -> List[str]:
        """
        Return the complete list of possible languages found in decoded sequence.
        Usually not really useful. Returned list may be empty even if 'language' property return something != 'Unknown'.
        """
    @property
    def language(self) -> str:
        '''
        Most probable language found in decoded sequence. If none were detected or inferred, the property will return
        "Unknown".
        '''
    @property
    def chaos(self) -> float: ...
    @property
    def coherence(self) -> float: ...
    @property
    def percent_chaos(self) -> float: ...
    @property
    def percent_coherence(self) -> float: ...
    @property
    def raw(self) -> bytes:
        """
        Original untouched bytes.
        """
    @property
    def submatch(self) -> List['CharsetMatch']: ...
    @property
    def has_submatch(self) -> bool: ...
    @property
    def alphabets(self) -> List[str]: ...
    @property
    def could_be_from_charset(self) -> List[str]:
        """
        The complete list of encoding that output the exact SAME str result and therefore could be the originating
        encoding.
        This list does include the encoding available in property 'encoding'.
        """
    def output(self, encoding: str = 'utf_8') -> bytes:
        """
        Method to get re-encoded bytes payload using given target encoding. Default to UTF-8.
        Any errors will be simply ignored by the encoder NOT replaced.
        """
    @property
    def fingerprint(self) -> str:
        """
        Retrieve the unique SHA256 computed using the transformed (re-encoded) payload. Not the original one.
        """

class CharsetMatches:
    """
    Container with every CharsetMatch items ordered by default from most probable to the less one.
    Act like a list(iterable) but does not implements all related methods.
    """
    def __init__(self, results: List[CharsetMatch] | None = None) -> None: ...
    def __iter__(self) -> Iterator[CharsetMatch]: ...
    def __getitem__(self, item: int | str) -> CharsetMatch:
        """
        Retrieve a single item either by its position or encoding name (alias may be used here).
        Raise KeyError upon invalid index or encoding not present in results.
        """
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def append(self, item: CharsetMatch) -> None:
        """
        Insert a single match. Will be inserted accordingly to preserve sort.
        Can be inserted as a submatch.
        """
    def best(self) -> CharsetMatch | None:
        """
        Simply return the first match. Strict equivalent to matches[0].
        """
    def first(self) -> CharsetMatch | None:
        """
        Redundant method, call the method best(). Kept for BC reasons.
        """
CoherenceMatch = Tuple[str, float]
CoherenceMatches = List[CoherenceMatch]

class CliDetectionResult:
    path: Incomplete
    unicode_path: Incomplete
    encoding: Incomplete
    encoding_aliases: Incomplete
    alternative_encodings: Incomplete
    language: Incomplete
    alphabets: Incomplete
    has_sig_or_bom: Incomplete
    chaos: Incomplete
    coherence: Incomplete
    is_preferred: Incomplete
    def __init__(self, path: str, encoding: str | None, encoding_aliases: List[str], alternative_encodings: List[str], language: str, alphabets: List[str], has_sig_or_bom: bool, chaos: float, coherence: float, unicode_path: str | None, is_preferred: bool) -> None: ...
    @property
    def __dict__(self) -> Dict[str, Any]: ...
    def to_json(self) -> str: ...
