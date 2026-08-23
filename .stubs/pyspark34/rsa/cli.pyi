import abc
import optparse
import rsa
import rsa.key
import typing
from _typeshed import Incomplete

HASH_METHODS: Incomplete
Indexable: Incomplete

def keygen() -> None:
    """Key generator."""

class CryptoOperation(metaclass=abc.ABCMeta):
    """CLI callable that operates with input, output, and a key."""
    keyname: str
    usage: str
    description: str
    operation: str
    operation_past: str
    operation_progressive: str
    input_help: str
    output_help: str
    expected_cli_args: int
    has_output: bool
    key_class: typing.Type[rsa.key.AbstractKey]
    def __init__(self) -> None: ...
    @abc.abstractmethod
    def perform_operation(self, indata: bytes, key: rsa.key.AbstractKey, cli_args: Indexable) -> typing.Any:
        """Performs the program's operation.

        Implement in a subclass.

        :returns: the data to write to the output.
        """
    def __call__(self) -> None:
        """Runs the program."""
    def parse_cli(self) -> typing.Tuple[optparse.Values, typing.List[str]]:
        """Parse the CLI options

        :returns: (cli_opts, cli_args)
        """
    def read_key(self, filename: str, keyform: str) -> rsa.key.AbstractKey:
        """Reads a public or private key."""
    def read_infile(self, inname: str) -> bytes:
        """Read the input file"""
    def write_outfile(self, outdata: bytes, outname: str) -> None:
        """Write the output file"""

class EncryptOperation(CryptoOperation):
    """Encrypts a file."""
    keyname: str
    description: str
    operation: str
    operation_past: str
    operation_progressive: str
    def perform_operation(self, indata: bytes, pub_key: rsa.key.AbstractKey, cli_args: Indexable = ()) -> bytes:
        """Encrypts files."""

class DecryptOperation(CryptoOperation):
    """Decrypts a file."""
    keyname: str
    description: str
    operation: str
    operation_past: str
    operation_progressive: str
    key_class = rsa.PrivateKey
    def perform_operation(self, indata: bytes, priv_key: rsa.key.AbstractKey, cli_args: Indexable = ()) -> bytes:
        """Decrypts files."""

class SignOperation(CryptoOperation):
    """Signs a file."""
    keyname: str
    usage: str
    description: Incomplete
    operation: str
    operation_past: str
    operation_progressive: str
    key_class = rsa.PrivateKey
    expected_cli_args: int
    output_help: str
    def perform_operation(self, indata: bytes, priv_key: rsa.key.AbstractKey, cli_args: Indexable) -> bytes:
        """Signs files."""

class VerifyOperation(CryptoOperation):
    """Verify a signature."""
    keyname: str
    usage: str
    description: str
    operation: str
    operation_past: str
    operation_progressive: str
    key_class = rsa.PublicKey
    expected_cli_args: int
    has_output: bool
    def perform_operation(self, indata: bytes, pub_key: rsa.key.AbstractKey, cli_args: Indexable) -> None:
        """Verifies files."""

encrypt: Incomplete
decrypt: Incomplete
sign: Incomplete
verify: Incomplete
