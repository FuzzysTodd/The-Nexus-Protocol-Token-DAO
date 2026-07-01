import http
import logging
from _typeshed import Incomplete
from typing import List, Tuple

__all__ = ['Data', 'LoggerLike', 'StatusLike', 'Origin', 'Subprotocol', 'ExtensionName', 'ExtensionParameter']

Data = str | bytes
LoggerLike = logging.Logger | logging.LoggerAdapter
StatusLike = http.HTTPStatus | int
Origin: Incomplete
Subprotocol: Incomplete
ExtensionName: Incomplete
ExtensionParameter = Tuple[str, str | None]
ExtensionHeader = Tuple[ExtensionName, List[ExtensionParameter]]
