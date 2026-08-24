import datetime
from typing import Any, Callable, Dict, Type

__all__ = ['pydantic_encoder', 'custom_pydantic_encoder', 'timedelta_isoformat']

def pydantic_encoder(obj: Any) -> Any: ...
def custom_pydantic_encoder(type_encoders: Dict[Any, Callable[[Type[Any]], Any]], obj: Any) -> Any: ...
def timedelta_isoformat(td: datetime.timedelta) -> str:
    """
    ISO 8601 encoding for Python timedelta object.
    """
