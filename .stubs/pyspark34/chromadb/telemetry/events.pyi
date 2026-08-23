from _typeshed import Incomplete
from chromadb.telemetry import TelemetryEvent as TelemetryEvent
from chromadb.utils.embedding_functions import get_builtins as get_builtins
from typing import ClassVar

class ClientStartEvent(TelemetryEvent):
    def __init__(self) -> None: ...

class ClientCreateCollectionEvent(TelemetryEvent):
    collection_uuid: str
    embedding_function: str
    def __init__(self, collection_uuid: str, embedding_function: str) -> None: ...

class CollectionAddEvent(TelemetryEvent):
    max_batch_size: ClassVar[int]
    collection_uuid: str
    add_amount: int
    with_documents: int
    with_metadata: int
    batch_size: Incomplete
    def __init__(self, collection_uuid: str, add_amount: int, with_documents: int, with_metadata: int, batch_size: int = 1) -> None: ...
    @property
    def batch_key(self) -> str: ...
    def batch(self, other: TelemetryEvent) -> CollectionAddEvent: ...

class CollectionUpdateEvent(TelemetryEvent):
    collection_uuid: str
    update_amount: int
    with_embeddings: int
    with_metadata: int
    with_documents: int
    def __init__(self, collection_uuid: str, update_amount: int, with_embeddings: int, with_metadata: int, with_documents: int) -> None: ...

class CollectionQueryEvent(TelemetryEvent):
    collection_uuid: str
    query_amount: int
    with_metadata_filter: bool
    with_document_filter: bool
    n_results: int
    include_metadatas: bool
    include_documents: bool
    include_distances: bool
    def __init__(self, collection_uuid: str, query_amount: int, with_metadata_filter: bool, with_document_filter: bool, n_results: int, include_metadatas: bool, include_documents: bool, include_distances: bool) -> None: ...

class CollectionGetEvent(TelemetryEvent):
    collection_uuid: str
    ids_count: int
    limit: int
    include_metadata: bool
    include_documents: bool
    def __init__(self, collection_uuid: str, ids_count: int, limit: int, include_metadata: bool, include_documents: bool) -> None: ...

class CollectionDeleteEvent(TelemetryEvent):
    collection_uuid: str
    delete_amount: int
    def __init__(self, collection_uuid: str, delete_amount: int) -> None: ...
