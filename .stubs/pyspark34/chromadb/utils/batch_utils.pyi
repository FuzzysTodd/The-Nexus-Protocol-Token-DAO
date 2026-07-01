from chromadb.api import API as API
from chromadb.api.types import Documents as Documents, Embeddings as Embeddings, IDs as IDs, Metadatas as Metadatas
from typing import List, Tuple

def create_batches(api: API, ids: IDs, embeddings: Embeddings | None = None, metadatas: Metadatas | None = None, documents: Documents | None = None) -> List[Tuple[IDs, Embeddings, Metadatas | None, Documents | None]]: ...
