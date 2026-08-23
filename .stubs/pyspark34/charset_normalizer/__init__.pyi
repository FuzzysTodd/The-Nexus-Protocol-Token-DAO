from .api import from_bytes as from_bytes, from_fp as from_fp, from_path as from_path, is_binary as is_binary
from .legacy import detect as detect
from .models import CharsetMatch as CharsetMatch, CharsetMatches as CharsetMatches
from .utils import set_logging_handler as set_logging_handler
from .version import VERSION as VERSION, __version__ as __version__

__all__ = ['from_fp', 'from_path', 'from_bytes', 'is_binary', 'detect', 'CharsetMatch', 'CharsetMatches', '__version__', 'VERSION', 'set_logging_handler']
