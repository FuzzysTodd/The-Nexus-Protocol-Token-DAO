from _typeshed import Incomplete
from chromadb.api.types import Documents as Documents, EmbeddingFunction as EmbeddingFunction, Embeddings as Embeddings
from chromadb.is_thin_client import is_thin_client as is_thin_client
from typing import Any, Dict, List

logger: Incomplete

class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    models: Dict[str, Any]
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2', device: str = 'cpu', normalize_embeddings: bool = False) -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

class Text2VecEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model_name: str = 'shibing624/text2vec-base-chinese') -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

class OpenAIEmbeddingFunction(EmbeddingFunction):
    def __init__(self, api_key: str | None = None, model_name: str = 'text-embedding-ada-002', organization_id: str | None = None, api_base: str | None = None, api_type: str | None = None, api_version: str | None = None) -> None:
        '''
        Initialize the OpenAIEmbeddingFunction.
        Args:
            api_key (str, optional): Your API key for the OpenAI API. If not
                provided, it will raise an error to provide an OpenAI API key.
            organization_id(str, optional): The OpenAI organization ID if applicable
            model_name (str, optional): The name of the model to use for text
                embeddings. Defaults to "text-embedding-ada-002".
            api_base (str, optional): The base path for the API. If not provided,
                it will use the base path for the OpenAI API. This can be used to
                point to a different deployment, such as an Azure deployment.
            api_type (str, optional): The type of the API deployment. This can be
                used to specify a different deployment, such as \'azure\'. If not
                provided, it will use the default OpenAI deployment.
            api_version (str, optional): The api version for the API. If not provided,
                it will use the api version for the OpenAI API. This can be used to
                point to a different deployment, such as an Azure deployment.

        '''
    def __call__(self, texts: Documents) -> Embeddings: ...

class CohereEmbeddingFunction(EmbeddingFunction):
    def __init__(self, api_key: str, model_name: str = 'large') -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

class HuggingFaceEmbeddingFunction(EmbeddingFunction):
    '''
    This class is used to get embeddings for a list of texts using the HuggingFace API.
    It requires an API key and a model name. The default model name is "sentence-transformers/all-MiniLM-L6-v2".
    '''
    def __init__(self, api_key: str, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2') -> None:
        '''
        Initialize the HuggingFaceEmbeddingFunction.

        Args:
            api_key (str): Your API key for the HuggingFace API.
            model_name (str, optional): The name of the model to use for text embeddings. Defaults to "sentence-transformers/all-MiniLM-L6-v2".
        '''
    def __call__(self, texts: Documents) -> Embeddings:
        '''
        Get the embeddings for a list of texts.

        Args:
            texts (Documents): A list of texts to get embeddings for.

        Returns:
            Embeddings: The embeddings for the texts.

        Example:
            >>> hugging_face = HuggingFaceEmbeddingFunction(api_key="your_api_key")
            >>> texts = ["Hello, world!", "How are you?"]
            >>> embeddings = hugging_face(texts)
        '''

class InstructorEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model_name: str = 'hkunlp/instructor-base', device: str = 'cpu', instruction: str | None = None) -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

class ONNXMiniLM_L6_V2(EmbeddingFunction):
    MODEL_NAME: str
    DOWNLOAD_PATH: Incomplete
    EXTRACTED_FOLDER_NAME: str
    ARCHIVE_FILENAME: str
    MODEL_DOWNLOAD_URL: str
    tokenizer: Incomplete
    model: Incomplete
    ort: Incomplete
    Tokenizer: Incomplete
    tqdm: Incomplete
    def __init__(self, preferred_providers: List[str] | None = None) -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

def DefaultEmbeddingFunction() -> EmbeddingFunction | None: ...

class GooglePalmEmbeddingFunction(EmbeddingFunction):
    """To use this EmbeddingFunction, you must have the google.generativeai Python package installed and have a PaLM API key."""
    def __init__(self, api_key: str, model_name: str = 'models/embedding-gecko-001') -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

class GoogleVertexEmbeddingFunction(EmbeddingFunction):
    def __init__(self, api_key: str, model_name: str = 'textembedding-gecko', project_id: str = 'cloud-large-language-models', region: str = 'us-central1') -> None: ...
    def __call__(self, texts: Documents) -> Embeddings: ...

def get_builtins() -> List[str]: ...
