from ._shared import decode_base64_to_bytes as decode_base64_to_bytes, encode_base64 as encode_base64
from ._version import VERSION as VERSION
from _typeshed import Incomplete
from typing import Any, BinaryIO, Dict, Tuple

class StorageEncryptionMixin: ...

class _EncryptionAlgorithm:
    """
    Specifies which client encryption algorithm is used.
    """
    AES_CBC_256: str
    AES_GCM_256: str

class _WrappedContentKey:
    """
    Represents the envelope key details stored on the service.

    :param str algorithm:
        The algorithm used for wrapping.
    :param bytes encrypted_key:
        The encrypted content-encryption-key.
    :param str key_id:
        The key-encryption-key identifier string.
    """
    algorithm: Incomplete
    encrypted_key: Incomplete
    key_id: Incomplete
    def __init__(self, algorithm, encrypted_key, key_id) -> None: ...

class _EncryptedRegionInfo:
    """
    Represents the length of encryption elements.
    This is only used for Encryption V2.

    :param int data_length:
        The length of the encryption region data (not including nonce + tag).
    :param str nonce_length:
        The length of nonce used when encrypting.
    :param int tag_length:
        The length of the encryption tag.
    """
    data_length: Incomplete
    nonce_length: Incomplete
    tag_length: Incomplete
    def __init__(self, data_length, nonce_length, tag_length) -> None: ...

class _EncryptionAgent:
    """
    Represents the encryption agent stored on the service.
    It consists of the encryption protocol version and encryption algorithm used.

    :param _EncryptionAlgorithm encryption_algorithm:
        The algorithm used for encrypting the message contents.
    :param str protocol:
        The protocol version used for encryption.
    """
    encryption_algorithm: Incomplete
    protocol: Incomplete
    def __init__(self, encryption_algorithm, protocol) -> None: ...

class _EncryptionData:
    """
    Represents the encryption data that is stored on the service.

    :param Optional[bytes] content_encryption_IV:
        The content encryption initialization vector.
        Required for AES-CBC (V1).
    :param Optional[_EncryptedRegionInfo] encrypted_region_info:
        The info about the authenticated block sizes.
        Required for AES-GCM (V2).
    :param _EncryptionAgent encryption_agent:
        The encryption agent.
    :param _WrappedContentKey wrapped_content_key:
        An object that stores the wrapping algorithm, the key identifier,
        and the encrypted key bytes.
    :param dict key_wrapping_metadata:
        A dict containing metadata related to the key wrapping.
    """
    content_encryption_IV: Incomplete
    encrypted_region_info: Incomplete
    encryption_agent: Incomplete
    wrapped_content_key: Incomplete
    key_wrapping_metadata: Incomplete
    def __init__(self, content_encryption_IV, encrypted_region_info, encryption_agent, wrapped_content_key, key_wrapping_metadata) -> None: ...

class GCMBlobEncryptionStream:
    """
    A stream that performs AES-GCM encryption on the given data as
    it's streamed. Data is read and encrypted in regions. The stream
    will use the same encryption key and will generate a guaranteed unique
    nonce for each encryption region.

    :param bytes content_encryption_key: The encryption key to use.
    :param BinaryIO data_stream: The data stream to read data from.
    """
    content_encryption_key: Incomplete
    data_stream: Incomplete
    offset: int
    current: bytes
    nonce_counter: int
    def __init__(self, content_encryption_key: bytes, data_stream: BinaryIO) -> None: ...
    def read(self, size: int = -1) -> bytes:
        """
        Read data from the stream. Specify -1 to read all available data.

        :param int size: The amount of data to read. Defaults to -1 for all data.
        :return: The bytes read.
        :rtype: bytes
        """

def is_encryption_v2(encryption_data: _EncryptionData | None) -> bool:
    """
    Determine whether the given encryption data signifies version 2.0.

    :param Optional[_EncryptionData] encryption_data: The encryption data. Will return False if this is None.
    :return: True, if the encryption data indicates encryption V2, false otherwise.
    :rtype: bool
    """
def modify_user_agent_for_encryption(user_agent: str, moniker: str, encryption_version: str, request_options: Dict[str, Any]) -> None:
    """
    Modifies the request options to contain a user agent string updated with encryption information.
    Adds azstorage-clientsideencryption/<version> immediately proceeding the SDK descriptor.

    :param str user_agent: The existing User Agent to modify.
    :param str moniker: The specific SDK moniker. The modification will immediately proceed azsdk-python-{moniker}.
    :param str encryption_version: The version of encryption being used.
    :param Dict[str, Any] request_options: The reuqest options to add the user agent override to.
    """
def get_adjusted_upload_size(length: int, encryption_version: str) -> int:
    """
    Get the adjusted size of the blob upload which accounts for
    extra encryption data (padding OR nonce + tag).

    :param int length: The plaintext data length.
    :param str encryption_version: The version of encryption being used.
    :return: The new upload size to use.
    :rtype: int
    """
def get_adjusted_download_range_and_offset(start: int, end: int, length: int, encryption_data: _EncryptionData | None) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Gets the new download range and offsets into the decrypted data for
    the given user-specified range. The new download range will include all
    the data needed to decrypt the user-provided range and will include only
    full encryption regions.

    The offsets returned will be the offsets needed to fetch the user-requested
    data out of the full decrypted data. The end offset is different based on the
    encryption version. For V1, the end offset is offset from the end whereas for
    V2, the end offset is the ending index into the stream.
    V1: decrypted_data[start_offset : len(decrypted_data) - end_offset]
    V2: decrypted_data[start_offset : end_offset]

    :param int start: The user-requested start index.
    :param int end: The user-requested end index.
    :param int length: The user-requested length. Only used for V1.
    :param Optional[_EncryptionData] encryption_data: The encryption data to determine version and sizes.
    :return: (new start, new end), (start offset, end offset)
    :rtype: Tuple[Tuple[int, int], Tuple[int, int]]
    """
def parse_encryption_data(metadata: Dict[str, Any]) -> _EncryptionData | None:
    """
    Parses the encryption data out of the given blob metadata. If metadata does
    not exist or there are parsing errors, this function will just return None.

    :param Dict[str, Any] metadata: The blob metadata parsed from the response.
    :return: The encryption data or None
    :rtype: Optional[_EncryptionData]
    """
def adjust_blob_size_for_encryption(size: int, encryption_data: _EncryptionData | None) -> int:
    """
    Adjusts the given blob size for encryption by subtracting the size of
    the encryption data (nonce + tag). This only has an affect for encryption V2.

    :param int size: The original blob size.
    :param Optional[_EncryptionData] encryption_data: The encryption data to determine version and sizes.
    :return: The new blob size.
    :rtype: int
    """
def encrypt_blob(blob, key_encryption_key, version):
    """
    Encrypts the given blob using the given encryption protocol version.
    Wraps the generated content-encryption-key using the user-provided key-encryption-key (kek).
    Returns a json-formatted string containing the encryption metadata. This method should
    only be used when a blob is small enough for single shot upload. Encrypting larger blobs
    is done as a part of the upload_data_chunks method.

    :param bytes blob:
        The blob to be encrypted.
    :param object key_encryption_key:
        The user-provided key-encryption-key. Must implement the following methods:
        wrap_key(key)--wraps the specified key using an algorithm of the user's choice.
        get_key_wrap_algorithm()--returns the algorithm used to wrap the specified symmetric key.
        get_kid()--returns a string key id for this key-encryption-key.
    :param str version: The client encryption version to use.
    :return: A tuple of json-formatted string containing the encryption metadata and the encrypted blob data.
    :rtype: (str, bytes)
    """
def generate_blob_encryption_data(key_encryption_key, version):
    """
    Generates the encryption_metadata for the blob.

    :param object key_encryption_key:
        The key-encryption-key used to wrap the cek associate with this blob.
    :param str version: The client encryption version to use.
    :return: A tuple containing the cek and iv for this blob as well as the
        serialized encryption metadata for the blob.
    :rtype: (bytes, Optional[bytes], str)
    """
def decrypt_blob(require_encryption, key_encryption_key, key_resolver, content, start_offset, end_offset, response_headers):
    """
    Decrypts the given blob contents and returns only the requested range.

    :param bool require_encryption:
        Whether the calling blob service requires objects to be decrypted.
    :param object key_encryption_key:
        The user-provided key-encryption-key. Must implement the following methods:
        wrap_key(key)--wraps the specified key using an algorithm of the user's choice.
        get_key_wrap_algorithm()--returns the algorithm used to wrap the specified symmetric key.
        get_kid()--returns a string key id for this key-encryption-key.
    :param object key_resolver:
        The user-provided key resolver. Uses the kid string to return a key-encryption-key
        implementing the interface defined above.
    :param bytes content:
        The encrypted blob content.
    :param int start_offset:
        The adjusted offset from the beginning of the *decrypted* content for the caller's data.
    :param int end_offset:
        The adjusted offset from the end of the *decrypted* content for the caller's data.
    :param Dict[str, Any] response_headers:
        A dictionary of response headers from the download request. Expected to include the
        'x-ms-meta-encryptiondata' header if the blob was encrypted.
    :return: The decrypted blob content.
    :rtype: bytes
    """
def get_blob_encryptor_and_padder(cek, iv, should_pad): ...
def encrypt_queue_message(message, key_encryption_key, version):
    """
    Encrypts the given plain text message using the given protocol version.
    Wraps the generated content-encryption-key using the user-provided key-encryption-key (kek).
    Returns a json-formatted string containing the encrypted message and the encryption metadata.

    :param object message:
        The plain text message to be encrypted.
    :param object key_encryption_key:
        The user-provided key-encryption-key. Must implement the following methods:
        wrap_key(key)--wraps the specified key using an algorithm of the user's choice.
        get_key_wrap_algorithm()--returns the algorithm used to wrap the specified symmetric key.
        get_kid()--returns a string key id for this key-encryption-key.
    :param str version: The client encryption version to use.
    :return: A json-formatted string containing the encrypted message and the encryption metadata.
    :rtype: str
    """
def decrypt_queue_message(message, response, require_encryption, key_encryption_key, resolver):
    """
    Returns the decrypted message contents from an EncryptedQueueMessage.
    If no encryption metadata is present, will return the unaltered message.
    :param str message:
        The JSON formatted QueueEncryptedMessage contents with all associated metadata.
    :param Any response:
        The pipeline response used to generate an error with.
    :param bool require_encryption:
        If set, will enforce that the retrieved messages are encrypted and decrypt them.
    :param object key_encryption_key:
        The user-provided key-encryption-key. Must implement the following methods:
        unwrap_key(key, algorithm)
            - returns the unwrapped form of the specified symmetric key usingthe string-specified algorithm.
        get_kid()
            - returns a string key id for this key-encryption-key.
    :param Callable resolver:
        The user-provided key resolver. Uses the kid string to return a key-encryption-key
        implementing the interface defined above.
    :return: The plain text message from the queue message.
    :rtype: str
    """
