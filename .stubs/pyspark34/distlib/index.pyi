from . import DistlibException as DistlibException
from .compat import HTTPBasicAuthHandler as HTTPBasicAuthHandler, HTTPPasswordMgr as HTTPPasswordMgr, Request as Request, build_opener as build_opener, string_types as string_types, urlparse as urlparse
from .util import ServerProxy as ServerProxy, zip_dir as zip_dir
from _typeshed import Incomplete

logger: Incomplete
DEFAULT_INDEX: str
DEFAULT_REALM: str

class PackageIndex:
    """
    This class represents a package index compatible with PyPI, the Python
    Package Index.
    """
    boundary: bytes
    url: Incomplete
    password_handler: Incomplete
    ssl_verifier: Incomplete
    gpg: Incomplete
    gpg_home: Incomplete
    def __init__(self, url: Incomplete | None = None) -> None:
        """
        Initialise an instance.

        :param url: The URL of the index. If not specified, the URL for PyPI is
                    used.
        """
    username: Incomplete
    password: Incomplete
    realm: Incomplete
    def read_configuration(self) -> None:
        """
        Read the PyPI access configuration as supported by distutils. This populates
        ``username``, ``password``, ``realm`` and ``url`` attributes from the
        configuration.
        """
    def save_configuration(self) -> None:
        """
        Save the PyPI access configuration. You must have set ``username`` and
        ``password`` attributes before calling this method.
        """
    def check_credentials(self) -> None:
        """
        Check that ``username`` and ``password`` have been set, and raise an
        exception if not.
        """
    def register(self, metadata):
        """
        Register a distribution on PyPI, using the provided metadata.

        :param metadata: A :class:`Metadata` instance defining at least a name
                         and version number for the distribution to be
                         registered.
        :return: The HTTP response received from PyPI upon submission of the
                request.
        """
    def get_sign_command(self, filename, signer, sign_password, keystore: Incomplete | None = None):
        """
        Return a suitable command for signing a file.

        :param filename: The pathname to the file to be signed.
        :param signer: The identifier of the signer of the file.
        :param sign_password: The passphrase for the signer's
                              private key used for signing.
        :param keystore: The path to a directory which contains the keys
                         used in verification. If not specified, the
                         instance's ``gpg_home`` attribute is used instead.
        :return: The signing command as a list suitable to be
                 passed to :class:`subprocess.Popen`.
        """
    def run_command(self, cmd, input_data: Incomplete | None = None):
        """
        Run a command in a child process , passing it any input data specified.

        :param cmd: The command to run.
        :param input_data: If specified, this must be a byte string containing
                           data to be sent to the child process.
        :return: A tuple consisting of the subprocess' exit code, a list of
                 lines read from the subprocess' ``stdout``, and a list of
                 lines read from the subprocess' ``stderr``.
        """
    def sign_file(self, filename, signer, sign_password, keystore: Incomplete | None = None):
        """
        Sign a file.

        :param filename: The pathname to the file to be signed.
        :param signer: The identifier of the signer of the file.
        :param sign_password: The passphrase for the signer's
                              private key used for signing.
        :param keystore: The path to a directory which contains the keys
                         used in signing. If not specified, the instance's
                         ``gpg_home`` attribute is used instead.
        :return: The absolute pathname of the file where the signature is
                 stored.
        """
    def upload_file(self, metadata, filename, signer: Incomplete | None = None, sign_password: Incomplete | None = None, filetype: str = 'sdist', pyversion: str = 'source', keystore: Incomplete | None = None):
        """
        Upload a release file to the index.

        :param metadata: A :class:`Metadata` instance defining at least a name
                         and version number for the file to be uploaded.
        :param filename: The pathname of the file to be uploaded.
        :param signer: The identifier of the signer of the file.
        :param sign_password: The passphrase for the signer's
                              private key used for signing.
        :param filetype: The type of the file being uploaded. This is the
                        distutils command which produced that file, e.g.
                        ``sdist`` or ``bdist_wheel``.
        :param pyversion: The version of Python which the release relates
                          to. For code compatible with any Python, this would
                          be ``source``, otherwise it would be e.g. ``3.2``.
        :param keystore: The path to a directory which contains the keys
                         used in signing. If not specified, the instance's
                         ``gpg_home`` attribute is used instead.
        :return: The HTTP response received from PyPI upon submission of the
                request.
        """
    def upload_documentation(self, metadata, doc_dir):
        """
        Upload documentation to the index.

        :param metadata: A :class:`Metadata` instance defining at least a name
                         and version number for the documentation to be
                         uploaded.
        :param doc_dir: The pathname of the directory which contains the
                        documentation. This should be the directory that
                        contains the ``index.html`` for the documentation.
        :return: The HTTP response received from PyPI upon submission of the
                request.
        """
    def get_verify_command(self, signature_filename, data_filename, keystore: Incomplete | None = None):
        """
        Return a suitable command for verifying a file.

        :param signature_filename: The pathname to the file containing the
                                   signature.
        :param data_filename: The pathname to the file containing the
                              signed data.
        :param keystore: The path to a directory which contains the keys
                         used in verification. If not specified, the
                         instance's ``gpg_home`` attribute is used instead.
        :return: The verifying command as a list suitable to be
                 passed to :class:`subprocess.Popen`.
        """
    def verify_signature(self, signature_filename, data_filename, keystore: Incomplete | None = None):
        """
        Verify a signature for a file.

        :param signature_filename: The pathname to the file containing the
                                   signature.
        :param data_filename: The pathname to the file containing the
                              signed data.
        :param keystore: The path to a directory which contains the keys
                         used in verification. If not specified, the
                         instance's ``gpg_home`` attribute is used instead.
        :return: True if the signature was verified, else False.
        """
    def download_file(self, url, destfile, digest: Incomplete | None = None, reporthook: Incomplete | None = None) -> None:
        """
        This is a convenience method for downloading a file from an URL.
        Normally, this will be a file from the index, though currently
        no check is made for this (i.e. a file can be downloaded from
        anywhere).

        The method is just like the :func:`urlretrieve` function in the
        standard library, except that it allows digest computation to be
        done during download and checking that the downloaded data
        matched any expected value.

        :param url: The URL of the file to be downloaded (assumed to be
                    available via an HTTP GET request).
        :param destfile: The pathname where the downloaded file is to be
                         saved.
        :param digest: If specified, this must be a (hasher, value)
                       tuple, where hasher is the algorithm used (e.g.
                       ``'md5'``) and ``value`` is the expected value.
        :param reporthook: The same as for :func:`urlretrieve` in the
                           standard library.
        """
    def send_request(self, req):
        """
        Send a standard library :class:`Request` to PyPI and return its
        response.

        :param req: The request to send.
        :return: The HTTP response from PyPI (a standard library HTTPResponse).
        """
    def encode_request(self, fields, files):
        """
        Encode fields and files for posting to an HTTP server.

        :param fields: The fields to send as a list of (fieldname, value)
                       tuples.
        :param files: The files to send as a list of (fieldname, filename,
                      file_bytes) tuple.
        """
    def search(self, terms, operator: Incomplete | None = None): ...
