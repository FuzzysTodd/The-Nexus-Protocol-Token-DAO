from .error_reporting import ValidationError as ValidationError
from _typeshed import Incomplete
from typing import Mapping, TypeVar

T = TypeVar('T', bound=Mapping)

class RedefiningStaticFieldAsDynamic(ValidationError):
    """According to PEP 621:

    Build back-ends MUST raise an error if the metadata specifies a field
    statically as well as being listed in dynamic.
    """

def validate_project_dynamic(pyproject: T) -> T: ...

EXTRA_VALIDATIONS: Incomplete
