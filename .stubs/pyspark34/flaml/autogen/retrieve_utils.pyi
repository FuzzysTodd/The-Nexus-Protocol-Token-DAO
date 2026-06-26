from _typeshed import Incomplete
from chromadb.api import API as API
from typing import Dict, List, Tuple

logger: Incomplete
TEXT_FORMATS: Incomplete

def num_tokens_from_text(text: str, model: str = 'gpt-3.5-turbo-0613', return_tokens_per_name_and_message: bool = False) -> int | Tuple[int, int, int]:
    """Return the number of tokens used by a text."""
def num_tokens_from_messages(messages: dict, model: str = 'gpt-3.5-turbo-0613'):
    """Return the number of tokens used by a list of messages."""
def split_text_to_chunks(text: str, max_tokens: int = 4000, chunk_mode: str = 'multi_lines', must_break_at_empty_line: bool = True, overlap: int = 10):
    """Split a long text into chunks of max_tokens."""
def split_files_to_chunks(files: list, max_tokens: int = 4000, chunk_mode: str = 'multi_lines', must_break_at_empty_line: bool = True):
    """Split a list of files into chunks of max_tokens."""
def get_files_from_dir(dir_path: str, types: list = ..., recursive: bool = True):
    """Return a list of all the files in a given directory."""
def get_file_from_url(url: str, save_path: str = None):
    """Download a file from a URL."""
def is_url(string: str):
    """Return True if the string is a valid URL."""
def create_vector_db_from_dir(dir_path: str, max_tokens: int = 4000, client: API = None, db_path: str = '/tmp/chromadb.db', collection_name: str = 'all-my-documents', get_or_create: bool = False, chunk_mode: str = 'multi_lines', must_break_at_empty_line: bool = True, embedding_model: str = 'all-MiniLM-L6-v2'):
    """Create a vector db from all the files in a given directory."""
def query_vector_db(query_texts: List[str], n_results: int = 10, client: API = None, db_path: str = '/tmp/chromadb.db', collection_name: str = 'all-my-documents', search_string: str = '', embedding_model: str = 'all-MiniLM-L6-v2') -> Dict[str, List[str]]:
    """Query a vector db."""
