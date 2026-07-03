import ctypes

class DataBlob(ctypes.Structure):
    """A wrapper for interacting with the _CRYPTOAPI_BLOB type and its many aliases. This type is
    exposed from Wincrypt.h in XP and above.

    The memory associated with a DataBlob itself does not need to be freed, as the Python runtime
    will correctly clean it up. However, depending on the data it points at, it may still need to be
    freed. For instance, memory created by ctypes.create_string_buffer is already managed, and needs
    to not be freed. However, memory allocated by CryptProtectData and CryptUnprotectData must have
    LocalFree called on pbData.

    See documentation for this type at:
    https://msdn.microsoft.com/en-us/7a06eae5-96d8-4ece-98cb-cf0710d2ddbd
    """
    def raw(self) -> bytes:
        """Copies the message from the DataBlob in natively allocated memory into Python controlled
        memory.
        :return A byte array that matches what is stored in native-memory."""

class WindowsDataProtectionAgent:
    """A mechanism for interacting with the Windows DP API Native library, e.g. Crypt32.dll."""
    def __init__(self, entropy: str = None) -> None: ...
    def protect(self, message: str) -> bytes:
        """Encrypts a message.
        :return cipher text holding the original message."""
    def unprotect(self, cipher_text: bytes) -> str:
        """Decrypts cipher text that is provided.
        :return The original message hidden in the cipher text."""
