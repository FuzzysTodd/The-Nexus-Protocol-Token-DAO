from send2trash.compat import text_type as text_type
from send2trash.util import preprocess_paths as preprocess_paths
from send2trash.win.IFileOperationProgressSink import create_sink as create_sink

def send2trash(paths) -> None: ...
