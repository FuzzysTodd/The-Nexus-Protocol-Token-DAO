from . import packages as packages, utils as utils
from .__version__ import __author_email__ as __author_email__, __build__ as __build__, __cake__ as __cake__, __description__ as __description__, __url__ as __url__, __version__ as __version__
from .api import delete as delete, get as get, head as head, options as options, post as post, put as put, request as request
from .exceptions import ConnectTimeout as ConnectTimeout, ConnectionError as ConnectionError, HTTPError as HTTPError, JSONDecodeError as JSONDecodeError, ReadTimeout as ReadTimeout, RequestException as RequestException, Timeout as Timeout, TooManyRedirects as TooManyRedirects, URLRequired as URLRequired
from .models import PreparedRequest as PreparedRequest, Request as Request, Response as Response
from .sessions import Session as Session, session as session
from .status_codes import codes as codes

def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version) -> None: ...
