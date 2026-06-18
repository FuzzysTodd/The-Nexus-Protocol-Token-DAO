from _typeshed import Incomplete
from typing import Dict, List

class PBIArtifact:
    objectId: Incomplete
    artifactType: Incomplete
    displayName: Incomplete
    provisionState: Incomplete
    description: Incomplete
    extendedProperties: Incomplete
    def __init__(self, objectId: str, artifactType: str, displayName: str, provisionState: str, description: str = '', extendedProperties: Dict[str, str] = None) -> None: ...

class ReservedNamesResponse:
    reservedNames: Incomplete
    artifactType: Incomplete
    def __init__(self, reservedNames: List[Dict[str, str]] = [], artifactType: str = '') -> None: ...
