import types
from ._typing import _T
from _typeshed import Incomplete
from sklearn.preprocessing import LabelEncoder
from typing import Any, Dict, List, Sequence

def py_str(x: bytes) -> str:
    """convert c string back to python string"""
def lazy_isinstance(instance: Any, module: str, name: str) -> bool:
    """Use string representation to identify a type."""

PANDAS_INSTALLED: bool
MultiIndex = object
DataFrame = object
Series = object
SKLEARN_INSTALLED: bool
XGBModelBase = object
XGBClassifierBase = object
XGBRegressorBase = object
LabelEncoder = object

def is_cudf_available() -> bool:
    """Check cuDF package available or not"""

class XGBoostLabelEncoder(LabelEncoder):
    """Label encoder with JSON serialization methods."""
    def to_json(self) -> Dict:
        """Returns a JSON compatible dictionary"""
    classes_: Incomplete
    def from_json(self, doc: Dict) -> None:
        """Load the encoder back from a JSON compatible dict."""
scipy_csr = object

def concat(value: Sequence[_T]) -> _T:
    """Concatenate row-wise."""

class LazyLoader(types.ModuleType):
    """Lazily import a module, mainly to avoid pulling in large dependencies."""
    module: Incomplete
    def __init__(self, local_name: str, parent_module_globals: Dict, name: str, warning: str | None = None) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def __dir__(self) -> List[str]: ...
