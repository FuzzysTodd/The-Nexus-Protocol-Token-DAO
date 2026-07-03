from .. import frames
from ..typing import ExtensionParameter
from .base import ClientExtensionFactory, Extension, ServerExtensionFactory
from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence, Tuple

__all__ = ['PerMessageDeflate', 'ClientPerMessageDeflateFactory', 'enable_client_permessage_deflate', 'ServerPerMessageDeflateFactory', 'enable_server_permessage_deflate']

class PerMessageDeflate(Extension):
    """
    Per-Message Deflate extension.

    """
    name: Incomplete
    remote_no_context_takeover: Incomplete
    local_no_context_takeover: Incomplete
    remote_max_window_bits: Incomplete
    local_max_window_bits: Incomplete
    compress_settings: Incomplete
    decoder: Incomplete
    encoder: Incomplete
    decode_cont_data: bool
    def __init__(self, remote_no_context_takeover: bool, local_no_context_takeover: bool, remote_max_window_bits: int, local_max_window_bits: int, compress_settings: Dict[Any, Any] | None = None) -> None:
        """
        Configure the Per-Message Deflate extension.

        """
    def decode(self, frame: frames.Frame, *, max_size: int | None = None) -> frames.Frame:
        """
        Decode an incoming frame.

        """
    def encode(self, frame: frames.Frame) -> frames.Frame:
        """
        Encode an outgoing frame.

        """

class ClientPerMessageDeflateFactory(ClientExtensionFactory):
    """
    Client-side extension factory for the Per-Message Deflate extension.

    Parameters behave as described in `section 7.1 of RFC 7692`_.

    .. _section 7.1 of RFC 7692: https://www.rfc-editor.org/rfc/rfc7692.html#section-7.1

    Set them to :obj:`True` to include them in the negotiation offer without a
    value or to an integer value to include them with this value.

    Args:
        server_no_context_takeover: prevent server from using context takeover.
        client_no_context_takeover: prevent client from using context takeover.
        server_max_window_bits: maximum size of the server's LZ77 sliding window
            in bits, between 8 and 15.
        client_max_window_bits: maximum size of the client's LZ77 sliding window
            in bits, between 8 and 15, or :obj:`True` to indicate support without
            setting a limit.
        compress_settings: additional keyword arguments for :func:`zlib.compressobj`,
            excluding ``wbits``.

    """
    name: Incomplete
    server_no_context_takeover: Incomplete
    client_no_context_takeover: Incomplete
    server_max_window_bits: Incomplete
    client_max_window_bits: Incomplete
    compress_settings: Incomplete
    def __init__(self, server_no_context_takeover: bool = False, client_no_context_takeover: bool = False, server_max_window_bits: int | None = None, client_max_window_bits: int | bool | None = True, compress_settings: Dict[str, Any] | None = None) -> None:
        """
        Configure the Per-Message Deflate extension factory.

        """
    def get_request_params(self) -> List[ExtensionParameter]:
        """
        Build request parameters.

        """
    def process_response_params(self, params: Sequence[ExtensionParameter], accepted_extensions: Sequence[Extension]) -> PerMessageDeflate:
        """
        Process response parameters.

        Return an extension instance.

        """

def enable_client_permessage_deflate(extensions: Sequence[ClientExtensionFactory] | None) -> Sequence[ClientExtensionFactory]:
    """
    Enable Per-Message Deflate with default settings in client extensions.

    If the extension is already present, perhaps with non-default settings,
    the configuration isn't changed.

    """

class ServerPerMessageDeflateFactory(ServerExtensionFactory):
    """
    Server-side extension factory for the Per-Message Deflate extension.

    Parameters behave as described in `section 7.1 of RFC 7692`_.

    .. _section 7.1 of RFC 7692: https://www.rfc-editor.org/rfc/rfc7692.html#section-7.1

    Set them to :obj:`True` to include them in the negotiation offer without a
    value or to an integer value to include them with this value.

    Args:
        server_no_context_takeover: prevent server from using context takeover.
        client_no_context_takeover: prevent client from using context takeover.
        server_max_window_bits: maximum size of the server's LZ77 sliding window
            in bits, between 8 and 15.
        client_max_window_bits: maximum size of the client's LZ77 sliding window
            in bits, between 8 and 15.
        compress_settings: additional keyword arguments for :func:`zlib.compressobj`,
            excluding ``wbits``.
        require_client_max_window_bits: do not enable compression at all if
            client doesn't advertise support for ``client_max_window_bits``;
            the default behavior is to enable compression without enforcing
            ``client_max_window_bits``.

    """
    name: Incomplete
    server_no_context_takeover: Incomplete
    client_no_context_takeover: Incomplete
    server_max_window_bits: Incomplete
    client_max_window_bits: Incomplete
    compress_settings: Incomplete
    require_client_max_window_bits: Incomplete
    def __init__(self, server_no_context_takeover: bool = False, client_no_context_takeover: bool = False, server_max_window_bits: int | None = None, client_max_window_bits: int | None = None, compress_settings: Dict[str, Any] | None = None, require_client_max_window_bits: bool = False) -> None:
        """
        Configure the Per-Message Deflate extension factory.

        """
    def process_request_params(self, params: Sequence[ExtensionParameter], accepted_extensions: Sequence[Extension]) -> Tuple[List[ExtensionParameter], PerMessageDeflate]:
        """
        Process request parameters.

        Return response params and an extension instance.

        """

def enable_server_permessage_deflate(extensions: Sequence[ServerExtensionFactory] | None) -> Sequence[ServerExtensionFactory]:
    """
    Enable Per-Message Deflate with default settings in server extensions.

    If the extension is already present, perhaps with non-default settings,
    the configuration isn't changed.

    """
