from . import NO_CONVERT as NO_CONVERT, __version__ as __version__, read as read, reads as reads
from _typeshed import Incomplete
from collections.abc import Generator
from jupyter_core.application import JupyterApp
from traitlets.config import LoggingConfigurable

def adapt_datetime_iso(val):
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object."""

algorithms_set: Incomplete
algorithms: Incomplete

class SignatureStore:
    """Base class for a signature store."""
    def store_signature(self, digest, algorithm) -> None:
        """Implement in subclass to store a signature.

        Should not raise if the signature is already stored.
        """
    def check_signature(self, digest, algorithm) -> None:
        """Implement in subclass to check if a signature is known.

        Return True for a known signature, False for unknown.
        """
    def remove_signature(self, digest, algorithm) -> None:
        """Implement in subclass to delete a signature.

        Should not raise if the signature is not stored.
        """
    def close(self) -> None:
        """Close any open connections this store may use.

        If the store maintains any open connections (e.g. to a database),
        they should be closed.
        """

class MemorySignatureStore(SignatureStore):
    """Non-persistent storage of signatures in memory."""
    cache_size: int
    data: Incomplete
    def __init__(self) -> None:
        """Initialize a memory signature store."""
    def store_signature(self, digest, algorithm) -> None:
        """Store a signature."""
    def check_signature(self, digest, algorithm):
        """Check a signature."""
    def remove_signature(self, digest, algorithm) -> None:
        """Remove a signature."""

class SQLiteSignatureStore(SignatureStore, LoggingConfigurable):
    """Store signatures in an SQLite database."""
    cache_size: Incomplete
    db_file: Incomplete
    db: Incomplete
    def __init__(self, db_file, **kwargs) -> None:
        """Initialize a sql signature store."""
    def close(self) -> None:
        """Close the db."""
    def init_db(self, db) -> None:
        """Initialize the db."""
    def store_signature(self, digest, algorithm) -> None:
        """Store a signature in the db."""
    def check_signature(self, digest, algorithm):
        """Check a signature against the db."""
    def remove_signature(self, digest, algorithm) -> None:
        """Remove a signature from the db."""
    def cull_db(self) -> None:
        """Cull oldest 25% of the trusted signatures when the size limit is reached"""

def yield_everything(obj) -> Generator[Incomplete, Incomplete, None]:
    """Yield every item in a container as bytes

    Allows any JSONable object to be passed to an HMAC digester
    without having to serialize the whole thing.
    """
def yield_code_cells(nb) -> Generator[Incomplete, None, None]:
    """Iterator that yields all cells in a notebook

    nbformat version independent
    """
def signature_removed(nb) -> Generator[None, None, None]:
    """Context manager for operating on a notebook with its signature removed

    Used for excluding the previous signature when computing a notebook's signature.
    """

class NotebookNotary(LoggingConfigurable):
    """A class for computing and verifying notebook signatures."""
    data_dir: Incomplete
    store_factory: Incomplete
    db_file: Incomplete
    algorithm: Incomplete
    digestmod: Incomplete
    secret_file: Incomplete
    secret: Incomplete
    store: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize the notary."""
    def compute_signature(self, nb):
        """Compute a notebook's signature

        by hashing the entire contents of the notebook via HMAC digest.
        """
    def check_signature(self, nb):
        """Check a notebook's stored signature

        If a signature is stored in the notebook's metadata,
        a new signature is computed and compared with the stored value.

        Returns True if the signature is found and matches, False otherwise.

        The following conditions must all be met for a notebook to be trusted:
        - a signature is stored in the form 'scheme:hexdigest'
        - the stored scheme matches the requested scheme
        - the requested scheme is available from hashlib
        - the computed hash from notebook_signature matches the stored hash
        """
    def sign(self, nb) -> None:
        """Sign a notebook, indicating that its output is trusted on this machine

        Stores hash algorithm and hmac digest in a local database of trusted notebooks.
        """
    def unsign(self, nb) -> None:
        """Ensure that a notebook is untrusted

        by removing its signature from the trusted database, if present.
        """
    def mark_cells(self, nb, trusted) -> None:
        """Mark cells as trusted if the notebook's signature can be verified

        Sets ``cell.metadata.trusted = True | False`` on all code cells,
        depending on the *trusted* parameter. This will typically be the return
        value from ``self.check_signature(nb)``.

        This function is the inverse of check_cells
        """
    def check_cells(self, nb):
        """Return whether all code cells are trusted.

        A cell is trusted if the 'trusted' field in its metadata is truthy, or
        if it has no potentially unsafe outputs.
        If there are no code cells, return True.

        This function is the inverse of mark_cells.
        """

trust_flags: dict

class TrustNotebookApp(JupyterApp):
    """An application for handling notebook trust."""
    version = __version__
    description: str
    examples: str
    flags = trust_flags
    reset: Incomplete
    notary: Incomplete
    def sign_notebook_file(self, notebook_path) -> None:
        """Sign a notebook from the filesystem"""
    def sign_notebook(self, nb, notebook_path: str = '<stdin>') -> None:
        """Sign a notebook that's been loaded"""
    def generate_new_key(self) -> None:
        """Generate a new notebook signature key"""
    def start(self) -> None:
        """Start the trust notebook app."""

main: Incomplete
