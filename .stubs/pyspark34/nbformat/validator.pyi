from ._imports import import_item as import_item
from .corpus.words import generate_corpus_id as generate_corpus_id
from .json_compat import ValidationError as ValidationError, get_current_validator as get_current_validator
from .reader import get_version as get_version
from .warnings import DuplicateCellId as DuplicateCellId, MissingIDFieldWarning as MissingIDFieldWarning
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Tuple

validators: Incomplete

def get_validator(version: Incomplete | None = None, version_minor: Incomplete | None = None, relax_add_props: bool = False, name: Incomplete | None = None):
    """Load the JSON schema into a Validator"""
def isvalid(nbjson, ref: Incomplete | None = None, version: Incomplete | None = None, version_minor: Incomplete | None = None):
    """Checks whether the given notebook JSON conforms to the current
    notebook format schema. Returns True if the JSON is valid, and
    False otherwise.

    To see the individual errors that were encountered, please use the
    `validate` function instead.
    """

class NotebookValidationError(ValidationError):
    """Schema ValidationError with truncated representation

    to avoid massive verbose tracebacks.
    """
    original: Incomplete
    ref: Incomplete
    message: Incomplete
    def __init__(self, original, ref: Incomplete | None = None) -> None:
        """Initialize the error class."""
    def __getattr__(self, key):
        """Get an attribute from the error."""
    def __unicode__(self):
        """Custom str for validation errors

        avoids dumping full schema and notebook to logs
        """

def better_validation_error(error, version, version_minor):
    """Get better ValidationError on oneOf failures

    oneOf errors aren't informative.
    if it's a cell type or output_type error,
    try validating directly based on the type for a better error message
    """
def normalize(nbdict: Any, version: int | None = None, version_minor: int | None = None, *, relax_add_props: bool = False, strip_invalid_metadata: bool = False) -> Tuple[int, Any]:
    """
    Normalise a notebook prior to validation.

    This tries to implement a couple of normalisation steps to standardise
    notebooks and make validation easier.

    You should in general not rely on this function and make sure the notebooks
    that reach nbformat are already in a normal form. If not you likely have a bug,
    and may have security issues.

    Parameters
    ----------
    nbdict : dict
        notebook document
    version : int
    version_minor : int
    relax_add_props : bool
        Whether to allow extra property in the Json schema validating the
        notebook.
    strip_invalid_metadata : bool
        Whether to strip metadata that does not exist in the Json schema when
        validating the notebook.

    Returns
    -------
    changes : int
        number of changes in the notebooks
    notebook : dict
        deep-copy of the original object with relevant changes.

    """
def validate(nbdict: Any = None, ref: str | None = None, version: int | None = None, version_minor: int | None = None, relax_add_props: bool = False, nbjson: Any = None, repair_duplicate_cell_ids: bool = ..., strip_invalid_metadata: bool = ...) -> None:
    '''Checks whether the given notebook dict-like object
    conforms to the relevant notebook format schema.

    Parameters
    ----------
    nbdict : dict
        notebook document
    ref : optional, str
        reference to the subset of the schema we want to validate against.
        for example ``"markdown_cell"``, `"code_cell"` ....
    version : int
    version_minor : int
    relax_add_props : bool
        Wether to allow extra properties in the JSON schema validating the notebook.
        When True, all known fields are validated, but unknown fields are ignored.
    nbjson
    repair_duplicate_cell_ids : bool
        Deprecated since 5.5.0 - will be removed in the future.
    strip_invalid_metadata : bool
        Deprecated since 5.5.0 - will be removed in the future.

    Returns
    -------
    None

    Raises
    ------
    ValidationError if not valid.

    Notes
    -----
    Prior to Nbformat 5.5.0 the `validate` and `isvalid` method would silently
    try to fix invalid notebook and mutate arguments. This behavior is deprecated
    and will be removed in a near future.

    Please explicitly call `normalize` if you need to normalize notebooks.
    '''
def iter_validate(nbdict: Incomplete | None = None, ref: Incomplete | None = None, version: Incomplete | None = None, version_minor: Incomplete | None = None, relax_add_props: bool = False, nbjson: Incomplete | None = None, strip_invalid_metadata: bool = False) -> Generator[Incomplete, None, None]:
    """Checks whether the given notebook dict-like object conforms to the
    relevant notebook format schema.

    Returns a generator of all ValidationErrors if not valid.

    Notes
    -----
    To fix: For security reasons, this function should *never* mutate its `nbdict` argument, and
    should *never* try to validate a mutated or modified version of its notebook.

    """
