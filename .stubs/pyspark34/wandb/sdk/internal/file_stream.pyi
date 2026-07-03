import requests
from ..lib import file_stream_utils as file_stream_utils
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, NamedTuple, Tuple, TypedDict
from wandb import util as util
from wandb.sdk.internal import internal_api as internal_api

class ProcessedChunk(TypedDict):
    offset: int
    content: List[str]

class ProcessedBinaryChunk(TypedDict):
    offset: int
    content: str
    encoding: str

logger: Incomplete

class Chunk(NamedTuple):
    filename: str
    data: Any

class DefaultFilePolicy:
    def __init__(self, start_chunk_id: int = 0) -> None: ...
    def process_chunks(self, chunks: List[Chunk]) -> bool | ProcessedChunk | ProcessedBinaryChunk | List['ProcessedChunk']: ...

class JsonlFilePolicy(DefaultFilePolicy):
    def process_chunks(self, chunks: List[Chunk]) -> ProcessedChunk: ...

class SummaryFilePolicy(DefaultFilePolicy):
    def process_chunks(self, chunks: List[Chunk]) -> bool | ProcessedChunk: ...

class StreamCRState:
    '''Stream state that tracks carriage returns.

    There are two streams: stdout and stderr. We create two instances for each stream.
    An instance holds state about:
        found_cr:       if a carriage return has been found in this stream.
        cr:             most recent offset (line number) where we found \\r.
                        We update this offset with every progress bar update.
        last_normal:    most recent offset without a \\r in this stream.
                        i.e. the most recent "normal" line.
    '''
    found_cr: bool
    cr: int | None
    last_normal: int | None
    def __init__(self) -> None: ...

class CRDedupeFilePolicy(DefaultFilePolicy):
    '''File stream policy for removing carriage-return erased characters.

    This is what a terminal does. We use it for console output to reduce the amount of
    data we need to send over the network (eg. for progress bars), while preserving the
    output\'s appearance in the web app.

    CR stands for "carriage return", for the character \\r. It tells the terminal to move
    the cursor back to the start of the current line. Progress bars (like tqdm) use \\r
    repeatedly to overwrite a line with newer updates. This gives the illusion of the
    progress bar filling up in real-time.
    '''
    global_offset: int
    stderr: Incomplete
    stdout: Incomplete
    def __init__(self, start_chunk_id: int = 0) -> None: ...
    @staticmethod
    def get_consecutive_offsets(console: Dict[int, str]) -> List[List[int]]:
        '''Compress consecutive line numbers into an interval.

        Args:
            console: Dict[int, str] which maps offsets (line numbers) to lines of text.
            It represents a mini version of our console dashboard on the UI.

        Returns:
            A list of intervals (we compress consecutive line numbers into an interval).

        Example:
            >>> console = {2: "", 3: "", 4: "", 5: "", 10: "", 11: "", 20: ""}
            >>> get_consecutive_offsets(console)
            [(2, 5), (10, 11), (20, 20)]
        '''
    @staticmethod
    def split_chunk(chunk: Chunk) -> Tuple[str, str]:
        '''Split chunks.

        Args:
            chunk: object with two fields: filename (str) & data (str)
            `chunk.data` is a str containing the lines we want. It usually contains \\n or \\r or both.
            `chunk.data` has two possible formats (for the two streams - stdout and stderr):
                - "2020-08-25T20:38:36.895321 this is my line of text\\nsecond line\\n"
                - "ERROR 2020-08-25T20:38:36.895321 this is my line of text\\nsecond line\\nthird\\n".

                Here\'s another example with a carriage return \\r.
                - "ERROR 2020-08-25T20:38:36.895321 \\r progress bar\\n"

        Returns:
            A 2-tuple of strings.
            First str is prefix, either "ERROR {timestamp} " or "{timestamp} ".
            Second str is the rest of the string.

        Example:
            >>> chunk = Chunk(filename="output.log", data="ERROR 2020-08-25T20:38 this is my line of text\\n")
            >>> split_chunk(chunk)
            ("ERROR 2020-08-25T20:38 ", "this is my line of text\\n")
        '''
    def process_chunks(self, chunks: List) -> List['ProcessedChunk']:
        '''Process chunks.

        Args:
            chunks: List of Chunk objects. See description of chunk above in `split_chunk(...)`.

        Returns:
            List[Dict]. Each dict in the list contains two keys: an `offset` which holds the line number
            and `content` which maps to a list of consecutive lines starting from that offset.
            `offset` here means global line number in our console on the UI.

        Example:
            >>> chunks = [
                Chunk("output.log", "ERROR 2020-08-25T20:38 this is my line of text\\nboom\\n"),
                Chunk("output.log", "2020-08-25T20:38 this is test\\n"),
            ]
            >>> process_chunks(chunks)
            [
                {"offset": 0, "content": [
                    "ERROR 2020-08-25T20:38 this is my line of text\\n",
                    "ERROR 2020-08-25T20:38 boom\\n",
                    "2020-08-25T20:38 this is test\\n"
                    ]
                }
            ]
        '''

class BinaryFilePolicy(DefaultFilePolicy):
    def __init__(self) -> None: ...
    def process_chunks(self, chunks: List[Chunk]) -> ProcessedBinaryChunk: ...

class FileStreamApi:
    """Pushes chunks of files to our streaming endpoint.

    This class is used as a singleton. It has a thread that serializes access to
    the streaming endpoint and performs rate-limiting and batching.

    TODO: Differentiate between binary/text encoding.
    """
    class Finish(NamedTuple):
        exitcode: int
    class Preempting(NamedTuple): ...
    class PushSuccess(NamedTuple):
        artifact_id: str
        save_name: str
    MAX_ITEMS_PER_PUSH: int
    def __init__(self, api: internal_api.Api, run_id: str, start_time: float, timeout: float = 0, settings: dict | None = None) -> None: ...
    def start(self) -> None: ...
    def set_default_file_policy(self, filename: str, file_policy: DefaultFilePolicy) -> None:
        """Set an upload policy for a file unless one has already been set."""
    def set_file_policy(self, filename: str, file_policy: DefaultFilePolicy) -> None: ...
    @property
    def heartbeat_seconds(self) -> int | float: ...
    def rate_limit_seconds(self) -> int | float: ...
    def stream_file(self, path: str) -> None: ...
    def enqueue_preempting(self) -> None: ...
    def push(self, filename: str, data: Any) -> None:
        """Push a chunk of a file to the streaming endpoint.

        Arguments:
            filename: Name of file that this is a chunk of.
            data: File data.
        """
    def push_success(self, artifact_id: str, save_name: str) -> None:
        """Notification that a file upload has been successfully completed.

        Arguments:
            artifact_id: ID of artifact
            save_name: saved name of the uploaded file
        """
    def finish(self, exitcode: int) -> None:
        """Clean up.

        Anything pushed after finish will be dropped.

        Arguments:
            exitcode: The exitcode of the watched process.
        """

MAX_SLEEP_SECONDS: Incomplete

def request_with_retry(func: Callable, *args: Any, **kwargs: Any) -> requests.Response | requests.RequestException:
    """Perform a requests http call, retrying with exponential backoff.

    Arguments:
        func:        An http-requesting function to call, like requests.post
        max_retries: Maximum retries before giving up.
                     By default, we retry 30 times in ~2 hours before dropping the chunk
        *args:       passed through to func
        **kwargs:    passed through to func
    """
