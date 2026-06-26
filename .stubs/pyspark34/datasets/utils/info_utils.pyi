import enum
from .. import config as config
from .logging import get_logger as get_logger
from _typeshed import Incomplete

logger: Incomplete

class VerificationMode(enum.Enum):
    """`Enum` that specifies which verification checks to run.

    The default mode is `BASIC_CHECKS`, which will perform only rudimentary checks to avoid slowdowns
    when generating/downloading a dataset for the first time.

    The verification modes:

    |                           | Verification checks                                                           |
    |---------------------------|------------------------------------------------------------------------------ |
    | `ALL_CHECKS`              | Split checks, uniqueness of the keys yielded in case of the GeneratorBuilder  |
    |                           | and the validity (number of files, checksums, etc.) of downloaded files       |
    | `BASIC_CHECKS` (default)  | Same as `ALL_CHECKS` but without checking downloaded files                    |
    | `NO_CHECKS`               | None                                                                          |

    """
    ALL_CHECKS: str
    BASIC_CHECKS: str
    NO_CHECKS: str

class ChecksumVerificationException(Exception):
    """Exceptions during checksums verifications of downloaded files."""
class UnexpectedDownloadedFile(ChecksumVerificationException):
    """Some downloaded files were not expected."""
class ExpectedMoreDownloadedFiles(ChecksumVerificationException):
    """Some files were supposed to be downloaded but were not."""
class NonMatchingChecksumError(ChecksumVerificationException):
    """The downloaded file checksum don't match the expected checksum."""

def verify_checksums(expected_checksums: dict | None, recorded_checksums: dict, verification_name: Incomplete | None = None): ...

class SplitsVerificationException(Exception):
    """Exceptions during splis verifications"""
class UnexpectedSplits(SplitsVerificationException):
    """The expected splits of the downloaded file is missing."""
class ExpectedMoreSplits(SplitsVerificationException):
    """Some recorded splits are missing."""
class NonMatchingSplitsSizesError(SplitsVerificationException):
    """The splits sizes don't match the expected splits sizes."""

def verify_splits(expected_splits: dict | None, recorded_splits: dict): ...
def get_size_checksum_dict(path: str, record_checksum: bool = True) -> dict:
    """Compute the file size and the sha256 checksum of a file"""
def is_small_dataset(dataset_size):
    """Check if `dataset_size` is smaller than `config.IN_MEMORY_MAX_SIZE`.

    Args:
        dataset_size (int): Dataset size in bytes.

    Returns:
        bool: Whether `dataset_size` is smaller than `config.IN_MEMORY_MAX_SIZE`.
    """
