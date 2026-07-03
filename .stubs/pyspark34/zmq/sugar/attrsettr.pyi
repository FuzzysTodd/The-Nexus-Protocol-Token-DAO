from typing import TypeVar

__all__ = ['AttributeSetter']

T = TypeVar('T')
OptValT = str | bytes | int

class AttributeSetter:
    def __setattr__(self, key: str, value: OptValT) -> None:
        """set zmq options by attribute"""
    def __getattr__(self, key: str) -> OptValT:
        """get zmq options by attribute"""
    def get(self, opt: int) -> OptValT:
        """Override in subclass"""
    def set(self, opt: int, val: OptValT) -> None:
        """Override in subclass"""
