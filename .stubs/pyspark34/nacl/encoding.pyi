from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

class _Encoder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def encode(data: bytes) -> bytes:
        """Transform raw data to encoded data."""
    @staticmethod
    @abstractmethod
    def decode(data: bytes) -> bytes:
        """Transform encoded data back to raw data.

        Decoding after encoding should be a no-op, i.e. `decode(encode(x)) == x`.
        """

Encoder: Incomplete

class RawEncoder(_Encoder):
    @staticmethod
    def encode(data: bytes) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> bytes: ...

class HexEncoder(_Encoder):
    @staticmethod
    def encode(data: bytes) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> bytes: ...

class Base16Encoder(_Encoder):
    @staticmethod
    def encode(data: bytes) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> bytes: ...

class Base32Encoder(_Encoder):
    @staticmethod
    def encode(data: bytes) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> bytes: ...

class Base64Encoder(_Encoder):
    @staticmethod
    def encode(data: bytes) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> bytes: ...

class URLSafeBase64Encoder(_Encoder):
    @staticmethod
    def encode(data: bytes) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> bytes: ...

class Encodable:
    def encode(self, encoder: Encoder = ...) -> bytes: ...
