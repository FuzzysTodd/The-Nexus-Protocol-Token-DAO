import abc
from abc import ABC, abstractmethod
from chromadb.api.models.Collection import Collection as Collection
from chromadb.api.types import CollectionMetadata as CollectionMetadata, Documents as Documents, EmbeddingFunction as EmbeddingFunction, Embeddings as Embeddings, GetResult as GetResult, IDs as IDs, Include as Include, Metadatas as Metadatas, QueryResult as QueryResult, Where as Where, WhereDocument as WhereDocument
from chromadb.config import Component as Component, Settings as Settings
from typing import Sequence

class API(Component, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def heartbeat(self) -> int:
        """Get the current time in nanoseconds since epoch.
        Used to check if the server is alive.

        Returns:
            int: The current time in nanoseconds since epoch

        """
    @abstractmethod
    def list_collections(self) -> Sequence[Collection]:
        '''List all collections.
        Returns:
            Sequence[Collection]: A list of collections

        Examples:
            ```python
            client.list_collections()
            # [collection(name="my_collection", metadata={})]
            ```
        '''
    @abstractmethod
    def create_collection(self, name: str, metadata: CollectionMetadata | None = None, embedding_function: EmbeddingFunction | None = ..., get_or_create: bool = False) -> Collection:
        '''Create a new collection with the given name and metadata.
        Args:
            name: The name of the collection to create.
            metadata: Optional metadata to associate with the collection.
            embedding_function: Optional function to use to embed documents.
                                Uses the default embedding function if not provided.
            get_or_create: If True, return the existing collection if it exists.

        Returns:
            Collection: The newly created collection.

        Raises:
            ValueError: If the collection already exists and get_or_create is False.
            ValueError: If the collection name is invalid.

        Examples:
            ```python
            client.create_collection("my_collection")
            # collection(name="my_collection", metadata={})

            client.create_collection("my_collection", metadata={"foo": "bar"})
            # collection(name="my_collection", metadata={"foo": "bar"})
            ```
        '''
    @abstractmethod
    def get_collection(self, name: str, embedding_function: EmbeddingFunction | None = ...) -> Collection:
        '''Get a collection with the given name.
        Args:
            name: The name of the collection to get
            embedding_function: Optional function to use to embed documents.
                                Uses the default embedding function if not provided.

        Returns:
            Collection: The collection

        Raises:
            ValueError: If the collection does not exist

        Examples:
            ```python
            client.get_collection("my_collection")
            # collection(name="my_collection", metadata={})
            ```
        '''
    @abstractmethod
    def get_or_create_collection(self, name: str, metadata: CollectionMetadata | None = None, embedding_function: EmbeddingFunction | None = ...) -> Collection:
        '''Get or create a collection with the given name and metadata.
        Args:
            name: The name of the collection to get or create
            metadata: Optional metadata to associate with the collection
            embedding_function: Optional function to use to embed documents

        Returns:
            The collection

        Examples:
            ```python
            client.get_or_create_collection("my_collection")
            # collection(name="my_collection", metadata={})
            ```
        '''
    @abstractmethod
    def delete_collection(self, name: str) -> None:
        '''Delete a collection with the given name.
        Args:
            name: The name of the collection to delete.

        Raises:
            ValueError: If the collection does not exist.

        Examples:
            ```python
            client.delete_collection("my_collection")
            ```
        '''
    @abstractmethod
    def reset(self) -> bool:
        """Resets the database. This will delete all collections and entries.

        Returns:
            bool: True if the database was reset successfully.
        """
    @abstractmethod
    def get_version(self) -> str:
        """Get the version of Chroma.

        Returns:
            str: The version of Chroma

        """
    @abstractmethod
    def get_settings(self) -> Settings:
        """Get the settings used to initialize the client.

        Returns:
            Settings: The settings used to initialize the client.

        """
    @property
    @abstractmethod
    def max_batch_size(self) -> int:
        """Return the maximum number of records that can be submitted in a single call
        to submit_embeddings."""
