import enum

__all__ = ['QuantType']

class QuantType(enum.IntEnum):
    DYNAMIC: int
    STATIC: int
    QAT: int
    WEIGHT_ONLY: int
