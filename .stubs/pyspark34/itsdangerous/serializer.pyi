import typing as _t
from .encoding import want_bytes as want_bytes
from .exc import BadPayload as BadPayload, BadSignature as BadSignature
from .signer import Signer as Signer
from _typeshed import Incomplete

def is_text_serializer(serializer: _t.Any) -> bool:
    """Checks whether a serializer generates text or binary."""

class Serializer:
    """A serializer wraps a :class:`~itsdangerous.signer.Signer` to
    enable serializing and securely signing data other than bytes. It
    can unsign to verify that the data hasn't been changed.

    The serializer provides :meth:`dumps` and :meth:`loads`, similar to
    :mod:`json`, and by default uses :mod:`json` internally to serialize
    the data to bytes.

    The secret key should be a random string of ``bytes`` and should not
    be saved to code or version control. Different salts should be used
    to distinguish signing in different contexts. See :doc:`/concepts`
    for information about the security of the secret key and salt.

    :param secret_key: The secret key to sign and verify with. Can be a
        list of keys, oldest to newest, to support key rotation.
    :param salt: Extra key to combine with ``secret_key`` to distinguish
        signatures in different contexts.
    :param serializer: An object that provides ``dumps`` and ``loads``
        methods for serializing data to a string. Defaults to
        :attr:`default_serializer`, which defaults to :mod:`json`.
    :param serializer_kwargs: Keyword arguments to pass when calling
        ``serializer.dumps``.
    :param signer: A ``Signer`` class to instantiate when signing data.
        Defaults to :attr:`default_signer`, which defaults to
        :class:`~itsdangerous.signer.Signer`.
    :param signer_kwargs: Keyword arguments to pass when instantiating
        the ``Signer`` class.
    :param fallback_signers: List of signer parameters to try when
        unsigning with the default signer fails. Each item can be a dict
        of ``signer_kwargs``, a ``Signer`` class, or a tuple of
        ``(signer, signer_kwargs)``. Defaults to
        :attr:`default_fallback_signers`.

    .. versionchanged:: 2.0
        Added support for key rotation by passing a list to
        ``secret_key``.

    .. versionchanged:: 2.0
        Removed the default SHA-512 fallback signer from
        ``default_fallback_signers``.

    .. versionchanged:: 1.1
        Added support for ``fallback_signers`` and configured a default
        SHA-512 fallback. This fallback is for users who used the yanked
        1.0.0 release which defaulted to SHA-512.

    .. versionchanged:: 0.14
        The ``signer`` and ``signer_kwargs`` parameters were added to
        the constructor.
    """
    default_serializer: _t.Any
    default_signer: _t_signer
    default_fallback_signers: _t_fallbacks
    secret_keys: Incomplete
    salt: Incomplete
    serializer: Incomplete
    is_text_serializer: Incomplete
    signer: Incomplete
    signer_kwargs: Incomplete
    fallback_signers: Incomplete
    serializer_kwargs: Incomplete
    def __init__(self, secret_key: _t_secret_key, salt: _t_opt_str_bytes = b'itsdangerous', serializer: _t.Any = None, serializer_kwargs: _t_opt_kwargs = None, signer: _t_signer | None = None, signer_kwargs: _t_opt_kwargs = None, fallback_signers: _t_fallbacks | None = None) -> None: ...
    @property
    def secret_key(self) -> bytes:
        """The newest (last) entry in the :attr:`secret_keys` list. This
        is for compatibility from before key rotation support was added.
        """
    def load_payload(self, payload: bytes, serializer: _t.Any | None = None) -> _t.Any:
        """Loads the encoded object. This function raises
        :class:`.BadPayload` if the payload is not valid. The
        ``serializer`` parameter can be used to override the serializer
        stored on the class. The encoded ``payload`` should always be
        bytes.
        """
    def dump_payload(self, obj: _t.Any) -> bytes:
        """Dumps the encoded object. The return value is always bytes.
        If the internal serializer returns text, the value will be
        encoded as UTF-8.
        """
    def make_signer(self, salt: _t_opt_str_bytes = None) -> Signer:
        """Creates a new instance of the signer to be used. The default
        implementation uses the :class:`.Signer` base class.
        """
    def iter_unsigners(self, salt: _t_opt_str_bytes = None) -> _t.Iterator[Signer]:
        """Iterates over all signers to be tried for unsigning. Starts
        with the configured signer, then constructs each signer
        specified in ``fallback_signers``.
        """
    def dumps(self, obj: _t.Any, salt: _t_opt_str_bytes = None) -> _t_str_bytes:
        """Returns a signed string serialized with the internal
        serializer. The return value can be either a byte or unicode
        string depending on the format of the internal serializer.
        """
    def dump(self, obj: _t.Any, f: _t.IO, salt: _t_opt_str_bytes = None) -> None:
        """Like :meth:`dumps` but dumps into a file. The file handle has
        to be compatible with what the internal serializer expects.
        """
    def loads(self, s: _t_str_bytes, salt: _t_opt_str_bytes = None, **kwargs: _t.Any) -> _t.Any:
        """Reverse of :meth:`dumps`. Raises :exc:`.BadSignature` if the
        signature validation fails.
        """
    def load(self, f: _t.IO, salt: _t_opt_str_bytes = None) -> _t.Any:
        """Like :meth:`loads` but loads from a file."""
    def loads_unsafe(self, s: _t_str_bytes, salt: _t_opt_str_bytes = None) -> _t_load_unsafe:
        """Like :meth:`loads` but without verifying the signature. This
        is potentially very dangerous to use depending on how your
        serializer works. The return value is ``(signature_valid,
        payload)`` instead of just the payload. The first item will be a
        boolean that indicates if the signature is valid. This function
        never fails.

        Use it for debugging only and if you know that your serializer
        module is not exploitable (for example, do not use it with a
        pickle serializer).

        .. versionadded:: 0.15
        """
    def load_unsafe(self, f: _t.IO, salt: _t_opt_str_bytes = None) -> _t_load_unsafe:
        """Like :meth:`loads_unsafe` but loads from a file.

        .. versionadded:: 0.15
        """
