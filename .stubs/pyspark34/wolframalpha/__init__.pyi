from _typeshed import Incomplete
from typing import Tuple

def xml_bool(str_val):
    """
    >>> xml_bool('true')
    True
    >>> xml_bool('false')
    False
    """

class Client:
    '''
    Wolfram|Alpha v2.0 client

    Basic usage is pretty simple. Get your App ID at
    https://products.wolframalpha.com/api/.
    Create the client with your App ID:

    >>> app_id = getfixture(\'API_key\')
    >>> client = Client(app_id)

    Send a query, which returns Results objects:

    >>> res = client.query(\'temperature in Washington, DC on October 3, 2012\')

    Result objects have `pods` (a Pod is an answer group from Wolfram Alpha):

    >>> for pod in res.pods:
    ...     pass  # do_something_with(pod)

    Pod objects have ``subpods`` (a Subpod is a specific response
    with the plaintext reply and some additional info):

    >>> for pod in res.pods:
    ...     for sub in pod.subpods:
    ...         print(sub.plaintext)
    temperature | Washington, District of Columbia
    Wednesday, October 3, 2012
    (70 to 81) °F (average: 75 °F)
    ...

    To query simply for the pods that have \'Result\' titles or are
    marked as \'primary\' using ``Result.results``:

    >>> print(next(res.results).text)
    (70 to 81) °F (average: 75 °F)
    (Wednesday, October 3, 2012)

    All objects returned are dictionary subclasses, so to find out which attributes
    Wolfram|Alpha has supplied, simply invoke ``.keys()`` on the object.
    Attributes formed from XML attributes can be accessed with or without their
    "@" prefix (added by xmltodict).

    '''
    app_id: Incomplete
    def __init__(self, app_id) -> None: ...
    @classmethod
    def from_env(cls):
        """
        Create a client with a key discovered from the keyring
        or environment variable. Raises an exception if no key
        is found.
        """
    def query(self, input, params=(), **kwargs):
        """
        Query Wolfram|Alpha using the v2.0 API

        Allows for arbitrary parameters to be passed in
        the query. For example, to pass assumptions:

        >>> client = Client(getfixture('API_key'))
        >>> res = client.query(input='pi', assumption='*C.pi-_*NamedConstant-')

        To pass multiple assumptions, pass multiple items
        as params:

        >>> params = (
        ...     ('assumption', '*C.pi-_*NamedConstant-'),
        ...     ('assumption', 'DateOrder_**Day.Month.Year--'),
        ... )
        >>> res = client.query(input='pi', params=params)

        For more details on Assumptions, see
        https://products.wolframalpha.com/api/documentation.html#6
        """

class ErrorHandler:
    def __init__(self, *args, **kwargs) -> None: ...

def identity(x): ...

class Document(dict):
    children: Tuple[str, ...]
    @classmethod
    def make(cls, path, key, value): ...
    def __getattr__(self, name): ...

class Assumption(Document):
    @property
    def text(self): ...

class Warning(Document): ...

class Image(Document):
    """
    Holds information about an image included with an answer.
    """
    key: str

class Subpod(Document):
    """
    Holds a specific answer or additional information relevant to said answer.
    """

class Pod(ErrorHandler, Document):
    """
    Groups answers and information contextualizing those answers.
    """
    children: Incomplete
    @property
    def primary(self): ...
    @property
    def texts(self):
        """
        The text from each subpod in this pod as a list.
        """
    @property
    def text(self): ...

class Result(ErrorHandler, Document):
    """
    Handles processing the response for the programmer.
    """
    key: str
    children: Incomplete
    @property
    def info(self):
        """
        The pods, assumptions, and warnings of this result.
        """
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def results(self):
        """
        The pods that hold the response to a simple, discrete query.
        """
    @property
    def details(self):
        """
        A simplified set of answer text by title.
        """
