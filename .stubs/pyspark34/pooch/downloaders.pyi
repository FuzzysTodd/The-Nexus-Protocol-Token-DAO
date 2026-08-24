from .utils import parse_url as parse_url
from _typeshed import Incomplete

def choose_downloader(url, progressbar: bool = False):
    '''
    Choose the appropriate downloader for the given URL based on the protocol.

    Parameters
    ----------
    url : str
        A URL (including protocol).
    progressbar : bool or an arbitrary progress bar object
        If True, will print a progress bar of the download to standard error
        (stderr). Requires `tqdm <https://github.com/tqdm/tqdm>`__ to be
        installed. Alternatively, an arbitrary progress bar object can be
        passed. See :ref:`custom-progressbar` for details.

    Returns
    -------
    downloader
        A downloader class, like :class:`pooch.HTTPDownloader`,
        :class:`pooch.FTPDownloader`, or :class: `pooch.SFTPDownloader`.

    Examples
    --------

    >>> downloader = choose_downloader("http://something.com")
    >>> print(downloader.__class__.__name__)
    HTTPDownloader
    >>> downloader = choose_downloader("https://something.com")
    >>> print(downloader.__class__.__name__)
    HTTPDownloader
    >>> downloader = choose_downloader("ftp://something.com")
    >>> print(downloader.__class__.__name__)
    FTPDownloader
    >>> downloader = choose_downloader("doi:DOI/filename.csv")
    >>> print(downloader.__class__.__name__)
    DOIDownloader

    '''

class HTTPDownloader:
    '''
    Download manager for fetching files over HTTP/HTTPS.

    When called, downloads the given file URL into the specified local file.
    Uses the :mod:`requests` library to manage downloads.

    Use with :meth:`pooch.Pooch.fetch` or :func:`pooch.retrieve` to customize
    the download of files (for example, to use authentication or print a
    progress bar).

    Parameters
    ----------
    progressbar : bool or an arbitrary progress bar object
        If True, will print a progress bar of the download to standard error
        (stderr). Requires `tqdm <https://github.com/tqdm/tqdm>`__ to be
        installed. Alternatively, an arbitrary progress bar object can be
        passed. See :ref:`custom-progressbar` for details.
    chunk_size : int
        Files are streamed *chunk_size* bytes at a time instead of loading
        everything into memory at one. Usually doesn\'t need to be changed.
    **kwargs
        All keyword arguments given when creating an instance of this class
        will be passed to :func:`requests.get`.

    Examples
    --------

    Download one of the data files from the Pooch repository:

    >>> import os
    >>> from pooch import __version__, check_version
    >>> url = "https://github.com/fatiando/pooch/raw/{}/data/tiny-data.txt"
    >>> url = url.format(check_version(__version__, fallback="main"))
    >>> downloader = HTTPDownloader()
    >>> # Not using with Pooch.fetch so no need to pass an instance of Pooch
    >>> downloader(url=url, output_file="tiny-data.txt", pooch=None)
    >>> os.path.exists("tiny-data.txt")
    True
    >>> with open("tiny-data.txt") as f:
    ...     print(f.read().strip())
    # A tiny data file for test purposes only
    1  2  3  4  5  6
    >>> os.remove("tiny-data.txt")

    Authentication can be handled by passing a user name and password to
    :func:`requests.get`. All arguments provided when creating an instance of
    the class are forwarded to :func:`requests.get`. We\'ll use
    ``auth=(username, password)`` to use basic HTTPS authentication. The
    https://httpbin.org website allows us to make a fake a login request using
    whatever username and password we provide to it:

    >>> user = "doggo"
    >>> password = "goodboy"
    >>> # httpbin will ask for the user and password we provide in the URL
    >>> url = f"https://httpbin.org/basic-auth/{user}/{password}"
    >>> # Trying without the login credentials causes an error
    >>> downloader = HTTPDownloader()
    >>> try:
    ...     downloader(url=url, output_file="tiny-data.txt", pooch=None)
    ... except Exception:
    ...     print("There was an error!")
    There was an error!
    >>> # Pass in the credentials to HTTPDownloader
    >>> downloader = HTTPDownloader(auth=(user, password))
    >>> downloader(url=url, output_file="tiny-data.txt", pooch=None)
    >>> with open("tiny-data.txt") as f:
    ...     for line in f:
    ...         print(line.rstrip())
    {
      "authenticated": true,
      "user": "doggo"
    }
    >>> os.remove("tiny-data.txt")

    '''
    kwargs: Incomplete
    progressbar: Incomplete
    chunk_size: Incomplete
    def __init__(self, progressbar: bool = False, chunk_size: int = 1024, **kwargs) -> None: ...
    def __call__(self, url, output_file, pooch, check_only: bool = False):
        """
        Download the given URL over HTTP to the given output file.

        Uses :func:`requests.get`.

        Parameters
        ----------
        url : str
            The URL to the file you want to download.
        output_file : str or file-like object
            Path (and file name) to which the file will be downloaded.
        pooch : :class:`~pooch.Pooch`
            The instance of :class:`~pooch.Pooch` that is calling this method.
        check_only : bool
            If True, will only check if a file exists on the server and
            **without downloading the file**. Will return ``True`` if the file
            exists and ``False`` otherwise.

        Returns
        -------
        availability : bool or None
            If ``check_only==True``, returns a boolean indicating if the file
            is available on the server. Otherwise, returns ``None``.

        """

class FTPDownloader:
    '''
    Download manager for fetching files over FTP.

    When called, downloads the given file URL into the specified local file.
    Uses the :mod:`ftplib` module to manage downloads.

    Use with :meth:`pooch.Pooch.fetch` or :func:`pooch.retrieve` to customize
    the download of files (for example, to use authentication or print a
    progress bar).

    Parameters
    ----------
    port : int
        Port used for the FTP connection.
    username : str
        User name used to login to the server. Only needed if the server
        requires authentication (i.e., no anonymous FTP).
    password : str
        Password used to login to the server. Only needed if the server
        requires authentication (i.e., no anonymous FTP). Use the empty string
        to indicate no password is required.
    account : str
        Some servers also require an "account" name for authentication.
    timeout : int
        Timeout in seconds for ftp socket operations, use None to mean no
        timeout.
    progressbar : bool
        If True, will print a progress bar of the download to standard error
        (stderr). Requires `tqdm <https://github.com/tqdm/tqdm>`__ to be
        installed. **Custom progress bars are not yet supported.**
    chunk_size : int
        Files are streamed *chunk_size* bytes at a time instead of loading
        everything into memory at one. Usually doesn\'t need to be changed.

    '''
    port: Incomplete
    username: Incomplete
    password: Incomplete
    account: Incomplete
    timeout: Incomplete
    progressbar: Incomplete
    chunk_size: Incomplete
    def __init__(self, port: int = 21, username: str = 'anonymous', password: str = '', account: str = '', timeout: Incomplete | None = None, progressbar: bool = False, chunk_size: int = 1024) -> None: ...
    def __call__(self, url, output_file, pooch, check_only: bool = False):
        """
        Download the given URL over FTP to the given output file.

        Parameters
        ----------
        url : str
            The URL to the file you want to download.
        output_file : str or file-like object
            Path (and file name) to which the file will be downloaded.
        pooch : :class:`~pooch.Pooch`
            The instance of :class:`~pooch.Pooch` that is calling this method.
        check_only : bool
            If True, will only check if a file exists on the server and
            **without downloading the file**. Will return ``True`` if the file
            exists and ``False`` otherwise.

        Returns
        -------
        availability : bool or None
            If ``check_only==True``, returns a boolean indicating if the file
            is available on the server. Otherwise, returns ``None``.

        """

class SFTPDownloader:
    """
    Download manager for fetching files over SFTP.

    When called, downloads the given file URL into the specified local file.
    Requires `paramiko <https://github.com/paramiko/paramiko>`__ to be
    installed.

    Use with :meth:`pooch.Pooch.fetch` or :func:`pooch.retrieve` to customize
    the download of files (for example, to use authentication or print a
    progress bar).

    Parameters
    ----------
    port : int
        Port used for the SFTP connection.
    username : str
        User name used to login to the server. Only needed if the server
        requires authentication (i.e., no anonymous SFTP).
    password : str
        Password used to login to the server. Only needed if the server
        requires authentication (i.e., no anonymous SFTP). Use the empty
        string to indicate no password is required.
    timeout : int
        Timeout in seconds for sftp socket operations, use None to mean no
        timeout.
    progressbar : bool or an arbitrary progress bar object
        If True, will print a progress bar of the download to standard
        error (stderr). Requires `tqdm <https://github.com/tqdm/tqdm>`__ to
        be installed.

    """
    port: Incomplete
    username: Incomplete
    password: Incomplete
    account: Incomplete
    timeout: Incomplete
    progressbar: Incomplete
    def __init__(self, port: int = 22, username: str = 'anonymous', password: str = '', account: str = '', timeout: Incomplete | None = None, progressbar: bool = False) -> None: ...
    def __call__(self, url, output_file, pooch) -> None:
        """
        Download the given URL over SFTP to the given output file.

        The output file must be given as a string (file name/path) and not an
        open file object! Otherwise, paramiko cannot save to that file.

        Parameters
        ----------
        url : str
            The URL to the file you want to download.
        output_file : str
            Path (and file name) to which the file will be downloaded. **Cannot
            be a file object**.
        pooch : :class:`~pooch.Pooch`
            The instance of :class:`~pooch.Pooch` that is calling this method.
        """

class DOIDownloader:
    '''
    Download manager for fetching files from Digital Object Identifiers (DOIs).

    Open-access data repositories often issue Digital Object Identifiers (DOIs)
    for data which provide a stable link and citation point. The trick is
    finding out the download URL for a file given the DOI.

    When called, this downloader uses the repository\'s public API to find out
    the download URL from the DOI and file name. It then uses
    :class:`pooch.HTTPDownloader` to download the URL into the specified local
    file. Allowing "URL"s  to be specified with the DOI instead of the actual
    HTTP download link. Uses the :mod:`requests` library to manage downloads
    and interact with the APIs.

    The **format of the "URL"** is: ``doi:{DOI}/{file name}``.

    Notice that there are no ``//`` like in HTTP/FTP and you must specify a
    file name after the DOI (separated by a ``/``).

    Use with :meth:`pooch.Pooch.fetch` or :func:`pooch.retrieve` to be able to
    download files given the DOI instead of an HTTP link.

    Supported repositories:

    * `figshare <https://www.figshare.com>`__
    * `Zenodo <https://www.zenodo.org>`__
    * `Dataverse <https://dataverse.org/>`__ instances

    .. attention::

        DOIs from other repositories **will not work** since we need to access
        their particular APIs to find the download links. We welcome
        suggestions and contributions adding new repositories.

    Parameters
    ----------
    progressbar : bool or an arbitrary progress bar object
        If True, will print a progress bar of the download to standard error
        (stderr). Requires `tqdm <https://github.com/tqdm/tqdm>`__ to be
        installed. Alternatively, an arbitrary progress bar object can be
        passed. See :ref:`custom-progressbar` for details.
    chunk_size : int
        Files are streamed *chunk_size* bytes at a time instead of loading
        everything into memory at one. Usually doesn\'t need to be changed.
    **kwargs
        All keyword arguments given when creating an instance of this class
        will be passed to :func:`requests.get`.

    Examples
    --------

    Download one of the data files from the figshare archive of Pooch test
    data:

    >>> import os
    >>> downloader = DOIDownloader()
    >>> url = "doi:10.6084/m9.figshare.14763051.v1/tiny-data.txt"
    >>> # Not using with Pooch.fetch so no need to pass an instance of Pooch
    >>> downloader(url=url, output_file="tiny-data.txt", pooch=None)
    >>> os.path.exists("tiny-data.txt")
    True
    >>> with open("tiny-data.txt") as f:
    ...     print(f.read().strip())
    # A tiny data file for test purposes only
    1  2  3  4  5  6
    >>> os.remove("tiny-data.txt")

    Same thing but for our Zenodo archive:

    >>> url = "doi:10.5281/zenodo.4924875/tiny-data.txt"
    >>> downloader(url=url, output_file="tiny-data.txt", pooch=None)
    >>> os.path.exists("tiny-data.txt")
    True
    >>> with open("tiny-data.txt") as f:
    ...     print(f.read().strip())
    # A tiny data file for test purposes only
    1  2  3  4  5  6
    >>> os.remove("tiny-data.txt")

    '''
    kwargs: Incomplete
    progressbar: Incomplete
    chunk_size: Incomplete
    def __init__(self, progressbar: bool = False, chunk_size: int = 1024, **kwargs) -> None: ...
    def __call__(self, url, output_file, pooch) -> None:
        """
        Download the given DOI URL over HTTP to the given output file.

        Uses the repository's API to determine the actual HTTP download URL
        from the given DOI.

        Uses :func:`requests.get`.

        Parameters
        ----------
        url : str
            The URL to the file you want to download.
        output_file : str or file-like object
            Path (and file name) to which the file will be downloaded.
        pooch : :class:`~pooch.Pooch`
            The instance of :class:`~pooch.Pooch` that is calling this method.

        """

def doi_to_url(doi):
    """
    Follow a DOI link to resolve the URL of the archive.

    Parameters
    ----------
    doi : str
        The DOI of the archive.

    Returns
    -------
    url : str
        The URL of the archive in the data repository.

    """
def doi_to_repository(doi):
    """
    Instantiate a data repository instance from a given DOI.

    This function implements the chain of responsibility dispatch
    to the correct data repository class.

    Parameters
    ----------
    doi : str
        The DOI of the archive.

    Returns
    -------
    data_repository : DataRepository
        The data repository object
    """

class DataRepository:
    @classmethod
    def initialize(cls, doi, archive_url) -> None:
        """
        Initialize the data repository if the given URL points to a
        corresponding repository.

        Initializes a data repository object. This is done as part of
        a chain of responsibility. If the class cannot handle the given
        repository URL, it returns `None`. Otherwise a `DataRepository`
        instance is returned.

        Parameters
        ----------
        doi : str
            The DOI that identifies the repository
        archive_url : str
            The resolved URL for the DOI
        """
    def download_url(self, file_name) -> None:
        """
        Use the repository API to get the download URL for a file given
        the archive URL.

        Parameters
        ----------
        file_name : str
            The name of the file in the archive that will be downloaded.

        Returns
        -------
        download_url : str
            The HTTP URL that can be used to download the file.
        """
    def populate_registry(self, pooch) -> None:
        """
        Populate the registry using the data repository's API

        Parameters
        ----------
        pooch : Pooch
            The pooch instance that the registry will be added to.
        """

class ZenodoRepository(DataRepository):
    base_api_url: str
    archive_url: Incomplete
    doi: Incomplete
    def __init__(self, doi, archive_url) -> None: ...
    @classmethod
    def initialize(cls, doi, archive_url):
        """
        Initialize the data repository if the given URL points to a
        corresponding repository.

        Initializes a data repository object. This is done as part of
        a chain of responsibility. If the class cannot handle the given
        repository URL, it returns `None`. Otherwise a `DataRepository`
        instance is returned.

        Parameters
        ----------
        doi : str
            The DOI that identifies the repository
        archive_url : str
            The resolved URL for the DOI
        """
    @property
    def api_response(self):
        """Cached API response from Zenodo"""
    @property
    def api_version(self):
        '''
        Version of the Zenodo API we are interacting with

        The versions can either be :

        - ``"legacy"``: corresponds to the Zenodo API that was supported until
          2023-10-12 (before the migration to InvenioRDM).
        - ``"new"``: corresponds to the new API that went online on 2023-10-13
          after the migration to InvenioRDM.

        The ``"new"`` API breaks backward compatibility with the ``"legacy"``
        one and could probably be replaced by an updated version that restores
        the behaviour of the ``"legacy"`` one.

        Returns
        -------
        str
        '''
    def download_url(self, file_name):
        """
        Use the repository API to get the download URL for a file given
        the archive URL.

        Parameters
        ----------
        file_name : str
            The name of the file in the archive that will be downloaded.

        Returns
        -------
        download_url : str
            The HTTP URL that can be used to download the file.

        Notes
        -----
        After Zenodo migrated to InvenioRDM on Oct 2023, their API changed. The
        link to the desired files that appears in the API response leads to 404
        errors (by 2023-10-17). The files are available in the following url:
        ``https://zenodo.org/records/{article_id}/files/{file_name}?download=1``.

        This method supports both the legacy and the new API.
        """
    def populate_registry(self, pooch) -> None:
        """
        Populate the registry using the data repository's API

        Parameters
        ----------
        pooch : Pooch
            The pooch instance that the registry will be added to.

        Notes
        -----
        After Zenodo migrated to InvenioRDM on Oct 2023, their API changed. The
        checksums for each file listed in the API reference is now an md5 sum.

        This method supports both the legacy and the new API.
        """

class FigshareRepository(DataRepository):
    archive_url: Incomplete
    doi: Incomplete
    def __init__(self, doi, archive_url) -> None: ...
    @classmethod
    def initialize(cls, doi, archive_url):
        """
        Initialize the data repository if the given URL points to a
        corresponding repository.

        Initializes a data repository object. This is done as part of
        a chain of responsibility. If the class cannot handle the given
        repository URL, it returns `None`. Otherwise a `DataRepository`
        instance is returned.

        Parameters
        ----------
        doi : str
            The DOI that identifies the repository
        archive_url : str
            The resolved URL for the DOI
        """
    @property
    def api_response(self):
        """Cached API response from Figshare"""
    def download_url(self, file_name):
        """
        Use the repository API to get the download URL for a file given
        the archive URL.

        Parameters
        ----------
        file_name : str
            The name of the file in the archive that will be downloaded.

        Returns
        -------
        download_url : str
            The HTTP URL that can be used to download the file.
        """
    def populate_registry(self, pooch) -> None:
        """
        Populate the registry using the data repository's API

        Parameters
        ----------
        pooch : Pooch
            The pooch instance that the registry will be added to.
        """

class DataverseRepository(DataRepository):
    archive_url: Incomplete
    doi: Incomplete
    def __init__(self, doi, archive_url) -> None: ...
    @classmethod
    def initialize(cls, doi, archive_url):
        """
        Initialize the data repository if the given URL points to a
        corresponding repository.

        Initializes a data repository object. This is done as part of
        a chain of responsibility. If the class cannot handle the given
        repository URL, it returns `None`. Otherwise a `DataRepository`
        instance is returned.

        Parameters
        ----------
        doi : str
            The DOI that identifies the repository
        archive_url : str
            The resolved URL for the DOI
        """
    @property
    def api_response(self):
        """Cached API response from a DataVerse instance"""
    @api_response.setter
    def api_response(self, response) -> None:
        """Update the cached API response"""
    def download_url(self, file_name):
        """
        Use the repository API to get the download URL for a file given
        the archive URL.

        Parameters
        ----------
        file_name : str
            The name of the file in the archive that will be downloaded.

        Returns
        -------
        download_url : str
            The HTTP URL that can be used to download the file.
        """
    def populate_registry(self, pooch) -> None:
        """
        Populate the registry using the data repository's API

        Parameters
        ----------
        pooch : Pooch
            The pooch instance that the registry will be added to.
        """
